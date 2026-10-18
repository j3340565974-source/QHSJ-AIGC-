# 从动作目标到空间正确、受力合理、节奏清晰的动作分镜与提示词

> 工作流 ID: `action-design`

**版本**: 3.0.0

**描述**: 从动作目标到空间正确、受力合理、节奏清晰的动作分镜与提示词

## 触发条件
- 打斗设计
- 动作戏
- 武打分镜
- 战斗动作
- 动作预演

## 阶段
### AC0 动作目标与安全边界
**输入**: 用, 户, 动, 作, 意, 图, 、, 人, 物, 能, 力, 、, 场, 景, 条, 件

**输出**: 动, 作, 目, 标, 、, 失, 败, 条, 件, 、, 禁, 止, 新, 增, 项, 、, 强, 度, 等, 级

**模块**:
- 模块: `../../references/action/qh-combat-direction-engine.md`, `../../references/action/qh-authentic-martial-taxonomy.md`

### AC1 空间与站位锁定
**输入**: 动, 作, 目, 标, 、, 场, 景, 图, 、, 人, 物, 锚, 点

**输出**: 站, 位, 声, 明, 、, 轴, 线, 、, 进, 退, 路, 线, 、, 可, 用, 空, 间

**模块**:
- 模块: `../../references/spatial/03-spatial-engine.md`, `../../references/spatial/qh-blocking-positioning-master.md`, `../../references/spatial/qh-spatial-deduction-engine.md`

### AC2 动作拆解与攻防节拍
**输入**: 空, 间, 状, 态, 、, 角, 色, 能, 力

**输出**: 起, 势, 、, 攻, 势, 、, 防, 御, 、, 命, 中, /, 落, 空, 、, 受, 力, 反, 馈, 、, 恢, 复, 状, 态

**模块**:
- 模块: `../../references/action/09-action-system.md`, `../../references/action/qh-martial-action-encyclopedia.md`, `../../references/storyboard/qh-fight-storyboard-dsl.md`, `../../references/action/qh-combat-rhythm-defense3state.md`

### AC3 摄影与物理反馈（并行）
**输入**: 动, 作, 节, 拍

**输出**: 机, 位, 、, 运, 镜, 、, 遮, 挡, 、, 惯, 性, 、, 碰, 撞, 、, 布, 料, 与, 环, 境, 反, 馈

**模块**:
- 模块: `../../references/cinematography/qh-action-cinematography-breakdown.md`, `../../references/vfx/qh-video-physics-precision.md`, `../../references/vfx/12-vfx-motion-physics.md`

**并行**: True

### AC4 逐镜输出与质量门禁
**输入**: 动, 作, 节, 拍, 、, 摄, 影, 、, 空, 间, 和, 物, 理, 结, 果

**输出**: 动, 作, 分, 镜, 、, 视, 频, 提, 示, 词, 、, 错, 误, 归, 因, 与, 修, 复, 清, 单

**模块**:
- 模块: `../../references/storyboard/08-storyboard-directing.md`, `../../references/production/04-dual-output-protocol.md`, `../../references/quality-safety/13-quality-gates.md`, `../../references/quality-safety/qh-quality-gate-review.md`

## 最终产物
- 动作目标卡
- 空间/轴线声明
- 动作节拍表
- 动作分镜
- 可选视频提示词
- 质量检查报告

