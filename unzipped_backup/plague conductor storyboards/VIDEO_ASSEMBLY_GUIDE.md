# PLAGUE CONDUCTOR - VIDEO ASSEMBLY SCRIPT
## FFmpeg Video Creation Guide

**Current Assets**: 15 images + 1 MP3 audio file  
**Video Duration**: ~2:55  
**Format**: 1080p (1920x1080) or 720p (1280x720)  

---

## QUICK START - Create Video

### Option 1: Automated FFmpeg Script (Recommended)

#### Step 1: Download FFmpeg
1. Go to: https://ffmpeg.org/download.html
2. Download for Windows (full version)
3. Install or extract to `C:\ffmpeg\` (or any location)
4. Add to PATH (or use full path in commands below)

#### Step 2: Create Video with Concatenation
Run this PowerShell script in the `00_PRODUCTION` folder:

```powershell
# Navigate to production folder
cd "d:\plague conductor storyboards\00_PRODUCTION"

# Define variables
$audioFile = "d:\plague conductor storyboards\01_SOURCE_AUDIO\Plague Conductor.mp3"
$outputVideo = "d:\plague conductor storyboards\plague_conductor_rough_cut.mp4"

# Create input file list with image durations
$inputList = @"
file 'INTRO_Scenes_1-9/Scene_006_INTRO_conductor_full_reveal.png'
duration 3
file 'INTRO_Scenes_1-9/Scene_008_INTRO_horde_rises_mass.png'
duration 3
file 'VERSE_1_Scenes_10-29/Scene_010_VERSE1_prison_exterior.png'
duration 2
file 'VERSE_1_Scenes_10-29/Scene_012_VERSE1_prisoner_closeup_scarred.png'
duration 2
file 'VERSE_1_Scenes_10-29/Scene_014_VERSE1_prisoners_dungeon_wide.png'
duration 2
file 'VERSE_1_Scenes_10-29/Scene_015_VERSE1_conductor_enters_dungeon.png'
duration 2
file 'VERSE_1_Scenes_10-29/Scene_020_VERSE1_prisoners_rising_freed.png'
duration 2
file 'VERSE_1_Scenes_10-29/Scene_024_VERSE1_prisoners_horde_sighting.png'
duration 2
file 'VERSE_1_Scenes_10-29/Scene_026_VERSE1_bait_positioned_ready.png'
duration 2
file 'VERSE_1_Scenes_10-29/Scene_029_VERSE1_chaos_spreads_engagements.png'
duration 2
file 'CHORUS_1_Scenes_30-37/Scene_035_CHORUS1_conductor_silhouette.png'
duration 3
file 'BRIDGE_Scenes_52-69/Scene_052_BRIDGE_opening_chaos_cuts.png'
duration 2
file 'BRIDGE_Scenes_52-69/Scene_056_BRIDGE_conductor_wild.png'
duration 2
file 'BRIDGE_Scenes_52-69/Scene_059_BRIDGE_horde_closeups_intense.png'
duration 2
file 'BRIDGE_Scenes_52-69/Scene_064_BRIDGE_conductor_control_threads.png'
duration 2
file 'BRIDGE_Scenes_52-69/Scene_065_BRIDGE_climax_all_elements.png'
duration 2
file 'BRIDGE_Scenes_52-69/Scene_067_BRIDGE_conductor_peak_arms_raised.png'
duration 2
file 'CHORUS_2_Scenes_70-76/Scene_072_CHORUS2_sacrifice_complete.png'
duration 3
file 'OUTRO_Scenes_77-90/Scene_077_OUTRO_conductor_descends.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_078_OUTRO_conductor_face_satisfied.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_079_OUTRO_ground_survey.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_081_OUTRO_distant_horde_horizon.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_082_OUTRO_village_lights_safe.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_083_OUTRO_conductor_high_ground.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_085_OUTRO_new_horde_emerging.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_086_OUTRO_baton_raised_again.png'
duration 2
file 'OUTRO_Scenes_77-90/Scene_087_OUTRO_landscape_pullback.png'
duration 3
"@

# Save input list to file
$inputList | Out-File -FilePath "input_list.txt" -Encoding UTF8

# Create video using FFmpeg
ffmpeg -f concat -safe 0 -i input_list.txt `
  -i "$audioFile" `
  -c:v libx264 -preset medium -crf 18 `
  -c:a aac -b:a 192k `
  -pix_fmt yuv420p `
  -shortest `
  "$outputVideo"

