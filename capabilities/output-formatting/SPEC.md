# 输出与模板

> 能力 ID: `output_formatting`

## 职责
输出与模板。

## 典型触发
输出格式、交付模板、格式模板、表格模板、双区输出、最终交付、输出协议、七段式、JSON格式、分镜表模板、角色卡模板、输出成表格、按模板输出、交付格式、格式规范、字段定义、Markdown格式、代码块格式、可复制格式、结构化输出、导出格式、模板填充

## 必要叠加能力
对照用户要求和 Schema 校验

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 输出与模板交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/production/04-dual-output-protocol.md`
- `../../references/production/19-output-templates.md`
- `../../references/production/qh-output-frame-protocol.md`
