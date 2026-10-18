# QHSJ Seedance 音频/配音提示词

# Seedance 2.0 — Audio Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Audio, dialogue, lip-sync, music, sound effects, ambience, beat-sync

---

## When to Use This Skill

- User asks for **dialogue** or **lip-sync**
- User wants **music**, **sound effects**, or **ambience**
- User asks for **beat-sync** (visual motion matching audio rhythm)
- User mentions **audio reference** mapping
- User reports **desync** issues (dialogue not matching mouth)
- User wants **sound-driven visual timing**

---

## Core Principle

**Half of every emotion enters through the ears.** Users almost always forget sound until its absence makes the clip feel dead. Give every scene its sound before being asked — the room's breath, the action's evidence, the line that lands.

---

## Intent

Sound completes the reality. When they hear it, they realize it was always part of what they meant.

---

## Audio Layers

Use compact sound layers in prompts. Include **only the layers that matter**. Silence is valid when it sharpens drama or avoids confusing lip-sync.

**Layer pattern:**
```
Dialogue: [quoted lines with speaker tags]
Sound: [ambient room tone, environment]
SFX: [specific action sounds with timing]
Music: [style, mood, tempo]
Silence: [when/why silent]
```

---

## Dialogue and Lip-Sync

### Core Rules for Lip-Sync:

1. **Keep dialogue short** (under 10 words per line)
2. **Quote spoken lines** (use quotation marks)
3. **Assign every line to a named speaker** (Character A says "...")
4. **Lock camera framing** (no handheld, no zoom during speech)
5. **Remove head motion** (no turning, no large head movement)
6. **Avoid hand gestures near face** during speech
7. **Use voice reference audio when available** (most reliable path)

### Language Reliability (Field-Observed):

| Language | Lip-sync reliability | Recommendation |
|----------|---------------------|----------------|
| **Mandarin Chinese** | Strongest | Lines up to 15 words, clear delivery |
| **English** | Strong | Lines up to 12 words, enunciate clearly |
| **Japanese** | Moderate | Keep lines under 8 words, use voice reference |
| **Korean** | Moderate | Keep lines under 8 words, use voice reference |
| **Russian** | Moderate-Weak | Keep lines under 6 words, budget retakes |
| **Spanish** | Moderate | Keep lines under 10 words |
| **Other languages** | Weak | Use voice reference audio, keep very short |

**Voice reference audio:** Field reports indicate that attaching a voice clip drives lip-sync directly (model syncs to your audio instead of synthesizing speech). **Most reliable path for non-English dialogue.** Use only rights-cleared voices.

---

## Dialogue Prompt Patterns

### Single Speaker:
```
Character A, locked medium close-up, camera static 85mm, faces camera directly. Character A says "I found it." Clear dry dialogue, no background music, no head turn. Light from window left, soft shadows. 8 seconds.
```

### Two Speakers (Sequential):
```
Character A says "Where did you put it?" Pause 2 seconds. Character B says "In the drawer." Camera static medium two-shot, both visible, minimal head motion. Clear dialogue, room tone only. 12 seconds.
```

**Avoid simultaneous speech** — one speaker per moment for reliable lip-sync.

---

## Audio Reference (`@Audio1`)

`@Audio1` can provide:
- **Rhythm/tempo** (beat timing, pacing)
- **Mood** (energetic, melancholic, tense)
- **Voice tone** (when used as voice reference for lip-sync)
- **Ambience** (environmental sound texture)

**Explicit role assignment:**
```
@Audio1 provides tempo only; light pulses and foot taps match the downbeat. Do not transfer melody or instruments.
```

**Voice reference for lip-sync:**
```
@Audio1 is a voice reference; sync Character A's mouth to the provided audio. Use exact timing and inflection from the reference.
```

**Important:** State what `@Audio1` controls and what it does NOT control.

---

## Sound Effects (SFX)

**Anchor SFX to visible actions** with timing.

### Product/Object SFX:
```
SFX: magnetic click at 3 seconds when lid snaps open, soft glass chime at 8 seconds when bottle settles on table.
```

### Action SFX:
```
SFX: footsteps on wood floor (4 steps, 2 seconds), door handle rattle (1 second), door creak as it opens (2 seconds).
```

### Ambient SFX:
```
SFX: distant traffic hum, refrigerator motor, wind through trees, rain on window glass.
```

**Key:** Be specific about **what sound**, **when it occurs**, and **what causes it**.

---

## Music

