# API Request Pattern Library — 160 normalized examples

## APIX001 — generic_image
Request:
```json
{"task_id":"T-0001","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0001","references":[{"asset_id":"A-0001","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX002 — editor
Request:
```json
{"task_id":"T-0002","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0002","references":[{"asset_id":"A-0002","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX003 — render
Request:
```json
{"task_id":"T-0003","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0003","references":[{"asset_id":"A-0003","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX004 — transcription
Request:
```json
{"task_id":"T-0004","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0004","references":[{"asset_id":"A-0004","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX005 — search
Request:
```json
{"task_id":"T-0005","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0005","references":[{"asset_id":"A-0005","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX006 — memory
Request:
```json
{"task_id":"T-0006","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0006","references":[{"asset_id":"A-0006","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX007 — checkpoint
Request:
```json
{"task_id":"T-0007","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0007","references":[{"asset_id":"A-0007","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX008 — generic_video
Request:
```json
{"task_id":"T-0008","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0008","references":[{"asset_id":"A-0008","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX009 — generic_image
Request:
```json
{"task_id":"T-0009","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0009","references":[{"asset_id":"A-0009","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX010 — editor
Request:
```json
{"task_id":"T-0010","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0010","references":[{"asset_id":"A-0010","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX011 — render
Request:
```json
{"task_id":"T-0011","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0011","references":[{"asset_id":"A-0011","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX012 — transcription
Request:
```json
{"task_id":"T-0012","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0012","references":[{"asset_id":"A-0012","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX013 — search
Request:
```json
{"task_id":"T-0013","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0013","references":[{"asset_id":"A-0013","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX014 — memory
Request:
```json
{"task_id":"T-0014","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0014","references":[{"asset_id":"A-0014","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX015 — checkpoint
Request:
```json
{"task_id":"T-0015","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0015","references":[{"asset_id":"A-0015","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX016 — generic_video
Request:
```json
{"task_id":"T-0016","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0016","references":[{"asset_id":"A-0016","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX017 — generic_image
Request:
```json
{"task_id":"T-0017","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0017","references":[{"asset_id":"A-0017","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX018 — editor
Request:
```json
{"task_id":"T-0018","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0018","references":[{"asset_id":"A-0018","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX019 — render
Request:
```json
{"task_id":"T-0019","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0019","references":[{"asset_id":"A-0019","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX020 — transcription
Request:
```json
{"task_id":"T-0020","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0020","references":[{"asset_id":"A-0020","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX021 — search
Request:
```json
{"task_id":"T-0021","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0021","references":[{"asset_id":"A-0021","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX022 — memory
Request:
```json
{"task_id":"T-0022","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0022","references":[{"asset_id":"A-0022","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX023 — checkpoint
Request:
```json
{"task_id":"T-0023","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0023","references":[{"asset_id":"A-0023","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX024 — generic_video
Request:
```json
{"task_id":"T-0024","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0024","references":[{"asset_id":"A-0024","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX025 — generic_image
Request:
```json
{"task_id":"T-0025","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0025","references":[{"asset_id":"A-0025","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX026 — editor
Request:
```json
{"task_id":"T-0026","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0026","references":[{"asset_id":"A-0026","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX027 — render
Request:
```json
{"task_id":"T-0027","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0027","references":[{"asset_id":"A-0027","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX028 — transcription
Request:
```json
{"task_id":"T-0028","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0028","references":[{"asset_id":"A-0028","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX029 — search
Request:
```json
{"task_id":"T-0029","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0029","references":[{"asset_id":"A-0029","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX030 — memory
Request:
```json
{"task_id":"T-0030","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0030","references":[{"asset_id":"A-0030","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.
