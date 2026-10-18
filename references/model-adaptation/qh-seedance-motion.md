# QHSJ Seedance 运动/动作

---
name: seedance-motion
description: "This skill should be used when the user asks for body action, choreography, physics, object movement, movement timing, action continuity, stunt direction, or motion-reference mapping in Seedance 2.0."
license: MIT
user-invocable: true
tags:
  - motion
  - choreography
  - physics
  - seedance-20
metadata:
  version: "6.7.0"
  updated: "2026-08-01"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-motion

Use physical verbs and consequences. Motion should be observable on screen, timed within the clip, and assigned to a subject or object. Prefer one strong action with a visible endpoint over several vague actions competing for attention.

## Intent

Motion is the verb of the user's story - the thing they came to see HAPPEN. The soul here is consequence: motion that begins, lands, and changes something feels lived; motion that loops feels generated. Every action carries the story one beat forward, or it doesn't belong in the clip.

## Motion Contract

State: actor/object, action, force level, timing, physical consequence, continuity requirement, and endpoint.

| Motion type | Strong phrase | Weak phrase |
|---|---|---|
| Subtle acting | `Character A inhales, grips the cup tighter, then sets it down without looking away` | `she feels nervous` |
| Product material | `condensation beads gather, merge, and slide down the bottle neck` | `the product looks refreshing` |
| Choreography | `Character B ducks under the swinging bag, pivots left, and stops in a guarded stance` | `fast action fight scene` |
| Object physics | `paper receipt lifts in the fan breeze, flips once, and lands face-up` | `papers move dynamically` |
| Environmental motion | `rain streaks diagonally across the backlight while puddle ripples spread from footsteps` | `stormy weather atmosphere` |

## Physics-Forward Pattern

State mass, force, and material, then name one consequence the camera can see: `the heavy oak door swings shut and the candle flames bend toward it` beats `the door closes dramatically`. Consequences prove the action: weight shows in landing compression, momentum in overshoot and recovery, friction in skid length, wind in what it displaces.

## Timing Pattern

Use a three-beat structure for short clips: setup, action, changed end state. Example: `0-2s: candle flame steady; 2-4s: door opens and flame bends; 4-6s: smoke trail curls toward the hallway`.

## Reference Motion Rules

For reference footage, use only owned, licensed, public-domain, stock, mocap, rehearsal, or self-recorded material. Map `@Video1` to motion, camera, timing, or blocking, not identity, unless the identity is authorized.

## Stability Rules

Hands, faces, logos, and product geometry drift when too many actions occur. Reduce motion around fragile details: lock the camera for lip-sync, keep hands in simple poses, ask product parts to remain rigid.

## Output Contract

Return the motion phrase, timing pattern, reference role map if any, and repaired prompt language.
