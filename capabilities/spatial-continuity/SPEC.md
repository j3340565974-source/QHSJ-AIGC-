# 空间推演与连续性

> 能力 ID: `spatial_continuity`

## 职责
空间推演与连续性。

## 典型触发
空间推演、空间关系、站位、轴线、180度轴线、180°轴线、连续性、空间一致性、走位、顶视图、人物位置、方位、镜头越轴、穿帮、位置锁定、场景结构、人物走位、左右站位、前后位置、越轴、轴线关系、人物位置变化、道具状态、视线方向、空间位置、动作连续、镜头接不上、动作接不上、场景布局、场面调度、人物朝向、人物方位、空间连续性

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
- `../../references/spatial/continuity-state-library/index.md`
- `../../references/spatial/qh-blocking-positioning-master.md`
- `../../references/spatial/qh-spatial-deduction-engine.md`
- `../../references/spatial/qh-spatial-reference-system-V3.md`
- `../../references/spatial/qh-spatial-sandbox-simulation.md`
- `../../references/cinematography/qh-spatial-topview-camera.md`
- `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`
