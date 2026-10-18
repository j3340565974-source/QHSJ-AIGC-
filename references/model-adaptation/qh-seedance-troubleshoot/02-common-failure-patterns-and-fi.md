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
