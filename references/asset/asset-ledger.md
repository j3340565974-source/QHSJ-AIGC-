# Production Ledger and 16-Item Asset Lock

The ledger converts creative ambiguity into tracked state.

## Lock 01 — project identity
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 02 — story/canon
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 03 — character identity
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 04 — face/hair
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 05 — wardrobe/accessories
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 06 — voice
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 07 — environment
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 08 — architectural anchors
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 09 — props
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 10 — vehicles/creatures
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 11 — style/palette
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 12 — lighting topology
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 13 — camera grammar
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 14 — spatial anchor
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 15 — performance grammar
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Lock 16 — continuity/version hash
Fields: `id`, `definition`, `source`, `state`, `dependencies`, `owner_role`, `approval`, `hash`, `last_changed`, `change_reason`, `rollback_to`.
Hard lock when: `approval == approved` and all dependencies pass.
Unlock requires: explicit change request + impacted downstream artifact list + QA rerun plan.

## Consistency score
`identity_score = 1 - weighted_sum(defect_i * weight_i)`
Weights are project-defined, not universal. Hard defects force a score of 0 for release gating regardless of cosmetic quality.
