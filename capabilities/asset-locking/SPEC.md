# 资产版本、锁定与分镜资产引用

> 能力 ID: `asset_locking`

## 职责
资产版本、锁定与分镜资产引用。

## 典型触发
角色锁定、场景锁定、资产冻结、分镜引用角色图

## 必要叠加能力
资产前置、角色、空间、项目状态与 QA

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 资产版本、锁定与分镜资产引用交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/asset/asset-ledger.md`
- `../../references/asset/asset-validation-cases-500.md`
- `../../references/asset/p1-asset-ledger.md`
- `../../references/asset/p1-asset-validation-cases-500.md`
- `../../references/spatial/qh-asset-spatial-ledger.md`
- `../../references/asset/qh-production-ledger-handbook.md`
- `../../references/asset/qhsj-asset-locking-protocol.md`
- `../../references/spatial/v322-qh-asset-spatial-ledger.md`
- `../../references/asset/v322-qh-production-ledger-handbook.md`
