# 保留创作语义与硬约束，按目标图像/视频模型编译语法

> 工作流 ID: `model-adaptation`

**版本**: 7.0.0

**描述**: 保留创作语义与硬约束，按目标图像/视频模型编译语法

## 触发条件
- 模型适配
- 平台适配
- 适配Seedance
- 适配可灵
- 适配Veo
- 模型语法转换

## 阶段
### MA0 目标模型与任务类型识别
**输入**: 原始提示词、任务目标、目标平台（如有）

**输出**: 目标模型、输入模态、时长/比例/参考资产限制

**模块**:
- 模块: `../../references/model-adaptation/model-atlas.md`, `../../references/model-adaptation/model-matrix-expanded.md`, `../../references/core/compatibility-matrix.md`

### MA1 能力与语法证据核对
**输入**: 目标模型和任务类型

**输出**: 已确认能力、未确认能力、语法限制与日期

**模块**:
- 模块: `../../references/model-adaptation/model-adapter-cards.md`, `../../references/model-adaptation/qh-agent-platform-adapters.md`, `../../references/model-adaptation/qh-seedance-pipeline.md`

### MA2 语义不变编译
**输入**: 原始提示词、硬约束和模型限制

**输出**: 目标平台格式、变量/参数和负面约束

**模块**:
- 模块: `../../references/model-adaptation/06-model-adaptation.md`, `../../references/model-adaptation/08-model-adapters.md`, `../../references/prompt-engineering/11-prompt-engineering.md`

### MA3 回归与失败预防
**输入**: 编译结果

**输出**: 语义差异清单、兼容风险、校验报告

**模块**:
- 模块: `../../references/quality-safety/failure-playbook-220.md`, `../../references/quality-safety/13-quality-gates.md`
- `scripts/validate_prompt.py`

## 最终产物
- 模型适配提示词
- 参数说明
- 兼容性与时效性声明
- 回归检查报告

