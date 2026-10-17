# QHSJ Seedance 配方/食谱库

# Seedance 2.0 — Recipes Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Templates, genre recipes, production patterns, reusable prompt structures

---

## When to Use This Skill

- User asks for a **template** or **starting pattern**
- User wants a **genre recipe** (product ad, lifestyle, drama, music video)
- User needs **production patterns** (commercial, animation, VFX, first/last frame)
- User asks for **reusable prompt structures**
- User wants guidance on **common video types** (short drama, talking head, space tour)

---

## Core Principle

**A recipe is a head start, never a mold.** The user wants the confidence of a proven shape with their own story inside it. Bend the recipe to the story every time — a user who feels templated has been failed even if the output is competent.

---

## Intent

Recipes provide proven patterns that work, but must be customized to the user's specific needs. Always adapt the recipe to the story, not the other way around.

---

## Recipe Families

| Family | Best use | Core pattern |
|--------|----------|--------------|
| **Product** | Ads, ecommerce, hero shots, material reveals | Product anchor + one material change + controlled camera + logo preservation |
| **Lifestyle** | Human use, food, travel, social clips | Simple action + lived environment + handheld or natural light + ambient sound |
| **Drama** | Emotion, dialogue, short narrative beats | Character tag + gesture + motivated camera + silence or sparse sound |
| **Music video** | Beat sync, dance, stylized edits | Rhythm reference + visible beat changes + light pulses + clear character blocking |
| **Landscape** | Establishing shots, nature, atmosphere | Slow camera + weather motion + layered depth + natural sound |
| **Commercial** | Brand-safe polish and function | Problem/use/result beat + precise product constraint + clean light |
| **Animation** | Original characters and stylized motion | Medium + shape language + palette + elastic or weighted motion |
| **VFX** | Transformations, particles, weather, energy | Source + material behavior + interaction + dissipation endpoint |
| **First/last frame** | In-between transitions, product state changes | First frame + last frame + continuous transition + identity locks |
| **Commercial campaign** | 6/10/15/30s variants, vertical/social cutdowns | Hook + product proof + end state + cutdown matrix + delivery notes |
| **Short drama (短剧)** | Fast-cut vertical mini-drama beats | Setup + reversal + cliffhanger + held reaction close |
| **Talking head (口播)** | Presenter, explainer, livestream-style pitch | Locked medium close-up + short quoted lines + minimal head motion + caption-safe framing |
| **Home/space tour** | Walkthrough of room, venue, or property | Single continuous take + steady forward path + light changes per zone + ambient sound only |

---

## Prompt Skeletons

### Product I2V
```
@Image1 is the product reference; preserve logo, label, shape, and materials exactly. [One material or light change]. Camera: [single move]. Lighting: [physical source]. Sound: [ambient/SFX].
```

**Example:**
```
@Image1 is the perfume bottle reference; preserve gold logo, glass transparency, and cap shape exactly. Cold white vapor rolls over bottle rim, sinks down sides, dissipates at base. Camera slow push-in 85mm macro, locked angle. Controlled studio lighting, white background, soft top light. Sound: low room tone, soft vapor hiss.
```

---

### Drama T2V
```
Character A [visible emotional action] in [specific setting]. Camera: [motivated framing]. Lighting: [motivated source]. Sound: [ambient or short dialogue]. End state: [changed expression/action].
```

**Example:**
```
Character A (woman in grey sweater, 30s, brown hair) sits at kitchen table, hands wrapped around coffee mug, gaze down. She looks up toward window with furrowed brow, releases mug, stands slowly. Camera static 50mm medium shot, eye-level. Morning window light from left, soft shadows. Sound: quiet kitchen ambience, refrigerator hum, distant bird call. Ends with Character A standing, facing window.
```

---

### Reference Motion
```
@Video1 provides only [camera/action/timing] reference; do not transfer identity, costume, logo, or environment. New subject: [authorized/original subject]. [Action and endpoint].
```

**Example:**
```
@Video1 provides camera movement reference only; do not transfer the person, clothing, or environment from the video. New subject: man in black suit, 40s, short grey hair, walks forward on city street at evening. Camera dollies backward at same pace, maintains medium shot. Street has wet pavement, neon signs, light rain. He walks 8 steps, stops at corner. Sound: rain on pavement, distant traffic.
```

