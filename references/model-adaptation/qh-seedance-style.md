# QHSJ Seedance 风格

# Seedance 2.0 — Style Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Visual style, art direction, render feel, period aesthetic, texture, animation style, realism level

---

## When to Use This Skill

- User asks for **visual style** or **art direction**
- User wants **specific aesthetic** (cyberpunk, retro, documentary, commercial)
- User mentions **render feel** (photorealistic, stylized, hand-drawn, clay)
- User requests **period aesthetic** (1970s film, Edo-period, Victorian)
- User wants **texture** or **material feel** (film grain, watercolor, glass, metal)
- User asks for **animation style** (2D, stop-motion, 3D render)
- User references **studio/franchise names** (needs safe rewrite)

---

## Core Principle

**Style Safety Rule:** Do NOT use studio, franchise, artist, or living-creator names as style anchors unless the user has clearly authorized workflow.

Instead, preserve the intended visual function by describing:
- **Medium** (live action, 2D, 3D, stop-motion, miniature)
- **Texture** (film grain, watercolor, clay, paper, metal, glass)
- **Palette** (warm/cool, saturated/muted, specific colors)
- **Lighting** (hard/soft, natural/artificial, color temperature)
- **Composition** (symmetrical, rule-of-thirds, centered, dynamic)
- **Era cues** (1970s texture, Victorian detail, retro tech)
- **Motion rhythm** (smooth, staccato, elastic, realistic weight)

---

## Intent

Users point at art they love and ask to stand near it. Honor the love while refusing the theft: find what the love is made of (light, texture, rhythm, era) and rebuild it as something the user owns.

---

## Style Safety Rewrites

When user references protected names, translate into production descriptors:

| User intent | Safe production descriptor |
|---|---|
| Cozy hand-drawn fantasy | `hand-painted 2D animation, soft watercolor backgrounds, rounded character silhouettes, warm pastel palette, gentle parallax` |
| Sharp cyberpunk action | `neon noir city, wet pavement reflections, high-contrast magenta and cyan light, fast lateral tracking, angular silhouettes` |
| Premium product realism | `clean commercial realism, controlled reflections, shallow depth of field, neutral background, polished material detail` |
| Retro documentary | `1970s documentary texture, muted film grain, practical daylight, handheld observational framing` |
| Children's animation | `soft clay-like characters, simple expressive faces, bright primary palette, bouncy squash-and-stretch motion` |
| Vintage film noir | `high-contrast black and white, hard side-lighting, venetian blind shadows, cigarette smoke haze, 1940s wardrobe` |
| Modern commercial | `clean white studio, soft box lighting, minimal shadows, polished surfaces, slow turntable rotation` |

---

## Layered Style Method

Separate style into **layers** instead of one broad label:

### 1. Medium
What is the production method?
- Live action, stop-motion, 2D animation, 3D render, miniature photography, paper cutout, clay animation

### 2. Surface Texture
What material feel?
- Film grain, watercolor bleed, paper texture, brushed metal, frosted glass, fabric weave, clay fingerprints

### 3. Palette
What color strategy?
- Warm (orange, yellow, red), cool (blue, cyan, teal), muted pastels, high-contrast, monochrome, sodium orange, neon

### 4. Camera/Render Behavior
How does the lens/render behave?
- Shallow depth of field, macro focus, orthographic (no perspective), handheld sway, locked tripod, fish-eye distortion

### 5. Motion Rhythm
How does motion feel?
- Smooth realistic, bouncy squash-and-stretch, staccato stop-motion, elastic cartoon physics, slow-motion grace

**Example layered style:**

```
Medium: Live action product photography
Surface: Polished glass and brushed aluminum
Palette: Cool blue-grey with warm accent light
Camera: Macro 100mm, shallow focus, locked tripod
Motion: Slow turntable rotation, 15 seconds per 360°
```

---

## Source-Look Lock

Realism styles stabilize when you **name the capture source** and **embrace its artifacts** instead of fighting them.

| Source look | Lock its artifacts |
|---|---|
| Phone-shot daily / UGC | `vertical handheld phone footage, slight grip sway, auto-exposure shifts, ambient room sound` |
| Livestream | `fixed webcam framing, flat ring light, mild compression, real-time caption pacing` |
| Security / dashcam | `locked high-angle camera, timestamp burn-in feel, low-light noise, no camera response to events` |
| Vintage film | `grainy film texture, gate weave, halation around highlights, era-correct contrast` |
| Studio commercial | `controlled reflections, clean background, polished material detail, zero handheld motion` |
| 1990s camcorder | `interlaced scan lines, blown-out highlights, auto-focus hunt, date stamp lower right` |
| Documentary 16mm | `film grain, hand-cranked feel, natural light, observational distance` |

**Key insight:** The flaw vocabulary IS the style. Faux-UGC that looks too clean reads as fake twice over.

---

## Hybrid Style Rule

If user asks for a **hybrid** style, assign each style to a specific layer:

**Example:** "Live-action product photography with illustrated UI overlays"

- **Product layer:** Clean commercial realism, controlled reflections, shallow depth of field
- **UI overlay layer:** Flat 2D vector illustration, bright cyan and yellow, simple line icons

Keep **character design, environment, lighting, and VFX in compatible registers**. Don't mix photorealistic humans with clay environments unless intentionally surreal.

---

## 2D Animation Grammar

