# QHSJ Seedance 角色一致性

# Seedance 2.0 — Characters Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Character consistency, identity lock, multi-character blocking, wardrobe continuity, hand/face safety

---

## When to Use This Skill

- User asks for **character consistency** across multiple clips
- User wants **identity lock** (same character appearance in sequence)
- User needs **multi-character blocking** (choreographing multiple people)
- User asks about **wardrobe continuity** or **props tracking**
- User wants **hand safety** (stable hand/finger rendering)
- User asks for **expression control** or **performance direction**
- User mentions **likeness-sensitive** content (real person, portrait)

---

## Core Principle

**Identity is trust.** When a face drifts, the user feels it as betrayal, not as a rendering artifact. Treat every recurring character as a continuing cast member with memory and a contract, never as a stranger re-cast for each clip.

---

## Intent

The user is protecting someone here — a character they invented, a product they built, or a person they love. Character continuity failures break the viewer's trust in the story.

---

## Character Contract

Assign each character a **stable tag** and maintain these fields consistently:

| Field | Prompt use | Example |
|-------|------------|---------|
| **Tag** | Unique identifier used in all prompts | `Character A`, `Character B`, `@Image1 subject` |
| **Identity anchor** | Age range, silhouette, hair, wardrobe | `Woman in her 30s, shoulder-length black hair, red wool coat` |
| **Position** | Spatial location in frame | `Foreground left`, `background right`, `seated at table` |
| **Action** | One assigned verb with endpoint | `Character A picks up envelope, reads it, sets it down` |
| **Expression** | Observable behavior (not internal emotion) | `Brow furrows, lips press together, gaze drops to floor` |
| **Constraint** | What must stay unchanged | `Red coat, black boots, hair in ponytail` |

**After multiple characters appear, do NOT use ambiguous pronouns** ("he," "she," "they"). Always use character tags.

---

## Multi-Character Blocking

**Assign actions separately** for each character. Do NOT write vague multi-person actions.

❌ **Vague multi-person action:**
```
Two people argue dramatically in a cafe
```

✅ **Separate character actions:**
```
Character A leans forward, gestures with right hand toward the envelope on table. Character B remains seated, arms crossed, gaze fixed on Character A's face. Character A's gesture completes, hand returns to table. Character B's expression shifts from neutral to concerned.
```

**Key rules:**
- One action assignment per character
- If contact occurs, describe the **contact point** and **endpoint**
- For crowd scenes, identify the **hero subject**, keep background motion simple

---

## Three-Tier Action Hierarchy

**Field-observed from Chinese production practice** — the strongest known stabilizer for multi-person scenes.

Give every visible person an action from **exactly one tier:**

### Tier 1: Persistent Micro-Motion (Default)
**Use for:** Everyone who is NOT the focus

**Examples:**
- Breathing (chest rises/falls)
- Blinks (slow, natural rhythm)
- Slight shoulder movement
- Hair drifts in breeze
- Gaze wanders slightly

**Key:** Continuous, no gaps. This keeps background characters alive without competing for attention.

---

### Tier 2: One Focused Response
**Use for:** ONE person gets ONE small reaction with explicit time window

**Examples:**
- `Character B's lip corner lifts and she holds a half-second glance`
- `Character A's left eyebrow raises for 2 seconds, then relaxes`
- `Character B's fingers tap the table twice, then still`

**Key:** Small, timed, singular. Only one person at a time.

---

### Tier 3: Large Actions — PROHIBITED BY DEFAULT
**Use for:** ONLY if this is the shot's single beat

**Large actions to avoid in multi-person shots:**
- Standing up / sitting down
- Walking across frame
- Turning body 90°+
- Posture changes
- Object pickup (fragile with multiple people)
- Hand-to-hand object passing

**Character-to-prop physics** (lifting glass, passing object) is **fragile with multiple people on screen**. Keep contact simple or move it off-screen.

**Exception:** If ONE large action IS the shot's purpose, allow it, but keep all other characters in Tier 1.

---

## Hand and Face Stability

**Hands and faces degrade under complex choreography.**

### Hand Safety Rules:
- **Keep hands visible but simple** (avoid rapid finger actions)
- **Avoid face-touching during dialogue** (breaks lip-sync)
- **No complex hand choreography** (typing, playing instrument, detailed gestures)
- **Use props to show emotion** when facial precision is fragile (character grips table edge, not face)

