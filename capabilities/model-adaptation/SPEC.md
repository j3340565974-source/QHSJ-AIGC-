# 模型与平台适配

> 能力 ID: `model_adaptation`

## 职责
模型与平台适配。

## 典型触发
Seedance、可灵、Veo、Runway、MJ、ComfyUI

## 必要叠加能力
提示词编译和适配后回归

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 模型与平台适配交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/model-adaptation/06-model-adaptation.md`
- `../../references/model-adaptation/08-model-adapters.md`
- `../../references/model-adaptation/10-model-adapters.md`
- `../../references/core/compatibility-matrix.md`
- `../../references/model-adaptation/model-adapter-cards.md`
- `../../references/model-adaptation/model-atlas.md`
- `../../references/model-adaptation/model-matrix-expanded.md`
- `../../references/core/p1-compatibility-matrix.md`
- `../../references/model-adaptation/p1-model-adapter-cards.md`
- `../../references/model-adaptation/p1-model-matrix-expanded.md`
