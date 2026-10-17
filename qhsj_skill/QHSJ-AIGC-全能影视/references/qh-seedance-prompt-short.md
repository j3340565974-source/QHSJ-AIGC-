# QHSJ Seedance 短视频提示词

# Seedance 2.0 — Prompt Short Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Prompt compression, compact prompts, Chinese short prompts, remove unnecessary language

---

## When to Use This Skill

- User asks for **compact prompt** or **short prompt**
- User wants **Chinese short prompt** (30-100 characters)
- User requests **prompt compression**
- User wants **removal of unnecessary language**
- User asks for **30-100 word output**
- User needs **minimal prompt** while preserving production signal

---

## Core Principle

**Compress without losing the production signal.** A short prompt still needs mode, subject, action, camera, light, sound (when useful), and constraints. Remove filler before removing physical details.

---

## Intent

Compression is an act of judgment about what the user loves most. What survives the cut is the soul of their shot; everything else goes first. If the user would mourn a deleted word, it was never filler.

---

## Compression Priority

**Preserve in this order:**

1. **Reference tags and their role** (`@Image1`, `@Video1`, `@Audio1`)
2. **Subject or product identity** (character name, product features)
3. **Action verb and visible endpoint** (what happens, where it ends)
4. **One camera move** (locked, dolly, pan — pick one)
5. **Physical light source or atmosphere** (golden hour, studio light)
6. **Audio cue or silence instruction** (dialogue, ambient sound)
7. **Safety, IP, or continuity constraint** (preserve logo, lock face)
8. **Sequence state clauses** (opening state, continuity locks, completed beats)

**Delete first:**
- Generic adjectives (beautiful, amazing, stunning)
- Duplicate style labels (cinematic epic dramatic)
- Obvious background details (trees sway, clouds move)
- Secondary camera moves (if you have dolly + pan, keep one)
- Secondary actions (if character does 3 things, keep the main one)

---

## Compact Templates

### T2V (Text-to-Video)
```
[Subject] [action and endpoint] in [scene]. Camera: [one move]. Light: [physical source]. Sound: [cue]. Constraint: [risk/continuity].
```

**Example:**
```
Woman in red coat walks forward 6 steps on park path. Camera static 50mm. Golden hour, sun behind camera. Sound: gravel footsteps. 10s.
```

---

### I2V (Image-to-Video)
```
@Image1 preserved; only [motion/light/camera] changes. Camera: [one move]. Sound: [cue]. Constraint: [what must not change].
```

**Example:**
```
@Image1 preserved; add hand motion only. Hand lifts coffee mug 10cm upward. Camera locked 85mm. Sound: ceramic scrape. Face/logo unchanged.
```

---

### V2V (Video-to-Video / Reference Motion)
```
@Video1 controls [motion/camera/timing] only; new subject [anchor]. [Action]. Do not transfer [identity/scene/logo].
```

**Example:**
```
@Video1 camera movement only; new subject: man in black suit. Walks forward 8 steps, urban street. Do not transfer @Video1 person/clothing.
```

---

### Chinese Compact Prompt
```
@Image1为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。声音：[提示]。
```

**Example:**
```
@Image1为参考，严格保持女性面部和红色外套不变；仅加入向前行走6步动作。镜头：静态50mm中景。黄金时段光线，太阳在镜头后方。声音：碎石路脚步声。10秒。
```

---

## Compression Examples

### Example 1: Long to Short (English)

**Original (150 words):**
```
A beautiful woman in a stunning red wool coat with brass buttons and black leather boots walks dramatically forward along a gravel path through a gorgeous park during late afternoon golden hour. The camera remains static using a 50mm lens at eye level in a medium shot as she approaches. The warm golden sunlight comes from approximately 20 degrees above the horizon behind the camera, creating soft shadows that stretch behind her. Her arms swing naturally by her sides as she takes exactly 6 steps at a steady, deliberate pace. The sound design includes her footsteps crunching on the gravel path in a steady rhythm, accompanied by distant bird calls and a light breeze rustling through the trees. The clip should be approximately 10 seconds in duration with continuous motion and no cuts. Her face and wardrobe must remain exactly as shown in the reference image.
```

**Compressed (48 words):**
```
@Image1 reference; preserve face, red coat, black boots exactly. Woman walks forward 6 steps on gravel path. Camera static 50mm medium shot, eye-level. Golden hour, sun 20° behind camera, soft shadows. Sound: gravel footsteps, distant birds, breeze. 10 seconds continuous motion.
```

**What was removed:**
- "Beautiful," "stunning," "gorgeous" (generic adjectives)
- "Dramatic" (weak adverb)
- "Brass buttons," "leather" (secondary wardrobe details kept in @Image1 reference)
- "Arms swing naturally" (obvious motion)
- "Steady deliberate pace" (redundant with "6 steps")
- "No cuts" (implied by "continuous motion")

**What was kept:**
- Reference tag and preservation
- Core action (walks forward 6 steps)
- Camera setup (static 50mm medium)
- Light source (golden hour, sun angle)
- Sound cues (footsteps, birds, breeze)
- Duration (10 seconds)

---

### Example 2: Product Prompt Compression

