# 项目状态与连续性资产

> 能力 ID: `project_state_management`

## 职责
项目状态与连续性资产。

## 典型触发
项目状态、状态机、跨轮次、上下文继承、状态文件、项目记忆、设定锁定、人物事实、世界观连续性、版本管理、生产台账、continuity、跨对话、设定锁、人物关系表、设定集、Canon、前情提要、连续创作、长期设定、版本记录、制作台账、记忆管理、前文设定

## 必要叠加能力
总控和回归质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 项目状态与连续性资产交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/spatial/continuity-state-library/index.md`
- `../../references/core/decision-protocol/index.md`
- `../../references/asset/qh-production-ledger-handbook.md`
