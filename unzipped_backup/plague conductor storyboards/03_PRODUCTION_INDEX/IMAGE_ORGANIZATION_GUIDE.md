# Image Organization Guide

Quick reference for organizing your 6 existing images into the production structure.

---

## Current Images → New Names & Locations

### Image 1: watermarked_img_11104808671304977021.jpg
**New Name**: `Scene_006_INTRO_conductor_full_reveal.jpg`  
**Location**: `00_PRODUCTION/INTRO_Scenes_1-9/`  
**Description**: Conductor standing full body on rocks with ornate baton  
**Scene Position**: Scene 6 of Intro (0:10 mark in video)  
**Purpose**: Establish the Conductor character  

---

### Image 2: watermarked_img_11601291132558078850.jpg
**New Name**: `Scene_008_INTRO_horde_rises_mass.jpg`  
**Location**: `00_PRODUCTION/INTRO_Scenes_1-9/`  
**Description**: Hundreds of zombies visible, swelling mass  
**Scene Position**: Scene 8 of Intro (0:12 mark in video)  
**Purpose**: Establish the threat scale  

---

### Image 3: watermarked_img_12804009360612180470.jpg
**New Name**: `Scene_035_CHORUS1_conductor_silhouette.jpg`  
**Location**: `00_PRODUCTION/CHORUS_1_Scenes_30-37/`  
**Description**: Plague doctor silhouette with arms spread wide, commanding  
**Scene Position**: Scene 35 of Chorus 1 (0:55 mark in video)  
**Purpose**: Peak power moment, conducting chaos  

---

### Image 4: watermarked_img_13277041989482373626.jpg
**New Name**: `Scene_047_VERSE2_orchestration_peak.jpg`  
**Location**: `00_PRODUCTION/VERSE_2_Scenes_38-51/`  
**Description**: Conductor conducting with rapid, precise movements  
**Scene Position**: Scene 47 of Verse 2 (1:28 mark in video)  
**Purpose**: Show orchestration at maximum power  

---

### Image 5: watermarked_img_4623410740600571935.jpg
**New Name**: `Scene_087_OUTRO_landscape_pullback.jpg`  
**Location**: `00_PRODUCTION/OUTRO_Scenes_77-90/`  
**Description**: Bird's eye aerial view showing entire scene - villages, horde, conductor, cycle  
**Scene Position**: Scene 87 of Outro (2:42 mark in video)  
**Purpose**: Epic finale showing complete situation and eternal cycle  

---

### Image 6: watermarked_img_7334137873320838238.jpg
**New Name**: `Scene_072_CHORUS2_sacrifice_complete.jpg`  
**Location**: `00_PRODUCTION/CHORUS_2_Scenes_70-76/`  
**Description**: Last prisoners falling in silhouette, sacrifice achieved  
**Scene Position**: Scene 72 of Chorus 2 (2:20 mark in video)  
**Purpose**: Show completion of sacrifice arc  

**ALTERNATE**: Could also be `Scene_030_CHORUS1_conductor_hands_closeup.jpg` in `CHORUS_1_Scenes_30-37/` if it shows conducting hands with baton

---

## File Organization Commands

### Windows PowerShell (Run in d:\plague conductor storyboards)

```powershell
# Step 1: Rename the files
Rename-Item -Path "watermarked_img_11104808671304977021.jpg" -NewName "Scene_006_INTRO_conductor_full_reveal.jpg"
Rename-Item -Path "watermarked_img_11601291132558078850.jpg" -NewName "Scene_008_INTRO_horde_rises_mass.jpg"
Rename-Item -Path "watermarked_img_12804009360612180470.jpg" -NewName "Scene_035_CHORUS1_conductor_silhouette.jpg"
Rename-Item -Path "watermarked_img_13277041989482373626.jpg" -NewName "Scene_047_VERSE2_orchestration_peak.jpg"
Rename-Item -Path "watermarked_img_4623410740600571935.jpg" -NewName "Scene_087_OUTRO_landscape_pullback.jpg"
Rename-Item -Path "watermarked_img_7334137873320838238.jpg" -NewName "Scene_072_CHORUS2_sacrifice_complete.jpg"

# Step 2: Move files to their respective folders
Move-Item -Path "Scene_006_INTRO_conductor_full_reveal.jpg" -Destination "00_PRODUCTION\INTRO_Scenes_1-9\"
Move-Item -Path "Scene_008_INTRO_horde_rises_mass.jpg" -Destination "00_PRODUCTION\INTRO_Scenes_1-9\"
Move-Item -Path "Scene_035_CHORUS1_conductor_silhouette.jpg" -Destination "00_PRODUCTION\CHORUS_1_Scenes_30-37\"
Move-Item -Path "Scene_047_VERSE2_orchestration_peak.jpg" -Destination "00_PRODUCTION\VERSE_2_Scenes_38-51\"
Move-Item -Path "Scene_087_OUTRO_landscape_pullback.jpg" -Destination "00_PRODUCTION\OUTRO_Scenes_77-90\"
Move-Item -Path "Scene_072_CHORUS2_sacrifice_complete.jpg" -Destination "00_PRODUCTION\CHORUS_2_Scenes_70-76\"
```

