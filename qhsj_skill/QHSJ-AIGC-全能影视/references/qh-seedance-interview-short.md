# QHSJ Seedance 采访短视频

# Seedance 2.0 — Interview Short Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Fast creative brief, short interview, compressed intake flow, quick director clarification

---

## When to Use This Skill

- User wants **fast brief** (minimal questions)
- User asks for **short interview** or **quick intake**
- User wants **compressed intake flow** (3 questions max)
- User needs **quick director-style clarification** before prompt writing
- **Speed matters more than exhaustive creative discovery**

---

## Core Principle

**Speed does not bypass story judgment.** Ask at most three questions, and only if the answer materially changes the prompt. Assume no film background: use everyday words, give pickable options, attach a default so "I don't know" never stalls the brief.

---

## Intent

The user knows what they want and is asking you to respect their momentum. The soul of this skill is restraint: find the one missing piece that would sink the generation, ask only that, and get out of the way. Speed is the form their trust takes.

---

## Process

### Step 1: Check What's Already Known
Don't ask questions the user already answered. If they provided enough information, skip to the brief immediately.

### Step 2: Ask Maximum 3 Questions (If Needed)
Only ask if the answer **materially changes the prompt.**

**Priority questions:**

1. **What happens in the video, and what is different at the end?**  
   *(not sure? I'll pick one simple action with a visible ending)*

2. **Is this one complete clip, connected clips, a longer scene to divide, a continuation of accepted footage, or are you unsure?**  
   *(not sure? I'll plan the whole story but only finalize the first prompt)*

3. **How must the complete story end, and do you have photos, clips, final frames, or sound that define the look, motion, or sound?**  
   *(none is fine; if continuing, I need the accepted clip or final frame)*

### Step 3: Produce Compact Brief
Deliver brief immediately after questions (or skip questions if user already supplied enough).

---

## Compact Brief Pattern

```
Mode: [T2V/I2V/V2V/R2V]
Subject: [anchor]
Beat: [before → action → final state]
Camera: [one move]
Light/style: [physical source and safe descriptor]
Sound: [dialogue/ambience/SFX/music/silence]
Constraints: [identity, IP, safety, product, prompt budget]
```

**Example:**

```
Mode: I2V
Subject: @Image1 woman in red coat
Beat: Standing at door → pushes door open → steps inside
Camera: Static 50mm medium shot
Light/style: Morning golden hour transitioning to warm interior sconces
Sound: Door creak, footsteps, quiet ambience
Constraints: Preserve face and red coat exactly from @Image1
```

---

## Question Guidelines

### 1. Everyday Words, Not Production Terms
❌ "What shot size and lens focal length?"  
✅ "Should the camera be close on their face, or show their whole body?"

### 2. Pickable Options (2-4 choices)
❌ "Describe the lighting"  
✅ "Should this feel bright and clean like an ad, or moody with shadows?"

### 3. Always Include Default
Every question ends with: **(not sure? I'll go with [default] — it works well)**

**Example:**
"Where does this happen — indoors or outdoors? (not sure? I'll go with outdoors in afternoon light)"

### 4. Adapt to User's Fluency
If user speaks production language (shot list, lens, blocking), switch to director terms immediately. Don't dumb down for professionals.

---

## When NOT to Ask

**Don't ask if:**
- User already answered it
- Answer wouldn't change the prompt
- User is a professional who already provided shot specs

**Example of unnecessary question:**
User: "I want a product video of my perfume bottle rotating on a white background"

❌ Bad: "What should be in the background?"  
→ They already said "white background"

✅ Good: Skip straight to brief or ask only about rotation speed/duration if critical

---

## Routing After Brief

**Route to appropriate skill:**

- **Connected clips, long scenes, unclear total duration:** → `seedance-sequence`
- **Continuation from accepted footage:** → `seedance-continuation`
- **Full standalone production prompt:** → `seedance-prompt`
- **Compact prompt:** → `seedance-prompt-short`
- **IP/likeness risk:** → `seedance-filter`
- **User starting from bad result:** → `seedance-troubleshoot`

---

## Example Fast Interview

### Example 1: User with Clear Idea

**User:** "I want my character walking through a park at sunset"

**Your response:** (No questions needed — enough info to proceed)

```
Quick brief:

Mode: T2V (or I2V if you have a character reference photo)
Subject: Character walking through park
Beat: Character enters park → walks forward on path → stops at bench
Camera: Static 50mm medium shot follows walking
Light: Sunset golden hour, sun low on horizon, warm orange light
Sound: Footsteps on gravel, distant birds, light breeze
Duration: ~12 seconds

Say "yes" and I'll write the full prompt, or tell me what to adjust (camera closer? Different ending? Reference photo?)
```

---

### Example 2: User with Vague Idea

**User:** "I want something cool for my product"

**Your response:** (Ask 2-3 questions max)

```
Quick questions to get started:

1. What happens to the product — does it rotate, open, light up, get picked up, or something else? (not sure? I'll do a slow 360° rotation — always looks polished)

2. Where will people watch this — phone apps like TikTok (tall screen) or YouTube (wide screen)? (not sure? I'll go tall 9:16 for social)

3. Do you have a photo of the actual product? (none is fine — I can describe a generic version, but real photo keeps it looking like yours)
```

---

### Example 3: User Wants Continuation

**User:** "Continue from the last clip — she should walk through the door"

**Your response:** (Ask for source)

```
Got it — to continue seamlessly, I need to see where the last clip actually ended (not where we planned it would end, but where it really ended).

Can you upload:
- The previous clip, or
- The final frame of the previous clip

Once I see the exact ending (her hand position, door angle, lighting), I'll write the continuation prompt that picks up from there.

(If you can't upload, describe exactly what's visible in the last second — where is her hand, how far is the door open, what's her body position?)
```

---

## Compact Brief Examples

### Example 1: Product Video

```
Mode: I2V
Subject: @Image1 glass perfume bottle
Beat: Bottle static → camera rotates 360° → ends front-center
Camera: 360° rotation, 15 seconds, starts/ends front
Light/style: Studio soft box 45° above, white background, controlled reflections
Sound: Quiet room tone only
Constraints: Preserve logo and bottle shape exactly from @Image1
```

---

### Example 2: Drama Scene

```
Mode: T2V
Subject: Woman in her 30s, grey sweater
Beat: Sitting at table, hands on mug → looks up toward window → stands slowly
Camera: Static 50mm medium shot, eye-level
Light/style: Morning window light from left, soft shadows
Sound: Kitchen ambience, refrigerator hum, distant bird call
Constraints: Minimal head motion for stable face
```

---

### Example 3: Sequence Project

```
Mode: Sequence (3 clips)
Story ending: Character reads letter, realizes truth, closes door with resolve
Clip 1 job: Establish character approaching door with letter in hand
Current clip: T2V establishing shot
Camera: Wide 28mm, static
Light/style: Afternoon golden hour, exterior
Sound: Footsteps, paper rustle, ambient
Constraints: Character wardrobe (red coat) locked across all 3 clips
Next: Provisional — finalize after Clip 1 accepted
```

---

## Anti-Patterns

❌ **Asking questions user already answered:**  
User: "My character walks through a park"  
You: "Where does this take place?"  
→ They already said "park"

❌ **Asking more than 3 questions:**  
You: "1. What's the subject? 2. What happens? 3. Where? 4. When? 5. How long? 6. What camera? 7. What sound?"  
→ Too many. Max 3.

❌ **Using production jargon with beginners:**  
"What focal length and aspect ratio?"  
→ Say: "Should the camera be close or far? Tall phone screen or wide TV screen?"

❌ **No default provided:**  
"What lighting do you want?"  
→ Add default: "What lighting — bright and clean, or moody with shadows? (not sure? I'll go with bright afternoon sun)"

---

## Output Structure

When using short interview skill, provide:

1. **Fast questions** (max 3, with defaults)
2. **Compact brief** (under 150 words)
3. **Recommended skill route** (which skill to use next)

---

## Summary

**Short interview workflow:**
1. Check what user already provided (skip questions if enough info)
2. Ask max 3 questions, only if answer changes prompt
3. Use everyday words, pickable options, always include default
4. Deliver compact brief (under 150 words)
5. Route to appropriate skill (sequence, continuation, prompt, troubleshoot)

**Key principle:** Find the one missing piece that would sink the generation, ask only that, get out of the way.

---

**Related skills:** seedance-interview, seedance-prompt, seedance-sequence, seedance-prompt-short
