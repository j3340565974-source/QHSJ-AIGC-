# 图片提示词

> 能力 ID: `image_prompt`

## 职责
图片提示词。

## 典型触发
图片提示词、图像提示词、出图提示词、绘图提示词、图生图提示词、生成图片提示词、midjourney、midjourney提示词、MJ提示词、SD提示词、flux提示词、画图prompt、静帧提示词、角色图提示词、生成图片、生成图像、出一张图、文生图、图像生成、图片生成、静帧图、单张图片、角色图、场景图、封面图、图像prompt、绘画prompt、出图、生图

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
- `../../references/prompt-engineering/07-prompt-engineering/index.md`
- `../../references/prompt-engineering/09-prompt-engineering.md`
- `../../references/prompt-engineering/11-prompt-engineering.md`
- `../../references/prompt-engineering/prompt-formulas.md`
- `../../references/aesthetics/visuals-style-library/index.md`
- `../../references/prompt-engineering/qh-image-prompt-engine.md`
- `../../references/spatial/qh-blocking-positioning-master.md`
- `../../references/spatial/qh-spatial-reference-system-V3.md`
- `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`
- `../../references/vfx/qh-video-physics-precision.md`
