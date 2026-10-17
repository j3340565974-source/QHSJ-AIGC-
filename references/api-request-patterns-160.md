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

## APIX031 — checkpoint
Request:
```json
{"task_id":"T-0031","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0031","references":[{"asset_id":"A-0031","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX032 — generic_video
Request:
```json
{"task_id":"T-0032","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0032","references":[{"asset_id":"A-0032","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX033 — generic_image
Request:
```json
{"task_id":"T-0033","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0033","references":[{"asset_id":"A-0033","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX034 — editor
Request:
```json
{"task_id":"T-0034","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0034","references":[{"asset_id":"A-0034","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX035 — render
Request:
```json
{"task_id":"T-0035","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0035","references":[{"asset_id":"A-0035","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX036 — transcription
Request:
```json
{"task_id":"T-0036","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0036","references":[{"asset_id":"A-0036","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX037 — search
Request:
```json
{"task_id":"T-0037","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0037","references":[{"asset_id":"A-0037","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX038 — memory
Request:
```json
{"task_id":"T-0038","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0038","references":[{"asset_id":"A-0038","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX039 — checkpoint
Request:
```json
{"task_id":"T-0039","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0039","references":[{"asset_id":"A-0039","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX040 — generic_video
Request:
```json
{"task_id":"T-0040","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0040","references":[{"asset_id":"A-0040","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX041 — generic_image
Request:
```json
{"task_id":"T-0041","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0041","references":[{"asset_id":"A-0041","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX042 — editor
Request:
```json
{"task_id":"T-0042","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0042","references":[{"asset_id":"A-0042","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX043 — render
Request:
```json
{"task_id":"T-0043","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0043","references":[{"asset_id":"A-0043","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX044 — transcription
Request:
```json
{"task_id":"T-0044","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0044","references":[{"asset_id":"A-0044","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX045 — search
Request:
```json
{"task_id":"T-0045","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0045","references":[{"asset_id":"A-0045","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX046 — memory
Request:
```json
{"task_id":"T-0046","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0046","references":[{"asset_id":"A-0046","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX047 — checkpoint
Request:
```json
{"task_id":"T-0047","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0047","references":[{"asset_id":"A-0047","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX048 — generic_video
Request:
```json
{"task_id":"T-0048","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0048","references":[{"asset_id":"A-0048","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX049 — generic_image
Request:
```json
{"task_id":"T-0049","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0049","references":[{"asset_id":"A-0049","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX050 — editor
Request:
```json
{"task_id":"T-0050","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0050","references":[{"asset_id":"A-0050","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX051 — render
Request:
```json
{"task_id":"T-0051","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0051","references":[{"asset_id":"A-0051","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX052 — transcription
Request:
```json
{"task_id":"T-0052","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0052","references":[{"asset_id":"A-0052","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX053 — search
Request:
```json
{"task_id":"T-0053","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0053","references":[{"asset_id":"A-0053","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX054 — memory
Request:
```json
{"task_id":"T-0054","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0054","references":[{"asset_id":"A-0054","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX055 — checkpoint
Request:
```json
{"task_id":"T-0055","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0055","references":[{"asset_id":"A-0055","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX056 — generic_video
Request:
```json
{"task_id":"T-0056","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0056","references":[{"asset_id":"A-0056","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX057 — generic_image
Request:
```json
{"task_id":"T-0057","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0057","references":[{"asset_id":"A-0057","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX058 — editor
Request:
```json
{"task_id":"T-0058","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0058","references":[{"asset_id":"A-0058","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX059 — render
Request:
```json
{"task_id":"T-0059","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0059","references":[{"asset_id":"A-0059","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX060 — transcription
Request:
```json
{"task_id":"T-0060","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0060","references":[{"asset_id":"A-0060","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX061 — search
Request:
```json
{"task_id":"T-0061","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0061","references":[{"asset_id":"A-0061","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX062 — memory
Request:
```json
{"task_id":"T-0062","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0062","references":[{"asset_id":"A-0062","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX063 — checkpoint
Request:
```json
{"task_id":"T-0063","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0063","references":[{"asset_id":"A-0063","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX064 — generic_video
Request:
```json
{"task_id":"T-0064","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0064","references":[{"asset_id":"A-0064","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX065 — generic_image
Request:
```json
{"task_id":"T-0065","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0065","references":[{"asset_id":"A-0065","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX066 — editor
Request:
```json
{"task_id":"T-0066","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0066","references":[{"asset_id":"A-0066","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX067 — render
Request:
```json
{"task_id":"T-0067","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0067","references":[{"asset_id":"A-0067","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX068 — transcription
Request:
```json
{"task_id":"T-0068","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0068","references":[{"asset_id":"A-0068","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX069 — search
Request:
```json
{"task_id":"T-0069","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0069","references":[{"asset_id":"A-0069","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX070 — memory
Request:
```json
{"task_id":"T-0070","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0070","references":[{"asset_id":"A-0070","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX071 — checkpoint
Request:
```json
{"task_id":"T-0071","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0071","references":[{"asset_id":"A-0071","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX072 — generic_video
Request:
```json
{"task_id":"T-0072","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0072","references":[{"asset_id":"A-0072","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX073 — generic_image
Request:
```json
{"task_id":"T-0073","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0073","references":[{"asset_id":"A-0073","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX074 — editor
Request:
```json
{"task_id":"T-0074","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0074","references":[{"asset_id":"A-0074","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX075 — render
Request:
```json
{"task_id":"T-0075","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0075","references":[{"asset_id":"A-0075","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX076 — transcription
Request:
```json
{"task_id":"T-0076","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0076","references":[{"asset_id":"A-0076","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX077 — search
Request:
```json
{"task_id":"T-0077","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0077","references":[{"asset_id":"A-0077","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX078 — memory
Request:
```json
{"task_id":"T-0078","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0078","references":[{"asset_id":"A-0078","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX079 — checkpoint
Request:
```json
{"task_id":"T-0079","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0079","references":[{"asset_id":"A-0079","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX080 — generic_video
Request:
```json
{"task_id":"T-0080","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0080","references":[{"asset_id":"A-0080","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX081 — generic_image
Request:
```json
{"task_id":"T-0081","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0081","references":[{"asset_id":"A-0081","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX082 — editor
Request:
```json
{"task_id":"T-0082","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0082","references":[{"asset_id":"A-0082","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX083 — render
Request:
```json
{"task_id":"T-0083","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0083","references":[{"asset_id":"A-0083","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX084 — transcription
Request:
```json
{"task_id":"T-0084","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0084","references":[{"asset_id":"A-0084","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX085 — search
Request:
```json
{"task_id":"T-0085","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0085","references":[{"asset_id":"A-0085","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX086 — memory
Request:
```json
{"task_id":"T-0086","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0086","references":[{"asset_id":"A-0086","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX087 — checkpoint
Request:
```json
{"task_id":"T-0087","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0087","references":[{"asset_id":"A-0087","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX088 — generic_video
Request:
```json
{"task_id":"T-0088","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0088","references":[{"asset_id":"A-0088","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX089 — generic_image
Request:
```json
{"task_id":"T-0089","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0089","references":[{"asset_id":"A-0089","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX090 — editor
Request:
```json
{"task_id":"T-0090","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0090","references":[{"asset_id":"A-0090","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX091 — render
Request:
```json
{"task_id":"T-0091","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0091","references":[{"asset_id":"A-0091","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX092 — transcription
Request:
```json
{"task_id":"T-0092","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0092","references":[{"asset_id":"A-0092","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX093 — search
Request:
```json
{"task_id":"T-0093","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0093","references":[{"asset_id":"A-0093","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX094 — memory
Request:
```json
{"task_id":"T-0094","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0094","references":[{"asset_id":"A-0094","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX095 — checkpoint
Request:
```json
{"task_id":"T-0095","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0095","references":[{"asset_id":"A-0095","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX096 — generic_video
Request:
```json
{"task_id":"T-0096","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0096","references":[{"asset_id":"A-0096","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX097 — generic_image
Request:
```json
{"task_id":"T-0097","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0097","references":[{"asset_id":"A-0097","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX098 — editor
Request:
```json
{"task_id":"T-0098","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0098","references":[{"asset_id":"A-0098","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX099 — render
Request:
```json
{"task_id":"T-0099","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0099","references":[{"asset_id":"A-0099","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX100 — transcription
Request:
```json
{"task_id":"T-0100","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0100","references":[{"asset_id":"A-0100","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX101 — search
Request:
```json
{"task_id":"T-0101","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0101","references":[{"asset_id":"A-0101","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX102 — memory
Request:
```json
{"task_id":"T-0102","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0102","references":[{"asset_id":"A-0102","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX103 — checkpoint
Request:
```json
{"task_id":"T-0103","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0103","references":[{"asset_id":"A-0103","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX104 — generic_video
Request:
```json
{"task_id":"T-0104","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0104","references":[{"asset_id":"A-0104","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX105 — generic_image
Request:
```json
{"task_id":"T-0105","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0105","references":[{"asset_id":"A-0105","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX106 — editor
Request:
```json
{"task_id":"T-0106","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0106","references":[{"asset_id":"A-0106","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX107 — render
Request:
```json
{"task_id":"T-0107","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0107","references":[{"asset_id":"A-0107","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX108 — transcription
Request:
```json
{"task_id":"T-0108","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0108","references":[{"asset_id":"A-0108","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX109 — search
Request:
```json
{"task_id":"T-0109","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0109","references":[{"asset_id":"A-0109","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX110 — memory
Request:
```json
{"task_id":"T-0110","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0110","references":[{"asset_id":"A-0110","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX111 — checkpoint
Request:
```json
{"task_id":"T-0111","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0111","references":[{"asset_id":"A-0111","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX112 — generic_video
Request:
```json
{"task_id":"T-0112","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0112","references":[{"asset_id":"A-0112","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX113 — generic_image
Request:
```json
{"task_id":"T-0113","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0113","references":[{"asset_id":"A-0113","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX114 — editor
Request:
```json
{"task_id":"T-0114","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0114","references":[{"asset_id":"A-0114","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX115 — render
Request:
```json
{"task_id":"T-0115","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0115","references":[{"asset_id":"A-0115","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX116 — transcription
Request:
```json
{"task_id":"T-0116","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0116","references":[{"asset_id":"A-0116","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX117 — search
Request:
```json
{"task_id":"T-0117","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0117","references":[{"asset_id":"A-0117","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX118 — memory
Request:
```json
{"task_id":"T-0118","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0118","references":[{"asset_id":"A-0118","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX119 — checkpoint
Request:
```json
{"task_id":"T-0119","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0119","references":[{"asset_id":"A-0119","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX120 — generic_video
Request:
```json
{"task_id":"T-0120","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0120","references":[{"asset_id":"A-0120","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX121 — generic_image
Request:
```json
{"task_id":"T-0121","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0121","references":[{"asset_id":"A-0121","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX122 — editor
Request:
```json
{"task_id":"T-0122","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0122","references":[{"asset_id":"A-0122","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX123 — render
Request:
```json
{"task_id":"T-0123","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0123","references":[{"asset_id":"A-0123","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX124 — transcription
Request:
```json
{"task_id":"T-0124","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0124","references":[{"asset_id":"A-0124","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX125 — search
Request:
```json
{"task_id":"T-0125","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0125","references":[{"asset_id":"A-0125","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX126 — memory
Request:
```json
{"task_id":"T-0126","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0126","references":[{"asset_id":"A-0126","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX127 — checkpoint
Request:
```json
{"task_id":"T-0127","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0127","references":[{"asset_id":"A-0127","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX128 — generic_video
Request:
```json
{"task_id":"T-0128","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0128","references":[{"asset_id":"A-0128","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX129 — generic_image
Request:
```json
{"task_id":"T-0129","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0129","references":[{"asset_id":"A-0129","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX130 — editor
Request:
```json
{"task_id":"T-0130","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0130","references":[{"asset_id":"A-0130","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX131 — render
Request:
```json
{"task_id":"T-0131","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0131","references":[{"asset_id":"A-0131","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX132 — transcription
Request:
```json
{"task_id":"T-0132","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0132","references":[{"asset_id":"A-0132","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX133 — search
Request:
```json
{"task_id":"T-0133","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0133","references":[{"asset_id":"A-0133","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX134 — memory
Request:
```json
{"task_id":"T-0134","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0134","references":[{"asset_id":"A-0134","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX135 — checkpoint
Request:
```json
{"task_id":"T-0135","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0135","references":[{"asset_id":"A-0135","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX136 — generic_video
Request:
```json
{"task_id":"T-0136","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0136","references":[{"asset_id":"A-0136","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX137 — generic_image
Request:
```json
{"task_id":"T-0137","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0137","references":[{"asset_id":"A-0137","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX138 — editor
Request:
```json
{"task_id":"T-0138","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0138","references":[{"asset_id":"A-0138","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX139 — render
Request:
```json
{"task_id":"T-0139","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0139","references":[{"asset_id":"A-0139","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX140 — transcription
Request:
```json
{"task_id":"T-0140","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0140","references":[{"asset_id":"A-0140","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX141 — search
Request:
```json
{"task_id":"T-0141","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0141","references":[{"asset_id":"A-0141","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX142 — memory
Request:
```json
{"task_id":"T-0142","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0142","references":[{"asset_id":"A-0142","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX143 — checkpoint
Request:
```json
{"task_id":"T-0143","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0143","references":[{"asset_id":"A-0143","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX144 — generic_video
Request:
```json
{"task_id":"T-0144","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0144","references":[{"asset_id":"A-0144","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX145 — generic_image
Request:
```json
{"task_id":"T-0145","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0145","references":[{"asset_id":"A-0145","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX146 — editor
Request:
```json
{"task_id":"T-0146","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0146","references":[{"asset_id":"A-0146","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX147 — render
Request:
```json
{"task_id":"T-0147","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0147","references":[{"asset_id":"A-0147","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX148 — transcription
Request:
```json
{"task_id":"T-0148","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0148","references":[{"asset_id":"A-0148","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX149 — search
Request:
```json
{"task_id":"T-0149","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0149","references":[{"asset_id":"A-0149","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX150 — memory
Request:
```json
{"task_id":"T-0150","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0150","references":[{"asset_id":"A-0150","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX151 — checkpoint
Request:
```json
{"task_id":"T-0151","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0151","references":[{"asset_id":"A-0151","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX152 — generic_video
Request:
```json
{"task_id":"T-0152","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0152","references":[{"asset_id":"A-0152","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX153 — generic_image
Request:
```json
{"task_id":"T-0153","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0153","references":[{"asset_id":"A-0153","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

## APIX154 — editor
Request:
```json
{"task_id":"T-0154","operation":"{operation}","model":"{model_if_any}","prompt_ir_ref":"PIR-0154","references":[{"asset_id":"A-0154","role":"character"}],"duration":{"seconds":{duration}},"output":{"aspect":"{aspect}","fps":{fps},"resolution":"{resolution}"},"metadata":{"adapter_version":"{adapter_version}"}}
```
Validation before send: schema validation, required capability check, fresh adapter status, secret-scan, size/duration limits, safety scan.
Response normalization: `job_id`, `status`, `media_uri`, `provider_model`, `provider_version`, `warnings`, `error_class`, `usage`, `provenance`.
Retry classes: network timeout → retry; rate limit → backoff; invalid parameter → do not retry unchanged; safety refusal → route to safe alternative; unknown error → capture and escalate.

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

