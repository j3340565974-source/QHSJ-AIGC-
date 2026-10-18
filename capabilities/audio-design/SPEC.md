# 声音/配音/音乐

> 能力 ID: `audio_design`

## 职责
声音/配音/音乐。

## 典型触发
音效、VO/OS、配音、环境声

## 必要叠加能力
表演节拍与时间轴、质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 声音/配音/音乐交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/audio/11-audio-sound.md`
- `../../references/audio/11-audio-voice.md`
- `../../references/audio/13-audio-sound.md`
- `../../references/audio/qh-vo-os-weaving.md`
- `../../references/audio/v322-11-audio-voice.md`
- `../../references/audio/v322-qh-vo-os-weaving.md`