### Windows Command Prompt (Run in d:\plague conductor storyboards)

```batch
REM Step 1: Rename the files
ren "watermarked_img_11104808671304977021.jpg" "Scene_006_INTRO_conductor_full_reveal.jpg"
ren "watermarked_img_11601291132558078850.jpg" "Scene_008_INTRO_horde_rises_mass.jpg"
ren "watermarked_img_12804009360612180470.jpg" "Scene_035_CHORUS1_conductor_silhouette.jpg"
ren "watermarked_img_13277041989482373626.jpg" "Scene_047_VERSE2_orchestration_peak.jpg"
ren "watermarked_img_4623410740600571935.jpg" "Scene_087_OUTRO_landscape_pullback.jpg"
ren "watermarked_img_7334137873320838238.jpg" "Scene_072_CHORUS2_sacrifice_complete.jpg"

REM Step 2: Move files to their respective folders
move "Scene_006_INTRO_conductor_full_reveal.jpg" "00_PRODUCTION\INTRO_Scenes_1-9\"
move "Scene_008_INTRO_horde_rises_mass.jpg" "00_PRODUCTION\INTRO_Scenes_1-9\"
move "Scene_035_CHORUS1_conductor_silhouette.jpg" "00_PRODUCTION\CHORUS_1_Scenes_30-37\"
move "Scene_047_VERSE2_orchestration_peak.jpg" "00_PRODUCTION\VERSE_2_Scenes_38-51\"
move "Scene_087_OUTRO_landscape_pullback.jpg" "00_PRODUCTION\OUTRO_Scenes_77-90\"
move "Scene_072_CHORUS2_sacrifice_complete.jpg" "00_PRODUCTION\CHORUS_2_Scenes_70-76\"
```

---

## Folder Final Structure After Organization

```
plague conductor storyboards/
├── 00_PRODUCTION/
│   ├── INTRO_Scenes_1-9/
│   │   ├── Scene_006_INTRO_conductor_full_reveal.jpg ✓
│   │   └── Scene_008_INTRO_horde_rises_mass.jpg ✓
│   │
│   ├── VERSE_1_Scenes_10-29/
│   │   └── [Empty - awaiting generated images]
│   │
│   ├── CHORUS_1_Scenes_30-37/
│   │   └── Scene_035_CHORUS1_conductor_silhouette.jpg ✓
│   │
│   ├── VERSE_2_Scenes_38-51/
│   │   └── Scene_047_VERSE2_orchestration_peak.jpg ✓
│   │
│   ├── BRIDGE_Scenes_52-69/
│   │   └── [Empty - awaiting generated images]
│   │
│   ├── CHORUS_2_Scenes_70-76/
│   │   └── Scene_072_CHORUS2_sacrifice_complete.jpg ✓
│   │
│   └── OUTRO_Scenes_77-90/
│       └── Scene_087_OUTRO_landscape_pullback.jpg ✓
│
├── 01_SOURCE_AUDIO/
│   └── Plague Conductor.mp3
│
├── 02_REFERENCE/
│   ├── plague conductor lyrics.txt
│   └── plague conductor music video storyboard.md
│
├── 03_PRODUCTION_INDEX/
│   ├── MASTER_IMAGE_INDEX.md
│   ├── SCENE_BREAKDOWN.md
│   └── IMAGE_ORGANIZATION_GUIDE.md (this file)
│
└── [Legacy - can archive/delete]
    └── watermarked_img_*.jpg (original watermarked versions)
```

---

## Naming Convention Reference

**Format**: `Scene_[###]_[SECTION]_[description].jpg`

**Components**:
- `Scene_` = Prefix for clarity
- `###` = Three-digit scene number (001-090) for proper sorting
- `[SECTION]` = INTRO, VERSE1, CHORUS1, VERSE2, BRIDGE, CHORUS2, OUTRO
- `description` = Short descriptive name (snake_case, lowercase)

**Benefits**:
- ✓ Sorts numerically in file explorer
- ✓ Aligns with storyboard scene numbers
- ✓ Quick visual identification
- ✓ Matches markdown references
- ✓ Professional appearance
- ✓ Easy to batch rename if needed

---

## Next Steps

1. **Execute rename & move commands** above to organize your 6 images
2. **Move audio file** to `01_SOURCE_AUDIO/`
3. **Move reference files** to `02_REFERENCE/`
4. **Generate remaining 84 images** using prompts from `plague conductor music video storyboard.md`
5. **Prioritize by tier**: 
   - Tier 1 (existing) ✓ Complete
   - Tier 2 (next 22-24 scenes)
   - Tier 3 (remaining scenes)
6. **Update MASTER_IMAGE_INDEX.md** as new images are added

---

## Production Timeline Example

With 6 images organized:
- **Week 1**: Generate Tier 1 & critical Tier 2 (Bridge, key Verses) = ~30 images
- **Week 2**: Generate remaining Verse and Chorus scenes = ~40 images  
- **Week 3**: Generate detail shots and effects support = ~14 images
- **Week 4**: Edit/compile video, add effects, finalize

**Total Rough Cut**: 4 weeks at 1-2 hours/day

