# 从创意到影视交付的分阶段生产管线；资产先行，先锁角色和场景，再进入分镜资产/视频提示词阶段。
> 工作流 ID: `full-production`

**版本**: 3.0.0
**描述**: 从创意到影视交付的分阶段生产管线；资产先行，先锁角色和场景，再进入分镜资产/视频提示词阶段。
## 触发条件
- 完整项目
- 完整短片
- 从创意到成片
- 全流程制作
- 一整套
- 全链路交付
- 从剧本到视频
## 准入条件
- 只有显式完整制作意图才启用全管线。
- 用户的否定/只做约束优先于管线的可选阶段。
- 实际图像/视频/音频生成仅在宿主工具可用并成功返回时记为完成。
## 输入
- 创意
- 用户硬约束
- 参考资产
- 平台/模型信息
- 项目状态
## 输出
- 需求 Canon
- 故事/剧本
- 资产包
- 空间账本
- 分镜
- 提示词/媒体产物（按请求）
- QA 与版本包
## 阶段
### P0 意图、Canon 与制作策略
**输入**: 原始创意
**输出**: 结构化意图, 交付矩阵, 技术/资源约束, 制作计划
**模块**:
- `workflows/intent-analysis.yaml`
- 模块: `../../references/director-style/01-director-thinking-core.md`, `../../references/core/qhsj-multiagent-review-protocol.md`
**门禁**: 需求拆解无遗漏, 用户禁止项明确
### P1 故事开发与剧本门控
**输入**: Canon, 创意目标
**输出**: 故事结构, 剧本, 场次表, 人物与道具变化
**模块**:
- 模块: `../../references/novel-screenwriting/01-novel-screenplay.md`, `../../references/novel-screenwriting/qh-screenplay-gate-engine.md`, `../../references/core/qh-cinematic-dramaturgy-rules.md`
**门禁**: 叙事因果, 角色动机, 场次目标, 对白可执行性
### P2 资产清单、视觉 Bible 与规格
**输入**: 剧本/场次, 参考图, 用户角色/场景设定
**输出**: 资产 ID 清单, 角色规格, 场景规格, 道具规格, 视觉 Bible, 锁定字段
**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/character-performance/05-character-performance.md`, `../../references/aesthetics/06-aesthetics-style.md`, `../../references/spatial/qh-scene-design-handbook.md`
**并行**: True
**门禁**: 所有关键资产有 ID 和规范规格
### P3 角色资产图与场景资产图生成/核验/锁定
**输入**: 资产规格
**输出**: 规范资产图或可投喂提示词, 版本锁, 资产一致性报告
**模块**:
- `workflows/asset-first.yaml`
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/asset/p1-asset-validation-cases-500.md`, `../../examples/templates/asset-lock-ledger.md`
**门禁**: 角色多视图一致, 场景拓扑一致, 道具身份一致, P0/P1 已修复
**失败回退**: 返回 P2 更新规格或重新生成；不允许绕过资产锁进入分镜资产阶段
### P4 空间底图与连续性推演
**输入**: 锁定的场景/角色/道具资产
**输出**: 坐标约定, 固定锚点, 角色位置/朝向/视线, 距离约束, 摄影机可行区
**模块**:
- 模块: `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`, `../../references/spatial/qh-spatial-deduction-engine.md`, `../../references/spatial/continuity-state-library.md`, `../../examples/templates/spatial-continuity-ledger.md`
**门禁**: 空间尺度来源清楚, 人物与场景关系可验证
### P5 分镜与动作/表演计划
**条件**: ['按任务需要调用动作、武术、VFX模块']
**输入**: 剧本/场次, 锁定资产, 空间底图
**输出**: 文字分镜, 镜头起终态, 动作/视线/表演/声音标记
**模块**:
- 模块: `../../references/storyboard/02-storyboard-directing.md`, `../../references/cinematography/03-cinematography.md`, `../../references/character-performance/05-character-performance.md`, `../../references/action/10-action-choreography.md`, `../../references/vfx/12-vfx-motion-physics.md`
**门禁**: 动作时长可实现, 站位与轴线正确, 表演有可见/可听依据
### P6 可选分镜资产构建
**条件**: 用户需要故事板图片、关键帧或每镜资产图
**输入**: 分镜, 锁定角色/场景/道具资产 ID 与版本, 空间账本
**输出**: 分镜资产, 逐镜参考引用矩阵
**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`, `../../examples/templates/storyboard-board.md`
**门禁**: 不重新设计锁定角色, 不改变场景拓扑, 每镜写清允许变化字段
### P7 提示词编译与目标模型适配
**条件**: 用户需要图片/视频提示词或实际媒体生成
**输入**: 已通过 QA 的分镜, 锁定资产引用, 模型能力证据
**输出**: 模型中立提示词, 图片/视频提示词, 适配差异和兼容风险
**模块**:
- 模块: `../../references/prompt-engineering/07-prompt-engineering.md`, `../../references/model-adaptation/08-model-adapters.md`, `../../references/model-adaptation/model-atlas.md`, `../../references/model-adaptation/model-matrix-expanded.md`, `../../references/prompt-engineering/14-ultimate-video-prompt.md`
**门禁**: 不修改 Canon/锁定资产, 时效性声明已核验或标注待验证
### P8 声音/VFX/后期计划
**条件**: 用户要求音频、特效或后期声音/视觉设计
**输入**: 分镜时间轴, 动作/环境状态, 交付媒介
**输出**: 声音分层、配音节拍、VFX参数和后期清单
**模块**:
- 模块: `../../references/audio/11-audio-voice.md`, `../../references/vfx/12-vfx-motion-physics.md`, `../../references/vfx/qh-vfx-parametric-library.md`
**门禁**: 音画时间对齐, 特效有空间/光照/受力因果
### P9 多智能体/多角色 QA 与修复回归
**输入**: 所有实际生成的产物及源文件
**输出**: 问题分级, 根因, 补丁, 回归报告, 未解决项
**模块**:
- 模块: `../../references/quality-safety/16-quality-gates.md`, `../../references/core/qhsj-multiagent-review-protocol.md`
- `scripts/audit_package.py`
- `scripts/validate_prompt.py`
**门禁**: 无未处理 P0/P1, 资源和资产依赖一致, 真实执行状态已记录
**失败回退**: 按根因返回受影响阶段，不重做无关通过项
### P10 交付打包与状态更新
**输入**: 通过门禁的成品/提示词/报告
**输出**: 交付清单, 版本标记, 项目状态更新, 风险与待生成项
**模块**:
- 模块: `../../schemas/project-state.schema.json`, `../../schemas/storyboard.schema.json`, `../../examples/templates/asset-lock-ledger.md`
**门禁**: 逐项对照需求验收, 未执行项明确标记
## 最终产物
- 需求和 Canon 清单
- 故事/剧本与场次表
- 角色/场景/道具资产规格、图像引用或生成提示词
- 资产锁定台账与空间连续性账本
- 文字分镜；按需生成分镜资产
- 按请求提供图片/视频提示词、模型适配或实际媒体产物
- 声音/VFX/后期方案（按需）
- QA、回归与交付状态报告