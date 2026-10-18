# 图片提示词

> 能力 ID: `image_prompt`

## 职责
图片提示词。

## 典型触发
图片提示词、MJ、绘图提示词

## 必要叠加能力
美学、提示词、质检、安全；指定平台时加适配

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 图片提示词交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/prompt-engineering/07-prompt-engineering.md`
- `../../references/prompt-engineering/09-prompt-engineering.md`
- `../../references/prompt-engineering/11-prompt-engineering.md`
- `../../references/prompt-engineering/p1-prompt-formulas.md`
- `../../references/aesthetics/p1-visuals-style-library.md`
- `../../references/prompt-engineering/prompt-formulas.md`
- `../../references/prompt-engineering/qh-image-prompt-engine.md`
- `../../references/prompt-engineering/v322-09-prompt-engineering.md`
- `../../references/aesthetics/visuals-style-library.md`
