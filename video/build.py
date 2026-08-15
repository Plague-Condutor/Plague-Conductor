#!/usr/bin/env python3
"""
Plague Conductor — music-video builder.

Turns an audio track + a folder of AI keyframe images into an .mp4 whose
hard cuts land on the music's energy onsets ("cut to the beat"), with a
gentle Ken-Burns zoom on every shot.

Usage:
    python3 build.py <audio> <frames_dir> <output.mp4> [min_gap] [max_gap]
"""
import subprocess, os, sys, math, array, re, shutil

FFMPEG = shutil.which("ffmpeg") or "/usr/local/bin/ffmpeg"
FPS   = 24
W, H  = 1920, 1080
MAX_SEGS = 120         # cap shot count; if exceeded, widen gaps


def sh(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def probe_duration(path):
    p = sh([FFMPEG, "-i", path])
    m = re.search(rb"Duration:\s(\d+):(\d+):(\d+(?:\.\d+)?)", p.stderr)
    if not m:
        sys.exit("ERROR: cannot read audio duration — is this a valid audio file?")
    h, mi, s = (float(x) for x in m.groups())
    return h * 3600 + mi * 60 + s

def decode_pcm(path, sr=8000):
    p = subprocess.run([FFMPEG, "-i", path, "-ac", "1", "-ar", str(sr),
                        "-f", "s16le", "-"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    a = array.array('h'); a.frombytes(p.stdout); return a, sr

def rms_env(samples, win=512):
    env, n = [], len(samples)
    for i in range(0, n - win, win):
        s = 0
        for j in range(i, i + win):
            v = samples[j]; s += v * v
        env.append(math.sqrt(s / win))
    return env

def detect_onsets(env, dt, min_spacing=0.45):
    """energy-flux peaks above a local moving-average threshold.
       Returns (time, strength) tuples; min_spacing avoids double-triggers."""
    flux = [0.0] * len(env)
    for i in range(1, len(env)):
        d = env[i] - env[i - 1]
        if d > 0:
            flux[i] = d
    win, out, last = 12, [], -1.0
    for i in range(win, len(env) - 1):
        avg = sum(flux[i - win:i]) / win
        thr = avg * 1.9 + 1e-9
        if flux[i] > thr and flux[i] >= flux[i - 1] and flux[i] >= flux[i + 1]:
            t = i * dt
            if t - last >= min_spacing:
                out.append((t, flux[i])); last = t
    return out

def build_segments(onsets, dur, min_gap, max_gap):
    """from each cut, jump to the STRONGEST onset within [t+min_gap, t+max_gap];
       fall back to the max-gap boundary when there is none."""
    segs, t = [], 0.0
    while t < dur - 0.05:
        lo, hi = t + min_gap, min(t + max_gap, dur)
        cands = [o for o in onsets if lo <= o[0] <= hi]
        cut = max(cands, key=lambda o: o[1])[0] if cands else hi
        segs.append(round(cut - t, 3)); t = cut
    return segs

def render_clip(img, dur, idx, out):
    total = max(2, int(round(dur * FPS)))
    # alternate zoom amount + drift direction for variety
    styles = [
        ("1.0+0.0014*on", "+0.35*on",  "+0.0*on"),
        ("1.06+0.0012*on", "-0.30*on", "+0.25*on"),
        ("1.0+0.0016*on",  "+0.0*on",  "-0.30*on"),
        ("1.05+0.0010*on", "-0.35*on", "-0.20*on"),
    ]
    z, dx, dy = styles[idx % len(styles)]
    SW, SH = W * 2, H * 2
    vf = (f"scale={SW}:{SH}:force_original_aspect_ratio=increase,crop={SW}:{SH},"
          f"setsar=1,"
          f"zoompan=z='min({z},1.32)':d={total}:"
          f"x='iw/2-(iw/zoom/2)+({dx})':y='ih/2-(ih/zoom/2)+({dy})':"
          f"s={W}x{H}:fps={FPS},format=yuv420p")
    cmd = [FFMPEG, "-y", "-loglevel", "error", "-i", img,
           "-vf", vf, "-frames:v", str(total), "-r", str(FPS),
           "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", out]
    sh(cmd)

def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    audio, frames_dir, output = sys.argv[1], sys.argv[2], sys.argv[3]
    min_gap = float(sys.argv[4]) if len(sys.argv) > 4 else 1.5
    max_gap = float(sys.argv[5]) if len(sys.argv) > 5 else 3.0

    frames = sorted(f for f in os.listdir(frames_dir)
                    if f.lower().endswith((".png", ".jpg", ".jpeg")))
    if not frames:
        sys.exit("ERROR: no images in frames dir")
    frames = [os.path.join(frames_dir, f) for f in frames]
    print(f"[1/5] {len(frames)} keyframes available")

    dur = probe_duration(audio)
    print(f"[2/5] audio duration: {dur:.1f}s")

    samples, sr = decode_pcm(audio)
    env = rms_env(samples)
    dt = 512 / sr
    ons = detect_onsets(env, dt)
    segs = build_segments(ons, dur, min_gap, max_gap)
    # if too many shots, widen the gaps and retry once
    while len(segs) > MAX_SEGS and min_gap < 6:
        min_gap += 0.5; max_gap += 0.6
        segs = build_segments(ons, dur, min_gap, max_gap)
    print(f"[3/5] {len(onns:=ons)} onsets -> {len(segs)} shots (gap {min_gap}-{max_gap}s)")

    clips_dir = os.path.join(os.path.dirname(output) or ".", "_clips")
    if os.path.isdir(clips_dir): shutil.rmtree(clips_dir)
    os.makedirs(clips_dir, exist_ok=True)
    clip_files = []
    for i, d in enumerate(segs):
        img = frames[i % len(frames)]
        cf = os.path.join(clips_dir, f"c{i:03d}.mp4")
        render_clip(img, d, i, cf)
        clip_files.append(cf)
        if (i + 1) % 10 == 0:
            print(f"      rendered {i+1}/{len(segs)} shots")
    print(f"[4/5] rendered {len(clip_files)} shots")

    # concat clips
    list_path = os.path.join(clips_dir, "list.txt")
    with open(list_path, "w") as fh:
        for cf in clip_files:
            fh.write(f"file '{os.path.abspath(cf)}'\n")
    silent = os.path.join(clips_dir, "silent.mp4")
    sh([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
        "-i", list_path, "-c", "copy", silent])

    # mux audio
    sh([FFMPEG, "-y", "-loglevel", "error", "-i", silent, "-i", audio,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", output])
    print(f"[5/5] wrote {output}  ({os.path.getsize(output)//1024} KB)")

if __name__ == "__main__":
    main()
