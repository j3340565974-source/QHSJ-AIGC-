# 12-Beat Emotion Curve Library

## Beat 01 — hook
Function: hook.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 02 — question
Function: question.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 03 — proof
Function: proof.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 04 — pressure
Function: pressure.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 05 — reaction
Function: reaction.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 06 — complication
Function: complication.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 07 — temporary_win
Function: temporary_win.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 08 — counterattack
Function: counterattack.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 09 — reveal
Function: reveal.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 10 — cost
Function: cost.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 11 — choice
Function: choice.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Beat 12 — cliffhanger
Function: cliffhanger.
Inputs: previous pressure, character goal, current knowledge state, time remaining.
Outputs: new information, emotion delta, spatial delta, continuity state.
Observable form: action, expression, dialogue fragment, sound cue, visual change.

## Adaptive timing equation
Given total runtime `T` and base weights `w_i`, compute provisional time `t_i=T*w_i/Σw_i`. Apply `clamp(min_i,max_i)` then renormalize all unclamped beats until `Σt_i=T`. Preserve mandatory reveal/turn beats with minimum time budgets.

## Curves
- tension: slow build → rapid escalation → peak → release
- grief: interruption → avoidance → leakage → admission → changed behavior
- comedy: setup → expectation → mismatch → reaction → escalation → snap return
- horror: normality → anomaly → recognition → proximity → false relief → violation
