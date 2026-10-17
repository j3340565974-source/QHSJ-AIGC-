# QHSJ Seedance VFX

# Seedance 2.0 — VFX Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** VFX, particles, energy, destruction, transformation, weather effects, smoke, fire, water

---

## When to Use This Skill

- User asks for **VFX** or **visual effects**
- User wants **particles** (dust, sparkles, embers, debris)
- User asks for **energy effects** (electricity, glows, auras)
- User wants **destruction** (breaking, shattering, crumbling)
- User asks for **transformation** (morphing, dissolving, materializing)
- User wants **weather effects** (rain, wind, fog, snow)
- User asks for **magical effects** (must translate to physical behavior)
- User wants **explosions, smoke, fire, water, or fluid effects**

---

## Core Principle

**VFX need physics.** Every effect must have:
1. **Source** (where it starts)
2. **Material behavior** (what it's made of)
3. **Motion path** (how it travels)
4. **Interaction** (with light, objects, surfaces)
5. **Dissipation** (how it ends)

**Avoid generic words** like "magical," "explosive," "cinematic" unless translated into **particles, fluids, smoke, light, debris, deformation, or energy behavior**.

---

## Intent

The user wants wonder, and wonder dies the moment it stops obeying physics. Every effect has a source, a journey, and an ending, so the impossible reads as witnessed rather than rendered.

---

## Effects Contract

For every VFX prompt, specify:

| Element | Description |
|---------|-------------|
| **Source** | Where the effect originates (object, body part, surface) |
| **Material** | What the effect is made of (particles, smoke, electricity, liquid, debris) |
| **Motion path** | Direction, speed, arc, rotation |
| **Light interaction** | Does it emit light? Catch light? Cast shadows? |
| **Object interaction** | Does it collide, stick, bounce, pass through? |
| **Dissipation** | How it ends (settle, fade, evaporate, freeze, collapse) |
| **Endpoint** | Final visible state (residue, glow, settled particles) |

---

## VFX Categories and Prompt Patterns

### 1. Particles

**Use for:** Dust, sparkles, embers, pollen, debris, confetti

**Prompt pattern:**
```
[Particle type] [material] particles [spawn from source], [motion path], [light interaction], [settle/fade/dissipate]
```

**Examples:**

```
Gold dust particles spiral upward from behind the logo, catch the backlight, create small golden sparkles as they rise, then settle slowly onto the table surface in a thin layer.
```

```
Paper confetti pieces in red, blue, and yellow burst upward from the box lid, tumble through the air in lazy arcs, some catch window light, all settle to the floor over 8 seconds.
```

```
Ash particles rise from the campfire in a vertical column, glow orange at the base, fade to grey as they rise 2 meters, then disperse in the wind.
```

**Stability note:** Keep the **source object stable** (logo, box, fire) — particles move, source doesn't morph.

---

### 2. Energy Effects

**Use for:** Electricity, glows, auras, light rays, pulses

**Prompt pattern:**
```
[Energy type] [color] [travels along/from source], [interaction with surface], [brightness change], [fade/dissipate]
```

**Examples:**

```
Thin blue electrical arcs crawl along the cable from plug to device, briefly illuminate fingerprints on the cable surface, pulse twice, then fade out over 3 seconds.
```

```
Soft white glow emanates from the crystal, illuminates the character's face from below, brightens over 4 seconds to peak, holds for 2 seconds, then dims gradually.
```

```
Green energy pulse travels up the character's arm from wrist to shoulder, leaves a faint glowing trail that persists for 2 seconds, then fades to nothing.
```

**Stability note:** Keep energy **attached to source** — arcs follow cables, glows stay centered on objects.

---

### 3. Smoke and Vapor

**Use for:** Smoke, steam, fog, mist, breath clouds

**Prompt pattern:**
```
[Smoke type] [color] [source], [density], [motion direction], [interaction with gravity/wind], [dissipate]
```

**Examples:**

```
Cold white vapor rolls over the rim of the glass, sinks down the outside surface, pools briefly on the table, then thins and dissipates near the tabletop.
```

```
Dark grey smoke rises from the candle after extinguishing, curls upward in a thin column, disperses into wisps at 1 meter height, ambient room air is still.
```

```
Morning mist hangs 1 meter above the ground, character walks through it, each step creates slow swirling eddies, mist parts around legs and reforms behind.
```

**Stability note:** Describe **density and direction** — "thin wispy" vs "thick rolling" changes the physics.

---

### 4. Fire and Heat

**Use for:** Flames, embers, heat distortion, explosions

**Prompt pattern:**
```
[Fire type] [color], [source], [motion], [light cast], [smoke interaction], [dissipate/extinguish]
```

**Examples:**

```
Small orange flame flickers at candle wick, casts warm dancing light on nearby surfaces, produces thin grey smoke rising vertically, flame sways slightly left then right over 6 seconds.
```

```
Explosion fireball expands rapidly from center point, bright yellow-orange core, darker red outer edge, throws sparks outward in radial pattern, debris flies away from center, fireball dissipates into dark smoke cloud over 4 seconds.
```

```
Heat distortion shimmer rises from hot pavement surface, visible as wavering air, distorts background buildings slightly, character walks through it, distortion remains constant.
```

**Stability note:** Fire **emits light** — specify what surfaces receive the glow.

---

### 5. Water and Fluids

**Use for:** Splashes, rain, pouring, ripples, waves

**Prompt pattern:**
```
[Liquid type] [source], [motion arc], [splash/ripple], [surface interaction], [settle]
```

**Examples:**

```
Water pours from bottle neck in smooth stream, arcs 30cm downward into glass, creates small splash and bubbles on impact, glass fills halfway, surface tension visible at rim.
```

```
Rain falls diagonally across frame from upper right to lower left, wind pushes droplets at 45° angle, puddles form and ripple outward from each raindrop impact, pavement reflects streetlight.
```

```
Single water droplet falls from leaf tip, travels downward in straight line over 1 second, hits puddle surface, creates concentric ripples expanding outward, ripples fade after 3 seconds.
```

**Stability note:** **Tie water to surfaces** — where does it land, how does it interact?

---

### 6. Transformation Effects

**Use for:** Morphing, dissolving, materializing, peeling, burning transitions

**Prompt pattern:**
```
[Object] [transformation verb] [from state A to state B], [which parts change first], [preserved elements], [endpoint]
```

**Examples:**

```
Paper sheet burns inward from the corner, char line advances across surface at steady pace, edges curl upward and turn black, center logo remains untouched white, final result is logo on charred background.
```

```
Glass bottle dissolves from top to bottom into fine sand particles, particles fall and accumulate at the base, bottle silhouette maintained by falling sand, completes in 10 seconds, final result is sand pile in bottle shape.
```

```
Character materializes from particles, feet appear first as golden particles coalesce, solidification travels upward over 8 seconds, head completes last, particles that don't attach drift away and fade.
```

**Stability note:** **Protect identity anchor** — if logo/face/product must remain recognizable, keep it stable while surroundings transform.

---

### 7. Weather Effects

**Use for:** Rain, wind, snow, fog, dust storms

**Prompt pattern:**
```
[Weather type] [intensity], [direction], [interaction with character/objects], [surface effects]
```

**Examples:**

```
Strong wind pushes through wheat field, stalks bend in waves from left to right, character's coat and hair blow to the right, dust swirls at ground level, trees in background sway.
```

```
Gentle snow falls vertically, flakes catch in character's hair and on coat shoulders, some melt immediately on warm surfaces, snow accumulates on cold metal railing, ground shows thin dusting.
```

```
Fog bank rolls in from the background at knee height, advances toward camera over 12 seconds, character's lower body becomes obscured, only torso and head remain clearly visible.
```

**Stability note:** Weather affects **everything in frame** — show multiple interaction points.

---

## VFX Integration Rules

### Rule 1: One Hero Effect Per Clip
**Don't mix:** particles + smoke + electricity + transformation in one 20-second clip.

**Instead:** Choose the hero effect, supporting elements stay subtle.

**Example:**
- **Hero effect:** Fire explosion
- **Supporting:** Smoke aftermath (simple), debris (minimal)
- **Not:** + particles + electricity + water splash

---

### Rule 2: Anchor Effects to Sources
Every effect must have a **clear visible source**.

❌ "Energy appears around the character"  
✅ "Energy pulses emanate from the crystal in her hand, travel up her arm"

❌ "Magical sparkles"  
✅ "Gold sparkles spiral upward from the wand tip"

---

### Rule 3: Effects Respect Physics
- **Gravity:** Particles settle down, smoke rises, liquids fall
- **Wind:** Shows direction, affects light objects more than heavy
- **Collision:** Particles bounce off surfaces, liquids splash on impact
- **Reflection:** Shiny particles catch light, wet surfaces reflect
- **Occlusion:** Effects pass behind objects, don't phase through

---

### Rule 4: Timing and Dissipation
Effects need an **endpoint**. Never leave effects "going forever."

**Three-step timing phrase:**
1. **Forms** (effect begins, source visible)
2. **Travels** (motion path, interactions)
3. **Dissipates** (settle, fade, evaporate, freeze, collapse)

**Example:**
```
Smoke rises from extinguished candle (forms), curls upward in thin column for 6 seconds (travels), disperses into wisps at ceiling height (dissipates).
```

---

### Rule 5: Protect Core Identity
For VFX near **faces, hands, logos, or text**, keep the core identity **stable**.

**Place effect around identity, not through it:**

❌ "Particles swirl through the logo"  
✅ "Particles spiral around the logo, catch backlight, settle on table — logo remains sharp"

❌ "Energy distorts the character's face"  
✅ "Energy aura glows around character's head, face features remain clear"

---

## Example VFX Prompts

### Example 1: Product Particles
```
A glass perfume bottle on white pedestal, gold dust particles spiral upward from behind the bottle base, catch the backlight and create small golden sparkles, rise 40cm in a gentle helix, then settle slowly onto the pedestal surface forming a thin golden ring. Bottle remains centered, sharp, and stable. Camera slow push-in 85mm macro, controlled studio lighting. 12 seconds continuous motion, particles complete cycle.
```

### Example 2: Electrical Energy
```
Close-up on a black charging cable, thin blue electrical arcs crawl from the plug end toward the device, arcs follow the cable's curve, briefly illuminate the braided surface texture, pulse twice with 1-second intervals, then fade to nothing. Cable remains stationary, camera static 100mm macro. Dark background, only arc light visible. 8 seconds.
```

### Example 3: Smoke Dissipation
```
A white ceramic cup on wooden table, cold white vapor rolls over the rim, sinks down the outside surface due to density, pools briefly on the table in a thin layer, then thins and dissipates outward. Morning window light from left, vapor catches light and glows softly. Camera static 50mm, medium shot. 10 seconds continuous vapor motion.
```

### Example 4: Paper Burn Transformation
```
A sheet of white paper on dark background, flame starts at bottom right corner, char line advances upward and leftward across the surface at steady pace, paper edges curl upward and blacken, center reveals a gold logo that remains untouched and bright. Fire completes consumption in 14 seconds, final frame shows gold logo on black charred background, thin smoke rising. Camera static 50mm, overhead view.
```

### Example 5: Rain and Wind
```
Urban street at dusk, rain falls diagonally from upper left to lower right at 45° angle, wind pushes droplets across frame. Character in dark coat walks toward camera, rain beads on coat fabric, puddles on pavement ripple outward from each step, streetlights reflect in wet surfaces. Camera handheld 35mm, follows character. 16 seconds continuous rain, wind intensity constant.
```

---

## Anti-Patterns

❌ **Vague effect words: "magical effect," "dramatic explosion"**  
→ Specify material, motion, light interaction, dissipation

❌ **Multiple unrelated effects in one clip**  
→ One hero effect, supporting elements stay subtle

❌ **Effects without sources: "particles appear"**  
→ Anchor to visible object: "particles rise from the wand tip"

❌ **No endpoint: "smoke continuously rises"**  
→ Add dissipation: "smoke rises 2 meters then disperses into thin wisps"

❌ **Effects obscure identity: "energy swirls through the logo"**  
→ Protect core: "energy pulses around the logo border, logo remains sharp"

❌ **Ignoring physics: "water falls upward"**  
→ Respect gravity, wind, collision unless intentionally surreal

---

## Summary

**VFX workflow:**
1. Identify effect type (particles, energy, smoke, fire, water, transformation, weather)
2. Specify: source, material, motion path, light interaction, object interaction, dissipation
3. Keep one hero effect per clip
4. Anchor effects to visible sources
5. Respect physics (gravity, wind, collision, reflection)
6. Add timing: forms → travels → dissipates
7. Protect core identity (faces, logos, products stay stable)

**Key principle:** Every effect has a source, a journey, and an ending — the impossible should read as witnessed.

---

**Related skills:** seedance-prompt, seedance-lighting, seedance-style, seedance-motion
