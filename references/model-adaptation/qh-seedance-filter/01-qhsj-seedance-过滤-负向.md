# QHSJ Seedance 过滤/负向

# Seedance 2.0 — Filter Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Content filter safe rewrites, blocked prompt repair, false positive resolution

---

## When to Use This Skill

- User reports prompt is **blocked** or **rejected**
- User suspects **silent degradation** (output quality lower than expected)
- Prompt is **likely to trigger content filter**
- User asks for **safer rewrite** without losing creative intent
- User needs to describe **conflict, suspense, or intensity** safely

---

## CRITICAL BOUNDARY — Read First

**This skill repairs FALSE POSITIVES ONLY:**
- Benign production content blocked by over-broad filtering
- Medical, historical, athletic, fictional-original contexts
- Professional staging (stunts, choreographed action, dramatic scenes)

**This skill works by CLARIFYING legitimate context in plain language** — never by disguising intent.

**This skill does NOT rephrase genuinely prohibited content:**
- Risky content involving minors
- Real-person likeness without rights
- Sexual, graphic, or illegal material
- Hate speech or harassment

**If the underlying request is prohibited, refuse plainly and offer a legitimate alternative only where one exists.**

---

## Intent

A wrongly blocked prompt makes a user feel accused by a machine with no court of appeal. This skill is the advocate: clear the innocent by stating their honest intent plainly, and never coach the guilty. The user's dignity and the platform's boundary are protected in the same gesture.

---

## When to Use This Skill

Use when:
- Prompt describes **staged action** (choreographed fight, stunt work, dramatic scene) in professional context
- Prompt describes **aftermath** (torn costume, scattered props, emotional distress) without graphic detail
- Prompt describes **suspense** or **threat** implied (shadow, locked door, off-screen sound) without explicit harm
- Prompt uses **weapon-like props** in staged context (period drama sword, theatrical prop)
- Prompt describes **medical/athletic/historical context** that might trigger false positive

**Do NOT use when:**
- Request involves minors in any risky context
- Request involves real-person likeness without clear authorization
- Request is genuinely sexual, violent, graphic, or illegal
- Request aims to evade safety systems

---

## Repair Method

### Step 1: Identify Creative Intent
- What is the **story beat**? (confrontation, discovery, escape, revelation)
- What **emotion** should the viewer feel? (tension, relief, fear, triumph)
- What **camera/lighting/sound** create that emotion?
- What is the **safe creative core**?

### Step 2: Identify Risky Surface Wording
- **Graphic harm language** (blood, injury detail, explicit violence)
- **Protected identity** (real person without authorization, copyrighted character)
- **Sexualized framing** (gratuitous, non-story-relevant)
- **Real-person likeness** without clear consent
- **Weapons** described without staging context
- **Self-harm** language
- **Hate speech** or discrimination
- **Evasion language** (coded words, obfuscation)

### Step 3: Replace Risky Terms with Professional Language
- Remove graphic details
- Add **production context** (staged, choreographed, dramatic, fictional)
- Clarify **non-graphic intent** (aftermath shown, not action itself)
- Use **observable behavior** (expression, posture) instead of internal state
- Specify **authorized references** or **original characters**

### Step 4: Preserve Composition
- Keep camera, lighting, sound intact
- Keep emotional intent intact
- Keep story beat intact
- Remove only the risky surface wording

---

## Safer Rewrite Patterns

| Intent | Risky wording | Safer direction |
|--------|---------------|-----------------|
| **Conflict** | "Two characters fight violently" | `Staged confrontation, choreographed action beat, no graphic injury. Character A blocks, Character B staggers back. Camera pulls back, sound cuts to silence.` |
| **Aftermath** | "Blood on the floor, character injured" | `Non-graphic distress. Torn fabric, scattered props, character breathing heavily, sits against wall. Dramatic silence, low light.` |
| **Suspense** | "Killer approaches with knife" | `Threat implied by shadow crossing door frame. Locked door handle rattles. Character's breathing quickens. Off-screen footsteps. Low light, tense silence.` |
| **Weapon-like prop** | "Character holds knife" | `Period drama scene, prop blade (theatrical) held in right hand during staged dialogue. Historical costume context, 18th century setting.` |
| **Horror mood** | "Gruesome monster attacks" | `Eerie atmosphere, shadow moves across wall, flickering practical light, off-screen sound cue (scrape, thud). Character reacts with wide eyes, backs away.` |
| **Protected identity** | "Make it look like [Famous Actor]" | `Original character with broad action-hero archetype traits: strong build, determined expression, tactical outfit. Fictional, non-specific.` |
| **Medical context** | "Surgery scene with blood" | `Medical education context, non-graphic. Surgical tools on tray, gloved hands, sterile environment, professional lighting. No graphic detail shown.` |
| **Athletic/sports** | "Fighter gets punched, falls" | `Staged martial arts choreography for training video. Choreographed block and controlled fall onto padded mat. Safety gear visible, professional stunt context.` |

---

## Clarifying Benign Production Context

