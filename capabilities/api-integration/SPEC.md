# API 工程集成

> 能力 ID: `api_integration`

## 职责
API 工程集成。

## 典型触发
API、接口契约、请求示例、接口集成、自动化接口、HTTP请求、JSON请求、Webhook、服务调用、本地模型、端点、参数校验、接口怎么接、API请求、接口调用、请求参数、响应结构、endpoint、webhook、SDK集成、鉴权、令牌认证、请求体、返回值、错误码、集成测试、API对接

## 必要叠加能力
模型/工具适配、安全测试

## 输入
- 用户需求与硬约束
- 项目状态（若有）

## 输出
- API 工程集成交付物

## 门禁
- 遵守 Asset-First 硬门禁（资产未锁定返回 BLOCKED_ASSET_NOT_LOCKED）
- 禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）

## 依赖
（见 routes.json capability_dependencies）

## 相关知识库
- `../../references/api-integration/api-contracts.md`
- `../../references/api-integration/api-request-patterns-160.md`
- `../../references/api-integration/p1-api-contracts.md`
- `../../references/api-integration/p1-api-request-patterns-160.md`
- `../../references/model-adaptation/qh-agent-platform-adapters.md`
- `../../references/api-integration/qh-external-skill-integration.md`
- `../../references/model-adaptation/v322-qh-agent-platform-adapters.md`
