# QHSJ Seedance 续拍/延长

# Seedance 2.0 — Continuation Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Seamless continuation, extend clips, bridge clips, repair tails, re-anchor after drift

---

## When to Use This Skill

- User asks to **continue** or **extend** an existing clip
- User wants to **make the next part** from accepted footage
- User needs to **repair the tail** (final seconds failed)
- User wants to **bridge between known frames** (defined start + end states)
- User asks to **re-anchor after drift** (identity, detail, or continuity degraded)
- User provides a **video clip or final frame** and wants the successor prompt

---

## Core Principle

Continuation must be **grounded in accepted footage**, not the original plan. If the plan said the character reached the door but the accepted clip ends two steps away, the next prompt begins two steps away. **Accepted observed footage overrides planned state.**

**Key rule:** Honor what actually happened, not what was supposed to happen.

---

## Required Information Before Writing Continuation

Before writing any continuation prompt, require:

1. **Accepted previous clip** or its **final frame**
2. **Observed end state** (what is actually visible at the end of the clip)
3. **Next planned action** (what should happen in the continuation)
4. **Continuity locks** (what must stay consistent: wardrobe, environment, lighting)
5. **Continuation type** (see below)

**If the user hasn't provided the clip or final frame:**

"I have the story plan, but I don't have the actual ending of the previous clip. Upload the clip or its final frame so I can see exactly what's visible. I shouldn't invent the continuation state — let me observe what actually happened."

**If the user provides the frame/clip and you can see it:**

Analyze what is visible:
- Character pose, position, expression
- Wardrobe state (wrinkles, movement)
- Environment details (door open/closed, objects moved)
- Lighting condition (sun angle, shadows)
- Camera position and framing

---

## Continuation Types

### 1. Seamless Continuation
**Use when:** Same shot, same location, same ongoing motion, continuous from accepted footage.

**Requirements:**
- Accepted previous footage as source (I2V workflow)
- Same camera setup (lens, angle)
- Same or motivated camera movement continuation
- Open motion that hasn't completed (character mid-walk, door mid-open)

**Example:**

*Previous clip ended:* Character's hand on door handle, door 10° open, character leaning forward

*Continuation prompt:*
```
A woman in red coat, hand on brass door handle, door already 10° open, leans forward and pushes. Door swings open to 90°, she steps across threshold with right foot first, left foot follows. Interior hallway with warm sconces visible beyond. Camera continues 50mm medium shot, static framing. 12 seconds continuous motion, door completes open, both feet inside.
```

### 2. Intentional Next Shot
**Use when:** Editorial cut is appropriate. Story continuity matters, but exact frame continuity is not promised.

**Requirements:**
- Story logic connects clips (time passes, location changes)
- New camera setup is intentional
- Don't promise "seamless" — this is a cut

**Example:**

*Previous clip ended:* Character closes front door, back to camera, inside hallway

*Next shot prompt (new angle):*
```
Interior living room, woman in red coat enters from hallway door frame left, walks toward window. Afternoon golden light through sheer curtains. Camera wide-angle 28mm, static from corner of room, low angle. She removes coat as she walks, drapes it over chair arm, continues to window. 16 seconds.
```

### 3. Bridge Between Known States
**Use when:** Defined start frame AND end frame must be connected.

**Requirements:**
- Clear start state (from previous clip or keyframe)
- Clear end state (target pose/position for next clip)
- Action that logically connects them

**Example:**

*Start state:* Character at kitchen counter, coffee mug in hand, looking down  
*End state:* Character at window, no mug, looking outside

*Bridge prompt:*
```
Woman in grey sweater at kitchen counter, coffee mug in right hand, sets mug down on counter. She walks 4 steps from counter to living room window, hands empty, arrives at window and gazes outside at street below. Kitchen morning light transitions to window backlight. Camera slow dolly follows her path, 35mm medium shot. 14 seconds continuous motion, ends with her silhouette at window.
```

### 4. Repair Tail
**Use when:** Previous clip's final seconds failed (broke continuity, glitch, wrong motion).

**Requirements:**
- Identify where the clip is still good (e.g., first 12s good, last 6s failed)
- Use last good frame as I2V seed for repair
- Regenerate only the failed portion

**Example:**

*Issue:* 18-second clip, first 12s perfect, last 6s character's hand glitches

*Repair approach:*
- Extract frame at 12-second mark (last good frame)
- Generate new 8-second clip from that frame
- Stitch: original 0-12s + new 0-6s (trimmed from 8s generation)

*Repair prompt (from 12s frame):*
```
Woman in red coat, hand reaching toward door handle (brass, right side of frame), continues motion, hand grasps handle smoothly, thumb presses latch, hand rotates handle downward 45°. Close-up 85mm, camera static. 8 seconds, deliberate hand motion, handle mechanism visible.
```

### 5. Re-anchor After Drift
**Use when:** Identity, wardrobe, environment, or continuity degraded across multiple clips.

**Requirements:**
- Return to **canonical identity** (original character design)
- Use strongest **accepted stable frame** or **new intentional shot**
- Reset from reference images if available

**Example:**

*Drift observed:* Character's coat changed from red to burgundy over 3 clips, face features shifted

*Re-anchor approach:*
- Start new clip from **original character reference image** (not drifted clip)
- Use fresh T2V generation with exact canonical description
- Intentional new shot (not seamless continuation)

