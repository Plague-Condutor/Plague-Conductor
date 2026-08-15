#!/usr/bin/env python3
"""
PLAGUE CONDUCTOR - Video Creator (Auto-detects available images)
Creates video using only images that exist in the production folder
"""

import sys
import subprocess
from pathlib import Path
from collections import defaultdict

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

# ============================================================================
# FUNCTIONS
# ============================================================================

def discover_images():
    """Automatically discover and sort available images"""
    print("\n✓ Discovering available images...")
    
    images = []
    for png_file in sorted(PRODUCTION_FOLDER.rglob("*.png")):
        # Extract scene number from filename (Scene_###)
        filename = png_file.name
        try:
            scene_num = int(filename.split("_")[1])
            images.append((scene_num, png_file))
            print(f"  ✓ Found: {png_file.parent.name}/{filename}")
        except:
            print(f"  ⚠ Skipping: {filename} (invalid format)")
    
    # Sort by scene number
    images.sort(key=lambda x: x[0])
    
    if not images:
        print("\n✗ No images found!")
        return []
    
    print(f"\n✓ Found {len(images)} images")
    return images


def check_audio():
    """Verify audio file exists"""
    if not AUDIO_FILE.exists():
        print(f"✗ Audio file missing: {AUDIO_FILE}")
        return False
    
    print(f"✓ Found audio: {AUDIO_FILE.name}")
    return True


def create_video_with_imageio(image_paths):
    """Create video using imageio"""
    import imageio
    import numpy as np
    from PIL import Image
    
    print("\n✓ Creating video...")
    print(f"  Images: {len(image_paths)}")
    print(f"  FPS: 24")
    print(f"  Resolution: 1920x1080")
    print(f"  Duration: ~{len(image_paths) * 2 / 24:.1f} seconds")
    
    # Create video writer
    writer = imageio.get_writer(
        str(OUTPUT_VIDEO),
        fps=24,
        codec='libx264',
        pixelformat='yuv420p',
        quality=7  # 0-10, lower is better
    )
    
    total_frames = len(image_paths) * 2 * 24  # 2 seconds per image at 24 fps
    frame_num = 0
    
    try:
        for idx, image_path in enumerate(image_paths, 1):
            # Load image
            img = Image.open(image_path)
            
            # Resize to 1920x1080 if needed
            if img.size != (1920, 1080):
                print(f"    Resizing {image_path.name} from {img.size} to 1920x1080")
                img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
            
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            img_array = np.array(img)
            
            # Write frame for 2 seconds (2 * 24 = 48 frames)
            frames_to_write = 48
            for _ in range(frames_to_write):
                writer.append_data(img_array)
                frame_num += 1
                percent = (frame_num / total_frames) * 100
                print(f"\r  Progress: {percent:.1f}% | Image {idx}/{len(image_paths)}", end="", flush=True)
        
        print()  # New line
        writer.close()
        return True
        
    except Exception as e:
        print(f"\n✗ Error creating video: {e}")
        import traceback
        traceback.print_exc()
        return False


def add_audio():
    """Add audio to video"""
    try:
        import subprocess
        
        print("\n✓ Adding audio to video...")
        
        # Create temp file for video+audio
        temp_video = str(OUTPUT_VIDEO).replace(".mp4", "_temp.mp4")
        
        cmd = [
            "ffmpeg",
            "-i", str(OUTPUT_VIDEO),
            "-i", str(AUDIO_FILE),
            "-c:v", "copy",
            "-c:a", "aac",
            "-shortest",
            "-y",
            temp_video
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Replace original with audio version
            import os
            os.remove(str(OUTPUT_VIDEO))
            os.rename(temp_video, str(OUTPUT_VIDEO))
            print("✓ Audio added successfully!")
            return True
        else:
            print(f"⚠ FFmpeg error: {result.stderr[:200]}")
            return False
            
    except Exception as e:
        print(f"⚠ Could not add audio: {e}")
        print("  Video saved without audio - add audio in video editor")
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
    print("PLAGUE CONDUCTOR - VIDEO CREATOR (Auto-detect Images)")
    print("=" * 70)
    
    # Install dependencies
    install_dependencies()
    
    # Discover images
    images = discover_images()
    if not images:
        sys.exit(1)
    
    # Check audio
    if not check_audio():
        sys.exit(1)
    
    # Extract just the paths (remove scene numbers)
    image_paths = [path for _, path in images]
    
    # Create video
    if not create_video_with_imageio(image_paths):
        sys.exit(1)
    
    # Add audio
    add_audio()
    
    # Verify
    if verify_output():
        print("\n" + "=" * 70)
        print("SUCCESS! Your rough cut is ready!")
        print("=" * 70)
        print(f"\n✓ Video: {OUTPUT_VIDEO}")
        print(f"✓ Images used: {len(image_paths)}/90 scenes ({int(len(image_paths)/90*100)}% coverage)")
        
        print("\n📋 Next steps:")
        print("  1. Generate Batch 2 (6 BRIDGE images)")
        print("  2. Generate Batch 3 (8 VERSE_1 images)")
        print("  3. Run this script again to update video")
        print("  4. Continue with remaining batches")
        print("  5. Final edit in DaVinci Resolve or Premiere")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
