# 参考图/视频反推

> 能力 ID: `reverse_engineering`

## 职责
参考图/视频反推。

## 典型触发
反推、参考素材、复刻、同风格

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
- `../../references/reverse-engineering/v322-15-reference-reverse-engineering.md`
