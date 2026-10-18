# 从能力需求到接口契约、参数校验、平台适配、安全边界与集成测试

> 工作流 ID: `api-integration`

**版本**: 8.0.0

**描述**: 从能力需求到接口契约、参数校验、平台适配、安全边界与集成测试

## 触发条件
- API集成
- 接口请求
- Agent集成
- 安装Skill
- 外部工具集成

## 阶段
### API0 需求和宿主能力盘点
**输入**: 目标宿主、可用工具、输入输出、网络/文件权限

**输出**: 能力矩阵、工具约束、缺失依赖清单

**模块**:
- 模块: `../../references/model-adaptation/qh-agent-platform-adapters.md`, `../../references/api-integration/qh-external-skill-integration.md`, `../../references/core/compatibility-matrix.md`

### API1 接口契约与请求结构
**输入**: 能力矩阵和数据流

**输出**: 请求/响应schema、错误码、重试策略和超时边界

**模块**:
- 模块: `../../references/api-integration/api-contracts.md`, `../../references/api-integration/api-request-patterns-160/index.md`

### API2 集成与参数验证
**输入**: 接口契约

**输出**: 适配层、字段验证、错误处理与日志约定

**模块**:
- 模块: `../../references/model-adaptation/06-model-adaptation.md`, `../../references/model-adaptation/08-model-adapters.md`
- `scripts/validate_prompt.py`

### API3 安全和回归测试
**输入**: 适配实现与集成场景

**输出**: 测试矩阵、失败回退方案、部署说明

**模块**:
- 模块: `../../references/quality-safety/15-safety-compliance.md`, `../../references/quality-safety/failure-playbook-220/index.md`, `../../references/quality-safety/qa-checklist-320/index.md`

## 最终产物
- 接口契约
- 参数示例
- 错误处理规则
- 集成测试矩阵
- 宿主兼容性说明