Write-Host "✓ Video created: $outputVideo"
```

---

## Alternative: Manual FFmpeg Command

If script doesn't work, run this command directly:

```bash
cd "d:\plague conductor storyboards\00_PRODUCTION"

ffmpeg -y ^
  -loop 1 -t 3 -i "INTRO_Scenes_1-9/Scene_006_INTRO_conductor_full_reveal.png" ^
  -loop 1 -t 3 -i "INTRO_Scenes_1-9/Scene_008_INTRO_horde_rises_mass.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_010_VERSE1_prison_exterior.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_012_VERSE1_prisoner_closeup_scarred.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_014_VERSE1_prisoners_dungeon_wide.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_015_VERSE1_conductor_enters_dungeon.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_020_VERSE1_prisoners_rising_freed.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_024_VERSE1_prisoners_horde_sighting.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_026_VERSE1_bait_positioned_ready.png" ^
  -loop 1 -t 2 -i "VERSE_1_Scenes_10-29/Scene_029_VERSE1_chaos_spreads_engagements.png" ^
  -loop 1 -t 3 -i "CHORUS_1_Scenes_30-37/Scene_035_CHORUS1_conductor_silhouette.png" ^
  -loop 1 -t 2 -i "BRIDGE_Scenes_52-69/Scene_052_BRIDGE_opening_chaos_cuts.png" ^
  -loop 1 -t 2 -i "BRIDGE_Scenes_52-69/Scene_056_BRIDGE_conductor_wild.png" ^
  -loop 1 -t 2 -i "BRIDGE_Scenes_52-69/Scene_059_BRIDGE_horde_closeups_intense.png" ^
  -loop 1 -t 2 -i "BRIDGE_Scenes_52-69/Scene_064_BRIDGE_conductor_control_threads.png" ^
  -loop 1 -t 2 -i "BRIDGE_Scenes_52-69/Scene_065_BRIDGE_climax_all_elements.png" ^
  -loop 1 -t 2 -i "BRIDGE_Scenes_52-69/Scene_067_BRIDGE_conductor_peak_arms_raised.png" ^
  -loop 1 -t 3 -i "CHORUS_2_Scenes_70-76/Scene_072_CHORUS2_sacrifice_complete.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_077_OUTRO_conductor_descends.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_078_OUTRO_conductor_face_satisfied.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_079_OUTRO_ground_survey.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_081_OUTRO_distant_horde_horizon.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_082_OUTRO_village_lights_safe.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_083_OUTRO_conductor_high_ground.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_085_OUTRO_new_horde_emerging.png" ^
  -loop 1 -t 2 -i "OUTRO_Scenes_77-90/Scene_086_OUTRO_baton_raised_again.png" ^
  -loop 1 -t 3 -i "OUTRO_Scenes_77-90/Scene_087_OUTRO_landscape_pullback.png" ^
  -i "../01_SOURCE_AUDIO/Plague Conductor.mp3" ^
  -filter_complex "[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v0];[1:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v1];[2:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v2];..." ^
  -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k ^
  -shortest "../plague_conductor_rough_cut.mp4"
