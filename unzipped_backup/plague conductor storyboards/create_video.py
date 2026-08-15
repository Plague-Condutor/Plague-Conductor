#!/usr/bin/env python3
"""
PLAGUE CONDUCTOR - Automatic Video Creator
Creates rough cut video from placeholder images + audio
"""

import os
import subprocess
import sys
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

PROJECT_ROOT = Path(r"d:\plague conductor storyboards")
PRODUCTION_FOLDER = PROJECT_ROOT / "00_PRODUCTION"
AUDIO_FILE = PROJECT_ROOT / "01_SOURCE_AUDIO" / "Plague Conductor.mp3"
OUTPUT_VIDEO = PROJECT_ROOT / "plague_conductor_rough_cut.mp4"

# Image sequence with durations (in seconds)
SCENES = [
    ("INTRO_Scenes_1-9", "Scene_006_INTRO_conductor_full_reveal.png", 3),
    ("INTRO_Scenes_1-9", "Scene_008_INTRO_horde_rises_mass.png", 3),
    ("VERSE_1_Scenes_10-29", "Scene_010_VERSE1_prison_exterior.png", 2),
    ("VERSE_1_Scenes_10-29", "Scene_012_VERSE1_prisoner_closeup_scarred.png", 2),
    ("VERSE_1_Scenes_10-29", "Scene_014_VERSE1_prisoners_dungeon_wide.png", 2),
    ("VERSE_1_Scenes_10-29", "Scene_015_VERSE1_conductor_enters_dungeon.png", 2),
    ("VERSE_1_Scenes_10-29", "Scene_020_VERSE1_prisoners_rising_freed.png", 2),
    ("VERSE_1_Scenes_10-29", "Scene_024_VERSE1_prisoners_horde_sighting.png", 2),
    ("VERSE_1_Scenes_10-29", "Scene_026_VERSE1_bait_positioned_ready.png", 2),
    ("VERSE_1_Scenes_10-29", "Scene_029_VERSE1_chaos_spreads_engagements.png", 2),
    ("CHORUS_1_Scenes_30-37", "Scene_035_CHORUS1_conductor_silhouette.png", 3),
    ("BRIDGE_Scenes_52-69", "Scene_052_BRIDGE_opening_chaos_cuts.png", 2),
    ("BRIDGE_Scenes_52-69", "Scene_056_BRIDGE_conductor_wild.png", 2),
    ("BRIDGE_Scenes_52-69", "Scene_059_BRIDGE_horde_closeups_intense.png", 2),
    ("BRIDGE_Scenes_52-69", "Scene_064_BRIDGE_conductor_control_threads.png", 2),
    ("BRIDGE_Scenes_52-69", "Scene_065_BRIDGE_climax_all_elements.png", 2),
    ("BRIDGE_Scenes_52-69", "Scene_067_BRIDGE_conductor_peak_arms_raised.png", 2),
    ("CHORUS_2_Scenes_70-76", "Scene_072_CHORUS2_sacrifice_complete.png", 3),
    ("OUTRO_Scenes_77-90", "Scene_077_OUTRO_conductor_descends.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_078_OUTRO_conductor_face_satisfied.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_079_OUTRO_ground_survey.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_081_OUTRO_distant_horde_horizon.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_082_OUTRO_village_lights_safe.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_083_OUTRO_conductor_high_ground.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_085_OUTRO_new_horde_emerging.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_086_OUTRO_baton_raised_again.png", 2),
    ("OUTRO_Scenes_77-90", "Scene_087_OUTRO_landscape_pullback.png", 3),
]

# ============================================================================
# FUNCTIONS
# ============================================================================

def check_ffmpeg():
    """Check if FFmpeg is installed"""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False


def check_files():
    """Verify all image and audio files exist"""
    print("\n✓ Checking files...")
    missing = []
    
    for folder, image, _ in SCENES:
        path = PRODUCTION_FOLDER / folder / image
        if not path.exists():
            missing.append(str(path))
            print(f"  ✗ Missing: {folder}/{image}")
        else:
            print(f"  ✓ Found: {folder}/{image}")
    
    if not AUDIO_FILE.exists():
        missing.append(str(AUDIO_FILE))
        print(f"  ✗ Missing: {AUDIO_FILE.name}")
    else:
        print(f"  ✓ Found: {AUDIO_FILE.name}")
    
    return len(missing) == 0


def create_concat_file():
    """Create FFmpeg concat demuxer input file"""
    concat_file = PRODUCTION_FOLDER / "concat_list.txt"
    
    print("\n✓ Creating concat file...")
    with open(concat_file, 'w') as f:
        for folder, image, duration in SCENES:
            image_path = f"{folder}/{image}"
            f.write(f"file '{image_path}'\n")
            f.write(f"duration {duration}\n")
    
    print(f"  Concat file created: {concat_file}")
    return concat_file


def build_ffmpeg_command(concat_file):
    """Build FFmpeg command"""
    cmd = [
        "ffmpeg",
        "-y",  # Overwrite output
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-i", str(AUDIO_FILE),
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        str(OUTPUT_VIDEO)
    ]
    return cmd


def create_video(concat_file):
    """Create video using FFmpeg"""
    cmd = build_ffmpeg_command(concat_file)
    
    print("\n✓ Creating video with FFmpeg...")
    print(f"  Command: {' '.join(cmd)}\n")
    
    try:
        # Change to production folder for relative paths
        os.chdir(PRODUCTION_FOLDER)
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Stream output
        for line in process.stdout:
            if "frame=" in line or "time=" in line or "bitrate=" in line:
                print(f"  {line.strip()}", end='\r')
        
        process.wait()
        
        if process.returncode == 0:
            return True
        else:
            print(f"\n✗ FFmpeg failed with code {process.returncode}")
            return False
            
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def verify_output():
    """Check if output video was created"""
    if OUTPUT_VIDEO.exists():
        size_mb = OUTPUT_VIDEO.stat().st_size / (1024 * 1024)
        print(f"\n✓ Video created successfully!")
        print(f"  File: {OUTPUT_VIDEO}")
        print(f"  Size: {size_mb:.1f} MB")
        return True
    else:
        print(f"\n✗ Video file not found: {OUTPUT_VIDEO}")
        return False


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 70)
    print("PLAGUE CONDUCTOR - VIDEO CREATOR")
    print("=" * 70)
    
    # Check FFmpeg
    if not check_ffmpeg():
        print("\n✗ FFmpeg not found!")
        print("  Install from: https://ffmpeg.org/download.html")
        print("  Add to PATH or specify full path")
        sys.exit(1)
    
    print("\n✓ FFmpeg found")
    
    # Check files
    if not check_files():
        print("\n✗ Some files are missing!")
        sys.exit(1)
    
    # Create concat file
    concat_file = create_concat_file()
    
    # Create video
    if not create_video(concat_file):
        sys.exit(1)
    
    # Verify
    if verify_output():
        print("\n" + "=" * 70)
        print("SUCCESS! Your video is ready!")
        print("=" * 70)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
