# 资产版本、锁定与分镜资产引用

> 能力 ID: `asset_locking`

## 职责
资产版本、锁定与分镜资产引用。

## 典型触发
资产锁定、锁定资产、角色资产锁定、人物资产锁定、场景资产锁定、资产冻结、锁定人物和场景、先锁定角色和场景、分镜资产引用、分镜资产引用角色图、资产版本管理、资产版本锁定、角色资产版本、场景资产版本、资产漂移修复、先锁定人物和场景、人物和场景先定稿、分镜图引用已锁定人物图、分镜图引用已锁定场景图、分镜图使用规范角色资产、逐镜图引用人物场景资产、先生成并锁定人物和场景资产、锁定资产后再生成分镜图、分镜引用已锁定参考图、人物与场景先定稿、资产版本不得漂移、资产依赖影响扫描、先出人物图场景图再做分镜、分镜必须引用锁定人物和场景、人物场景资产定稿后再制作分镜、把角色图和场景图锁定后做分镜、先做人物场景图再生成每镜图

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
- `../../references/asset/asset-validation-cases-500/index.md`
- `../../references/spatial/qh-asset-spatial-ledger.md`
- `../../references/asset/qh-production-ledger-handbook.md`
- `../../references/asset/qhsj-asset-locking-protocol.md`
