# 门禁分级权威定义

## P0 — 硬门禁

- **判定标准**：涉及资产一致性、安全合规、依赖完整性的规则
- **违反时行为**：返回错误码并停止执行，不允许继续
- **与错误码映射**：
  - Asset-First 资产未锁定 → `BLOCKED_ASSET_NOT_LOCKED`
  - 禁止用户跳过 P0，违反时返回 `GATE_P0_CANNOT_SKIP`
  - 前置依赖未满足 → `DEPENDENCY_UNMET`

## P1 — 软门禁

- **判定标准**：涉及质量、完整性但不阻塞核心交付的规则
- **违反时行为**：警告并要求用户显式确认，确认后可继续
- **与错误码映射**：
  - 未命中路由 → `NO_ROUTE_MATCHED`
  - 无显式交付物 → `INTENT_ANALYSIS_FALLBACK`
  - Schema 校验失败 → `SCHEMA_VALIDATION_FAILED`

## P2 — 提示

- **判定标准**：优化建议、风格偏好、非关键完整性
- **违反时行为**：记录但不阻塞执行
- **与错误码映射**：
  - 非法 gate_level → `INVALID_GATE_LEVEL`
  - 产物缺失 → `ARTIFACT_NOT_FOUND`
