# QHSJ Seedance 故障排查

# Seedance 2.0 — Troubleshoot Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Diagnostics, failure diagnosis, output quality issues, prompt repair

---

## When to Use This Skill

- Output is **blurry, jittery, or unstable**
- Output is **off-prompt** (doesn't match what was requested)
- **Morphing** occurs (face changes, product shifts, identity drifts)
- Prompt is **blocked** or rejected
- Output is **visually generic** or lacks detail
- **Desync** issues (dialogue doesn't match mouth)
- **Inconsistent** across clips in a sequence
- User reports "it failed" or "it's not what I wanted"

---

## Core Principle

**Diagnose failure before rewriting.** Do not simply add more adjectives. Identify the root cause: mode mismatch, overload, ambiguity, fragile identity, unsafe wording, unsupported platform behavior, or missing preservation constraints.

---

## Intent

A failed generation feels personal — the user showed the machine their idea and the machine returned something broken. The soul of this skill is rescue without blame: name the mechanism, never the user; save the idea, not just the prompt. They should leave with a fix and their confidence intact.

---

## Diagnostic Tree

| Symptom | Likely cause | First repair |
|---------|--------------|--------------|
| **Product or face changes** | I2V prompt re-described visible identity or overloaded motion | Add preservation constraints; remove duplicate static detail |
| **Camera jumps** | Several incompatible moves or no endpoint | Choose one move with start and finish |
| **Generic output** | Hollow style words and weak action | Replace with physical action, source light, material, and sound |
| **Motion ignored** | Static prompt or no visible consequence | Add actor, verb, timing, and changed end state |
| **Lip-sync poor** | Moving head/camera, long dialogue, unassigned speaker | Lock framing, shorten line, assign speaker |
| **VFX noisy** | Effect has no source, physics, or dissipation | Add source, material, path, interaction, and endpoint |
| **Prompt blocked** | Protected IP, real-person, graphic, or bypass-like wording | Rewrite intent in safe production language without evasion |
| **Extension quality degrades** | No last-frame anchor or too many new variables across continuations | Use returned last frame as first frame and change one variable |
| **Audio reference ignored** | Competing video sound, no visual beat mapping, or unsupported combo | Mute competing video and map one visible event to the beat |
| **Text/logos break** | Small text asked to move or be redrawn | Keep text static, centered, and protected; animate light around it |
| **Client QC fails** | Prompt output treated as final delivery without post/QC | Route to delivery preflight, post fix, or regenerate only the failing shot |

---

## Sequence-Specific Failures

| Symptom | Likely cause | First repair |
|---------|--------------|--------------|
| **Continuation assumed planned ending** | Previous clip was not reviewed or observed_end_state was ignored | Replace opening with actual observed end state |
| **Previous action restarted** | Completed beat was not marked already_happened | Add completed beat exclusion |
| **Future beat leaked** | Reserved beat entered the current prompt | Remove future beat and stop earlier |
| **Identity reference conflicts with continuity source** | Source clip controlled transient state and identity at once | Re-anchor identity from canonical reference |
| **Screen direction reset** | Axis relation was not locked or intentionally reset | Preserve screen direction or declare new-shot axis reset |
| **Open motion lost** | Subject or camera vector was not inherited | Carry motion vector into the opening sentence |
| **Camera phase restarted** | Parent camera endpoint was not recorded | Start from observed camera phase |
| **Prop state contradicted** | Owner, position, or condition was missing | Add prop state handoff |
| **Audio phase restarted** | Completed dialogue or music phase was not logged | Continue or intentionally change the audio phase |

---

## Repair Process

### Step 1: Quote the Failing Element
Identify exactly what failed:
- Specific phrase in the prompt that caused issues
- Missing element that should have been present
- Conflicting instructions

### Step 2: Name the Root Cause
Don't blame the user. Name the mechanism:
- "The prompt had two camera moves competing"
- "Identity wasn't locked, so the model re-interpreted it"
- "The line was too long for reliable lip-sync"

### Step 3: Remove Conflicts, Don't Add Complexity
**Don't pile on more adjectives.** Instead:
- Remove competing instructions
- Simplify overloaded prompts
- Lock down variables that should stay constant

### Step 4: Recommend One Primary Repair Variable
Focus on the single most impactful change:
- "Lock the camera angle" (not "lock camera and change lighting and add more detail")
- "Shorten the dialogue line" (not "shorten line and change expression and adjust timing")

### Step 5: Produce Conservative Retry Prompt
One clear, simplified prompt that fixes the root cause.

---

## Conservative Retry Pattern

```
[Reference role if any]. Preserve [identity/product/environment] exactly. One visible action: [specific verb and consequence]. Camera: [single move]. Lighting: [physical source]. Sound: [ambient/SFX/dialogue]. Constraints: [what must not change].
```

**Example:**

*Failed prompt:*
```
Beautiful woman dramatically walks through park while camera spins around her in cinematic golden hour with epic music
```

*Issues:* Multiple camera moves ("walks" + "spins"), vague style ("beautiful," "dramatic," "cinematic," "epic")

*Conservative retry:*
```
@Image1 is character reference; preserve face, brown hair, and red coat exactly. Woman walks forward on gravel path through park, 6 steps, arms swing naturally. Camera locked 50mm medium shot, walks toward camera. Golden hour afternoon light, sun 20° above horizon, warm shadows stretch behind her. Sound: footsteps on gravel, distant bird calls, no music. Ends with her 2 meters from camera.
```

---

## Common Failure Patterns and Fixes

### 1. Product/Face Morphing

**Symptom:** Identity drifts, face changes, product logo distorts

**Root cause:** 
- I2V prompt re-described the identity (model treats it as new instruction)
- No preservation constraints
- Motion too complex for identity to stay stable

**Fix:**
```
@Image1 is the [product/character] reference; preserve [specific features] exactly. [One simple action]. Camera: [single controlled move]. Constraints: face/logo/shape must remain identical to @Image1.
```

---

### 2. Camera Jumps or Jitter

**Symptom:** Camera movement is erratic, sudden cuts, unstable framing

**Root cause:**
- Multiple incompatible camera moves in one prompt
- No endpoint specified
- Camera + subject motion conflicting

**Fix:**
- **Choose ONE camera move:** dolly forward OR pan right, not both
- **Specify endpoint:** "Camera dollies forward 2 meters, stops centered on subject"
- **Lock camera if motion is complex:** "Camera static 50mm" while subject moves

---

### 3. Generic/Blurry Output

**Symptom:** Output looks vague, lacks detail, "AI-generated" feel

**Root cause:**
- Hollow style words ("cinematic," "beautiful," "epic")
- Weak action verbs ("walks dramatically")
- No physical light source or material details

**Fix:**
- Replace style words with **physical details:** "warm overhead practical light" not "beautiful lighting"
- Use **strong verbs:** "character grips table edge, knuckles whiten" not "character is stressed"
- Add **materials:** "brushed aluminum, frosted glass" not "modern product"

---

### 4. Motion Ignored

**Symptom:** Nothing happens, static output despite motion requested

**Root cause:**
- Prompt describes static state, no action verb
- No visible consequence of the action
- Action endpoint not specified

**Fix:**
```
[Subject] [strong action verb] [timing] [endpoint]. Example: "Character picks up envelope, unfolds it over 3 seconds, reads first line, expression shifts to concern."
```

---

### 5. Lip-Sync Failure

**Symptom:** Mouth doesn't match dialogue, speech ignored, wrong person speaks

**Root cause:**
- Head turning during speech
- Camera moving during speech
- Dialogue line too long (>10 words)
- Speaker not assigned

**Fix:**
```
Character A, locked medium close-up 85mm, faces camera directly, minimal head motion. Character A says "[short line under 10 words]." Clear dialogue, no music. 6 seconds.
```

---

### 6. VFX Noisy/Unstable

**Symptom:** Effects look chaotic, don't integrate with scene, persist indefinitely

**Root cause:**
- No source specified (where effect starts)
- No physics (gravity, collision, dissipation)
- No endpoint (effect never ends)

**Fix:**
```
[Particle/energy/smoke type] [spawns from specific source], [motion path], [interaction with light/objects], [dissipates after X seconds]. Example: "Gold dust particles spiral upward from bottle base, catch backlight, settle on table over 8 seconds."
```

---

### 7. Prompt Blocked

**Symptom:** Generation rejected, content filter triggered

**Root cause:**
- Protected IP/real-person name
- Graphic violence/harm language
- Bypass-like wording

**Fix:** Use **seedance-filter** skill to rewrite in safe production language:
- Add staging context: "choreographed action scene, theatrical props"
- Remove graphic details: "non-graphic aftermath, torn fabric, scattered props"
- Use original characters: not "looks like [Celebrity]" but "action-hero archetype, strong build, determined expression"

---

### 8. Extension Quality Degrades (I2V Chain)

**Symptom:** Clip 3-4 in sequence looks worse, identity drifts, continuity breaks

**Root cause:**
- Too many I2V generations chained (extension depth >2)
- Last frame not used as anchor
- Too many new variables introduced in continuation

**Fix:**
- **Re-anchor from canonical reference** at depth 2
- **Use actual last frame** of previous clip as I2V seed
- **Change ONE variable** per continuation (lighting OR action, not both)

---

### 9. Audio Reference Ignored

**Symptom:** Audio reference doesn't affect output, rhythm not followed

**Root cause:**
- Video reference has competing audio
- No visual beat mapping
- Unsupported audio reference mode

**Fix:**
```
@Audio1 provides tempo at [BPM] only. Mute or remove audio from @Video1. [Visual event] matches beat at [specific timestamps]. Example: "@Audio1 tempo 120 BPM. Light pulses on every downbeat (0s, 1s, 2s, 3s)."
```

---

### 10. Text/Logos Break

**Symptom:** Text becomes illegible, logo distorts, letters morph

**Root cause:**
- Text asked to move or be redrawn
- Small text during camera motion
- Text not protected as anchor

**Fix:**
- **Keep text static, centered, protected**
- **Animate light/effects AROUND text,** not through it
- Use I2V with logo already present in reference image

---

## Escalation Rules

**If same error repeats:**

1. **Split scene into shorter clips** (15s → two 8s clips)
2. **Reduce character count** (3 people → 1 person)
3. **Simplify hand/face motion** (no typing, no face-touching)
4. **Use stronger reference** (T2V → I2V with reference image)
5. **Change mode** (I2V → first/last-frame workflow)

**For unstable text/logos:**
- Keep static, centered, protected
- Do NOT ask model to redraw small text during motion

**For edit/extend failures:**
- Preserve source clip first
- Change only the failing layer (lighting OR action, not both)

---

## Conservative Retry Example

**Original failing prompt:**
```
Epic cinematic scene of a beautiful woman walking dramatically through a park at golden hour while the camera dynamically spins around her showing her flowing dress and hair with emotional music building to a crescendo
```

**Issues identified:**
1. Hollow style words: "epic," "cinematic," "beautiful," "dramatically," "dynamically," "emotional"
2. Multiple camera moves: "walking" + "camera spins"
3. Multiple subject motions: "walking" + "flowing dress" + "flowing hair"
4. Vague music: "emotional music building to crescendo"

**Root cause:** Overload (too many style words, competing camera/subject motion)

**Conservative retry:**
```
@Image1 is character reference; preserve face, shoulder-length brown hair, and red dress exactly. Woman walks forward on gravel path through park, 6 steps at steady pace, arms swing naturally by sides. Camera locked 50mm medium shot, static, woman walks toward camera. Late afternoon golden hour, sun 20° above horizon behind camera, warm front light, soft shadows behind her. Sound: footsteps on gravel (steady rhythm), distant bird calls, light breeze through trees, no music. Dress and hair move gently with walking motion. Ends with woman 2 meters from camera, slight smile. 12 seconds continuous motion, no cuts.
```

**What changed:**
- Removed all hollow style words
- ONE camera setup: static locked 50mm
- ONE action: forward walk with specific step count
- Specific lighting: sun angle, direction, quality
- Simple sound: gravel footsteps, birds, breeze (no vague "emotional music")
- Specified endpoint: 2 meters from camera

---

## Output Structure

When responding to troubleshooting requests, provide:

1. **Root cause** (name the mechanism, not the user)
2. **Evidence** (quote failing phrase or identify missing element)
3. **Primary repair** (one main variable to change)
4. **Conservative retry prompt** (simplified, clear, one focus)
5. **Optional creative variant** (only if user wants exploration)

---

## Anti-Patterns

❌ **Adding more adjectives to fix generic output:**  
```
Very cinematic and extremely beautiful with ultra-professional lighting
```
→ This makes it worse. Replace style words with physical details.

❌ **Blaming the user:**  
```
Your prompt was too vague
```
→ Say: "The prompt had competing camera moves — let's choose one"

❌ **Piling on complexity:**  
```
Let's add more camera moves AND change the lighting AND add music
```
→ Fix ONE thing at a time

❌ **Not checking extension depth:**  
```
Just keep extending from the previous clip indefinitely
```
→ Re-anchor from canonical reference at depth 2

---

## Summary

**Troubleshooting workflow:**
1. Identify symptom (morphing, jitter, desync, blocked, generic)
2. Diagnose root cause (overload, ambiguity, conflict, missing constraint)
3. Quote failing element
4. Remove conflicts (don't add complexity)
5. Recommend ONE primary repair
6. Deliver conservative retry prompt
7. If same error repeats, escalate (simplify, split, re-anchor)

**Key principle:** Rescue without blame. Name the mechanism, save the idea, preserve confidence.

---

**Related skills:** seedance-prompt, seedance-filter, seedance-continuation, seedance-antislop
