# QHSJ Seedance 提示词结构

---
name: seedance-prompt
description: "This skill should be used when the user asks to write, improve, translate, compress, or debug a Seedance 2.0 video prompt; mentions T2V, I2V, V2V, R2V, camera direction, prompt quality, or provides reference assets for a production-ready prompt."
license: MIT
user-invocable: true
tags:
  - prompt-engineering
  - video-generation
  - seedance-20
metadata:
  version: "6.7.0"
  updated: "2026-08-01"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-prompt

Before producing prompt text, a prompt-ready block, a rewrite, an example, or a compiled clip, classify the brief and complete its canonical narrative or non-narrative record. Translate that record into visible or audible carriers and keep its internal labels out of final generation prose.

Build production-ready Seedance prompts from clear concepts or supplied reference assets. Treat the prompt as a short shooting brief: it must say what changes on screen, what the camera does, what the light and sound contribute, and what must stay stable. Keep final prompts under the platform prompt budget and remove filler before delivery.

## Intent

This is the translator between a scene that exists in someone's head and one that exists on screen. The user has already imagined it; the job is to lose as little as possible in transit. Success is a first generation close enough that they can react instead of explain. Each revision inherits everything the story has already decided and changes only what the reaction asked for - a draft is a conversation, not a restart.

## Director Formula

Before filling slots, run a director's read gate. A narrative, story, or performance brief must consider: function, turn, POV, power shift, objective, obstacle/tactic, contradiction, one visible suppressed behavior, one non-transferable detail, and one explicit genre refusal. A non-narrative utility, product-only, abstract, VFX, or ambient brief must have a two-line utility intent and refusal, with no fabricated psychology. For narrative work, name a single intention and let it choose camera, lighting, blocking, performance, and sound together. The formula below is the container for a coherent setup, not a checklist of independent decorations.

The director's read is internal planning, not prompt copy. Compile its turn, visible suppressed behavior, and non-transferable detail into visible or audible carriers. Do not paste labels such as `POV`, `power shift`, `hidden want`, or `subtext` into the generation prompt, and do not ship an abstract feeling where blocking, gesture, prop use, camera endpoint, motivated light, dialogue contradiction, silence, or a sound cue can carry it.

Use `Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints`. Put the subject and primary action first because early clauses set the shot hierarchy. Do not force every slot if a reference asset already shows the information; for I2V, describe only the motion, camera, timing, transformation, audio, and preservation constraints that the still image cannot show.

| Slot | Use for | Prompt-ready pattern |
|---|---|---|
| Subject | The anchor the model must track. | `Original ceramic perfume bottle on black acrylic, label preserved exactly` |
| Action | The visible change. | `condensation beads form and slide down the glass over five seconds` |
| Scene | Only what is not already in references. | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | One primary move with endpoint. | `slow dolly-in from medium product shot to macro label detail` |
| Light and style | Physical light plus safe visual language. | `warm practical key from frame left, cool blue rim, clean commercial realism` |
| Audio | Ambient bed, SFX, dialogue, or silence. | `Sound: low room tone, soft glass chime on final frame` |
| Constraints | Preservation and exclusions. | `do not alter logo, shape, label, or cap geometry` |

## Mode Gate

Choose the mode before drafting. **T2V** needs subject, action, scene, camera, light, style, and constraints because nothing is visible yet. **I2V** starts from `@Image1` and adds only motion, time, camera, lighting transition, audio, and preservation. **V2V** should map `@Video1` to source clip, camera move, action rhythm, blocking, edit target, or extension anchor rather than accidentally transferring identity. **R2V** must list every reference role and state what must not transfer. **FLF2V** uses `@Image1` as first frame and `@Image2` as last frame, then describes only the continuous transition.

| Mode | Drafting priority | Common mistake | Repair |
|---|---|---|---|
| T2V | Build the whole shot in compact layers. | Too many events in one clip. | Keep one visible beat and one endpoint. |
| I2V | Preserve visible identity; add motion. | Re-describing the image until the product or face drifts. | Say `preserve @Image1 exactly`; add only dynamic changes. |
| V2V | Transfer motion, camera, or timing. | Copying unauthorized likeness or scene details. | Use owned/licensed/authorized references and restrict transfer role. |
| R2V | Assign separate roles to each asset. | One reference asked to control identity, pose, scene, and style. | Split roles or prioritize the most important role. |
| FLF2V | Move from first frame to last frame. | Treating the last frame as vague mood instead of endpoint. | State `@Image2` is the final visual target. |
| Edit | Preserve the source clip while changing one layer. | Rewriting the whole scene and losing continuity. | Say `@Video1 is the source clip; change only...` |
| Extend | Continue from accepted source footage only. | Starting from a planned ending or inventing the clip state. | Use the observed end state from accepted footage. |

## Prompt Build Process

First, classify the brief and complete the correct lane record before prompt compilation. For a narrative lane, identify the single visible beat and the intention it serves, then map to carriers; for a non-narrative lane, keep the concrete utility intent and refuse invented drama. Next, assign reference roles before adding adjectives. Then write a compact first draft in the director formula order. Finally, run a self-check: one main subject, one main action, one motivated main camera move, physically motivated lighting, performance written as a visible gesture rather than an emotion word, assigned character tags, sound intent, and no hollow boosters.

## Compression Rules

When the prompt is too long, cut in this order: duplicate style adjectives, generic quality words, background details visible in references, secondary camera moves, secondary actions, and speculative emotional labels. Keep preservation constraints, action timing, and role maps. If a user requests a bilingual or mixed-language prompt, use language mixing only for clarity: reference roles, dialogue language, technical camera terms, and safe production constraints. Do not use another language to hide unsafe intent.

## Output Contract

Return:

1. Mode: T2V, I2V, V2V, R2V, FLF2V, edit, or extend.
2. Reference role map, if any.
3. Final prompt under the verified active-surface prompt budget.
4. Optional Chinese compressed version when useful.
5. Shot-list or delivery note when the prompt belongs to a professional sequence.
6. Safety or copyright note when relevant.

Before finalizing, run an anti-slop pass and remove vague quality boosters.
