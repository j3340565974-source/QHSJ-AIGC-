# QHSJ Seedance 反低质(antislop)规则

# Seedance 2.0 — Antislop Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Remove generic AI filler, hollow superlatives, vague language, weak verbs

---

## When to Use This Skill

- Prompt contains **generic AI filler** ("cinematic," "epic," "stunning")
- Prompt has **hollow superlatives** ("beautiful," "amazing," "dramatic")
- Prompt uses **vague language** without physical details
- Prompt has **bloated adjectives** (three synonyms for one quality)
- Prompt has **weak verbs** ("walks dramatically" instead of specific action)
- Prompt needs **sharper production-specific wording**

---

## Core Principle

**Remove filler that hides missing visual decisions.** A strong Seedance prompt uses observable nouns, verbs, camera moves, light sources, sound cues, and constraints. A weak prompt asks for excellence without saying what excellence looks or sounds like.

---

## Intent

Users reach for giant empty words precisely because they care intensely and don't know where to put it. The soul of de-slopping is conservation: every deleted "epic" must come back as a visible choice that holds the same caring. Strip a prompt without honoring the feeling that bloated it, and the user hears that their excitement was wrong.

---

## Visibility Test

**Every major phrase should be:**
- Visible to a camera
- Measurable by a light meter
- Audible in the mix
- Observable as motion

**If a phrase cannot pass that test, replace it with production language.**

| Filler word | Ask what it means | Strong replacement pattern |
|-------------|-------------------|---------------------------|
| **cinematic** | What camera and light make it cinematic? | `locked close-up, warm practical key, cool rim light` |
| **epic** | What is the scale or stake? | `wide low-angle shot, tiny figure against storm wall` |
| **beautiful** | What color, texture, or light behavior? | `pearl highlights on wet ceramic, soft window bounce` |
| **dynamic** | What moves, how fast, and where does it end? | `fast lateral track ending on the hero label` |
| **professional** | What production setup? | `clean commercial tabletop, controlled reflection, no clutter` |
| **dramatic** | What camera angle, lighting, or pause? | `low-angle shot, hard side-light, 3-second held silence` |
| **stunning** | What specific visual quality? | `high-contrast backlight, rim glow on edges` |
| **amazing** | What specific feature? | `macro focus on texture, water droplets catch light` |

---

## The Six Slop Classes

Classify before rewriting — each class has a different repair:

### 1. Empty Evaluators
**Examples:** "cinematic," "epic," "stunning," "amazing," "gorgeous," "breathtaking"

**Problem:** They claim quality without specifying what creates it

**Fix:** Convert each to the **one observable detail** that earns it

❌ "Cinematic lighting"  
✅ "Warm overhead practical light, cool blue rim from window, hard shadows"

❌ "Epic landscape"  
✅ "Wide low-angle shot, mountain 5km distant, tiny figure in foreground"

---

### 2. Borrowed Image-Model Tokens
**Examples:** "8K," "masterpiece," "trending on ArtStation," "highly detailed," "photorealistic"

**Problem:** These are image-gen settings or quality tags, not video production language

**Fix:** **Delete.** Quality and resolution are settings, not prose.

❌ "8K ultra-high-definition masterpiece"  
✅ (Remove entirely, focus on actual production details)

---

### 3. Tag Salad
**Examples:** Comma-separated keyword dumps ported from image prompting

```
woman, red dress, park, sunset, walking, beautiful, dramatic, cinematic, golden hour, flowing hair, emotional
```

**Problem:** No sentence structure, no action arc, no time axis

**Fix:** Rewrite as **shooting-brief prose** — one sentence per element, with action and time

✅ "Woman in red dress walks forward on park path during golden hour sunset. She takes 6 steps at steady pace, hair and dress move with breeze. Camera static 50mm medium shot. 10 seconds."

---

### 4. Negation Slop
**Examples:** "no blur," "no artifacts," "no extra fingers," "no watermark"

**Problem:** **Negation summons** — telling the model what NOT to do often makes it focus on exactly that

**Fix:** Describe what **IS there** instead. Keep negation only in the **constraint slot** if necessary.

❌ "No blurry faces, no distortion, no artifacts"  
✅ "Face sharp and clear, locked camera 85mm, controlled studio lighting"

