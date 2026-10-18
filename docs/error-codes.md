# 错误码注册表

| 错误码 | 级别 | 含义 | 触发条件 | 处理建议 |
|---|---|---|---|---|
| BLOCKED_ASSET_NOT_LOCKED | P0 | 资产未锁定 | Asset-First 检查失败 | 先完成资产锁定 |
| GATE_P0_CANNOT_SKIP | P0 | P0 门禁不可跳过 | 禁止用户跳过 P0 | 强制要求完成 |
| GATE_SPATIAL_PHYSICS_MISSING | P1 | 图片/视频提示词缺少空间锚点或物理锁定 | visual-prompt 门禁检查失败 | 补齐绝对方位坐标系与物理锁定项 |
| DEPENDENCY_UNMET | P0 | 前置依赖未满足 | 依赖闭包失败 | 补齐依赖 |
| NO_ROUTE_MATCHED | P1 | 未命中任何路由 | query 无匹配且无创作线索 | 提示 3 条候选 |
| INTENT_ANALYSIS_FALLBACK | P1 | 含创作线索但无显式交付物 | 未命中显式路由 | 转入 intent-analysis 意图解析 |
| SCHEMA_VALIDATION_FAILED | P1 | Schema 校验失败 | 输入/输出不合法 | 返回 schema 提示 |
| INVALID_GATE_LEVEL | P2 | gate_level 非法值 | routes.json 中 gate_level 不在 P0/P1/P2 | 修正后重跑 build_routes |
| ARTIFACT_NOT_FOUND | P2 | runs/ 中文件不存在 | 引用的 run 产物缺失 | 检查 run_id |
