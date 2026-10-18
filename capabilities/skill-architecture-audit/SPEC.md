# Skill 路由/代码审计

> 能力 ID: `skill_architecture_audit`

## 职责
Skill 路由/代码审计。

## 典型触发
路由缺失、逻辑矛盾、漏洞、重构、修复

## 必要叠加能力
全包清点、测试、路由覆盖率回归

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- Skill 路由/代码审计交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/platform/20-coverage-and-conflicts.md`
- `../../references/api-integration/p1-route-grammar.md`
- `../../references/api-integration/route-grammar.md`
- `../../references/platform/v322-20-coverage-and-conflicts.md`
