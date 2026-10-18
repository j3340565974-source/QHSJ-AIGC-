## Example Prompts

### Example 1: Simple Dialogue
```
Character A, woman in red coat, seated at cafe table, medium close-up, camera locked 85mm. Character A faces camera, minimal head motion. Character A says "I don't believe you." Clear dry dialogue, soft cafe ambience (distant conversation, espresso machine). 6 seconds.
```

### Example 2: Product SFX
```
Glass perfume bottle on white pedestal, camera slow push-in 85mm macro. Sound: low room tone. SFX: bottle cap unscrews with soft twist sound at 3 seconds, cap lifts off with gentle pop at 4 seconds, cap sets down on pedestal with soft clink at 7 seconds. No music. 10 seconds.
```

### Example 3: Beat-Sync
```
@Audio1 provides electronic music tempo at 120 BPM. Dancer in black outfit, studio white background, camera locked wide-angle. Dancer's right foot taps floor on every downbeat (every second): 0s, 1s, 2s, 3s, 4s. Arms pulse upward on beats 2 and 4. Studio lights pulse brighter on every beat. 5 seconds continuous motion.
```

### Example 4: Two-Speaker Dialogue
```
Interior office, two characters at desk. Character A (man in suit) frame left says "What did they say?" Pause 2 seconds, Character A's expression shifts to concern. Character B (woman in blazer) frame right says "They declined." Camera static medium two-shot, both visible. Clear dialogue, minimal head motion, quiet office ambience. 10 seconds.
```

### Example 5: Voice Reference Lip-Sync
```
@Audio1 is a voice reference with Mandarin dialogue; sync Character A's mouth to the provided audio exactly. Character A, woman in her 30s, grey sweater, seated at table, medium close-up, camera locked 85mm. Character A faces camera directly, hands on table, no head turn. Soft window light from left. 8 seconds.
```

---

## Anti-Patterns

❌ **Long dialogue lines:**  
```
"I was thinking about what you said yesterday and I realize now that you were right about everything"
```
→ Too long, will desync. Split into 2-3 clips.

❌ **Head turning during speech:**  
```
Character turns to face camera while saying "I don't know"
```
→ Turn OR speak, not both. Turn, pause, then speak.

❌ **Vague music description:**  
```
Epic cinematic music
```
→ Specify: tempo, instruments, mood, when it starts/ends

❌ **No speaker assignment:**  
```
"Where are you going?" someone asks
```
→ Tag clearly: `Character A says "Where are you going?"`

❌ **Competing audio layers:**  
```
Dialogue + music + SFX + ambience all fighting for attention
```
→ Choose 1-2 layers per clip. Dialogue + ambience OR music + SFX, not all four.

---

## Summary

**Audio workflow:**
1. Choose layers (dialogue, sound, SFX, music, silence)
2. Keep dialogue short (under 10 words), quote lines, assign speakers
3. Lock camera for lip-sync (static, no head turns)
4. Use voice reference audio for non-English dialogue
5. Anchor SFX to visible actions with timing
6. Describe music by function (mood, tempo, instruments)
7. Match visual events to audio beats for beat-sync
8. Include ambience for realism
9. Troubleshoot desync: shorten, lock, simplify

**Key principle:** Audio supports the visible beat instead of becoming a second competing prompt.

---

**Related skills:** seedance-prompt, seedance-characters, seedance-motion, seedance-sequence