---

### First/Last Frame
```
@Image1 is the first frame. @Image2 is the last frame. Preserve [identity/product/scene anchors]. Generate a continuous transition from [start state] to [end state]. Camera: [locked or one controlled move]. Sound: [ambient/SFX].
```

**Example:**
```
@Image1 is the first frame: coffee cup on table, hand approaching from right. @Image2 is the last frame: hand gripping cup handle, lifted 10cm above table. Preserve white ceramic cup, wooden table, morning window light. Generate continuous transition: hand enters frame right, fingers wrap around handle, hand lifts cup smoothly upward. Camera static 85mm macro, locked angle. Sound: quiet room tone, soft ceramic scrape as cup lifts.
```

---

### Animation
```
Original [character archetype] [action] in [environment]. Style: [medium, line quality, texture, palette]. Motion: [rhythm]. Camera and sound: [simple support].
```

**Example:**
```
Original character: round-bodied fox with oversized ears, orange and cream colors, sits on tree stump. Fox's ears perk up, head tilts left, eyes widen, tail swishes once. Forest clearing background with soft watercolor trees. Style: hand-painted 2D animation, rounded shapes, warm pastel palette, gentle line quality. Motion: bouncy squash-and-stretch, elastic ear movement. Camera static wide shot. Sound: light music-box melody, soft wind through trees.
```

---

## Genre-Specific Recipes

### Product Ad (15-second)
**Structure:** Hero product + one feature/benefit + end card with logo

**Skeleton:**
```
[Product name/description] on [clean surface]. [One material change or use demonstration]. Camera: [slow controlled movement]. Lighting: [clean studio or motivated natural]. Sound: [minimal SFX]. Ends with product centered, logo visible.
```

**Example:**
```
Glass water bottle with steel cap on white marble counter. Hand enters frame left, unscrews cap with quarter-turn, lifts bottle to pour water into clear glass, sets bottle back centered. Camera slow arc from left to front, 85mm lens, shallow focus. Clean studio lighting, soft top light, white background. Sound: cap twist, water pour, bottle set down. Ends with bottle centered, brand logo sharp and visible.
```

---

### Lifestyle/UGC (vertical, 10-second)
**Structure:** POV or handheld authentic moment

**Skeleton:**
```
[POV or handheld shot] [person] [simple relatable action] in [real environment]. Camera: [natural handheld or phone]. Lighting: [natural available light]. Sound: [ambient real environment].
```

**Example:**
```
Vertical handheld phone footage, POV looking down at hands holding iced coffee cup at outdoor cafe. Hands rotate cup to show condensation, straw, brand label. Background: blurred cafe tables, sunlight, people walking. Camera slight grip sway, auto-exposure adjusts. Natural afternoon sunlight, soft shadows. Sound: ambient cafe chatter, distant traffic, ice clink in cup.
```

---

### Short Drama (短剧) — 3-clip beat
**Structure:** Setup + reversal + cliffhanger reaction

**Clip 1 — Setup (6s):**
```
Character A [neutral or positive action], unaware. Camera: [establishing].
```

**Clip 2 — Reversal (5s):**
```
[Event/discovery happens]. Camera: [quick cut or motivated move].
```

**Clip 3 — Cliffhanger (4s):**
```
Character A [held reaction close-up], ends on suspense. Camera: [tight on face].
```

**Example:**

*Clip 1:*
```
Character A (woman in red dress) walks through apartment hallway, checking phone, slight smile. Camera handheld follows medium shot. Bright hallway lighting. Sound: footsteps, phone notification chime. 6 seconds.
```

*Clip 2:*
```
Character A reaches bedroom door, pushes it open, freezes. Camera quick push-in to her face. Hallway light dims, blue light spills from doorway. Sound: door creak, sudden silence. 5 seconds.
```

*Clip 3:*
```
Close-up on Character A's face, smile fades, eyes widen, breath catches. Camera locked tight on face, 85mm. Blue light from off-screen illuminates left side of face. Sound: slow heartbeat, held breath. Ends on frozen expression. 4 seconds.
```

