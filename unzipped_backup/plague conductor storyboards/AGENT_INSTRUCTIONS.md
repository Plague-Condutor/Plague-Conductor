# 🎬 PLAGUE CONDUCTOR - AGENT EXECUTION GUIDE

**Agent Task**: Generate AI imagery to complete music video

---

## CRITICAL: You Must USE an Image Generator

**This task requires calling an AI image generation API:**
- ✅ DALL-E 3 (https://openai.com/dall-e-3)
- ✅ Midjourney (https://www.midjourney.com/)
- ✅ Claude (https://claude.ai/) - has image generation
- ✅ Stable Diffusion (local or API)

**You CANNOT complete this by organizing files. You must GENERATE new images.**

---

## CURRENT STATUS

**Images We Have**: 15 total
- 9 OUTRO images (Batch 1) ✅ Complete
- 4 Existing images (scattered sections)
- 2 Extra placeholder versions

**Images We Need**: 75 more to reach 90/90

**Current Generation Task**: Batch 2 (BRIDGE)
- 6 images needed
- All prompts in: `03_PRODUCTION_INDEX/01_BRIDGE_CHAOS_6IMAGES.md`

---

## STEP-BY-STEP INSTRUCTIONS

### Step 1: Open Batch 2 Document
```
File: d:\plague conductor storyboards\03_PRODUCTION_INDEX\01_BRIDGE_CHAOS_6IMAGES.md
Section: "EXECUTION INSTRUCTIONS"
Copy all 6 prompts (Prompt 1 through Prompt 6)
```

### Step 2: Generate Each Image
For EACH of the 6 prompts:

1. **Prompt 1 (Scene 52 - Opening Chaos):**
   ```
   Ultra-fast montage composition showing multiple simultaneous violent elements: 
   lightning strike in upper portion, zombie snarling in middle-left, prisoner screaming 
   in middle-right, conductor's baton movement in lower section, rapid rapid-cut visual 
   effect, frenzy and chaos, extreme intensity, dark and violent, compositional chaos 
   representing the musical tremolo chaos
   ```

2. **Generate in your AI tool** (DALL-E 3 recommended for complexity):
   - Use EXACT prompt text
   - Set resolution: 1024×1024 or 1280×720
   - Quality: High/Premium
   - Save as PNG/JPG

3. **Save with exact filename:**
   ```
   Scene_052_BRIDGE_opening_chaos_cuts.jpg
   ```

### Step 3: Organize into Project Folder
Move all generated images to:
```
d:\plague conductor storyboards\00_PRODUCTION\BRIDGE_Scenes_52-69\
```

**Expected 6 files after completion:**
- Scene_052_BRIDGE_opening_chaos_cuts.jpg
- Scene_056_BRIDGE_conductor_wild.jpg
- Scene_059_BRIDGE_horde_closeups_intense.jpg
- Scene_064_BRIDGE_conductor_control_threads.jpg
- Scene_065_BRIDGE_climax_all_elements.jpg
- Scene_067_BRIDGE_conductor_peak_arms_raised.jpg

### Step 4: Verify Files
```powershell
cd "d:\plague conductor storyboards\00_PRODUCTION\BRIDGE_Scenes_52-69"
Get-ChildItem -Filter "Scene_*.jpg" | Select-Object Name | Format-Table -AutoSize
```

Should return 6 files.

### Step 5: Run Video Compilation
```powershell
cd "d:\plague conductor storyboards"
python create_video_smart.py
```

This will:
- Detect all 21 images (15 + 6 new)
- Compile into single MP4 video
- Save to: `plague_conductor_rough_cut.mp4`

### Step 6: Commit & Push to GitHub
```powershell
cd "d:\plague conductor storyboards"
git add .
git commit -m "Add Bridge batch images (Batch 2 - 6 scenes)"
git push origin main
```

---

## ALL BATCH PROMPTS (Ready to Use)

### BATCH 2 - BRIDGE (6 images) - CURRENT
📄 File: `03_PRODUCTION_INDEX/01_BRIDGE_CHAOS_6IMAGES.md`
Section: Prompts 1-6

### BATCH 3 - VERSE_1 (8 images) - QUEUED NEXT
📄 File: `03_PRODUCTION_INDEX/02_VERSE1_PRISON_8IMAGES.md`
Scenes: 10, 12, 14, 15, 20, 24, 26, 29

### BATCH 4 - INTRO (7 images) - AFTER VERSE_1
📄 File: (Create if needed)
Scenes: 1-9 (select key moments)

---

## SUCCESS CRITERIA

**Batch 2 Complete When:**
- ✅ 6 images generated with AI
- ✅ Saved with Scene_### format
- ✅ In BRIDGE_Scenes_52-69 folder
- ✅ Video compiles to 55+ seconds
- ✅ Pushed to GitHub

**Overall Goal:**
- Generate 75+ more images
- Reach 50% visual coverage (45/90 scenes)
- Create full playable rough cut
- Maintain clean GitHub history

---

## IMPORTANT NOTES

1. **Scene numbering is CRITICAL** - video sort depends on Scene_### format
2. **Quality matters** - these are placeholder quality, but should look professional
3. **Batch workflow** - complete one batch at a time, push to GitHub after each
4. **Prompts are copy-paste ready** - use exact text from markdown files
5. **Monitor script watches** - when you finish Batch 2, `monitor_and_update.ps1` will auto-compile video

---

## WHAT NOT TO DO

❌ Don't manually organize file structure (it's already done)
❌ Don't modify prompt text (copy-paste exactly)
❌ Don't change Scene numbering (it controls video sequence)
❌ Don't generate all 90 images at once (batch workflow keeps it organized)
❌ Don't skip the git commit/push (history matters for production tracking)

---

## QUESTIONS FOR AGENT

If unsure:
- Which image generator should I use? → DALL-E 3 preferred for this project
- How many batches total? → 8-10 batches to reach 90 scenes
- Should I generate all at once? → No, one batch at a time
- What if an image fails to generate? → Regenerate or use alternative until acceptable

---

**Agent Status**: Ready to generate Batch 2 (BRIDGE - 6 images)
**Deadline**: No rush - quality > speed
**Success Metric**: 6 images in folder → video compiles → push to GitHub