```

---

## Option 2: Using Video Editing Software

### Recommended Options:
1. **DaVinci Resolve** (Free, professional) - https://www.blackmagicdesign.com/products/davinci
2. **OBS Studio** (Free, streaming/recording) - https://obsproject.com
3. **HitFilm Express** (Free) - https://hitfilm.com/express
4. **Adobe Premiere Pro** (Paid, industry standard)

**Steps for DaVinci Resolve (Easiest)**:
1. Download and install DaVinci Resolve
2. Create new project
3. Import all 15 PNG images into media pool
4. Drag to timeline in order
5. Set duration per image (2-3 seconds)
6. Import MP3 audio track
7. Sync to music
8. Export as MP4

---

## Option 3: Create Timeline/Timing Guide

If you want to use video editing software, here's the exact timing:

| Scene | Image | Duration | Total Time |
|-------|-------|----------|------------|
| 6 | Intro 1 | 3s | 0:00-0:03 |
| 8 | Intro 2 | 3s | 0:03-0:06 |
| 10 | V1 Prison Ext | 2s | 0:06-0:08 |
| 12 | V1 Prisoner 1 | 2s | 0:08-0:10 |
| 14 | V1 Prisoners Wide | 2s | 0:10-0:12 |
| 15 | V1 Conductor Enter | 2s | 0:12-0:14 |
| 20 | V1 Prisoners Rise | 2s | 0:14-0:16 |
| 24 | V1 Spot Horde | 2s | 0:16-0:18 |
| 26 | V1 Bait Set | 2s | 0:18-0:20 |
| 29 | V1 Chaos | 2s | 0:20-0:22 |
| 35 | Chorus 1 | 3s | 0:22-0:25 |
| 52 | Bridge 1 | 2s | 0:25-0:27 |
| 56 | Bridge 2 | 2s | 0:27-0:29 |
| 59 | Bridge 3 | 2s | 0:29-0:31 |
| 64 | Bridge 4 | 2s | 0:31-0:33 |
| 65 | Bridge 5 | 2s | 0:33-0:35 |
| 67 | Bridge 6 | 2s | 0:35-0:37 |
| 72 | Chorus 2 | 3s | 0:37-0:40 |
| 77 | Outro 1 | 2s | 0:40-0:42 |
| 78 | Outro 2 | 2s | 0:42-0:44 |
| 79 | Outro 3 | 2s | 0:44-0:46 |
| 81 | Outro 4 | 2s | 0:46-0:48 |
| 82 | Outro 5 | 2s | 0:48-0:50 |
| 83 | Outro 6 | 2s | 0:50-0:52 |
| 85 | Outro 7 | 2s | 0:52-0:54 |
| 86 | Outro 8 | 2s | 0:54-0:56 |
| 87 | Outro 9 | 3s | 0:56-0:59 |

**Total**: ~59 seconds (placeholder with 15 images)
**Full**: ~175 seconds (2:55 with all 90 scenes)

---

## Audio Information

**File**: `01_SOURCE_AUDIO/Plague Conductor.mp3`  
**Duration**: ~2:55 (175 seconds)  
**Quality**: Use as is for rough cut

---

## Expected Output

**Final Video**: `plague_conductor_rough_cut.mp4`  
**Resolution**: 1920x1080 (Full HD)  
**Codec**: H.264 video + AAC audio  
**File Size**: ~50-100 MB  
**Quality**: Good (CRF 18)  

---

## Next Steps After Video Creation

1. ✓ Create rough cut with 15 images
2. Generate remaining 75 images (Batches 4-8)
3. Re-compile video with full 90 scenes
4. Add effects/transitions (optional)
5. Color grade/polish
6. Final export

---

## Troubleshooting

**FFmpeg not found**: 
- Install from https://ffmpeg.org/download.html
- Add to Windows PATH
- Or use full path: `C:\ffmpeg\bin\ffmpeg.exe`

**Image not found error**:
- Make sure all file paths are correct
- Check folder structure matches
- Use full absolute paths if relative paths fail

**Audio sync issues**:
- FFmpeg will sync to shortest input
- Video will be shortened if audio is shorter
- Expected: ~59 seconds with 15 images

**Quality issues**:
- Increase `-crf` value (lower = better quality, 0-51, default 28, use 18-23)
- Change `-preset` (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)

---

## Quick Test Version

Create a 10-second preview with just 5 images:

```bash
ffmpeg -loop 1 -t 2 -i INTRO_Scenes_1-9/Scene_006_INTRO_conductor_full_reveal.png ^
  -loop 1 -t 2 -i INTRO_Scenes_1-9/Scene_008_INTRO_horde_rises_mass.png ^
  -loop 1 -t 2 -i VERSE_1_Scenes_10-29/Scene_010_VERSE1_prison_exterior.png ^
  -loop 1 -t 2 -i VERSE_1_Scenes_10-29/Scene_012_VERSE1_prisoner_closeup_scarred.png ^
  -loop 1 -t 2 -i VERSE_1_Scenes_10-29/Scene_014_VERSE1_prisoners_dungeon_wide.png ^
  -i "../01_SOURCE_AUDIO/Plague Conductor.mp3" ^
  -filter_complex "[0:v]scale=1920:1080[v0];[1:v]scale=1920:1080[v1];[2:v]scale=1920:1080[v2];[3:v]scale=1920:1080[v3];[4:v]scale=1920:1080[v4];[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[v]" ^
  -map "[v]" -map "1:a" -c:v libx264 -c:a aac -shortest test_preview.mp4
```

---

## READY TO BUILD VIDEO!

Choose your method:
1. **FFmpeg (Fast & Automated)** - Run PowerShell script
2. **Video Editing Software (Visual)** - Use DaVinci Resolve
3. **Manual Assembly (Control)** - Use timing guide above

Which would you like to try?

