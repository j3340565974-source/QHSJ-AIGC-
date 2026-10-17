# Prompt Engineering Formula Library

## Universal IR formula
`intent + identity + context + visible_action + temporal_beats + camera + lighting + material + audio + output + references + constraints`

## High-precision image formula
`object + state + change + parameters`

## Video formula
`subject_anchor → environment_anchor → action_beats → camera_path → performance_process → physical_feedback → lighting/audio_continuity → end_state`

## Weight semantics
Where a target parser supports weighted tokens, represent weights in the adapter layer. Do not assume `(term:1.2)` works identically across all models.

## Negative strategy
If the model supports negative prompts, compile explicit defect prevention. If not, convert “avoid X” into a positive desired state.

## Uncertainty labels
`verified` = official/current source; `public` = project documentation; `heuristic` = field practice; `inferred` = engineering inference; `unknown` = not safely claimable.
