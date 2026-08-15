# 🎬 PLAGUE CONDUCTOR - AGENT BRIEFING

Copy and paste the command below to your autonomous agent:

---

## **AGENT TASK BRIEF** (Copy This)

```
I've set up a music video production pipeline on GitHub at: https://github.com/plague-dr-general/Plague-Conductor

Your Task: Generate AI imagery for a dark metal music video.

Current Status: 15/90 scenes complete. Need to generate 6 BRIDGE images next.

Step-by-step:
1. Read AGENT_INSTRUCTIONS.md in the repo (contains everything)
2. Open 03_PRODUCTION_INDEX/01_BRIDGE_CHAOS_6IMAGES.md 
3. Copy all 6 prompts from the "EXECUTION INSTRUCTIONS" section
4. Generate each image using DALL-E 3 or Midjourney
5. Save with exact filenames: Scene_052_BRIDGE_*.jpg through Scene_067_BRIDGE_*.jpg
6. Move all 6 images to: 00_PRODUCTION/BRIDGE_Scenes_52-69/
7. Run: python create_video_smart.py (auto-compiles video)
8. Run: git add . && git commit -m "Add Bridge batch images" && git push

Success: Video should compile to 21 images (55+ seconds) and push to GitHub.

After finishing Batch 2, Batch 3 (VERSE_1 - 8 images) is ready in BATCH_3_VERSE1_READY.md
```

---

## **SHORT VERSION** (If Agent Prefers Brief)

```
Repo: https://github.com/plague-dr-general/Plague-Conductor
Read: AGENT_INSTRUCTIONS.md
Generate: Batch 2 (6 BRIDGE images using prompts in 01_BRIDGE_CHAOS_6IMAGES.md)
Save: Scene_### format to BRIDGE_Scenes_52-69 folder
Run: python create_video_smart.py then git push
```

---

## **Quick Reference**

| What | Command/Location |
|------|------------------|
| Repo Link | https://github.com/plague-dr-general/Plague-Conductor |
| Instructions | AGENT_INSTRUCTIONS.md |
| Current Batch | 01_BRIDGE_CHAOS_6IMAGES.md (6 images) |
| Next Batch | BATCH_3_VERSE1_READY.md (8 images) |
| Video Compile | `python create_video_smart.py` |
| Push to GitHub | `git add . && git commit -m "Add Bridge batch images" && git push` |
| Save Location | `00_PRODUCTION/BRIDGE_Scenes_52-69/` |
| Filename Format | `Scene_###_BRIDGE_[description].jpg` |

---

## **Agent Checklist**

- [ ] Read AGENT_INSTRUCTIONS.md
- [ ] Open 01_BRIDGE_CHAOS_6IMAGES.md
- [ ] Copy 6 prompts
- [ ] Generate 6 images (DALL-E 3 or Midjourney)
- [ ] Save with Scene_### filenames
- [ ] Move to BRIDGE_Scenes_52-69 folder
- [ ] Run: `python create_video_smart.py`
- [ ] Run: `git add . && git commit -m "Add Bridge batch images" && git push`
- [ ] Verify video compiled (55+ seconds)
- [ ] Ready for Batch 3

---

Generated: 2026-08-14
Production Status: 15/90 scenes (17% complete)
Next Milestone: 21/90 scenes (23% complete) after Bridge batch
