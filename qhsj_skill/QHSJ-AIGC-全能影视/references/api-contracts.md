# API Contract Matrix

## MiniMax H3/Hailuo
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Pavo (Agnes Video 2.5 / 2.5 Flash)
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Kling 3.0
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Veo 3.1
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Sora 2
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Runway Gen-4
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Seedance 2.5
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Luma Ray
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Vidu
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## PixVerse
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Pika
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Midjourney v6
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Midjourney v7
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## FLUX
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## SDXL
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## GPT-Image
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## Nano Banana
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## 即梦
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## 可灵
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d

## 豆包
request_fields: task_id, model, prompt, reference_assets, duration, aspect_ratio, resolution, seed, audio_policy, metadata
conditional_fields: first_frame, last_frame, keyframes, multi_shot, style_reference, character_reference, environment_reference
response_fields: job_id, status, media_uri, metadata, provider_version, warnings, errors
validation: reject unknown hard fields; allow adapter-specific `extensions` only under a namespaced object; store raw response checksum.
freshness: 7d
