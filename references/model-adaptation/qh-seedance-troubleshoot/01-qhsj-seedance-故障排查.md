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
