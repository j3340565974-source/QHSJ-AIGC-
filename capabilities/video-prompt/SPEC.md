# 视频提示词

> 能力 ID: `video_prompt`

## 职责
视频提示词。

## 典型触发
视频提示词、文生视频、图生视频、视频prompt、视频生成提示词、AI视频、视频生成、首尾帧、运镜提示词、视频续写、镜头续接、视频分段、视频投喂、生成视频、视频生成提示、动态视频、镜头视频提示、视频生成词、一段视频、视频生成方案

## 必要叠加能力
提示词、分镜/摄影/空间/表演/物理/声音/质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 视频提示词交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/prompt-engineering/14-ultimate-video-prompt.md`
- `../../references/prompt-engineering/prompt-transformation-lab/index.md`
- `../../references/prompt-engineering/qh-seedance-prompt-short.md`
- `../../references/prompt-engineering/qh-seedance-prompt.md`
- `../../references/spatial/qh-blocking-positioning-master.md`
- `../../references/spatial/qh-spatial-reference-system-V3.md`
- `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`
- `../../references/spatial/qh-segment-splicing.md`
- `../../references/vfx/qh-video-physics-precision.md`
- `../../references/vfx/13-vfx-motion-physics.md`
- `../../references/cinematography/qh-camera-language-complete.md`
