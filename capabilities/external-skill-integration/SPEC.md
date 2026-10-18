# 外部 Skill/Agent 集成

> 能力 ID: `external_skill_integration`

## 职责
外部 Skill/Agent 集成。

## 典型触发
Claude Code、Codex、Dify、Coze、千问、豆包等

## 必要叠加能力
API/宿主兼容性检查

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 外部 Skill/Agent 集成交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/api-integration/api-contracts.md`
- `../../references/api-integration/p1-api-contracts.md`
- `../../references/model-adaptation/qh-agent-platform-adapters.md`
- `../../references/api-integration/qh-external-skill-integration.md`
- `../../references/model-adaptation/v322-qh-agent-platform-adapters.md`
