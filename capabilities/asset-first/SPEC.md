# 资产前置管线

> 能力 ID: `asset_first`

## 职责
资产前置管线。

## 典型触发
资产包、锚点卡、先做设定图

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