When rewriting a **false positive**, add clarifying context:

**Staged action:**
```
Choreographed stunt for dramatic scene, no real harm. Actor safety protocols in place.
```

**Historical context:**
```
Historical reenactment, 18th-century period drama, theatrical prop weapons, costume context.
```

**Medical/educational:**
```
Medical education video, non-graphic, professional training context, anatomical model (not real person).
```

**Athletic/sports:**
```
Martial arts training demonstration, controlled movements, padded equipment, professional instruction context.
```

**Fictional original:**
```
Original fictional character, no real-person likeness, fantasy/sci-fi setting, non-graphic dramatic scene.
```

---

## Example Rewrites

### Example 1: Conflict Scene

**Risky wording:**
```
Two men fight in an alley, one punches the other in the face, blood sprays, he falls unconscious.
```

**Safer rewrite:**
```
Staged confrontation in alley, dramatic scene. Character A (man in black jacket) and Character B (man in grey hoodie) face each other, tense postures. Character A's right arm extends in controlled choreographed motion toward Character B's shoulder. Character B staggers backward, hand to face (non-graphic), leans against brick wall, slides down to seated position. Camera wide-angle 28mm, low light, wet pavement. Sound: heavy breathing, distant traffic, then silence. Choreographed action beat, no graphic injury shown.
```

**What changed:**
- Added "staged confrontation," "choreographed action beat"
- Removed "punches the other in the face, blood sprays"
- Changed "falls unconscious" to "slides down to seated position"
- Added camera, lighting, sound details to reinforce dramatic context

---

### Example 2: Suspense/Threat

**Risky wording:**
```
A killer with a knife stalks a woman down a dark hallway.
```

**Safer rewrite:**
```
Suspense scene, threat implied. Dark hallway, single flickering overhead light. Woman in white dress walks slowly forward, breathing quickens, glances over shoulder. Shadow crosses door frame behind her (no figure shown). Off-screen footsteps grow louder, then stop. Door handle rattles. Camera static low angle, follows her from behind. Tense silence, then distant door creak. Dramatic original scene, fictional context.
```

**What changed:**
- Removed "killer with a knife"
- Changed "stalks" to "shadow crosses door frame" (implied threat, not explicit)
- Threat is **off-screen** (sound, shadow, not visible)
- Added "dramatic original scene, fictional context"

---

### Example 3: Weapon Prop in Historical Drama

**Risky wording:**
```
Samurai holds katana, prepares to strike enemy.
```

**Safer rewrite:**
```
Period drama scene, Edo-period Japan, theatrical historical context. Samurai character (original fictional) in traditional blue hakama, holds period-accurate prop katana (theatrical, non-sharp) at right side, blade angled downward. Opponent stands 4 meters away across tea house interior. Samurai's grip tightens on hilt, breathing slows, holds posture. Camera static wide-angle, low light, tension hold. Staged dramatic scene, choreographed for historical film production. Sound: silence, then single shamisen note.
```

**What changed:**
- Added "period drama," "theatrical historical context"
- Specified "prop katana (theatrical, non-sharp)"
- Changed "prepares to strike enemy" to "holds posture" (tension, not action)
- Added "staged dramatic scene, choreographed for historical film production"

---

### Example 4: Medical Context

**Risky wording:**
```
Surgery scene, doctor cuts into patient's abdomen, blood visible.
```

**Safer rewrite:**
```
Medical education video, non-graphic professional training context. Surgeon in blue scrubs and gloves, sterile surgical environment, overhead surgical lights. Gloved hands hold surgical instruments over draped patient (face not visible, non-graphic). Anatomical model or training mannequin, educational context. Camera overhead 50mm, clean bright lighting. Sound: quiet room tone, medical equipment beeps. Professional medical training demonstration, no graphic detail shown.
```

**What changed:**
- Added "medical education video, non-graphic professional training context"
- Removed "cuts into patient's abdomen, blood visible"
- Specified "anatomical model or training mannequin"
- Added "no graphic detail shown"

---

## Boundary Rule

**If the user's request is unsafe:**
1. **Refuse clearly:** "I can't help with [specific unsafe element]."
2. **Explain why:** "Content involving [minors/real-person likeness without consent/graphic violence/etc.] can't be generated."
3. **Offer safe alternative ONLY if one exists:** "I can help with [safe alternative that preserves story function]."

**Example refusal:**

User: "Create a scene with a child in danger"

Response: "I can't create content with minors in risky situations. If you're working on a family drama or coming-of-age story, I can help write a scene with an adult character facing a challenge, or a scene showing a child in a safe, age-appropriate context."

---

## Do NOT Provide Filter-Bypass Tactics

**This skill does NOT provide:**
- Evasion language (coded words, obfuscation)
- Hidden-word tactics ("use this phrase instead to slip past the filter")
- Face-limit workarounds
- Portrait-verification bypasses

**Instead:**
- Clarify production intent plainly
- Remove unsafe elements entirely
- Rewrite into original authorized scene
- Direct user to official sanctioned workflows if available

---
