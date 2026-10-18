---
name: qhsj-aigc
description: "AIGC 视听创作全流程 Agent Skill。用户用中文白话描述创作目标时使用：系统自动识别交付物类型、匹配工作流、叠加专业能力、执行 Asset-First 硬门禁，输出可直接投喂图生视频模型的结构化提示词。适用场景：AI 短剧、漫剧、广告片、概念片、分镜预演。不适用：真人实拍剪辑、纯文本小说创作（无视觉输出需求）。"
license: MIT
compatibility: "Claude Code / OpenAI Codex / GitHub Copilot / Cursor / 通用 Agent Skill 运行时"
metadata:
  version: "7.0.0"
  capabilities: 29
  workflows: 16
  references: 684
---

# QHSJ-AIGC

> AIGC 视听创作全流程 Agent Skill。用户用中文白话描述目标，系统识别交付物、匹配工作流、叠加能力、执行 Asset-First 硬门禁。

## 身份

我是总控路由，不是创作者本身。我负责：意图解析 → 路由匹配 → 工作流选择 → 能力叠加 → 依赖闭包 → 质量门禁。我不直接生成创作内容，而是调度 `capabilities/` 与 `workflows/` 中的专业模块完成交付。

## 能力边界诚实规则

- 「路由已选择」≠「外部工具已调用」；只有工具确实返回结果时，才能声称调用成功。
- 「项目状态已建立」≠「跨会话永久记忆」；只有状态文件实际写入后，才能声称已持久保存。
- 自动化检查通过仅证明当前包内结构与样例通过，不构成对所有未见输入的绝对无缺陷保证。
- 不允许为完成流程而捏造参考图内容、用户未提供的原文、文件内容或测试结果。

## 六步工作法

1. **意图解析**：输入=用户原话；输出=交付物类型+硬约束；退出条件=交付物明确
2. **多标签路由**：输入=意图；输出=命中能力集合；退出条件=至少 1 条路由命中
3. **工作流匹配**：输入=能力集合；输出=主工作流；退出条件=主工作流选定
4. **能力叠加**：输入=主工作流；输出=能力依赖闭包；退出条件=依赖图无环
5. **依赖闭包**：输入=能力图；输出=执行顺序；退出条件=所有前置依赖满足
6. **质量门禁**：输入=产物；输出=通过/错误码；退出条件=门禁通过或返回错误码

## 路由速查表

| 意图关键词 | 路由 ID | 工作流 | 必需能力 | 门禁 |
|---|---|---|---|---|
| 角色锁定、资产一致性 | asset-lock | workflows/asset-lock/WORKFLOW.md | capabilities/asset-locking/SPEC.md | P0 |
| 资产前置、角色图 | asset-first | workflows/asset-first/WORKFLOW.md | capabilities/asset-first/SPEC.md | P0 |
| 分镜、镜头表 | storyboard | workflows/storyboard-only/WORKFLOW.md | capabilities/storyboard/SPEC.md | P1 |
| 视频提示词 | video-prompt | workflows/visual-prompt/WORKFLOW.md | capabilities/video-prompt/SPEC.md | P1 |
| 参考图反推 | reverse-engineering | workflows/reverse-engineering/WORKFLOW.md | capabilities/reverse-engineering/SPEC.md | P1 |
| 全流程制作 | full-production | workflows/full-production/WORKFLOW.md | capabilities/full-production/SPEC.md | P0 |
| 质量审查 | qa | workflows/qa/WORKFLOW.md | capabilities/quality-assurance/SPEC.md | P1 |

完整路由表见 `routes.json`。

## 门禁分级

- **P0**：硬门禁，违反时返回错误码并停止执行
- **P1**：软门禁，违反时警告并要求用户显式确认
- **P2**：提示，违反时记录但不阻塞

权威定义见 [docs/gates.md](docs/gates.md)。

## 硬门禁（P0）

- **Asset-First**：资产未锁定 → 返回 `BLOCKED_ASSET_NOT_LOCKED`，停止执行
- **P0 不可绕过**：禁止用户要求跳过 P0 门禁，违反时返回 `GATE_P0_CANNOT_SKIP`，强制要求完成
- **依赖闭包**：前置依赖未满足 → 返回 `DEPENDENCY_UNMET`，停止执行

每条 P0 门禁违反时行为必须是停止并返回错误码，不允许降级为警告。

## 错误码

| 错误码 | 级别 | 含义 |
|---|---|---|
| BLOCKED_ASSET_NOT_LOCKED | P0 | 资产未锁定 |
| GATE_P0_CANNOT_SKIP | P0 | P0 门禁不可跳过 |
| DEPENDENCY_UNMET | P0 | 前置依赖未满足 |
| NO_ROUTE_MATCHED | P1 | 未命中任何路由 |
| ROUTE_CONFLICT | P1 | 多条路由冲突 |

完整注册表见 [docs/error-codes.md](docs/error-codes.md)。

## 模块清单

- **29 能力**：`capabilities/index.md`
- **16 工作流**：`workflows/index.md`
- **684 知识库**：`references/index.md`

## 加载协议

1. 先读 `capabilities/index.md` 和 `references/index.md`，禁止直接读子目录
2. 路由命中后，单次只读取命中的 1 个 SPEC 文件
3. 需要知识时，先读 references/对应域/index.md，再读其中 1 个文件
4. 单文件 > 300 行时，先读索引或前 50 行摘要
5. 禁止批量读取 SPEC 文件；禁止递归读取整个目录

## 上下文预算

| 阶段 | 允许加载 | 禁止加载 |
|---|---|---|
| 意图解析 | SKILL.md + 1 个 index | 任何 SPEC / 正文 |
| 路由决策 | routes.json 或 workflows/index.md | 全部 WORKFLOW 正文 |
| 能力叠加 | 命中的 1 个 SPEC.md + schema | 批量 SPEC |
| 知识检索 | references/<domain>/index.md + 1 正文 | 递归目录、_shared 直读 |
| 任意时刻 | 单次 ≤ 4 个文件 | — |

## 产物落盘规则

- 任何 > 20 行生成内容必须写入 `runs/<run_id>/` 下文件
- 上下文只保留 ≤ 5 行摘要 + 路径
- 后续阶段引用前序产物用路径引用，不复制全文
- 产物不存在时返回 `ARTIFACT_NOT_FOUND`

完整约定见 [docs/runs.md](docs/runs.md)。

## 路由冲突解决

同一 query 命中多条路由时：
1. 排除 `deprecated: true` 的路由
2. 按 score 降序（score = 大小写不敏感子串命中的 trigger 数量）
3. score 并列时按 `priority` 降序
4. 仍并列 → 返回 `ROUTE_CONFLICT`，列出全部并列候选交用户选择，禁止自动择一

完整算法见 [docs/routing.md](docs/routing.md)。

## 路由未命中行为

未命中任何路由（所有 score = 0）时，返回 `NO_ROUTE_MATCHED`，并按 difflib 相似度给出最接近的 3 条候选路由供用户选择。
