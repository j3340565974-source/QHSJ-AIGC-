# 从动作目标到空间正确、受力合理、节奏清晰的动作分镜与提示词

> 工作流 ID: `action-design`

**版本**: 7.0.0

**描述**: 从动作目标到空间正确、受力合理、节奏清晰的动作分镜与提示词

## 触发条件
- 打斗设计
- 动作戏
- 武打分镜
- 战斗动作
- 动作预演

## 阶段
### AC0 动作目标与安全边界
**输入**: 用户动作意图、人物能力、场景条件

**输出**: 动作目标、失败条件、禁止新增项、强度等级

**模块**:
- 模块: `../../references/action/qh-combat-direction-engine.md`, `../../references/action/qh-authentic-martial-taxonomy.md`

### AC1 空间与站位锁定
**输入**: 动作目标、场景图、人物锚点

**输出**: 站位声明、轴线、进退路线、可用空间

**模块**:
- 模块: `../../references/spatial/03-spatial-engine.md`, `../../references/spatial/qh-blocking-positioning-master.md`, `../../references/spatial/qh-spatial-deduction-engine.md`

### AC2 动作拆解与攻防节拍
**输入**: 空间状态、角色能力

**输出**: 起势、攻势、防御、命中/落空、受力反馈、恢复状态

**模块**:
- 模块: `../../references/action/09-action-system.md`, `../../references/action/qh-martial-action-encyclopedia.md`, `../../references/storyboard/qh-fight-storyboard-dsl.md`, `../../references/action/qh-combat-rhythm-defense3state.md`

### AC3 摄影与物理反馈（并行）
**输入**: 动作节拍

**输出**: 机位、运镜、遮挡、惯性、碰撞、布料与环境反馈

**模块**:
- 模块: `../../references/cinematography/qh-action-cinematography-breakdown.md`, `../../references/vfx/qh-video-physics-precision.md`, `../../references/vfx/12-vfx-motion-physics.md`

**并行**: True

### AC4 逐镜输出与质量门禁
**输入**: 动作节拍、摄影、空间和物理结果

**输出**: 动作分镜、视频提示词、错误归因与修复清单

**模块**:
- 模块: `../../references/storyboard/08-storyboard-directing.md`, `../../references/production/04-dual-output-protocol.md`, `../../references/quality-safety/13-quality-gates.md`, `../../references/quality-safety/qh-quality-gate-review.md`

## 最终产物
- 动作目标卡
- 空间/轴线声明
- 动作节拍表
- 动作分镜
- 可选视频提示词
- 质量检查报告

