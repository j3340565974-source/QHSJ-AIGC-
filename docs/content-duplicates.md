# 重复段落候选 (C4)

| 文件1 | 文件2 | 相似度 | 片段 |
|---|---|---|---|
| README.md | docs/readme-before-l2.md | 1.00 | <div align="center">
  <img src="assets/logo.png" alt="QHSJ  |
| README.md | docs/readme-before-l2.md | 1.00 | > 🎬 面向 **AIGC 视听创作** 的工业级全流程技能包：**1 总控 + 29 能力 + 16 工作流 + 30 |
| README.md | docs/readme-before-l2.md | 1.00 | ```
📋 意图解析 → 🧭 多标签路由 → ✍️ 小说/剧本 → 🖼️ 资产锁定 → 📐 空间连续性 → 🎬 分镜导演 |
| README.md | docs/readme-before-l2.md | 1.00 | > 🔑 **核心铁律**：资产锁定是分镜资产生成的**硬门禁**。角色图、场景图、道具图未生成/核验/锁定前，工作流必须 |
| README.md | docs/readme-before-l2.md | 1.00 | 一套**给 AI 助手执行的 AIGC 全流程创作规则库**（Agent Skill）。用户用中文白话描述目标，系统自动 |
| README.md | docs/readme-before-l2.md | 1.00 | 1. **不漂移** —— 角色 / 场景 / 道具**先锁定再进分镜**（Asset-First），跨镜跨集一致性有据 |
| README.md | docs/readme-before-l2.md | 1.00 | > ⚠️ **能力边界诚实规则**：「路由已选择」≠「外部工具已调用」；「项目状态已建立」≠「跨会话永久记忆」。自动化检 |
| README.md | docs/readme-before-l2.md | 1.00 | 管线与题材解耦，凡「**创意 → 剧本 → 资产 → 分镜 → 提示词 → 模型投喂**」的 AIGC 创作都可套用： |
| README.md | docs/readme-before-l2.md | 1.00 | - **AI 短剧 / 漫剧 / 短视频剧集**（高密度场景）
- **AI 广告片 / 品牌宣传片 / 概念片**
- |
| README.md | docs/readme-before-l2.md | 1.00 | 完整触发词、依赖关系与章节索引以 `routing/route-registry.json` 为准。 |
| README.md | docs/readme-before-l2.md | 1.00 | **全局仲裁顺序**：安全与适用政策 > 用户明确硬约束 > 来源事实和项目 Canon > 因果/空间/动作/物理连续 |
| README.md | docs/readme-before-l2.md | 1.00 | > ⚠️ 用户的否定约束（"只要分镜，不要提示词""只写小说，不做视觉设计"）必须被保留，不得由依赖关系偷偷扩大交付范围 |
| README.md | docs/readme-before-l2.md | 1.00 | 建议使用 **Python 3.10+**。运行包审计和单元测试需要 `PyYAML`；Schema 元验证需要 `js |
| README.md | docs/readme-before-l2.md | 1.00 | ```bash
# 安装依赖（审计脚本需要）
pip install PyYAML jsonschema |
| README.md | docs/readme-before-l2.md | 1.00 | `/写剧本` · `/台词诊断` · `/数字资产包` · `/素材形态` · `/做分镜` · `/语速自检` · ` |
| README.md | docs/readme-before-l2.md | 1.00 | ```text
QHSJ-AIGC-全能影视/
├── SKILL.md                       # |
| README.md | docs/readme-before-l2.md | 1.00 | - **v3.0.0**（2026-10-18）— 全量路由、资产锁定与空间连续性版。统一命名 QHSJ AIGC 全能 |
| README.md | docs/readme-before-l2.md | 1.00 | 本项目采用 **MIT License**，完整条款见 [LICENSE](LICENSE)。 |
| README.md | docs/readme-before-l2.md | 1.00 | <div align="center">
  <img src="assets/logo.png" alt="作者头像" |
| README.md | docs/readme-before-l2.md | 1.00 | 如果在使用中遇到 **bug、逻辑漏洞、路由缺失、模型适配问题**，或有 **功能建议、合作意向**，欢迎通过以下方式联 |
| README.md | docs/readme-before-l2.md | 1.00 | > 💡 **反馈建议**：提交问题时请附上触发的自然语言原文、期望行为、实际行为，以及（若涉及生成）目标模型与画幅。作者 |
| README.md | docs/readme-before-l2.md | 1.00 | <div align="center">
  <p><strong>Made with ❤️ for AIGC Crea |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | **Mx-Shell的解法**（《丧尸清道夫》海外播放破2亿）：
- 主角用**机器人**（不需要人脸一致性，金属质感A |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | - 全片几乎没有对白，靠画面、动作、表情、环境叙事
- 用机器人的动作表达情感（如轻轻抚摸塑料模特的脸）
- 用环境细节 |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | **核心**：从第一层到第五层越来越具体。前四层是"是什么"，第五层是"什么感觉"。 |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | **禁忌**：不写空泛词汇（高级、好看、震撼、有感觉），全部替换成具体、可见、可执行的描述。 |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | 1. **脑子里先有画面，然后用文字往死里写细**：机器人的手不是"一只手"，而是"生锈的金属右手，三根手指微微弯曲，手 |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | **成本控制**：先用低分辨率/短时长生成预览，选好后再高清生成。不要每个镜头都高清抽卡，只对关键镜头高清抽卡。 |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | 1. 放弃传统首尾帧模式，不做逐帧手绘
2. 只用三类参考图：场景图+人物一致性图+关键道具图
3. 固定人物提示词：每 |
| references/novel-screenwriting/qh-mxshell-narrative-method.md | references/novel-screenwriting/v322-qh-mxshell-narrative-method.md | 1.00 | 1. **固定人物描述词**：精确外貌+服装+特征，每次完整复制不修改
2. **参考图锁定**：生成1-2张高质量人物 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/novel-screenwriting/p1-film-language-library.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/novel-screenwriting/v322-qh-dialogue-speed-check.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/novel-screenwriting/p1-creative-theory.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/novel-screenwriting/v322-qh-screenplay-gate-engine.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/novel-screenwriting/v322-01-novel-engine.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/novel-screenwriting/v322-qh-dialogue-doctor-7d.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/quality-safety/v322-18-safety-originality.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/quality-safety/v322-qh-platform-safety-compliance-guide.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/quality-safety/v322-16-quality-gates.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/quality-safety/v322-qh-quality-gate-review.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/quality-safety/v322-17-evolution-kb.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/quality-safety/p1-qa-checklist-320.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/quality-safety/p1-failure-playbook-220.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/vfx/v322-qh-anime-ultimate-vfx-paradigm.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/vfx/v322-13-vfx-motion-physics.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/genre/p1-genre-playbooks.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/storyboard/p1-scene-atom-library.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/storyboard/p1-shot-recipe-library.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/storyboard/v322-qh-storyboard-board-lite.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/prompt-engineering/p1-prompt-transformation-lab.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/prompt-engineering/v322-23-prompt-operator-engineering.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/prompt-engineering/p1-bonsai-context-engineering.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/prompt-engineering/v322-09-prompt-engineering.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/prompt-engineering/p1-wording-and-safety.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/prompt-engineering/v322-qh-prompt-feeding-checklist.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/prompt-engineering/p1-prompt-formulas.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/spatial/v322-05-spatial-continuity.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/spatial/v322-qh-spatial-reference-system-V3.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/spatial/v322-qh-asset-spatial-ledger.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/spatial/p1-continuity-state-library.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-authentic-martial-taxonomy.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-combat-rhythm-defense3state.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-12-action-choreography.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-action-ultimate-finisher.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-martial-arts-arsenal.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-martial-arts-combat-library.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-combat-direction-engine.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-action-previs-15grid.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/action/v322-qh-xuanhuan-magic-combat.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/p1-platform-algorithm-evidence.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/p1-platform-script-patterns-180.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/v322-qh-aspect-ratio-adaptation.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/p1-hook-library.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/v322-22-media-type-atlas.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/v322-20-coverage-and-conflicts.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/v322-03-short-video.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/platform/p1-platform-playbooks.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/asset/p1-asset-package-spec.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/asset/p1-asset-ledger.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/asset/v322-qh-asset-first-pipeline.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/asset/p1-asset-validation-cases-500.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/asset/v322-qh-production-ledger-handbook.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/cinematography/v322-qh-camera-specs-15rules.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/cinematography/v322-qh-spatial-topview-camera.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/cinematography/v322-qh-lighting-and-antifake.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/cinematography/v322-qh-camera-transitions-6types.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/core/p1-decision-protocol.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/core/v322-14-style-cultural-knowledge.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/core/p1-source-derived-core.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/core/v322-qh-cinematic-dramaturgy-rules.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/core/p1-compatibility-matrix.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/p1-emotion-curves.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/p1-performance-recipes.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/v322-qh-emotion-beat-curve.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/v322-qh-facs-emotion-recipes.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/v322-qh-character-lineage-and-sheets.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/v322-qh-wenxi-micro-expression.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/v322-qh-facs-au-dictionary.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/v322-qh-facs-micro-expression.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
| references/novel-screenwriting/v322-02-screenwriting.md | references/character-performance/v322-06-performance-control.md | 1.00 | > 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整 |