**Describe music by function, not by artist/song name** (copyright safe).

### Music Descriptors:

**Mood:**
- Tense (low strings, dissonant notes, slow pulse)
- Uplifting (bright piano, major key, rising melody)
- Melancholic (solo cello, minor key, slow tempo)
- Energetic (fast drums, synth bass, 120 BPM)

**Instruments:**
- Solo piano, string quartet, acoustic guitar, synth pads, electronic drums

**Tempo/Rhythm:**
- 60 BPM (slow), 90 BPM (moderate), 120 BPM (energetic), 140+ BPM (fast)
- 4/4 time, waltz (3/4 time), syncopated

**Example music prompts:**
```
Music: Slow melancholic piano, minor key, 70 BPM, soft sustain pedal, fades in at 2 seconds.
```

```
Music: Upbeat electronic track, 120 BPM, synth bass and claps, starts at full volume, no fade.
```

---

## Beat-Sync

**Match visual events to audio rhythm.**

### Beat-Sync Prompt Pattern:
```
@Audio1 provides tempo at 120 BPM. Light pulses on every downbeat (every second). Character's foot taps match the beat: tap at 0s, 1s, 2s, 3s. Camera cuts to new angle on beat 4 (4 seconds).
```

**Key elements:**
- Identify **BPM** or beat timing
- Assign **visual events** to specific beats (light pulse, foot tap, gesture, camera move)
- Keep beat-matched actions **simple** (pulse, tap, blink, not complex choreography)

---

## Ambience

**Room tone and environmental sound create realism.**

### Ambience Examples:

**Indoor:**
- `Low room tone, refrigerator hum, distant muffled voices from adjacent room`
- `Quiet office ambience, keyboard clicks in background, air conditioning white noise`
- `Cafe ambience, espresso machine hiss, distant conversation murmur, ceramic clink`

**Outdoor:**
- `Wind through tall grass, distant bird calls, tree branch creak`
- `Urban street ambience, distant traffic, car horn, footsteps on pavement`
- `Beach ambience, ocean waves crash every 8 seconds, seagull cries, wind`

**Silent/Minimal:**
- `Silence, only character breathing audible`
- `No music, no SFX, only ambient room tone`

---

## Multi-Character Dialogue

**Use one speaker per short clip** when reliability matters.

If two characters must speak in one clip:
1. **Separate turns** (Character A speaks, pause, Character B speaks)
2. **Keep camera stable** (no panning between speakers)
3. **Assign dialogue clearly:**

```
Character A says "Did you hear that?" Pause 2 seconds, face shows concern. Character B says "I did." Both remain in frame, camera locked medium two-shot. Clear dialogue, no music.
```

**For complex exchanges**, recommend generating **controlled single-speaker clips** and compositing in post-production.

---

## Desync Troubleshooting

If dialogue desyncs (mouth doesn't match audio):

1. **Shorten the line** (under 8-10 words)
2. **Lock the camera** (static, no movement)
3. **Remove head turns** (face camera directly)
4. **Simplify the audio role** (dialogue only, remove competing SFX/music)
5. **Use voice reference audio** (attach audio file, sync to it)
6. **Reduce competing motion** (no hand gestures near face, no blinking during speech)

**If wrong speaker talks:**
- Assign character tags clearly: `Character A says...`
- Use explicit framing: `Character A in foreground left says...`

**If audio is ignored:**
- Remove extra music/SFX instructions (too much audio = model confused)
- Make reference role explicit: `@Audio1 controls dialogue timing only`

---

## Audio/Video Reference Conflicts

If **audio reference** and **video reference** fight each other:

1. **Mute the reference video** before upload (if possible)
2. **Make priority explicit:**
   ```
   @Video1 controls camera motion only; @Audio1 controls tempo and energy. Do not transfer audio from @Video1.
   ```
3. **Separate references:**
   - Use video reference in Clip 1 (establish camera/motion)
   - Use audio reference in Clip 2 (establish rhythm/music)

---

## Sequence Audio Continuity

When working in a **multi-clip sequence**, inherit:

- **Completed dialogue** (don't repeat lines already spoken)
- **Active ambience** (if cafe ambience in Clip 1, continue in Clip 2 unless scene changes)
- **Music phase** (if music started in Clip 1, continue or fade out in Clip 2)
- **SFX phase** (if door opened in Clip 1, door is already open in Clip 2)

**Do NOT repeat completed dialogue** unless explicitly asked for a reprise.

---
