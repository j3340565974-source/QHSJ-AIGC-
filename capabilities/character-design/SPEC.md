# 角色及视觉资产

> 能力 ID: `character_design`

## 职责
角色及视觉资产。

## 典型触发
角色卡、角色设定、角色资产、角色设计、人物设定、角色四视图、四视图、三视图、角色立绘、角色一致性、人物外观、服装设计、道具资产、场景资产、资产板、人物图、角色图、人设图、人物定妆照、角色定妆照、人物资产图、角色资产图、人物设定图、角色设定图、角色造型设计图、角色外观、人物定妆、角色定妆、角色三视图、人物三视图、人物四视图、立绘、人物造型、服装造型、人物小传、年龄身高、脸部特征、形象设计、角色造型、人物造型设计、先设计人物图、先生成角色图、人物和场景视觉设定、角色与场景美术设定

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
