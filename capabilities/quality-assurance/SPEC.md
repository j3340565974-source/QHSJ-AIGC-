# 质量门禁与修复

> 能力 ID: `quality_assurance`

## 职责
质量门禁与修复。

## 典型触发
审查、检查、验证、找 bug、穿帮

## 必要叠加能力
按缺陷反向调用根因模块

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 质量门禁与修复交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/quality-safety/13-quality-gates.md`
- `../../references/quality-safety/14-quality-evolution.md`
- `../../references/quality-safety/16-quality-gates.md`
- `../../references/quality-safety/failure-playbook-220.md`
- `../../references/quality-safety/p1-failure-playbook-220.md`
- `../../references/quality-safety/p1-qa-checklist-320.md`
- `../../references/quality-safety/qa-checklist-320.md`
- `../../references/prompt-engineering/qh-prompt-feeding-checklist.md`
- `../../references/quality-safety/qh-quality-gate-review.md`
- `../../references/novel-screenwriting/qh-screenplay-gate-engine.md`
