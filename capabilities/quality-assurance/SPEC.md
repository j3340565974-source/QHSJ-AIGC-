# 质量门禁与修复

> 能力 ID: `quality_assurance`

## 职责
质量门禁与修复。

## 典型触发
检查、审查、质检、质量检查、质量门禁、QA、QC、排查、找漏洞、找bug、修复、验证、测试、检查逻辑、一致性检查、有没有问题、错误清单、穿帮检查、崩坏检查、帮我检查、检查一下、哪里有问题、找出漏洞、查找bug、debug、排查错误、修复问题、逻辑是否通顺、检查自洽、校验一遍、回归测试、自动化测试、错误定位、找矛盾、一致性审查、有没有遗漏、完整性检查、检查断链

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
- `../../references/quality-safety/failure-playbook-220/index.md`
- `../../references/quality-safety/qa-checklist-320/index.md`
- `../../references/prompt-engineering/qh-prompt-feeding-checklist.md`
- `../../references/quality-safety/qh-quality-gate-review.md`
- `../../references/novel-screenwriting/qh-screenplay-gate-engine.md`
