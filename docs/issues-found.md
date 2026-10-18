# 问题清单 (Stage A)

## 声明值 vs 实际值

| 编号 | 类型 | 位置 | 声明值 | 实际值 | 严重级别 |
|---|---|---|---|---|---|
| ISSUE-A-001 | 总文件数 | 全仓库 | 344 | 345 | P1 |
| ISSUE-A-002 | 章节数 | 所有 .md `#` 行 | 15,244 | 9,813 | P1 |
| ISSUE-A-003 | 边数 | Markdown 相对路径引用 | 16,718 | 1,366 | P1 |
| ISSUE-A-004 | 能力数量 | capabilities/ | 29 | 0（无 capabilities/ 目录） | P0 |
| ISSUE-A-005 | 工作流格式 | workflows/ | WORKFLOW.md | 16 个 .yaml + index.yaml | P0 |
| ISSUE-A-006 | SKILL.md name | SKILL.md frontmatter | qhsj-aigc | qhsj-aigc-film | P0 |
| ISSUE-A-007 | SKILL.md 行数 | SKILL.md | ≤500 | 451（符合） | OK |
| ISSUE-A-008 | 知识库数量 | references/*.md | 303 | 303 | OK |
| ISSUE-A-009 | 工作流数量 | workflows/ | 16 | 16（yaml） | OK |
| ISSUE-A-010 | MANIFEST version | MANIFEST.json | 7.0.0 | 3.0.0 | P0 |
| ISSUE-A-011 | references/index.md 行数 | references/index.md | ≤100 | 2,739 | P0 |
| ISSUE-A-012 | 超限文件数 | 全仓库 | 0 | 67 | P1 |

## 数量自洽性

- 1 + 29 + 16 + 303 = 349 ≠ 声明总文件 344（实际 345）
- 口径差异：总文件 345 = 7(root) + 2(assets) + 1(evals) + 303(references) + 3(routing) + 2(schemas) + 5(scripts) + 4(templates) + 1(tests) + 17(workflows) = 345
- 声明 1+29+16+303=349 与 344/345 均不吻合，**口径待澄清**：可能 1 总控指 SKILL.md，29 能力指 SKILL.md 内路由表（无独立文件），16 工作流指 yaml，303 知识库指 references。但 1+29+16+303=349 无法解释 344/345。标记为「口径待澄清」，不计为错误。

## 结构检查

| 检查项 | 结果 |
|---|---|
| 每个能力目录有 SPEC.md | ❌ 无 capabilities/ 目录 |
| 每个工作流目录有 WORKFLOW.md | ❌ 工作流为 .yaml 文件，无 WORKFLOW.md |
| 存在 misc/other/temp/new/old 命名 | ⚠️ 4 个文件名含 "template"（19-output-templates.md 等），属合法"模板"语义，非临时文件，**误报** |
| README 数字一致性 | README 徽章显示 345 文件，与实际一致；声明口径 344 为旧值 |

## 口径疑点记录

- **章节数差异**：MANIFEST.json 声明 `reference_section_headings: 15244`，实际扫描所有 .md 的 `#` 行仅 9,813。可能 MANIFEST 的统计脚本将某些非标题行计入，或统计口径不同。**口径待澄清**。
- **边数差异**：声明 16,718，实际 1,366。差异巨大，可能声明值包含了 references/index.md 中的大量索引条目或 YAML 中的 modules 引用。**口径待澄清**。

## 已知冲突（需阶段 G 处理）

- SKILL.md name `qhsj-aigc-film` 与目标 `qhsj-aigc` 不一致
- MANIFEST.json version `3.0.0` 与目标 `7.0.0` 不一致
- 工作流为 YAML 格式，目标要求 WORKFLOW.md
- 无 capabilities/ 目录，29 个能力仅存在于 SKILL.md 路由表中

## 口径待澄清项（不计为错误）

1. 总文件 344 vs 345（实际）vs 349（1+29+16+303）
2. 章节数 15,244 vs 9,813
3. 边数 16,718 vs 1,366
