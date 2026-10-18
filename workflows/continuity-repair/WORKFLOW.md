# 针对人物、空间、动作、道具、光线、镜头轴线和段间状态进行定位修复

> 工作流 ID: `continuity-repair`

**版本**: 3.0.0

**描述**: 针对人物、空间、动作、道具、光线、镜头轴线和段间状态进行定位修复

## 触发条件
- 连续性修复
- 空间穿帮修复
- 人物位置不一致
- 角色一致性检查
- 镜头接不上

## 阶段
### CR0 内容类型和边界识别
**输入**: 剧, 本, 、, 分, 镜, 、, 提, 示, 词, 、, 生, 成, 结, 果, 描, 述, 或, 多, 段, 视, 频, 计, 划

**输出**: 项, 目, 事, 实, 、, 场, 景, /, 镜, 头, 范, 围, 、, 用, 户, 禁, 止, 改, 动, 项

**模块**:
- 模块: `../../references/core/decision-protocol.md`, `../../references/spatial/continuity-state-library.md`

### CR1 连续性状态重建
**输入**: 相, 关, 场, 次, 、, 镜, 头, 和, 资, 产, 记, 录

**输出**: 起, 态, /, 终, 态, 、, 人, 物, 位, 置, 、, 道, 具, 状, 态, 、, 轴, 线, 与, 光, 向

**模块**:
- 模块: `../../references/spatial/03-spatial-engine.md`, `../../references/spatial/04-spatial-continuity.md`, `../../references/spatial/qh-spatial-reference-system-V3.md`, `../../references/asset/asset-ledger.md`

### CR2 问题定位与最小修复
**输入**: 连, 续, 性, 状, 态, 表, 和, 故, 障, 现, 象

**输出**: 根, 因, 、, 影, 响, 范, 围, 、, 最, 小, 变, 更, 方, 案

**模块**:
- 模块: `../../references/quality-safety/failure-playbook-220.md`, `../../references/quality-safety/qa-checklist-320.md`, `../../references/quality-safety/qh-quality-gate-review.md`

### CR3 回归测试与交付
**输入**: 修, 复, 后, 的, 内, 容

**输出**: 修, 复, 差, 异, 、, 通, 过, 项, 、, 残, 余, 风, 险

**模块**:
- 模块: `../../references/quality-safety/13-quality-gates.md`, `../../references/quality-safety/14-quality-evolution.md`

## 最终产物
- 连续性状态表
- 根因报告
- 最小修复版本
- 回归检查报告