When style is **2D, anime, or cel-based**, follow these rules:

**No lens behavior:** 2D animation doesn't have depth of field, lens distortion, or bokeh unless explicitly painted. Don't prompt for "shallow focus" or "wide-angle lens" in stylized 2D work.

**Layer grammar:**
- Foreground, mid-ground, background move at different speeds (parallax)
- Held frames (character still, background moves)
- Burst motion (fast action with smears/impact frames)

**Motion:**
- **Held animation:** Character pose holds for 3-5 frames, then snaps to next pose
- **Smears:** Fast motion shows elongated blur shapes between keyframes
- **Impact frames:** Single high-contrast frame at moment of contact (punch, landing)

---

## Period Aesthetic Cues

When user wants a **period look**, specify era-correct details:

**1970s documentary:**
- `16mm film grain, muted earth tones, practical daylight, handheld observational framing, analog audio warmth`

**Victorian era:**
- `gaslight warm yellow glow, heavy drapery, ornate wood furniture, high-collar wardrobe, dust motes in window light`

**1980s commercial:**
- `oversaturated color, soft focus glow, pastel wardrobe, geometric patterns, synth underscore`

**Edo-period Japan:**
- `paper lantern warm light, wooden architecture, tatami texture, indigo and earth-tone wardrobe, natural fiber fabrics`

---

## Continuity and Style Inheritance

When working in a **sequence** (multi-clip story):

- **Inherit medium grammar** from previous clips (don't switch from live action to 2D mid-sequence)
- **Lock canonical design** (character appearance, wardrobe, environment)
- **Maintain lighting continuity** (time-of-day, color temperature)
- **Match motion rhythm** (if Clip 1 was smooth, Clip 2 shouldn't be staccato)

**Style may color the clip, but cannot change:**
- Character identity or wardrobe
- Product design (for commercial work)
- Environment architecture
- Events reserved for future clips

---

## Example Style Prompts

### Example 1: Cozy Hand-Drawn Fantasy
```
Hand-painted 2D animation, soft watercolor backgrounds with visible brush texture, rounded character silhouettes, warm pastel palette (peach, lavender, mint green), gentle parallax scrolling, held animation with 3-frame poses, no lens effects. A young traveler in cream cloak walks through a forest clearing, sunlight filters through leaves in painted rays. Gentle music-box melody.
```

### Example 2: Cyberpunk Street Scene
```
Neon noir city street at night, wet black pavement reflects magenta and cyan neon signs, steam rises from grates, angular building silhouettes against dark sky. High-contrast lighting, hard shadows. Camera fast lateral tracking at street level, 35mm lens. Character in black jacket and reflective visor walks through frame, puddles ripple. Synth bass underscore, rain hiss.
```

### Example 3: Vintage 1970s Documentary
```
16mm film grain, muted color palette (olive, rust, mustard yellow), practical daylight through large windows, handheld observational camera, slight breathing motion. Interior of 1970s office, wood-paneled walls, rotary phone on desk, typewriter. Person in brown polyester suit reviews paperwork. Ambient room tone, analog warmth.
```

### Example 4: Clean Product Commercial
```
Clean white studio background, soft box lighting from 45° above, minimal shadows, controlled reflections on polished aluminum product surface. Shallow depth of field 85mm lens, product centered, slow turntable rotation (15 seconds per 360°). Surfaces are pristine, no dust, no handheld motion. Silence, then soft product-place sound.
```

### Example 5: Phone-Shot UGC
```
Vertical handheld phone footage, slight grip sway, auto-exposure shifts as subject moves past window, ambient room sound (distant traffic, fridge hum). Person in casual hoodie talks to camera from bedroom, posters on wall behind, natural window light from left. Camera occasionally drifts down then corrects. Real-time pacing, no cuts.
```

---

## Anti-Patterns

❌ **Using studio/franchise names: "Make it look like [Studio Name] style"**  
→ Rewrite as production descriptors (medium, texture, palette, camera, motion)

❌ **Vague style terms: "cinematic," "dramatic," "epic"**  
→ Translate into specific lighting, camera, color, and motion choices

❌ **Mixing incompatible registers: photorealistic human + clay environment**  
→ Keep all elements in compatible style registers unless intentionally surreal

❌ **Prompting lens behavior in 2D animation**  
→ 2D doesn't have depth of field or bokeh unless painted

❌ **Ignoring era artifacts: "1990s footage but too clean"**  
→ Lock the source artifacts (grain, compression, auto-focus hunt)

---

## Output Structure

When responding to style requests, provide:

1. **Safe style descriptor** (if user mentioned protected names, show the rewrite)
2. **Layered breakdown** (medium, texture, palette, camera, motion)
3. **Source-look lock** (if applicable — name the capture source and its artifacts)
4. **One integrated prompt sentence** ready for Seedance 2.0

---

## Summary

**Style workflow:**
1. Identify user's style intent (what they love about the reference)
2. Rewrite protected names into production descriptors
3. Layer the style: medium, texture, palette, camera, motion
4. Lock source artifacts for realism styles
5. Maintain continuity in sequences
6. Deliver safe, prompt-ready style description

**Key principle:** Rebuild the love as something the user owns — describe the light, texture, and rhythm instead of naming the source.

---

**Related skills:** seedance-prompt, seedance-lighting, seedance-camera, seedance-sequence
