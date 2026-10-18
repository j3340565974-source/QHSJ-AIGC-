## APIX155 — render
Request:
```json
{"task_id":"T-0155","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0155","references":[{"asset_id":"A-0155","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX156 — transcription
Request:
```json
{"task_id":"T-0156","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0156","references":[{"asset_id":"A-0156","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX157 — search
Request:
```json
{"task_id":"T-0157","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0157","references":[{"asset_id":"A-0157","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX158 — memory
Request:
```json
{"task_id":"T-0158","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0158","references":[{"asset_id":"A-0158","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX159 — checkpoint
Request:
```json
{"task_id":"T-0159","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0159","references":[{"asset_id":"A-0159","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX160 — generic_video
Request:
```json
{"task_id":"T-0160","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0160","references":[{"asset_id":"A-0160","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