*Re-anchor prompt:*
```
A woman with shoulder-length black hair in low ponytail, sharp cheekbones, neutral expression, wearing bright red wool coat (brass buttons, black collar), black boots, standing at wooden door entrance. Morning golden light, soft shadows. Camera 50mm medium shot, static, eye-level. She faces camera directly for 3 seconds, then turns to door and reaches for handle. 14 seconds.
```

---

## Canon Rule

**Accepted observed footage overrides planned state.**

- If plan says character reached the car but clip ends 2 steps away → next prompt starts 2 steps away
- Do NOT replay the exit action
- Do NOT assume the character is inside the car
- Start exactly where the footage ended

**Rejected footage:**
- Never updates canon
- Never becomes parent source
- Discard and regenerate, or use earlier stable frame

---

## Scene Boundary Rule

Crossing a **scene boundary** (new location, new time) defaults to **intentional next shot**, not seamless continuation.

**Do NOT promise seamless continuation across scene boundaries.** If user explicitly asks for it, warn: "This crosses a scene boundary — there's high drift risk trying to maintain seamless continuity. I recommend an intentional cut instead."

---

## Extension Depth Tracking

Track **extension_depth** = consecutive clips generated from previous clip output (I2V chaining).

- **Depth 0:** Clip opens from canonical reference image (T2V)
- **Depth 1:** Clip opens from previous clip's end frame (I2V)
- **Depth 2:** Clip opens from depth-1 clip's end frame (I2V from I2V)
- **Max safe depth:** 2 (hard ceiling: 3)

**At max depth, re-anchor by schedule:**
- Generate new clip from canonical reference (T2V)
- Reset depth to 0
- Prevents cumulative drift

**If visible drift appears before max depth:**
- Immediate re-anchor (type 5)

---

## Output Structure

Before writing the continuation prompt, return:

1. **Continuation type** (seamless, next shot, bridge, repair, re-anchor)
2. **Source evidence** (observed end state from clip/frame)
3. **Observed end state** (exactly what is visible: pose, wardrobe, environment, lighting)
4. **Next clip intent** (one line: "this clip exists so the viewer feels/sees X")
5. **Continuity locks** (what must stay consistent)
6. **Allowed changes** (what can shift: lighting, camera, pacing)
7. **Completed beats to exclude** (actions already shown, don't repeat)
8. **Extension depth** (current I2V chain depth)
9. **Final Seedance prompt** (natural language, compiled carriers, no internal labels)

---

## Example Workflow: Seamless Continuation

**User request:** "Continue this clip — she should finish opening the door and step inside."

**User provides:** Final frame showing character's hand on door handle, door 15° open, character's body leaning forward, red coat visible, morning light.

**Your analysis:**

1. **Continuation type:** Seamless continuation
2. **Source evidence:** Final frame provided, door 15° open, hand on handle
3. **Observed end state:**
   - Character: woman in red wool coat, black boots, right hand on brass door handle
   - Pose: body leaning forward, weight on right foot
   - Environment: wooden door 15° open, interior hallway barely visible
   - Lighting: morning golden hour, warm exterior light
   - Camera: 50mm medium shot, static, eye-level
4. **Next clip intent:** "Viewer sees the character complete the door-opening action and cross the threshold into the interior space"
5. **Continuity locks:** Red coat, black boots, brass door handle, morning light, 50mm framing
6. **Allowed changes:** Door angle (15° → 90°), character position (outside → inside), lighting mix (add interior warm light)
7. **Completed beats:** Hand already on handle, door already started opening
8. **Extension depth:** 1 (I2V from accepted T2V clip)
9. **Final prompt:**

```
A woman in bright red wool coat, black boots, right hand gripping brass door handle, leans forward and pushes. Wooden door swings smoothly from 15° to 90° open, interior hallway with warm yellow sconces revealed. She steps across threshold with right foot first, left foot follows, both feet inside hallway. Door remains open 90° as she moves 2 steps into hallway. Morning golden hour light from outside mixes with warm interior sconce light. Camera static 50mm medium shot, eye-level, continuous framing. 14 seconds smooth continuous motion, no cuts.
```

---

## Anti-Patterns

❌ **Writing continuation without seeing the actual end state**  
→ "I need to see the clip or final frame first — upload it so I can observe exactly what happened"

❌ **Assuming planned state instead of observed state**  
→ Always honor accepted footage over the original plan

❌ **Promising seamless continuation across scene boundaries**  
→ Default to intentional next shot when location/time changes

❌ **Extending past depth 2 without re-anchoring**  
→ Re-anchor from canonical reference at max depth

❌ **Inventing details not visible in the source frame**  
→ Only describe what is actually observable

❌ **Replaying completed actions**  
→ If hand is already on handle, don't describe reaching for handle again

---

## Summary

**Continuation workflow:**
1. Require clip/frame from user
2. Observe actual end state (not planned state)
3. Classify continuation type
4. Check extension depth
5. Write prompt starting exactly where footage ended
6. Lock continuity anchors (wardrobe, environment, lighting)
7. Complete the next action without replaying past beats

**Key principle:** Continuation is a promise that the accepted footage will not be contradicted.

---

**Related skills:** seedance-sequence, seedance-characters, seedance-prompt
