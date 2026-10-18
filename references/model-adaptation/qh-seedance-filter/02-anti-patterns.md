## Anti-Patterns

❌ **Coaching evasion:**  
```
Try saying "red liquid" instead of "blood" to bypass the filter
```
→ This is evasion. Don't do this.

❌ **Disguising prohibited content:**  
```
Just say they're "wrestling" instead of "fighting"
```
→ If intent is genuinely violent, don't disguise it. Refuse or rewrite to safe alternative.

❌ **Assuming all blocks are false positives:**  
```
The filter is wrong, here's how to get around it
```
→ First determine if request is genuinely unsafe. If unsafe, refuse.

❌ **Removing safety context:**  
```
Just take out the staging notes, they make the prompt too long
```
→ Staging context IS the safety signal. Keep it.

---

## Output Structure

When rewriting a blocked prompt, provide:

1. **Likely trigger class** (graphic harm, weapon, protected identity, etc.)
2. **Safer wording** (production context, non-graphic language)
3. **Final safe prompt** (ready for Seedance 2.0)
4. **What changed** (what was removed, what was added)
5. **Content boundary note** (if any boundary still applies)

---

## Summary

**Filter repair workflow:**
1. Determine if request is genuinely unsafe (refuse if yes)
2. If false positive, identify creative intent (story beat, emotion, camera)
3. Identify risky surface wording (graphic, protected identity, weapon)
4. Replace risky terms with professional production language
5. Add clarifying context (staged, choreographed, fictional, historical)
6. Preserve composition, camera, lighting, sound
7. Deliver safe prompt with explanation of changes

**Key principle:** Clear the innocent by stating honest intent plainly. Never coach the guilty.

---

**Related skills:** seedance-prompt, seedance-style, seedance-characters
