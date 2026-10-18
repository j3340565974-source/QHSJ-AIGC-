# 安全与原创性

> 能力 ID: `safety_originality`

## 职责
安全与原创性。

## 典型触发
合规、安全检查、原创性、侵权、版权、避免抄袭、平台规则、负面约束、内容审核、生成安全、版权风险、原创度、查重、涉嫌抄袭、侵权风险、肖像权、商标风险、合规审查、内容安全、敏感内容、合法合规、授权范围、版权检查、原创性检查

## 必要叠加能力
所有最终交付前必跑

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- 安全与原创性交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/quality-safety/15-safety-compliance.md`
- `../../references/quality-safety/18-safety-originality.md`
- `../../references/prompt-engineering/p1-wording-and-safety.md`
- `../../references/quality-safety/qh-platform-safety-compliance-guide.md`
- `../../references/quality-safety/v322-18-safety-originality.md`
- `../../references/quality-safety/v322-qh-platform-safety-compliance-guide.md`
- `../../references/prompt-engineering/wording-and-safety.md`
