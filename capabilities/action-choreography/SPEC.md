# 动作/打斗编排

> 能力 ID: `action_choreography`

## 职责
动作/打斗编排。

## 典型触发
打戏、攻防、武术、动作预演

## 必要叠加能力
空间、摄影、表演、物理/VFX、质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 动作/打斗编排交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/action/09-action-system.md`
- `../../references/action/10-action-choreography.md`
- `../../references/action/12-action-choreography.md`
- `../../references/cinematography/qh-action-cinematography-breakdown.md`
- `../../references/action/qh-action-previs-15grid.md`
- `../../references/action/qh-action-ultimate-finisher.md`
- `../../references/action/qh-authentic-martial-taxonomy.md`
- `../../references/action/qh-combat-direction-engine.md`
- `../../references/action/qh-combat-rhythm-defense3state.md`
- `../../references/storyboard/qh-fight-storyboard-dsl.md`