**Original (120 words):**
```
A premium glass perfume bottle sits elegantly on a pristine white marble pedestal in a clean, professional studio environment with carefully controlled lighting. The camera performs a smooth, slow 360-degree rotation around the bottle over the course of exactly 15 seconds, starting at the front-center position and ending at the same front-center position. Soft box lighting is positioned at approximately 45 degrees above the product, creating beautiful controlled reflections on the glass surface without any harsh shadows. The white background remains perfectly clean and uncluttered. The brand logo and product label remain sharp, clear, and highly visible throughout the entire rotation. The sound design consists only of quiet, subtle room tone with no music or sound effects. The bottle itself remains perfectly centered and completely static while only the camera rotates around it.
```

**Compressed (42 words):**
```
Glass perfume bottle on white pedestal. Camera 360° rotation, 15s, starts/ends front-center. Soft box 45° above, controlled reflections, white background. Logo/label sharp and visible. Sound: quiet room tone. Bottle static, camera moves only.
```

---

### Example 3: Chinese Prompt Compression

**Original (Chinese, 180+ characters):**
```
一位美丽的年轻女性，穿着华丽的红色羊毛大衣和黑色皮靴，在公园的碎石小路上充满戏剧性地向前行走。镜头使用50毫米镜头保持静态，在眼睛高度拍摄中景画面。温暖的黄金时段阳光从镜头后方大约地平线以上20度的位置照射过来，在她身后形成柔和的阴影。她以稳定的步伐向前走了整整6步，双臂在身体两侧自然摆动。音效设计包括她的脚步声在碎石路上发出有节奏的嘎吱声，伴随着远处的鸟鸣声和轻微的微风吹过树木的声音。整个片段大约10秒钟，持续运动，没有剪辑。她的面部和服装必须与参考图像完全一致。
```

**Compressed (Chinese, 68 characters):**
```
@Image1为参考，保持面部、红色外套、黑靴不变。女性碎石路上向前走6步。镜头静态50mm中景。黄金时段光，太阳在镜头后20度。声音：脚步声、鸟鸣、风声。10秒。
```

---

## Bilingual Compression

**When to use mixed language:**
- Reference tags remain in English (`@Image1`, not `@图片1`)
- Technical camera terms often stay in English (50mm, 4K)
- Dialogue stays in target language
- Core action/scene in target language

**Example (Chinese with English references):**
```
@Image1为产品参考，严格保持logo和瓶身形状。旋转镜头360°,15秒。柔光45°从上方。声音：安静环境音。
```

---

## Sequence Compression

**When compressing continuation prompts, preserve:**
1. **Actual opening state** (from observed end of previous clip)
2. **Continuity locks** (wardrobe, identity, environment)
3. **Completed beat exclusions** (don't repeat what already happened)
4. **Reserved future beats** (don't leak future action)

**Example sequence compression:**

*Clip 2 continuing from Clip 1:*

**Full prompt:**
```
Character A in red coat (from previous clip) stands at door, hand already on brass handle (end state of Clip 1). She pushes door open, steps inside with right foot first, left foot follows. Door swings to 90° open. Interior hallway with warm sconces visible. Camera continues 50mm static. Morning light from outside mixes with interior warm light. Sound: door creak, footsteps. 14 seconds. Completed: hand reaching for handle (Clip 1). Reserved: character turning to face camera (Clip 3).
```

**Compressed:**
```
Character A (red coat), hand on brass handle, pushes door 90° open, steps inside (right foot, left foot). Interior hallway, warm sconces. Camera 50mm static. Morning + interior light. Sound: door creak, footsteps. 14s. Exclude: hand-reaching (done). Reserve: face-turn.
```

---

## Anti-Patterns

❌ **Compressing away constraints:**  
Original: "Preserve logo exactly as shown in @Image1"  
Over-compressed: (removed entirely)  
→ This breaks identity lock. Keep constraints.

❌ **Compressing away the action endpoint:**  
Original: "Character walks forward 6 steps, stops 2 meters from camera"  
Over-compressed: "Character walks"  
→ No endpoint = model decides when to stop

❌ **Removing reference tags:**  
Original: "@Image1 is character reference; preserve face and wardrobe"  
Over-compressed: "Character in red coat"  
→ Without @Image1, identity will drift

❌ **Compressing physical details into generic words:**  
Original: "Golden hour, sun 20° behind camera, soft front light"  
Over-compressed: "Nice lighting"  
→ "Nice" is meaningless. Keep physical details.

---

## Output Structure

When compressing a prompt, return:

1. **Compact prompt** (30-100 words, or ~50-80 Chinese characters)
2. **One-line note** (only if something important was removed)

**Example output:**

*Compact prompt:*
```
@Image1 preserved. Woman walks forward 6 steps, gravel path. Camera static 50mm. Golden hour, sun behind. Sound: footsteps, birds. 10s.
```

*Note: Removed generic adjectives ("beautiful," "stunning") and redundant motion details. All essential production elements preserved.*

---

## Summary

**Compression workflow:**
1. Identify essential elements (reference tags, subject, action, camera, light, sound, constraints)
2. Remove generic adjectives first
3. Remove duplicate style labels
4. Remove obvious background details
5. Keep one camera move (delete secondary moves)
6. Keep main action (delete secondary actions)
7. Preserve constraints (identity locks, continuity)
8. Target 30-100 words (English) or ~50-80 characters (Chinese)

**Key principle:** What survives the cut is the soul of the shot. Remove filler before physical details.

---

**Related skills:** seedance-prompt, seedance-antislop, seedance-vocab-zh
