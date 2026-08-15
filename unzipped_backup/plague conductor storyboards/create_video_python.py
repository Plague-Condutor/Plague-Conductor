#!/usr/bin/env python3
"""
PLAGUE CONDUCTOR - Video Creator (Pure Python - No FFmpeg needed!)
Uses imageio + numpy for video creation
"""

import sys
import subprocess
from pathlib import Path

# ============================================================================
# INSTALL DEPENDENCIES
# ============================================================================

def install_dependencies():
    """Install required packages"""
    packages = ["imageio", "imageio-ffmpeg", "numpy", "Pillow"]
    
    print("✓ Checking/installing required packages...")
    for package in packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"  ✓ {package} already installed")
        except ImportError:
            print(f"  ✓ Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
            print(f"    {package} installed")

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


def create_video_with_imageio():
    """Create video using imageio"""
    import imageio
    import numpy as np
    from PIL import Image
    
    print("\n✓ Creating video...")
    print(f"  FPS: 24")
    print(f"  Resolution: 1920x1080")
    print(f"  Codec: H.264")
    
    # Create video writer
    writer = imageio.get_writer(
        str(OUTPUT_VIDEO),
        fps=24,
        codec='libx264',
        pixelformat='yuv420p',
        quality=7  # 0-10, lower is better
    )
    
    total_duration = sum(duration for _, _, duration in SCENES)
    frame_num = 0
    total_frames = total_duration * 24
    
    try:
        for idx, (folder, image_file, duration) in enumerate(SCENES, 1):
            image_path = PRODUCTION_FOLDER / folder / image_file
            
            # Load image
            img = Image.open(image_path)
            
            # Resize to 1920x1080 if needed
            if img.size != (1920, 1080):
                img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
            
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            img_array = np.array(img)
            
            # Write frame for duration seconds (duration * fps frames)
            frames_to_write = int(duration * 24)
            for _ in range(frames_to_write):
                writer.append_data(img_array)
                frame_num += 1
                percent = (frame_num / total_frames) * 100
                print(f"\r  Progress: {percent:.1f}% | Scene {idx}/{len(SCENES)}", end="", flush=True)
        
        print()  # New line
        writer.close()
        return True
        
    except Exception as e:
        print(f"\n✗ Error creating video: {e}")
        return False


def add_audio():
    """Add audio to video using ffmpeg-python or moviepy"""
    try:
        # Try using moviepy
        import moviepy.editor as mpy
        
        print("\n✓ Adding audio to video...")
        
        video = mpy.VideoFileClip(str(OUTPUT_VIDEO))
        audio = mpy.AudioFileClip(str(AUDIO_FILE))
        
        # Set audio to video
        final_video = video.with_audio(audio)
        
        # Write final output
        final_video.write_videofile(
            str(OUTPUT_VIDEO),
            codec='libx264',
            audio_codec='aac',
            verbose=False,
            logger=None
        )
        
        print("✓ Audio added successfully!")
        return True
        
    except Exception as e:
        print(f"\n⚠ Could not add audio with moviepy: {e}")
        print("  Attempting alternative method...")
        
        # Try using imageio + ffmpeg directly
        try:
            import subprocess
            cmd = [
                "ffmpeg",
                "-i", str(OUTPUT_VIDEO),
                "-i", str(AUDIO_FILE),
                "-c:v", "copy",
                "-c:a", "aac",
                "-shortest",
                "-y",
                str(OUTPUT_VIDEO).replace(".mp4", "_with_audio.mp4")
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            print("✓ Audio added with ffmpeg!")
            return True
        except:
            print("⚠ Could not add audio. Video saved without audio.")
            print(f"  Add audio manually in video editor: {OUTPUT_VIDEO}")
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
    print("PLAGUE CONDUCTOR - VIDEO CREATOR (Pure Python)")
    print("=" * 70)
    
    # Install dependencies
    install_dependencies()
    
    # Check files
    if not check_files():
        print("\n✗ Some files are missing!")
        sys.exit(1)
    
    # Create video
    if not create_video_with_imageio():
        sys.exit(1)
    
    # Add audio
    add_audio()
    
    # Verify
    if verify_output():
        print("\n" + "=" * 70)
        print("SUCCESS! Your video is ready!")
        print("=" * 70)
        print(f"\nVideo location: {OUTPUT_VIDEO}")
        print("\nNext steps:")
        print("  1. Generate remaining images (Batches 2-8)")
        print("  2. Run this script again to update video")
        print("  3. Add effects/transitions in video editor")
        print("  4. Export final version")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
