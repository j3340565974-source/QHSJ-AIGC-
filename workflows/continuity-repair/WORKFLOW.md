# 针对人物、空间、动作、道具、光线、镜头轴线和段间状态进行定位修复

> 工作流 ID: `continuity-repair`

**版本**: 7.0.0

**描述**: 针对人物、空间、动作、道具、光线、镜头轴线和段间状态进行定位修复

## 触发条件
- 连续性修复
- 空间穿帮修复
- 人物位置不一致
- 角色一致性检查
- 镜头接不上

## 阶段
### CR0 内容类型和边界识别
**输入**: 剧本、分镜、提示词、生成结果描述或多段视频计划

**输出**: 项目事实、场景/镜头范围、用户禁止改动项

**模块**:
- 模块: `../../references/core/decision-protocol.md`, `../../references/spatial/continuity-state-library.md`

### CR1 连续性状态重建
**输入**: 相关场次、镜头和资产记录

**输出**: 起态/终态、人物位置、道具状态、轴线与光向

**模块**:
- 模块: `../../references/spatial/03-spatial-engine.md`, `../../references/spatial/04-spatial-continuity.md`, `../../references/spatial/qh-spatial-reference-system-V3.md`, `../../references/asset/asset-ledger.md`

### CR2 问题定位与最小修复
**输入**: 连续性状态表和故障现象

**输出**: 根因、影响范围、最小变更方案

**模块**:
- 模块: `../../references/quality-safety/failure-playbook-220.md`, `../../references/quality-safety/qa-checklist-320.md`, `../../references/quality-safety/qh-quality-gate-review.md`

### CR3 回归测试与交付
**输入**: 修复后的内容

**输出**: 修复差异、通过项、残余风险

**模块**:
- 模块: `../../references/quality-safety/13-quality-gates.md`, `../../references/quality-safety/14-quality-evolution.md`

## 最终产物
- 连续性状态表
- 根因报告
- 最小修复版本
- 回归检查报告

