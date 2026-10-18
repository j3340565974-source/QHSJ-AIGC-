# 将已有剧本转换为可执行分镜；先建立并锁定角色/场景资产，再生成可选分镜资产和视频提示词。

> 工作流 ID: `script-to-screen`

**版本**: 7.0.0

**描述**: 将已有剧本转换为可执行分镜；先建立并锁定角色/场景资产，再生成可选分镜资产和视频提示词。

## 触发条件
- 把剧本拆成分镜
- 剧本转分镜
- 剧本到分镜
- 剧本转视频
- 已有剧本做分镜
- 每镜生成视频提示词
- 分镜图引用角色资产

## 准入条件
- 用户有源剧本或要求先创作/补全剧本。
- 需要图像分镜时，资产锁定是前置门禁。
- 用户明确只要文字分镜、不需要资产图或提示词时，跳过相应交付而保留空间与连续性检查。

## 输入
- 剧本/创意
- 参考资产
- 项目 Canon
- 交付约束

## 输出
- 剧本诊断
- 场次表
- 资产台账
- 空间账本
- 分镜表
- 可选分镜资产/视频提示词
- QA 报告

## 阶段
### S0 需求、Canon 与剧本诊断
**输入**: 原始剧本, 用户硬约束

**输出**: 需求矩阵, Canon, 叙事缺口, 交付范围

**模块**:
- 模块: `../../references/novel-screenwriting/01-novel-screenplay.md`, `../../references/novel-screenwriting/qh-screenplay-gate-engine.md`, `../../references/core/qhsj-multiagent-review-protocol.md`

**门禁**: 不得改写用户明确保留的事实, 诊断与重写任务分开

### S1 场次拆分与资产提取
**输入**: 诊断后的剧本或原剧本

**输出**: 场次表, 角色表, 场景表, 道具表, 出入场和状态变化

**模块**:
- 模块: `../../references/novel-screenwriting/01-novel-screenplay.md`, `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/asset/qh-production-ledger-handbook.md`

**门禁**: 每场目标/地点/时间/人物/关键道具明确

### S2 角色、场景、道具规格和参考资产核对
**输入**: 资产清单, 现有参考图, Canon

**输出**: 资产 ID, 角色规格, 场景规格, 道具规格, 视觉 Bible

**模块**:
- 模块: `../../references/character-performance/05-character-performance.md`, `../../references/aesthetics/06-aesthetics-style.md`, `../../references/spatial/qh-scene-design-handbook.md`, `../../references/asset/qhsj-asset-locking-protocol.md`

**并行**: True

**门禁**: 同一资产仅有一个规范版本, 冲突参考图有明确优先级

### S3 生成角色/场景资产并锁定
**输入**: 角色/场景/道具规格

**输出**: 规范资产图或可投喂提示词, 资产状态, 版本锁定台账

**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/asset/p1-asset-validation-cases-500.md`, `../../examples/templates/asset-lock-ledger.md`

**门禁**: 身份/空间/材质一致, P0/P1 缺陷已修复, 未人工确认资产标记 locked_provisional

**失败回退**: 返回 S2 修复规格或重生成；不允许进入 S4

### S4 建立空间、站位、距离与视线账本
**输入**: 已锁定场景资产, 角色规格, 道具规格, 场次表

**输出**: 坐标系, 场景固定锚点, 人物路径, 人物间距离, 目光目标, 摄影机可行区, 轴线

**模块**:
- 模块: `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`, `../../references/spatial/qh-spatial-deduction-engine.md`, `../../references/spatial/continuity-state-library.md`, `../../examples/templates/spatial-continuity-ledger.md`

**门禁**: 尺寸来源透明, 注视目标存在, 距离支持动作, 摄影机路径可行

### S5 逐镜分镜编排
**输入**: 场次表, 锁定资产引用, 空间账本, 表演目标

**输出**: 文字分镜表, 镜头起态/终态, 声画节拍, 连续性字段

**模块**:
- 模块: `../../references/storyboard/02-storyboard-directing.md`, `../../references/cinematography/03-cinematography.md`, `../../references/character-performance/05-character-performance.md`, `../../references/cinematography/qh-shot-language-quickref.md`

**门禁**: 每镜目标清楚, 时长支持动作, 轴线/景别/机位/视线不冲突

### S6 可选分镜资产与视频提示词
**条件**: 用户明确要求分镜图片、关键帧或视频提示词

**输入**: 分镜表, 角色/场景/道具参考图及版本, 模型约束

**输出**: 逐镜资产图/提示词, 视频提示词, 目标模型适配说明

**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`, `../../references/prompt-engineering/07-prompt-engineering.md`, `../../references/model-adaptation/08-model-adapters.md`, `../../references/prompt-engineering/14-ultimate-video-prompt.md`

**门禁**: 逐镜引用锁定资产, 动作/空间/时间码相容, 明确允许变化与禁止变化

### S7 分层 QA 与根因回退
**输入**: 剧本, 分镜, 资产台账, 提示词（如有）

**输出**: 问题清单, 根因, 修复记录, 回归报告

**模块**:
- 模块: `../../references/quality-safety/16-quality-gates.md`, `../../references/core/qhsj-multiagent-review-protocol.md`, `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`
- `scripts/validate_prompt.py`

**门禁**: P0/P1 无未解决项, 所有失败项都有回归状态

**失败回退**: 按根因返回 S0-S6 受影响阶段，修复后重新执行相关门禁

## 最终产物
- 剧本诊断与场次表
- 角色/场景/道具资产台账与锁定状态
- 空间连续性账本
- 完整分镜表
- 用户需要时的逐镜分镜资产与视频提示词
- 质量与回归报告

