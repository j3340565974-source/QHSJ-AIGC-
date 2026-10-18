# 资产前置管线

> 能力 ID: `asset_first`

## 职责
资产前置管线。

## 典型触发
资产前置、先做角色资产、先做资产、资产包、角色场景道具清单、资产清单、锚点卡、资产锚点、角色定妆、场景设定图、道具设定图、人物和场景图、角色和场景图、人物与场景图、角色与场景图、人物场景设定图、角色场景设定图、先设计人物和场景图、先做人物和场景图、先出人物和场景图、先做角色和场景图、先出角色和场景图、人设图和场景图、人物设定图和场景设定图、角色设定图和场景设定图、场景布局图、环境概念图、角色资产板、场景资产、道具资产、人物资产、视觉锚点、角色资产、场景设定板、道具设定板、角色参考板、资产一致性、资产库、先做角色、多视图资产、先设计人设图和场景图、先把人物和场景做出来、先出人物定妆图与场景设定图、人物场景图完成后再分镜、先定角色和场景视觉资产

## 必要叠加能力
角色、场景、空间、美学、提示词

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 资产前置管线交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/asset/asset-ledger.md`
- `../../references/asset/asset-package-spec.md`
- `../../references/asset/asset-validation-cases-500.md`
- `../../references/asset/p1-asset-ledger.md`
- `../../references/asset/p1-asset-package-spec.md`
- `../../references/asset/p1-asset-validation-cases-500.md`
- `../../references/asset/qh-asset-first-pipeline.md`
- `../../references/asset/qhsj-asset-locking-protocol.md`
- `../../references/asset/v322-qh-asset-first-pipeline.md`
