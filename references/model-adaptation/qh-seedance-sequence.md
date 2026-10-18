# QHSJ Seedance 序列/多镜

# Seedance 2.0 — Sequence Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Multi-clip sequencing, shot connectivity, continuity planning

---

## When to Use This Skill

- User asks to break a **long video idea** (>20s) into a sequence of clips
- User provides a **screenplay, storyboard, or narrative outline** to turn into Seedance clips
- User wants **continuity between shots** (I2V seeding, character handoff, environment consistency)
- User asks for **shot list** or **sequence breakdown** for a multi-scene story

---

## Core Principle

Seedance 2.0 has a **~20-second native generation limit** per clip. Longer narratives require **sequencing**: breaking the story into connected clips where each clip's end frame seeds the next clip's start (I2V workflow).

**Key constraints:**
- Each clip = **one camera setup** (lens, angle, movement)
- Each clip = **one lighting condition** (time-of-day, mood, color)
- **Transitions happen between clips**, not within a single prompt
- **Character poses and environment state** must be described consistently across clips

---

## Workflow

### 1. Director's Read (Narrative Analysis)

Before writing prompts, analyze the user's story with these fields:

```
Subject: [who/what is the focus across the sequence]
Core Action: [the through-line event spanning multiple clips]
Scene: [environment, location, props that persist]
Emotional Arc: [how mood/energy changes across clips]
Key Transitions: [where camera, lighting, or action shifts]
Continuity Anchors: [character wardrobe, props, environment details that must stay consistent]
Audio Through-Line: [dialogue, music, or sound that spans clips]
Pacing: [which clips are slow/fast, where tension builds]
Constraints: [technical limits — actor count, VFX load, lighting complexity]
Output Intent: [trailer, full scene, vertical social clip, etc.]
```

### 2. Shot Breakdown

Divide the narrative into **clips of 15-20 seconds each**. For each clip, specify:

