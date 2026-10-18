# 项目状态与连续性资产

> 能力 ID: `project_state_management`

## 职责
项目状态与连续性资产。

## 典型触发
状态机、Canon、跨轮次、台账

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
- `../../references/spatial/continuity-state-library.md`
- `../../references/core/decision-protocol.md`
- `../../references/spatial/p1-continuity-state-library.md`
- `../../references/core/p1-decision-protocol.md`
- `../../references/asset/qh-production-ledger-handbook.md`
- `../../references/asset/v322-qh-production-ledger-handbook.md`
