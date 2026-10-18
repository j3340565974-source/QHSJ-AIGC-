# 先建立资产清单与规范，再分别生成角色/场景/道具资产，完成核验锁定后才能生成分镜资产。
> 工作流 ID: `asset-first`

**版本**: 7.0.0
**描述**: 先建立资产清单与规范，再分别生成角色/场景/道具资产，完成核验锁定后才能生成分镜资产。
## 触发条件
- 资产前置
- 角色资产板
- 角色四视图
- 角色设定图
- 先做资产
- 先做人物设定图和场景设定图
- 先出角色图和场景图
- 人物场景图后做分镜
- 先出人物和场景图
- 先做人物和场景图
- 先设计人物和场景图
- 资产包
- 先锁定人物和场景
- 锁定角色资产
- 锁定场景资产
- 分镜资产引用角色图
- 先做人物和场景设定图
## 准入条件
- 用户要求角色、场景、道具资产或其一致性。
- 用户要求分镜资产时，角色和场景基准必须可追溯；缺少的资产先建规格与待生成任务。
- 只做文字资产规格时，不调用或假称已调用图像生成器。
## 输入
- 原始用户需求与硬约束
- 当前剧本/大纲/场次表（若有）
- 现有参考图、角色档案、场景图、道具图
- schemas/project-state.schema.json
## 输出
- 资产目录与唯一 ID 清单
- 角色规格、场景规格、道具规格
- 角色/场景/道具资产提示词或实际资产引用
- 版本和锁定台账
- 资产质量报告
- 空间锚点图/文字拓扑与分镜资产引用矩阵（需要时）
## 状态契约
```yaml
ids:
  character: CHAR-###
  prop: PROP-###
  scene: SCENE-###
  shot_asset: SHOT-S##-###
lock_states:
- draft
- review
- locked
- locked_provisional
- superseded
- blocked
- needs_recheck
require_versioned_changes: true
```

## 阶段
### A0 Canon 与输入盘点
**输入**: 用户需求, 剧本/场次, 参考素材, 项目状态
**输出**: 硬约束表, Canon, 缺失变量表, 资产来源表
**模块**:
- 模块: `../../references/director-style/01-director-thinking-core.md`, `../../references/novel-screenwriting/01-novel-screenplay.md`, `../../references/asset/qhsj-asset-locking-protocol.md`
**门禁**: 资产范围已明确, 用户硬约束已保留
### A1 建立资产目录与稳定 ID
**输入**: Canon, 角色/场景/道具线索
**输出**: 角色清单, 场景清单, 道具清单, 唯一 ID, 依赖关系
**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/asset/asset-ledger.md`, `../../examples/templates/asset-lock-ledger.md`
**门禁**: 无重复 ID, 每个资产都有类型和来源
### A2 角色与视觉总规范
**输入**: 资产清单, 用户视觉要求
**输出**: 视觉 Bible, 角色规格卡, 锁定字段/可变字段, 场景美术规格
**模块**:
- 模块: `../../references/character-performance/05-character-performance.md`, `../../references/aesthetics/06-aesthetics-style.md`, `../../references/cinematography/qh-color-style-master.md`, `../../references/asset/qhsj-asset-locking-protocol.md`
**并行**: True
**门禁**: 角色身份字段齐全, 视觉风格不与 Canon 冲突
### A3 角色资产图生成或提示词交付
**输入**: 角色规格卡, 视觉 Bible
**输出**: 每个角色的多视图资产图或完整可投喂提示词, 来源记录
**模块**:
- 模块: `../../references/character-performance/qh-character-lineage-and-sheets.md`, `../../references/asset/qhsj-asset-locking-protocol.md`, `../../examples/templates/character-sheet.md`
**并行**: True
**门禁**: 同一角色多视图身份一致, 无无依据的换脸/换装/比例漂移
### A4 场景资产图生成或提示词交付
**输入**: 场景规格, 场景锚点清单, 视觉 Bible
**输出**: 每个场景的整体布局与关键视角资产图或完整提示词
**模块**:
- 模块: `../../references/spatial/qh-scene-design-handbook.md`, `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`
**并行**: True
**门禁**: 不同视角保持同一拓扑, 出入口/墙体/固定锚点无自相矛盾
### A5 道具资产准备
**输入**: 道具清单, 角色/场景依赖
**输出**: 道具规格, 道具资产图或提示词, 持有人/初始状态
**模块**:
- 模块: `../../references/spatial/qh-scene-design-handbook.md`, `../../references/asset/qhsj-asset-locking-protocol.md`
**并行**: True
**门禁**: 轮廓/材质/尺寸级别/握持方式明确
### A6 资产核验与版本锁定
**输入**: 角色/场景/道具产物, 原始 Canon
**输出**: 规范资产版本, 锁定台账, 质量报告, 未解决项
**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/asset/p1-asset-validation-cases-500.md`, `../../references/quality-safety/16-quality-gates.md`, `../../examples/templates/asset-lock-ledger.md`
**门禁**: 身份门禁, 结构门禁, 材质门禁, 约束门禁, 来源门禁
**失败回退**: 将缺陷归因到规格或生成阶段，修复后重验；禁止跳过锁定门禁
### A7 空间拓扑与连续性底图
**输入**: 已核验场景资产, 角色身高/比例, 道具规格
**输出**: 坐标约定, 固定锚点, 人物路径, 视线目标, 距离约束, 摄影机可行区
**模块**:
- 模块: `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`, `../../references/spatial/qh-spatial-deduction-engine.md`, `../../references/spatial/qh-spatial-sandbox-simulation.md`, `../../examples/templates/spatial-continuity-ledger.md`
**门禁**: 尺度来源已标记, 人物位置/朝向/视线不冲突, 相机路线可行
### A8 可选分镜资产生成
**条件**: 用户明确需要分镜图、关键帧、分镜资产或逐镜图像
**输入**: 锁定角色资产, 锁定场景资产, 道具资产, 空间账本, 分镜设计
**输出**: 逐镜资产图/提示词, 资产引用矩阵, 每镜 allowed_variations
**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`, `../../references/storyboard/02-storyboard-directing.md`, `../../references/cinematography/qh-shot-language-quickref.md`, `../../examples/templates/storyboard-board.md`
**门禁**: 每镜引用角色/场景/道具 ID 与版本, 未授权变化字段为空, 视线/距离/相机/动作检查通过
**失败回退**: 回退到 A2-A7 对应阶段；不得通过提示词重复“保持一致”掩盖根因
### A9 最终资产与依赖回归
**输入**: 资产台账, 所有引用资产的下游产物
**输出**: 交付包, 资产依赖图, QA 报告, 变更影响报告
**模块**:
- 模块: `../../references/core/qhsj-multiagent-review-protocol.md`, `../../references/quality-safety/16-quality-gates.md`
- `scripts/check_package.py`, `scripts/run_evals.py`
**门禁**: 无 P0/P1 未解决项, 所有下游引用版本正确
## 最终产物
- 资产目录与唯一 ID
- 角色资产规格和多视图资产图/提示词
- 场景资产规格和整体/关键角度资产图/提示词
- 道具规格与资产图/提示词
- 资产锁定和版本台账
- 空间拓扑与连续性账本
- 可选分镜资产及其引用矩阵
- 资产质量报告与待确认项
## 失败策略
- 不得声称未调用的图像模型已经成功生成资产。
- 用户未批准时使用 locked_provisional，而不是 approved/locked。
- 任何锁定资产变更必须升级版本并触发下游回归。