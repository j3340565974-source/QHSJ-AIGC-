# Model Matrix — Individually maintained adapters

Global rule: every entry below is independent. The package must never merge two models merely because their controls look similar. `source_type` is evidence class; `checked_at` and `refresh_after` are mandatory at runtime.

## MiniMax H3/Hailuo
- kind: video
- evidence: secondary/public API verification required
- syntax/compiler rule: Do not hard-code any timestamp grammar unless current source confirms it; compile from IR beats and validate current endpoint schema.
- control surface: text→video/image→video/audio-aware workflows; exact controls depend on endpoint.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Pavo (Agnes Video 2.5 / 2.5 Flash)
- kind: video
- evidence: secondary public SDK documentation
- syntax/compiler rule: Support mode text/keyframe/reference only when adapter confirms current schema; treat 4–12s and size options as volatile.
- control surface: mode + references + duration + prompt; verify endpoint before execution.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Kling 3.0
- kind: video
- evidence: official API/docs
- syntax/compiler rule: Multi-shot syntax and reference handles must be generated from current schema; do not mix API JSON with UI-only syntax.
- control surface: shot blocks, duration allocation, reference elements, first/last frame where available.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Veo 3.1
- kind: video
- evidence: official Google docs
- syntax/compiler rule: Native audio and reference-based generation are available in current public materials; compile scene/action/audio as separate IR fields.
- control surface: text, image/reference, camera control, audio intent, extension where supported.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Sora 2
- kind: video
- evidence: official OpenAI API docs
- syntax/compiler rule: Current public API exposes model, duration, size and optional input reference. Treat dimensions/durations as adapter fields refreshed from docs.
- control surface: POST /v1/videos; model + prompt + duration + size + optional input_reference.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Runway Gen-4
- kind: video
- evidence: official Runway help
- syntax/compiler rule: Gen-4 uses an image input workflow in the cited guide; prompts emphasize motion. Avoid unsupported negative prompt recipes.
- control surface: image + motion-focused prompt + duration/resolution fields from current endpoint.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Seedance 2.5
- kind: video
- evidence: public guide + current community skills
- syntax/compiler rule: Compile assets through a normalized media-reference manifest; use timeline beats instead of unsupported pseudo-syntax.
- control surface: prompt + reference media + timing beats + audio intent + aspect/duration.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Luma Ray
- kind: video
- evidence: current vendor docs required
- syntax/compiler rule: Adapter remains capability-discovered because endpoint names/limits change quickly.
- control surface: text/image/reference → clip with current endpoint parameters.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Vidu
- kind: video
- evidence: official current API docs
- syntax/compiler rule: Prompt max length and durations are endpoint/model-dependent; use live model registry before request.
- control surface: model + prompt + duration + seed + aspect_ratio + resolution.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## PixVerse
- kind: video
- evidence: current vendor/API docs required
- syntax/compiler rule: Separate scene prompt from parameter object; reference and audio capabilities are adapter-discovered.
- control surface: prompt + assets + duration/aspect/quality + optional reference controls.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Pika
- kind: video
- evidence: current vendor/API docs required
- syntax/compiler rule: Keep generation intent model-neutral; compile only documented fields.
- control surface: prompt + reference/media + motion/control parameters confirmed at runtime.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Midjourney v6
- kind: image
- evidence: official parameter docs
- syntax/compiler rule: Parameters are appended after prompt; use --ar etc only where supported by current mode.
- control surface: prompt + terminal parameters.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Midjourney v7
- kind: image
- evidence: official parameter docs
- syntax/compiler rule: Use current v7 image/reference parameters and preserve parameter-at-end ordering.
- control surface: prompt + --ar/--s/--q/--seed/--iw/--sref/--oref as applicable.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## FLUX
- kind: image
- evidence: official BFL docs + agent guidance
- syntax/compiler rule: Positive description is preferred; current BFL guidance says FLUX does not support negative prompts in the cited best-practice skill.
- control surface: subject + action + style + context + lighting + technical details; multi-reference by current model.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## SDXL
- kind: image
- evidence: open ecosystem
- syntax/compiler rule: Supports weighted prompt syntax in common UIs, but exact parser varies; keep weights adapter-specific.
- control surface: prompt tokens + weights + negative prompt + sampler/steps/CFG via runtime adapter.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## GPT-Image
- kind: image
- evidence: official OpenAI docs required
- syntax/compiler rule: Keep image request schema separate from text-only model prompts; use live API adapter.
- control surface: instruction + reference images + size/quality/background according to current API.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## Nano Banana
- kind: image
- evidence: official Google docs
- syntax/compiler rule: Treat as multimodal image generation/editing family; use multiple references through the current API/host integration.
- control surface: edit/generate instruction + references + desired composition.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## 即梦
- kind: image/video
- evidence: vendor UI/API dependent
- syntax/compiler rule: Use natural-language compiler and isolate volatile UI parameters.
- control surface: brief + image/video references + current workspace settings.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## 可灵
- kind: image/video
- evidence: vendor/API dependent
- syntax/compiler rule: Use current adapter for model family; do not mix current endpoint names with legacy UI recipes.
- control surface: prompt + reference + duration/aspect + motion controls from current docs.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.

## 豆包
- kind: image/video
- evidence: vendor/API dependent
- syntax/compiler rule: Keep prompt compiler platform-neutral and compile to current vendor schema.
- control surface: prompt + reference + current model parameters.
- IR mapping:
  1. subject_identity → stable asset IDs and visible descriptors
  2. scene_context → location, time, environment and continuity state
  3. action → observable action verbs and temporal beats
  4. camera → framing, lens intent, position, motion and focus
  5. lighting → source, direction, quality, color temperature and contrast intent
  6. audio → dialogue, SFX, ambience, music policy
  7. references → file IDs, reference roles and strength values when supported
  8. output → duration, aspect, resolution and quality settings
- refusal rule: if current adapter cannot validate a field, omit it or mark it `unsupported`; never fabricate a parameter.
- freshness: checked_at: 2026-09-29; refresh_after_days: 7 for volatile API details, 30 for stable prompt guidance.
