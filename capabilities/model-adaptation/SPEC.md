# 模型与平台适配

> 能力 ID: `model_adaptation`

## 职责
模型与平台适配。

## 典型触发
模型适配、平台适配、适配Seedance、Seedance、即梦、可灵、Kling、Veo、Runway、Sora、Midjourney、ComfyUI、模型参数、模型语法、目标模型、API格式、API调用、兼容矩阵、适配模型、适配平台、模型限制、模型格式、模型专用语法、Pika、Flux、HunyuanVideo、模型兼容、模型调用格式、转成某模型、跨模型转换

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
- `../../references/model-adaptation/10-model-adapters/index.md`
- `../../references/core/compatibility-matrix.md`
- `../../references/model-adaptation/model-adapter-cards/index.md`
- `../../references/model-adaptation/model-atlas/index.md`
- `../../references/model-adaptation/model-matrix-expanded/index.md`
