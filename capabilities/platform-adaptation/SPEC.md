# 内容平台适配

> 能力 ID: `platform_adaptation`

## 职责
内容平台适配。

## 典型触发
抖音、小红书、B站、视频号、TikTok

## 必要叠加能力
平台证据/策略和质检

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 内容平台适配交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/platform/22-media-type-atlas.md`
- `../../references/platform/p1-platform-algorithm-evidence.md`
- `../../references/platform/p1-platform-playbooks.md`
- `../../references/platform/p1-platform-script-patterns-180.md`
- `../../references/platform/platform-algorithm-evidence.md`
- `../../references/platform/platform-playbooks.md`
- `../../references/platform/platform-script-patterns-180.md`
- `../../references/platform/qh-aspect-ratio-adaptation.md`
- `../../references/platform/v322-22-media-type-atlas.md`
- `../../references/platform/v322-qh-aspect-ratio-adaptation.md`
