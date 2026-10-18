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
