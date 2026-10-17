# QHSJ 外部 Skill 研究与整合登记
检索日期：2026-09-25

> 本文件记录联网检索到的公开 Skill 项目，以及已经吸收到 QHSJ 本地能力层的工程思想。
> 不直接复制第三方仓库源代码；以能力映射、路由契约、测试规则和适配器方式整合。

## 1. Cinematography / 摄影与镜头语言

来源：
- fal-ai-community/skills — `cinematography`
  https://github.com/fal-ai-community/skills
- 该项目公开说明包含景别、角度、镜头运动、焦段感、光影、色彩、场面调度和生产前 QC；仓库许可说明为 MIT。
- QHSJ 对应：
  `07-visual-language.md`
  `qh-camera-language-complete.md`
  `qh-camera-specs-15rules.md`
  `qh-cinematography-lighting-encyclopedia.md`

吸收：
- 风格词必须落到可观察的镜头决策。
- 镜头运动必须物理可成立。
- 景别、角度、焦段感不能互相矛盾。
- 光线方向与色彩逻辑必须连续。

## 2. Storyboard / Previs

来源：
- gainubi/storyboard-video-skill
  https://github.com/gainubi/storyboard-video-skill
- 项目公开 SKILL 强调 panel-by-panel、shot language、motion continuity、视觉节拍和 consolidated prompt。
- QHSJ 对应：
  `04-storyboard-directing.md`
  `qh-storyboard-board-lite.md`
  `qh-action-previs-15grid.md`

吸收：
- 面板不是剧情摘要，而是观看设计。
- 每个 panel 优先表达一个可读动作或状态变化。
- 镜头、运动、连续性必须绑定。

## 3. AI 漫剧 / AI短剧

来源：
- zenstory-ai/drama-skills
  https://github.com/zenstory-ai/drama-skills
- 公开资料显示其是 MIT 许可的 11-skill 短剧/漫剧生产集合，覆盖剧本、视觉设定、分镜、图片/视频提示词和审查。
- QHSJ 对应：
  `qh-asset-first-pipeline.md`
  `qh-production-ledger-handbook.md`
  `qh-screenplay-gate-engine.md`
  `qh-segment-splicing.md`

吸收：
- 创作事实写入项目文件。
- 上游修改应回到对应 owner 文档。
- 先预览后生产。
- 生成前后的事实、资产、提示词和 QC 分开治理。

## 4. AI漫剧长线工作流

来源：
- nanzhipro/phase-ai-anime-skill
  https://github.com/nanzhipro/phase-ai-anime-skill
- 公开 SKILL 采用 phase / node / adapter / manifest 的外部状态管理模式。
- QHSJ 对应：
  `qh-fullchain-orchestrator.md`
  `qh-production-ledger-handbook.md`

吸收：
- 角色、世界观、场景、音频、视频任务外部化。
- image job / video job / TTS job 使用稳定 manifest 衔接。
- provider-neutral job spec。
- 节点可以替换，但输入输出合同不能被静默破坏。
- 真实模型调用前做环境与鉴权检查。

## 5. AI视觉导演总控

来源：
- jijiutong/ai-visual-director
  https://github.com/jijiutong/ai-visual-director
- 公开项目强调 Intake → Director Decisions → Character/Scene Anchors → Storyboard → Platform Prompts → QC → Execution Package。
- 项目公开许可为 MIT。
- QHSJ 对应：
  `qh-director-master-v4.md`
  `qh-asset-first-pipeline.md`
  `qh-output-frame-protocol.md`

吸收：
- 稳定治理层常驻：路由、格式合同、锁状态、Prompt QC、自动修复。
- 创作增强层按项目加载。
- draft / locked / committed 状态分离。
- 角色与场景资产先于大量镜头生成。

## 6. 动作导演

来源：
- irenerachel/fight-prompt-director
  https://github.com/irenerachel/fight-prompt-director
- 公开仓库为 MIT。
- 核心方法：完成条件、角色动作档案、攻击-回应-位移因果链、镜头职责、跨镜状态继承、单变量排错。
- QHSJ 对应：
  `qh-combat-direction-engine.md`
  `qh-fight-storyboard-dsl.md`
  `qh-action-cinematography-breakdown.md`

吸收：
- 每次动作必须得到回应和位置结果。
- 每镜只承担主要职责。
- 跨镜继承位置、方向、速度、武器和损伤。
- 动作、镜头、参考素材分层排错。

## 7. 更长链路的导演框架

来源：
- Krenlis/director-craft-framework
  https://github.com/Krenlis/director-craft-framework
- 公开说明覆盖剧本/剧情/分镜/镜头/光影/表演/对白/动作/VFX/平台化提示词和审阅纠偏。
- QHSJ 当前已有对应能力，作为覆盖度核对来源，不直接复制。

吸收：
- 导演判断、前期制片、AI生产三层要同时成立。
- 用物理可执行描述替代形容词堆砌。
- 失败按层归因，而不是整段随机重写。

## 8. AI Comic / 动态漫画

来源：
- jis60224/ai-comic-skills
  https://github.com/jis60224/ai-comic-skills
- 公开仓库提供剧本、分镜、视频提示词、视觉资产多个 skill 分包。
- 适合作为“AI漫剧多 skill 拆分”结构的覆盖核对来源。

吸收：
- 剧本、分镜、视频提示词、视觉资产分层。
- 同一资产事实从角色库/场景库下游复用，减少跨镜漂移。

## 9. 研究边界

“所有相关 Skill 全网全部整合”不是可验证的有限集合；GitHub 等公开仓库持续新增和变更。

因此本次实际完成的是：
- 对当前可检索公开来源做覆盖性整合
- 将关键能力映射到 QHSJ 已有模块
- 新增统一全链路编排层
- 增加模板调度层与回归检查
- 不复制第三方完整源代码，避免将来源文本误当作 QHSJ 自有知识库

新增来源不会自动获得生产路由权，必须经过能力映射、许可证检查、冲突检查和回归测试。