- **Clip number** and **duration estimate**
- **Camera setup** (lens, angle, movement)
- **Lighting condition** (time, mood, color temperature)
- **Subject state** (pose, expression, wardrobe)
- **Action** (what changes during this clip)
- **Continuity notes** (what must match the previous/next clip)
- **I2V seed strategy** (if this clip uses the prior clip's end frame as input)

**Example:**

```
Clip 1 (18s): Wide establishing shot, 35mm, dolly forward
- Morning golden light, soft shadows
- Character enters frame left in red coat, neutral expression
- Ends with character centered, hand reaching for door handle
- I2V seed: none (T2V generation)

Clip 2 (16s): Medium shot, 50mm, static
- Same golden light, now character is indoors (light through window)
- I2V seed: Clip 1 end frame (character hand on door handle, red coat visible)
- Action: character opens door, steps inside, closes door
- Ends with character back to camera, door closed

Clip 3 (20s): Close-up, 85mm, slow push-in
- Interior lighting, warm practicals, blue hour window light
- I2V seed: Clip 2 end frame (character back to camera, red coat, closed door)
- Action: character turns to face camera, slow zoom to face
- Ends with character's face filling frame, subtle smile
```

### 3. Prompt Writing for Each Clip

Use the **seedance-prompt** skill structure for each clip:

```
[Subject description, wardrobe, pose] + [Action verbs, motion path, timing] + [Scene details, props, spatial layout] + [Camera: lens, angle, movement] + [Lighting: time-of-day, quality, color] + [Audio: dialogue, music, effects] + [Constraints: no cuts, no new characters mid-clip]
```

**Continuity checklist for each prompt:**
- Match **wardrobe, hair, accessories** from prior clip
- Match **environment state** (door open/closed, object positions)
- Match **lighting continuity** (if same location/time)
- Specify **I2V seed image** if using prior clip's end frame

### 4. I2V Seeding Strategy

When a clip should **continue from the previous clip**, use **I2V workflow**:

- Extract the **final frame** of Clip N
- Use it as the **seed image** for Clip N+1
- In Clip N+1's prompt, describe the **starting state** (character pose, environment) to match the seed image
- Then describe the **action/change** that happens in Clip N+1

**Example I2V prompt (Clip 2 seeded from Clip 1):**

```
A woman in a red wool coat, hand on a brass door handle, standing at a wooden door, neutral expression. She pushes the door open, steps across the threshold into a warmly lit interior hallway, and closes the door behind her with her left hand. The door closes fully as she takes two steps forward, back to camera. Hallway has warm yellow sconces and a blue-hour window at the far end. Camera static, 50mm lens, eye-level medium shot. Continuous motion, no cuts.
```

**Seed image:** Final frame of Clip 1 (woman's hand on door handle, red coat visible)

---

## Handling Transitions

**Camera transitions** (wide → close-up, pan → static) happen **between clips**, not within.

- **Cut:** End Clip 1 with subject in position A. Start Clip 2 with subject in same position A, new camera angle.
- **Match-cut:** End Clip 1 with a visual motif (hand gesture, object). Start Clip 2 with same motif in new context.
- **Time-skip:** End Clip 1 at moment X. Start Clip 2 at moment X+5 minutes, describe environment changes (lighting shift, new props).

**Do NOT prompt for:**
- "Camera transitions from wide to close-up" (Seedance renders one camera setup per clip)
- "Cut to..." (transitions happen in editing, not in the prompt)

---

## Pacing and Timing

**Seedance 2.0 default pacing:** ~20 seconds of **continuous motion**. To control pacing:

- **Slow moment:** "Character moves slowly, each step deliberate, 3 seconds per gesture"
- **Fast moment:** "Character sprints across the frame in 4 seconds, camera whip-pan to follow"
- **Pause/beat:** "Character stops mid-frame for 2 seconds, expression shifts from neutral to concerned, then resumes walking"

**Do NOT use vague pacing words:**
- ❌ "Cinematic pacing" (hollow, ambiguous)
- ❌ "Dramatic timing" (non-specific)
- ✅ "Action completes in 6 seconds, then 3-second hold on character's face"

---

## Continuity Anchors

To maintain **character/environment consistency** across clips:

**Character anchors:**
- Wardrobe: "red wool coat, black boots, silver watch on left wrist"
- Hair: "shoulder-length black hair in low ponytail, loose strands framing face"
- Props: "leather satchel over right shoulder, brass keyring in right hand"

**Environment anchors:**
- Fixed objects: "wooden door with brass handle, white plaster walls, terracotta floor tiles"
- Lighting: "morning golden hour, sun 20° above horizon, soft shadows 3 meters long"
- Spatial layout: "door on left side of frame, hallway extends 8 meters to window at far end"

**Repeat anchors in each prompt** to prevent model drift.

---

## Anti-Patterns

❌ **One prompt for a 60-second narrative**  
→ Split into 3-4 clips of 15-20s each

❌ **"Camera pans, then cuts to close-up, then transitions to..."**  
→ One camera move per clip; transitions happen between clips

❌ **No continuity notes between clips**  
→ Every clip must describe starting state (pose, wardrobe, environment) even if "unchanged"

❌ **I2V seeding without state description**  
→ I2V prompt must describe the seed image's visible state (pose, objects) before describing new action

❌ **Vague sequence descriptions: "Then the story continues..."**  
→ Specify exact action, camera, lighting for each clip

---

## Example Workflow: 60-Second Trailer Sequence

**User request:** "A samurai walks through a village at dawn, enters a tea house, and faces an opponent. Make it 60 seconds."

**Step 1: Director's Read**

```
Subject: lone samurai, dark blue hakama, katana at waist
Core Action: journey from village street → tea house interior → confrontation
Scene: Edo-period village, wooden buildings, stone path, paper lanterns
Emotional Arc: calm → anticipation → tension
Key Transitions: exterior→interior at 30s mark, lighting warm→cool
Continuity Anchors: samurai wardrobe (blue hakama, katana), tea house door (red frame, paper screen)
Audio: footsteps on stone, sliding door, shamisen underscore
Pacing: slow build, final 15s accelerates
Constraints: 1 character until final clip (opponent reveal)
Output Intent: vertical trailer for social
```

**Step 2: Shot Breakdown**

```
Clip 1 (20s): Establishing wide, samurai enters village street
Clip 2 (18s): Medium tracking shot, samurai walks to tea house door
Clip 3 (12s): Close-up, samurai hand opens door, steps inside
Clip 4 (10s): Interior wide, opponent visible across tea house
```

**Step 3: Prompts**

**Clip 1 (T2V):**
```
A lone samurai in dark blue hakama and white gi, katana sheathed at left waist, walks slowly down a stone-paved village street at dawn. Wooden buildings with thatched roofs line both sides, paper lanterns glow softly in blue pre-dawn light. He walks toward camera, each step deliberate, sandals clicking on stone, mist swirling at knee-height. Camera wide-angle 24mm, static low angle, 1 meter off ground. Golden hour just beginning, cool blue shadows, warm orange edge-light from horizon. 20 seconds of continuous forward motion, no cuts. Footsteps and distant crow caw, shamisen underscore fades in.
```

**Clip 2 (I2V from Clip 1 end frame):**
```
The samurai in dark blue hakama, now 3 meters from camera, continues walking forward on the stone path toward a red-framed tea house with paper screen doors. His right hand rests on katana hilt as he approaches. Camera dollies backward at same pace as his walk, maintaining medium shot framing, 50mm lens, eye-level. Dawn light intensifies to warm golden hour, long shadows stretch behind him. He stops 1 meter from the tea house door, hand moves to door frame. 18 seconds, continuous motion, shamisen grows louder.
```

**Clip 3 (I2V from Clip 2 end frame):**
```
Close-up on the samurai's hand, calloused palm and fingers, pressing against the red wooden door frame of the tea house. The paper screen door slides open slowly from right to left, revealing a dim interior with warm orange lantern light. Camera static 85mm macro, focused on hand and door mechanism. Blue dawn exterior light contrasts with warm interior glow. Hand completes slide, door opens fully, samurai's blue hakama edge enters frame as he steps across threshold. 12 seconds, slow deliberate motion, door slide sound and shamisen peak.
```

**Clip 4 (I2V from Clip 3 end frame):**
```
Interior of the tea house, warm orange paper lantern light, low wooden table in center. The samurai in blue hakama stands just inside the doorway, back to camera, morning light silhouetting him from behind. Across the table, 4 meters away, another figure sits in shadow—opponent in black hakama, katana visible, face obscured. The samurai takes one slow step forward, hand moves to katana hilt. Camera static wide-angle 28mm, low angle from behind tea table. Warm practicals overhead, blue backlight from door. 10 seconds, tension hold, shamisen cuts to silence, then single shakuhachi note.
```

---

## Troubleshooting Sequence Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Character wardrobe changes between clips | No continuity anchors in prompts | Repeat exact wardrobe description in every clip |
| Lighting inconsistency (same scene, different light) | Each clip uses vague lighting terms | Lock time-of-day + sun angle + color temp across clips |
| I2V clip doesn't match seed image | Prompt doesn't describe seed image state | Start I2V prompt by describing seed image's visible state |
| Environment drifts (tea house becomes tavern) | No spatial anchors | Repeat key environment details (wall color, floor type, props) |
| Pacing feels rushed or uneven | No timing specified per action | Add "X completes in N seconds, holds for M seconds" |
| Action breaks continuity (character teleports) | Action start/end poses not specified | End each clip with exact pose, start next clip with same pose |

---

## Summary

**Sequence workflow:**
1. Analyze narrative with Director's Read
2. Break into 15-20s clips, one camera setup each
3. Specify continuity anchors (wardrobe, environment, lighting)
4. Write prompts using seedance-prompt structure + I2V seeds
5. Define transitions between clips (not within prompts)
6. Add timing for pacing control

**Key principle:** Each clip is **self-contained** but **anchored to prior/next clips** via I2V seeding and continuity description.

---

**Related skills:** seedance-prompt, seedance-continuation, seedance-characters, seedance-pipeline