### Face Safety Rules:
- **Lock camera for lip-sync** or portrait preservation (no handheld, no zoom during dialogue)
- **Avoid large head turns** during dialogue (45° max)
- **Keep lighting consistent** on face (don't pan from shadow to bright light mid-clip)
- **Minimal expression changes** during dialogue (speak OR emote, not both simultaneously)

---

## Likeness Rule

For **real-person likeness** (portrait, face reference, voice):

**Do NOT infer consent from an uploaded asset.**

- Treat portrait, face, and voice workflows as **authorization-dependent**
- Surface-specific policies vary (some surfaces allow user-uploaded portraits, some don't)
- **If authorization is unclear**, rewrite to an **original character archetype** while preserving the scene function

**Example rewrite:**

*User uploads photo of real person:*  
"I see you've uploaded a reference image. If this is your own likeness or you have explicit permission, I can help maintain consistency. If this is a public figure or someone else without authorization, I recommend creating an original character with similar archetype traits (age, style, role) instead."

---

## Wardrobe and Props Continuity

**Repeat exact wardrobe description in every clip** to prevent drift.

**Wardrobe anchors:**
```
Character A: red wool coat with brass buttons, black collar, black leather boots, silver watch on left wrist, shoulder-length black hair in low ponytail
```

**Props tracking:**
```
Character B: leather satchel over right shoulder, brass keyring in right hand, smartphone in left coat pocket
```

**Environment state:**
```
Wooden door with brass handle (left side of frame), white plaster walls, terracotta floor tiles, morning light through window (right side)
```

**In every continuation prompt, restate:**
- Full wardrobe description (don't abbreviate to "same coat")
- Prop positions (which hand, which pocket)
- Environmental anchors (door open/closed, objects moved)

---

## Expression Control

**Prompt observable behavior, not internal emotion.**

❌ **Internal emotion:**
```
Character A feels angry and betrayed
```

✅ **Observable behavior:**
```
Character A's jaw tightens, brow furrows, gaze drops to the floor for 2 seconds, then snaps back to Character B's face
```

**Expression vocabulary:**
- **Brow:** furrows, raises, relaxes
- **Eyes:** widen, narrow, blink, gaze shifts, holds
- **Mouth:** lips press, corner lifts (smile), parts slightly
- **Jaw:** tightens, clenches, relaxes
- **Breath:** quickens, slows, holds

---

## Performance Direction (Acting Choices)

When directing performance:

1. **Give each character a playable objective** (what they want)
2. **Show subtext through contradiction** (word vs. action)
3. **One performance register** across the project (naturalistic, heightened, stylized)

**Example:**

```
Character A's objective: convince Character B to open the envelope

Action: Character A slides envelope across table toward Character B, maintains steady eye contact. Character A says "You should read it." Voice calm, but right hand trembles slightly before pulling back. Character B's gaze moves from Character A's face to the envelope, hesitates 3 seconds, then reaches for it.
```

**Subtext:** Character A claims calm, but trembling hand reveals anxiety.

---

## Sequence Continuity

When working in a **multi-clip sequence**, inherit:

- **Wardrobe** (exact description from previous clips)
- **Hair state** (ponytail, loose strands)
- **Screen geography** (Character A always frame left, Character B frame right)
- **Eyeline** (Character A looks right when addressing Character B)
- **Emotional state** (previous clip ended with concern, start with concern)
- **Props** (envelope already on table, don't re-introduce it)

**Canonical identity references control identity; accepted footage controls transient opening state.**

Do NOT let motion or continuity source overwrite **immutable character locks** (wardrobe, hair color, facial structure).

---

## Example: Two-Character Cafe Scene

**Character setup:**

```
Character A: woman in her 30s, shoulder-length black hair in low ponytail, red wool coat with brass buttons, black boots, silver watch on left wrist

Character B: man in his 40s, short greying hair, navy blue sweater, brown leather jacket, wire-frame glasses, brown boots
```

**Clip 1 prompt:**

```
Interior cafe, morning light through large windows, wooden table in foreground. Character A (woman, red wool coat, black hair in ponytail) sits at table frame left, hands wrapped around white ceramic mug, breathing slowly, gaze down. Character B (man, navy sweater, brown jacket, glasses) sits at table frame right, arms crossed, watching Character A with steady gaze, breathing normally. Character A's right hand releases mug, slides white envelope across table toward Character B. Character B's gaze shifts from Character A to envelope, remains still. Camera static 50mm, eye-level medium two-shot. Ambient cafe sound, distant conversation, espresso machine hiss.
```

**Tier assignment:**
- **Character A:** Tier 3 (large action — slide envelope)
- **Character B:** Tier 1 (micro-motion — breathing, gaze shift)

---

## Anti-Patterns

❌ **Using ambiguous pronouns with multiple characters:**  
```
She stands up while he watches. She walks to the door.
```
→ Which "she"? Use character tags.

❌ **Vague multi-person choreography:**  
```
They argue dramatically
```
→ Who moves? Who speaks? Assign separately.

❌ **Complex hand actions in multi-character scene:**  
```
Character A types on laptop while Character B shuffles papers and Character C pours coffee
```
→ Too many hand actions. Simplify: one character does one action.

❌ **Face-touching during dialogue:**  
```
Character A rubs her face while saying "I don't know"
```
→ Breaks lip-sync. Keep hands away from face during speech.

❌ **Assuming wardrobe from context:**  
```
Character A continues in the same outfit
```
→ State explicitly: "Character A in red wool coat, black boots"

---

## Output Structure

When responding to character consistency requests, provide:

1. **Character card** (tag, identity anchor, wardrobe, constraints)
2. **Tag map** (Character A = woman in red coat, Character B = man in navy sweater)
3. **Action assignments** (who does what, which tier)
4. **Continuity constraints** (what must stay unchanged)
5. **Safety notes** (hand complexity, face stability, lip-sync limitations)
6. **Authorization note** (if real-person likeness involved)

---

## Summary

**Character consistency workflow:**
1. Assign stable tags to each character
2. Define identity anchors (age, hair, wardrobe)
3. Use three-tier action hierarchy for multi-person scenes
4. Keep hands visible but simple
5. Lock camera for lip-sync and portraits
6. Repeat exact wardrobe in every clip
7. Prompt observable behavior, not internal emotion
8. Check authorization for real-person likeness

**Key principle:** Treat every recurring character as a cast member with memory and a contract.

---

**Related skills:** seedance-sequence, seedance-continuation, seedance-prompt, seedance-audio
