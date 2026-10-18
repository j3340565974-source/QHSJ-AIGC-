# 从能力需求到接口契约、参数校验、平台适配、安全边界与集成测试

> 工作流 ID: `api-integration`

**版本**: 3.0.0

**描述**: 从能力需求到接口契约、参数校验、平台适配、安全边界与集成测试

## 触发条件
- API集成
- 接口请求
- Agent集成
- 安装Skill
- 外部工具集成

## 阶段
### API0 需求和宿主能力盘点
**输入**: 目, 标, 宿, 主, 、, 可, 用, 工, 具, 、, 输, 入, 输, 出, 、, 网, 络, /, 文, 件, 权, 限

**输出**: 能, 力, 矩, 阵, 、, 工, 具, 约, 束, 、, 缺, 失, 依, 赖, 清, 单

**模块**:
- 模块: `../../references/model-adaptation/qh-agent-platform-adapters.md`, `../../references/api-integration/qh-external-skill-integration.md`, `../../references/core/compatibility-matrix.md`

### API1 接口契约与请求结构
**输入**: 能, 力, 矩, 阵, 和, 数, 据, 流

**输出**: 请, 求, /, 响, 应, s, c, h, e, m, a, 、, 错, 误, 码, 、, 重, 试, 策, 略, 和, 超, 时, 边, 界

**模块**:
- 模块: `../../references/api-integration/api-contracts.md`, `../../references/api-integration/api-request-patterns-160.md`

### API2 集成与参数验证
**输入**: 接, 口, 契, 约

**输出**: 适, 配, 层, 、, 字, 段, 验, 证, 、, 错, 误, 处, 理, 与, 日, 志, 约, 定

**模块**:
- 模块: `../../references/model-adaptation/06-model-adaptation.md`, `../../references/model-adaptation/08-model-adapters.md`
- `scripts/validate_prompt.py`

### API3 安全和回归测试
**输入**: 适, 配, 实, 现, 与, 集, 成, 场, 景

**输出**: 测, 试, 矩, 阵, 、, 失, 败, 回, 退, 方, 案, 、, 部, 署, 说, 明

**模块**:
- 模块: `../../references/quality-safety/15-safety-compliance.md`, `../../references/quality-safety/failure-playbook-220.md`, `../../references/quality-safety/qa-checklist-320.md`

## 最终产物
- 接口契约
- 参数示例
- 错误处理规则
- 集成测试矩阵
- 宿主兼容性说明

