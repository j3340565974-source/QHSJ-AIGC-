# 角色及视觉资产

> 能力 ID: `character_design`

## 职责
角色及视觉资产。

## 典型触发
角色卡、外观、四视图、服装

## 必要叠加能力
美学、资产、提示词、质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 角色及视觉资产交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/character-performance/05-character-performance.md`
- `../../references/asset/asset-package-spec.md`
- `../../references/asset/p1-asset-package-spec.md`
- `../../references/character-performance/qh-character-lineage-and-sheets.md`
- `../../references/character-performance/v322-qh-character-lineage-and-sheets.md`
