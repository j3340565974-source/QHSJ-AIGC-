# Deep Model Adapter Cards

This file is deliberately model-by-model. It does not assume that similar controls imply identical syntax.

## 01. MiniMax H3/Hailuo

### Capability discovery
At runtime query the adapter registry for supported operations: image-to-video, reference-to-video, keyframe interpolation, character consistency. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "MiniMax H3/Hailuo"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 02. Pavo Agnes Video 2.5

### Capability discovery
At runtime query the adapter registry for supported operations: reference-to-video, keyframe interpolation, character consistency, environment consistency. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Pavo Agnes Video 2.5"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 03. Pavo Agnes Video 2.5 Flash

### Capability discovery
At runtime query the adapter registry for supported operations: keyframe interpolation, character consistency, environment consistency, multi-shot. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Pavo Agnes Video 2.5 Flash"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 04. Kling 3.0

### Capability discovery
At runtime query the adapter registry for supported operations: character consistency, environment consistency, multi-shot, audio-aware. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Kling 3.0"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 05. Veo 3.1

### Capability discovery
At runtime query the adapter registry for supported operations: environment consistency, multi-shot, audio-aware, image editing. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Veo 3.1"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 06. Sora 2

### Capability discovery
At runtime query the adapter registry for supported operations: multi-shot, audio-aware, image editing, inpainting. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Sora 2"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 07. Runway Gen-4

### Capability discovery
At runtime query the adapter registry for supported operations: audio-aware, image editing, inpainting, outpainting. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Runway Gen-4"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 08. Seedance 2.5

### Capability discovery
At runtime query the adapter registry for supported operations: image editing, inpainting, outpainting, style transfer. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Seedance 2.5"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 09. Luma Ray

### Capability discovery
At runtime query the adapter registry for supported operations: inpainting, outpainting, style transfer. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Luma Ray"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 10. Vidu

### Capability discovery
At runtime query the adapter registry for supported operations: outpainting, style transfer. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Vidu"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 11. PixVerse

### Capability discovery
At runtime query the adapter registry for supported operations: style transfer. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "PixVerse"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 12. Pika

### Capability discovery
At runtime query the adapter registry for supported operations: text-to-video, image-to-video, reference-to-video, keyframe interpolation. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Pika"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 13. Midjourney v6

### Capability discovery
At runtime query the adapter registry for supported operations: image-to-video, reference-to-video, keyframe interpolation, character consistency. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Midjourney v6"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 14. Midjourney v7

### Capability discovery
At runtime query the adapter registry for supported operations: reference-to-video, keyframe interpolation, character consistency, environment consistency. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Midjourney v7"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 15. FLUX

### Capability discovery
At runtime query the adapter registry for supported operations: keyframe interpolation, character consistency, environment consistency, multi-shot. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "FLUX"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 16. SDXL

### Capability discovery
At runtime query the adapter registry for supported operations: character consistency, environment consistency, multi-shot, audio-aware. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "SDXL"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 17. GPT-Image

### Capability discovery
At runtime query the adapter registry for supported operations: environment consistency, multi-shot, audio-aware, image editing. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "GPT-Image"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 18. Nano Banana

### Capability discovery
At runtime query the adapter registry for supported operations: multi-shot, audio-aware, image editing, inpainting. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "Nano Banana"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 19. 即梦

### Capability discovery
At runtime query the adapter registry for supported operations: audio-aware, image editing, inpainting, outpainting. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "即梦"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 20. 可灵

### Capability discovery
At runtime query the adapter registry for supported operations: image editing, inpainting, outpainting, style transfer. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "可灵"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.

## 21. 豆包

### Capability discovery
At runtime query the adapter registry for supported operations: inpainting, outpainting, style transfer. If a feature is absent, set `unsupported` and choose a fallback path.

### Prompt grammar
Preferred representation before compilation:
`SUBJECT | CONTEXT | ACTION | TEMPORAL_BEATS | CAMERA | PERFORMANCE | LIGHT | MATERIAL | AUDIO | OUTPUT | REFERENCES | CONSTRAINTS`.
The final compiler may reorder or rename fields only when the target schema requires it.

### Parameter categories
- identity: stable asset IDs, reference roles, character/environment locks
- motion: action verb, acceleration, direction, contact, recovery
- camera: framing, position, lens intent, focus, movement and speed profile
- temporal: total duration, beat list, cut points, end state
- image controls: aspect, resolution, quality, seed and guidance where supported
- audio: dialogue intent, SFX, ambience, voice identity, music policy

### Constraint translation
1. Hard creative fact → keep verbatim in IR.
2. Soft aesthetic preference → compile as stylistic preference.
3. Unsupported parameter → remove or translate to observable language.
4. Negative instruction → use native negative field only if supported; otherwise restate as desired positive state.

### Example compiler input
```yaml
model: "豆包"
subject: "character_A with locked identity"
scene: "warehouse_at_night"
action: ["turns head", "takes two steps", "raises left hand"]
camera: "medium close-up, slow lateral track"
lighting: "single sodium-vapor source from screen right, cool ambient fill"
audio: ["shoe contact", "cloth movement", "distant machinery"]
references: ["character_A_sheet", "warehouse_anchor"]
```

### Failure cases
- UI syntax copied into API request → schema error.
- API field treated as universal → silent parameter drop.
- Reference role unspecified → identity drift.
- Too many actions in a single clip → motion collapse.
- End-state omitted → seam mismatch.

### Audit
Evidence: current adapter registry.
Checked: 2026-09-29.
Refresh: 7 days for API limits, 30 days for prompting guidance.
