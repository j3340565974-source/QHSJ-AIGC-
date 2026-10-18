# 保留创作语义与硬约束，按目标图像/视频模型编译语法

> 工作流 ID: `model-adaptation`

**版本**: 3.0.0

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
**输入**: 原, 始, 提, 示, 词, 、, 任, 务, 目, 标, 、, 目, 标, 平, 台, （, 如, 有, ）

**输出**: 目, 标, 模, 型, 、, 输, 入, 模, 态, 、, 时, 长, /, 比, 例, /, 参, 考, 资, 产, 限, 制

**模块**:
- 模块: `../../references/model-adaptation/model-atlas.md`, `../../references/model-adaptation/model-matrix-expanded.md`, `../../references/core/compatibility-matrix.md`

### MA1 能力与语法证据核对
**输入**: 目, 标, 模, 型, 和, 任, 务, 类, 型

**输出**: 已, 确, 认, 能, 力, 、, 未, 确, 认, 能, 力, 、, 语, 法, 限, 制, 与, 日, 期

**模块**:
- 模块: `../../references/model-adaptation/model-adapter-cards.md`, `../../references/model-adaptation/qh-agent-platform-adapters.md`, `../../references/model-adaptation/qh-seedance-pipeline.md`

### MA2 语义不变编译
**输入**: 原, 始, 提, 示, 词, 、, 硬, 约, 束, 和, 模, 型, 限, 制

**输出**: 目, 标, 平, 台, 格, 式, 、, 变, 量, /, 参, 数, 和, 负, 面, 约, 束

**模块**:
- 模块: `../../references/model-adaptation/06-model-adaptation.md`, `../../references/model-adaptation/08-model-adapters.md`, `../../references/prompt-engineering/11-prompt-engineering.md`

### MA3 回归与失败预防
**输入**: 编, 译, 结, 果

**输出**: 语, 义, 差, 异, 清, 单, 、, 兼, 容, 风, 险, 、, 校, 验, 报, 告

**模块**:
- 模块: `../../references/quality-safety/failure-playbook-220.md`, `../../references/quality-safety/13-quality-gates.md`
- `scripts/validate_prompt.py`

## 最终产物
- 模型适配提示词
- 参数说明
- 兼容性与时效性声明
- 回归检查报告

