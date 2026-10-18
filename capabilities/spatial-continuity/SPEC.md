# 空间推演与连续性

> 能力 ID: `spatial_continuity`

## 职责
空间推演与连续性。

## 典型触发
站位、轴线、方位、连续性、穿帮

## 必要叠加能力
项目状态与质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 空间推演与连续性交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/spatial/04-spatial-continuity.md`
- `../../references/spatial/05-spatial-continuity.md`
- `../../references/spatial/continuity-state-library.md`
- `../../references/spatial/p1-continuity-state-library.md`
- `../../references/spatial/qh-blocking-positioning-master.md`
- `../../references/spatial/qh-spatial-deduction-engine.md`
- `../../references/spatial/qh-spatial-reference-system-V3.md`
- `../../references/spatial/qh-spatial-sandbox-simulation.md`
- `../../references/cinematography/qh-spatial-topview-camera.md`
- `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`
