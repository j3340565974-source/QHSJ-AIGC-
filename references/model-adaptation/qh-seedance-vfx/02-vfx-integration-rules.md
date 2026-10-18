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