---

### Talking Head (口播) — Presenter/explainer
**Structure:** Locked framing + short dialogue lines + caption-safe

**Skeleton:**
```
[Character] [medium close-up, faces camera], camera locked [lens]. [Character] says "[short line 1]." Pause. Says "[short line 2]." [Lighting]. Sound: clear dialogue, minimal room tone. Caption-safe framing (head not cut off).
```

**Example:**
```
Character A (man in navy blue shirt, 30s, short black hair) medium close-up, centered, faces camera directly. Camera locked 85mm, eye-level, vertical 9:16 frame. Character A says "This is the simplest way." Pause 1 second, slight smile. Says "Just follow these three steps." Minimal head motion, hands gesture below frame at waist level. Clean white background, soft front ring light, even exposure. Sound: clear dry dialogue, quiet room tone. 10 seconds.
```

---

### Home/Space Tour
**Structure:** One continuous take walking through space

**Skeleton:**
```
[Location] interior, camera moves forward through [room/space], [describe zones as camera passes]. Camera: [steady forward dolly or handheld walk]. Lighting: [natural changes per zone]. Sound: [ambient only, footsteps optional].
```

**Example:**
```
Modern apartment interior, camera moves forward from entryway through living room to floor-to-ceiling windows. Entryway: wooden floor, coat rack, mirror (warm overhead light). Living room: grey sofa, coffee table, bookshelf (afternoon natural light from windows). Windows: city view, soft curtains, potted plant (bright backlight). Camera steady forward dolly, 24mm wide-angle, eye-level, 20-second continuous shot. Lighting transitions from warm interior to bright window backlight. Sound: ambient room tone, distant city sounds, no music.
```

---

## Selection Rule

**If a user gives many goals, choose the recipe that protects the most fragile requirement:**

- **Product identity** beats camera spectacle
- **Lip-sync** beats large head motion
- **Character consistency** beats complex choreography
- **First/last-frame target accuracy** beats extra style changes
- **Safety and authorization** beat style mimicry

**Example:**

User asks for: "Product ad with dramatic camera moves and character dialogue and transformation effects"

**Choose:** Product recipe (protect product identity first)  
**Simplify:** One clean camera move, no dialogue (risks desync), minimal effects (keep product sharp)

---

## Customization Checklist

Before delivering a recipe-based prompt:

1. **Subject:** Replace generic with user's specific subject
2. **Action:** Replace generic with user's specific beat
3. **Camera:** Match camera to user's stated style or mood
4. **Lighting:** Match lighting to time-of-day, location, mood
5. **Audio:** Match audio to user's genre (dialogue, music, ambient)
6. **Constraints:** Add user's specific requirements (logo visible, wardrobe color, duration)

**Never deliver a generic template unchanged.**

---

## Anti-Patterns

❌ **Rigid template without customization:**  
```
Product on white background, camera rotates, clean lighting.
```
→ Add user's specific product, brand requirements, style

❌ **Mixing incompatible recipes:**  
```
Product ad + drama dialogue + VFX + music video beat-sync all in one 15-second clip
```
→ Choose one primary recipe, keep supporting elements minimal

❌ **Assuming user wants the default:**  
```
"I'll use the standard product ad template"
```
→ Ask which aspect matters most (product clarity? emotion? story?)

---

## Output Structure

When providing a recipe, return:

1. **Recipe selected** (which family, why it fits)
2. **Customization notes** (what changes from skeleton to user's needs)
3. **Prompt skeleton** (generic structure)
4. **Customized final prompt** (ready for Seedance 2.0)
5. **Campaign/delivery notes** (if applicable — cutdowns, localization, textless)

---

## Summary

**Recipe workflow:**
1. Identify user's primary goal and constraints
2. Select recipe family that protects most fragile requirement
3. Start with prompt skeleton
4. Customize: subject, action, camera, lighting, audio
5. Deliver final prompt with rationale

**Key principle:** Recipes are head starts, not molds. Bend the recipe to the story every time.

---

**Related skills:** seedance-prompt, seedance-sequence, seedance-style, seedance-pipeline
