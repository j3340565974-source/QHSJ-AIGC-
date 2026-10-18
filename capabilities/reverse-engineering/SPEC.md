# 参考图/视频反推

> 能力 ID: `reverse_engineering`

## 职责
参考图/视频反推。

## 典型触发
反推、参考图、参考视频、图像分析、视频分析、复刻提示词、一比一还原、1:1还原、同风格、参考素材、反向工程、视觉拆解、参考图分析、画面拆解、参考图反推、参考视频反推、反推提示词、反向拆解、拉片分析、拆解参考图、拆解参考视频、按图还原、照着参考图、复刻构图、逆向分析、还原镜头、参考素材分析、镜头拆解、视觉反推、风格反推

## 必要叠加能力
美学、提示词、质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 参考图/视频反推交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/reverse-engineering/05-reverse-engineering.md`
- `../../references/reverse-engineering/09-reverse-engineering.md`
- `../../references/reverse-engineering/15-reference-reverse-engineering.md`
- `../../references/reverse-engineering/qh-image-reverse-engine.md`
- `../../references/reverse-engineering/qh-video-reverse-engine.md`
