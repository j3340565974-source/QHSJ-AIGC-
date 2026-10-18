# 错误码注册表

| 错误码 | 级别 | 含义 | 触发条件 | 处理建议 |
|---|---|---|---|---|
| BLOCKED_ASSET_NOT_LOCKED | P0 | 资产未锁定 | Asset-First 检查失败 | 先完成资产锁定 |
| GATE_P0_CANNOT_SKIP | P0 | P0 门禁不可跳过 | 禁止用户跳过 P0 | 强制要求完成 |
| DEPENDENCY_UNMET | P0 | 前置依赖未满足 | 依赖闭包失败 | 补齐依赖 |
| NO_ROUTE_MATCHED | P1 | 未命中任何路由 | query 无匹配 | 提示 3 条候选 |
| ROUTE_CONFLICT | P1 | 多条路由冲突 | 命中多条且优先级相同 | 提示用户选择 |
| SCHEMA_VALIDATION_FAILED | P1 | Schema 校验失败 | 输入/输出不合法 | 返回 schema 提示 |
| INVALID_GATE_LEVEL | P2 | gate_level 非法值 | routes.json 中 gate_level 不在 P0/P1/P2 | 修正后重跑 build_routes |
| ARTIFACT_NOT_FOUND | P2 | runs/ 中文件不存在 | 引用的 run 产物缺失 | 检查 run_id |