---

### 5. Adjective Stacking
**Examples:** "beautiful gorgeous stunning woman," "epic dramatic cinematic scene"

**Problem:** Three synonyms for one quality — dilutes attention

**Fix:** Pick the **single detail** that matters

❌ "Beautiful gorgeous stunning dress"  
✅ "Silk dress with pearl highlights, soft drape, burgundy color"

---

### 6. Feel-Suffix Words (Multilingual)
**Examples:**
- Chinese: 电影感 (diànyǐng gǎn - "film feel"), 氛围感 (fēnwéi gǎn - "atmosphere feel")
- Japanese: 雰囲気のある (fun'iki no aru - "has atmosphere")
- Korean: 감성적인 (gamseongjeog-in - "emotional feel")
- Spanish: atmosférico ("atmospheric")
- Russian: атмосферный (atmosferniy - "atmospheric")
- English: "vibey," "moody," "aesthetic"

**Problem:** Vague feeling words without physical cause

**Fix:** Name the **physical cause** of the feeling

❌ Chinese: "电影感的画面" ("film-feel visuals")  
✅ "低角度镜头,暖色实用光源,冷蓝边缘光" ("low-angle shot, warm practical light, cool blue rim light")

❌ English: "Moody and atmospheric"  
✅ "Low light, fog at ground level, single practical lamp, shadow fills 60% of frame"

---

## Rewrite Process

### Step 1: Underline All Slop
Mark every:
- Empty evaluator (cinematic, epic, beautiful)
- Image token (8K, masterpiece)
- Tag salad (comma dumps)
- Negation (no blur, no artifacts)
- Adjective stack (gorgeous stunning)
- Feel-suffix word (vibey, 电影感)

### Step 2: Classify by Slop Class
Determine which of the six classes each marked phrase belongs to.

### Step 3: Decide Replacement Type
Each word should become:
- **Camera** (locked 50mm, dolly forward)
- **Light** (warm overhead practical, cool rim)
- **Motion** (walks 6 steps, hand grips table edge)
- **Material** (brushed aluminum, frosted glass)
- **Sound** (footsteps on gravel, distant bird calls)
- **Constraint** (face must stay sharp, logo preserved)

### Step 4: Reduce Duplicates
If three adjectives mean the same thing, keep one physical detail.

### Step 5: Check Character Budget
Keep prompt concise, preserve reference tags (`@Image1`, `@Video1`).

---

## Example Rewrites

### Example 1: Empty Evaluators

**Original:**
```
Cinematic epic scene of a beautiful woman in a stunning dress walking dramatically through a gorgeous park
```

**Slop identified:**
- Cinematic (empty evaluator)
- Epic (empty evaluator)
- Beautiful (empty evaluator)
- Stunning (empty evaluator)
- Dramatically (weak adverb)
- Gorgeous (empty evaluator)

**Rewritten:**
```
Woman in burgundy silk dress walks forward on gravel path through park. Camera locked 50mm medium shot, walks toward camera. Late afternoon golden hour, sun 20° behind camera, warm front light, soft shadows behind her. She takes 6 steps at steady pace. Sound: footsteps on gravel, distant bird calls. 10 seconds.
```

**What changed:**
- "Cinematic" → specific camera setup (locked 50mm, golden hour, specific sun angle)
- "Beautiful woman" → removed (describe wardrobe/action instead)
- "Stunning dress" → specific material and color (burgundy silk)
- "Dramatically" → specific pacing (6 steps at steady pace)
- "Gorgeous park" → specific sound/environment (gravel path, bird calls)

---

### Example 2: Tag Salad

**Original:**
```
product, glass bottle, white background, studio lighting, rotating, clean, professional, 8K, photorealistic, commercial, high quality
```

**Rewritten:**
```
Glass perfume bottle on white pedestal, controlled studio environment. Camera slow 360° rotation around bottle over 15 seconds, starting front-center, ending front-center. Soft box lighting 45° above, white background, controlled reflections on glass surface. Logo and label visible, sharp. Sound: quiet room tone. Bottle remains centered and static during camera rotation.
```

**What changed:**
- Tag dump → full sentences with action arc
- "8K, photorealistic, high quality" → deleted (settings, not prose)
- "Professional" → specific setup (controlled reflections, clean background)
- "Rotating" → specific camera move (360° rotation over 15 seconds)

---

### Example 3: Negation Slop

**Original:**
```
Character face, no blur, no distortion, no artifacts, no extra fingers, no watermark, clear and sharp
```

**Rewritten:**
```
Character A, medium close-up 85mm, camera locked, faces camera directly. Face sharp and well-lit, controlled studio lighting from 45° above. Hands visible at waist level, simple resting pose. 8 seconds.
```

**What changed:**
- "No blur, no distortion, no artifacts" → positive description (sharp, well-lit, locked camera)
- "No extra fingers" → simple resting pose (avoid complex hand motion)
- "No watermark" → removed (not needed in prompt)

---

### Example 4: Adjective Stacking

**Original:**
```
Beautiful gorgeous stunning amazing dress with incredible fantastic wonderful colors
```

**Rewritten:**
```
Silk evening dress in deep burgundy with pearl highlights, soft drape, reaches floor length
```

**What changed:**
- 7 adjectives (beautiful, gorgeous, stunning, amazing, incredible, fantastic, wonderful) → 0
- Added specific details: material (silk), color (deep burgundy), texture (pearl highlights, soft drape), length (floor length)

---

### Example 5: Feel-Suffix Words (Chinese)

**Original (Chinese):**
```
电影感的夜景,氛围感很强,很有情绪
```
(Film-feel night scene, strong atmosphere feel, very emotional)

**Rewritten:**
```
城市夜景,低角度镜头。暖黄路灯光,冷蓝背景。湿润路面反射灯光。镜头缓慢推进,15秒。环境音:远处车流,雨滴落在地面。
```
(Urban night scene, low-angle shot. Warm yellow streetlight, cool blue background. Wet pavement reflects lights. Camera slow push-in, 15 seconds. Ambient sound: distant traffic, raindrops on ground.)

**What changed:**
- "电影感" (film-feel) → specific camera (low-angle, slow push-in)
- "氛围感很强" (strong atmosphere feel) → specific lighting (warm yellow streetlight, cool blue background, wet reflections)
- "很有情绪" (very emotional) → specific sound (distant traffic, rain)

---

## Do Not Over-Correct

**Keep useful genre/period language when paired with concrete direction.**

✅ **Good:** "Film noir hallway with hard venetian-blind shadows, high-contrast black and white"  
❌ **Over-corrected:** (Remove "film noir" entirely)

✅ **Good:** "1970s documentary texture, 16mm film grain, muted earth tones"  
❌ **Over-corrected:** (Remove "1970s documentary" entirely)

**Keep terms that communicate:**
- Medium (2D animation, stop-motion, live action)
- Era (1970s, Victorian, Edo-period)
- Palette (monochrome, pastel, neon)
- Lens behavior (shallow focus, wide-angle distortion)

---

## Anti-Patterns

❌ **Replacing one vague word with another vague word:**  
"Cinematic" → "Artistic"  
→ Both are empty. Use physical details instead.

❌ **Removing all descriptive language:**  
Original: "Beautiful woman in stunning dress"  
Over-corrected: "Woman in dress"  
→ Keep specific details: "Woman in burgundy silk dress"

❌ **Adding more empty words to fix emptiness:**  
"Cinematic" → "Very cinematic and ultra-professional"  
→ This makes it worse

---

## Output Structure

When de-slopping a prompt, return:

1. **Removed words** (list of slop identified)
2. **Replacements grouped by type:**
   - Camera: [specific camera details]
   - Light: [specific light sources]
   - Motion: [specific actions with timing]
   - Sound: [specific audio details]
   - Constraints: [what must stay unchanged]
3. **Tightened prompt** (final clean version)

---

## Summary

**De-slop workflow:**
1. Mark all empty evaluators, image tokens, tag salad, negations, adjective stacks, feel-suffix words
2. Classify by slop class (1-6)
3. Replace each with observable camera/light/motion/material/sound/constraint
4. Reduce duplicates (one detail, not three synonyms)
5. Keep useful genre/period language when concrete

**Key principle:** Every deleted "epic" must come back as a visible choice that holds the same caring.

---

**Related skills:** seedance-prompt, seedance-troubleshoot, seedance-style
