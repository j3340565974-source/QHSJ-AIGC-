# QHSJ 全链路自动化整合层
版本：3.2.2

## 1. 目标

把“用户白话输入”变成可执行生产任务，而不是让用户自己选择知识库文件。

统一链路：

`白话输入 → 任务分类 → 调度诊断 → 模板选择 → 导演IR → 剧作/资产 → 空间 → 表演 → 摄影/镜头 → 美术/美学 → 动作 → VFX → Prompt编译 → 模型适配 → 音画/后期 → QC → 输出 → 状态记录`

## 2. 模态路由

| 用户意图 | 主路由 | 关键能力 |
|---|---|---|
| 小说/故事 | 小说引擎 | 世界观、人物、长线结构、连续性 |
| 影视/短剧/漫剧剧本 | 编剧引擎 | 节拍、场次、对白、冲突、生产标签 |
| 短视频 | 短视频引擎 | Hook、节奏、口播、平台结构 |
| 分镜/故事板 | Storyboard | 面板、镜号、景别、机位、运动、连续性 |
| AI 图片 | Image Prompt | 主体、构图、光影、材质、模型适配 |
| AI 视频 | Video Prompt | 主体动作、环境运动、镜头、时间、音频、约束 |
| 动作/打斗 | Action | 动作因果、攻防、位移、镜头职责 |
| 表演 | Performance | 可见表演、FACS/AU、微表情、身体状态 |
| 美术/审美 | Art Direction | 风格、色彩、材质、置景、造型、视觉系统 |
| 摄影 | Cinematography | 景别、角度、焦段、镜头运动、布光、色彩 |
| AI 漫剧 | Manga/Anime Pipeline | 角色锚点、分镜、图生视频、TTS、合成 |
| 工作流自动化 | Workflow | manifest、状态、phase、adapter、QC |

## 3. 外部 Skill 整合原则

只吸收“能力契约”和“工程方法”，不整包复制第三方源代码。

外部能力分为：
1. `adopted`：已合并为 QHSJ 本地流程规则。
2. `mapped`：已有 QHSJ 模块覆盖，仅建立映射。
3. `adapter`：需要外部工具/API 才能执行，由模型适配层处理。
4. `reference-only`：用于研究，不进入默认路由。

## 4. 影视/AI影视整合

### Cinematography

引入核心能力：
- 主体与动作先于空泛“电影感”
- 景别/角度/焦段感/运镜必须互相一致
- 光源方向与色彩逻辑稳定
- 单镜头优先一个主动作、一个主空间关系
- 镜头语言直接服务戏剧功能

对应 QHSJ：
- `07-visual-language.md`
- `qh-camera-language-complete.md`
- `qh-shot-language-quickref.md`
- `qh-cinematography-lighting-encyclopedia.md`

### Storyboard / Previs

引入核心能力：
- panel-by-panel 拆解
- 每面板一个可读动作
- 镜头职责、运动、连续性提示
- 故事节拍和视觉节奏关联
- 结尾画面必须有明确功能

对应 QHSJ：
- `04-storyboard-directing.md`
- `qh-storyboard-board-lite.md`
- `qh-action-previs-15grid.md`
- `qh-scene-design-handbook.md`

## 5. AI短剧 / AI漫剧整合

统一为：

`原著/点子 → 单集剧本 → 视觉设定 → 角色/场景资产 → 分镜 → 图片提示词 → 视频提示词 → 音频 → 生产任务 → 合成 → 审查`

增加工程约束：
- 角色/服装/场景事实外部化
- manifest 连接上下游
- provider-neutral job spec
- 每阶段可独立交接
- 先预演、后真实生成
- 真实生成必须有明确授权/工具权限
- 不为了“凑完整流程”伪造不存在的上游事实

对应 QHSJ：
- `qh-asset-first-pipeline.md`
- `qh-production-ledger-handbook.md`
- `qh-character-lineage-and-sheets.md`
- `qh-screenplay-gate-engine.md`
- `qh-segment-splicing.md`

## 6. 动作指导整合

统一动作原子：

`完成条件 → 角色动作档案 → 发起 → 接触 → 回应 → 位移 → 下一拍接口`

强制继承：
- 位置
- 朝向
- 速度
- 武器
- 损伤
- 角色间距离
- 镜头职责

对应 QHSJ：
- `12-action-choreography.md`
- `qh-combat-direction-engine.md`
- `qh-fight-storyboard-dsl.md`
- `qh-martial-action-encyclopedia.md`
- `qh-action-cinematography-breakdown.md`

## 7. AI美学 / 美术整合

审美不再作为空泛形容词层，而进入可执行参数：
- 目的
- 构图
- 比例
- 色彩
- 光影
- 材质
- 纹理
- 运动语言
- 角色造型
- 场景置景
- 反复出现的视觉母题

对应 QHSJ：
- `08-aesthetics-art-direction.md`
- `qh-audiovisual-aesthetic-presets.md`
- `qh-color-style-master.md`
- `qh-color-psychology-master.md`
- `qh-gufeng-style.md`

## 8. Prompt 工程整合

采用：

`事实层 → 导演层 → 物理层 → 摄影层 → 美学层 → 模型语法层 → 负向/约束层 → QC`

禁止用堆砌“cinematic / masterpiece / 8K”等空泛词替代：
- 镜头位置
- 主体动作
- 空间关系
- 光源方向
- 动作终点
- 连续状态

对应 QHSJ：
- `09-prompt-engineering.md`
- `qh-prompt-feeding-checklist.md`
- `qh-prompt-template-vault.md`
- `qh-image-prompt-engine.md`

## 9. 工作流工程整合

引入四类合同：

### Intake Contract
确定：
- 输入素材
- 任务类型
- 输出媒介
- 用户明确模型/模板
- 平台
- 时长/画幅
- 连续性要求

### Phase Contract
每一阶段定义：
- 输入
- 输出
- 必填字段
- 完成条件
- 失败条件
- 下一阶段入口

### Adapter Contract
模型适配器只负责：
- 平台语法
- 参数能力
- 参考素材能力
- 时长/尺寸约束
- 模型专属字段

不得重新定义故事事实。

### QC Contract
按层归因：
`故事 / 导演 / 资产 / 空间 / 表演 / 物理 / 编译 / 模型能力 / 工具权限`

失败只修对应层，不随机重写整个任务。

## 10. 输出治理

默认：
`📄框外人类可读 + 🤖框内AI可执行`

显式命中 alt 模板时：
- 仅本轮替换默认双区格式
- 保留物理锁定、左右手、动作闭环
- 仍执行其他适用 QC
- 下一轮无条件恢复默认

