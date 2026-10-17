# Bonsai-derived context engineering layer

## Scope
This file transfers architecture patterns from the public Bonsai local-LLM optimization project into QHSJ as model-agnostic runtime policy. It does not vendor Bonsai source code and does not treat one hardware profile as universal.

## 1. Budget gate
The Bonsai project documents a 65,536-token context, 8,192-token generation reserve and 1,024-token safety reserve, producing a 56,320-token input budget for its specific 64k/8GB operating profile. It also documents a fast character-floor gate at 84,480 characters and a second accurate-token gate. Those values are therefore kept only as a named profile in `config/context-optimization.yaml`.

For other models, calculate:
`input_budget = model_context - requested_output_reserve - host_overhead - safety_margin`.

If the model context is unknown, choose a conservative estimate and mark it as estimated.

## 2. Duplicate suppression
Use this order:
`normalized hash → n-gram similarity → imported capability cluster → route-level canonical owner`.
Do not deduplicate merely because two items discuss the same topic; only suppress content when the output semantics remain covered by the surviving item.

## 3. Prefix reuse
Stable, immutable system/reference blocks can share a cache key. Cache identity must include content hash and source/version metadata. Never reuse a cached block after its source or hard constraints change.

## 4. Stream safety
Long-running model responses must be processed incrementally. UTF-8 boundaries must be reconstructed across chunks before decoding; SSE events must be stateful; client disconnects must be observable rather than treated as successful completion.

## 5. Failure isolation
Schema errors, safety blocks and permission failures are deterministic and should not be retried. Timeouts, 429, transient 5xx and connection resets may be retried with bounded backoff.

## 6. Local-first portability
The same policy works for local llama.cpp-compatible endpoints, cloud APIs, agent SDKs and workflow platforms. The transport is an adapter; the route graph and prompt IR remain host-neutral.

## 7. Quality caveat
Bonsai's published performance numbers are machine/configuration-specific. They must not be copied into general claims for every model or computer.
