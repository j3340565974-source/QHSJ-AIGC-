# 输出与模板

> 能力 ID: `output_formatting`

## 职责
输出与模板。

## 典型触发
JSON、双区输出、角色卡/分镜表模板

## 必要叠加能力
对照用户要求和 Schema 校验

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 输出与模板交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/production/04-dual-output-protocol.md`
- `../../references/production/19-output-templates.md`
- `../../references/production/qh-output-frame-protocol.md`
- `../../references/production/v322-19-output-templates.md`
- `../../references/production/v322-qh-output-frame-protocol.md`
