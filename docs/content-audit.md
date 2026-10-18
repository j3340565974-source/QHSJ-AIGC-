# 内容审计台账

> 状态：v8.0.0 终审。全部 P0/P1 问题已修复并复验通过，`make check-all` 全绿。

## 审计范围

- `core/`、capabilities SPEC.md、workflows WORKFLOW.md 逐文件语义审查
- 跨文件规则一致性、依赖图、术语、门禁、计数、悬空引用、重复段落

## 问题清单

### ISSUE-C-001
- 类型：C4 重复与漂移
- 位置：references/ 全域（`v322-*.md` / `p1-*.md` 版本化副本与原版重复）
- 冲突内容：版本化副本与权威版段落高度重复，占用知识库条目
- 严重级别：P1
- 裁决：v8.0.0 原子化去壳——独有正文（含物理锁定层）先合并回权威主文件，再删除 155 个别名/门户壳、3 对 `v322-*` 重复目录、2 个 vfx 遗留别名
- 依据：docs/content-duplicates.md、ADR-004
- 状态：已修复（复验通过）

### ISSUE-C-002
- 类型：C2 门禁一致性
- 位置：全仓库 P0 门禁声明
- 检查结果：所有 SPEC.md 统一声明「禁止绕过 P0 门禁（违反时返回 GATE_P0_CANNOT_SKIP）」；SKILL.md 与 docs/gates.md 定义一致
- 严重级别：P0
- 裁决：通过
- 状态：已验证

### ISSUE-C-003
- 类型：C3 依赖图
- 位置：routes.json capability_dependencies
- 检查结果：check_package #5 循环依赖检测通过，无环
- 严重级别：P0
- 裁决：通过
- 状态：已验证

### ISSUE-C-004
- 类型：C8 悬空引用
- 位置：全仓库
- 检查结果：check_package #11 与 check_content C8 通过，无悬空引用（生成型报告除外）
- 严重级别：P1
- 裁决：通过
- 状态：已验证

### ISSUE-C-005
- 类型：C5 术语一致性
- 位置：全仓库
- 检查结果：check_content C5 通过，glossary 禁用名未出现在非 glossary 文件
- 严重级别：P1
- 裁决：通过
- 状态：已验证

### ISSUE-C-006
- 类型：C6 数字一致性
- 位置：全仓库
- 检查结果：29 能力 / 16 工作流 / 527 知识库与 manifest.declared_counts 及 references/index.md 域计数一致
- 严重级别：P1
- 裁决：通过
- 状态：已验证

### ISSUE-C-007
- 类型：C1 规则矛盾
- 位置：SKILL.md 硬门禁 ↔ capabilities SPEC.md ↔ workflows WORKFLOW.md
- 检查结果：Asset-First、P0 门禁不可绕过（正向声明）、依赖闭包三条硬门禁在 SKILL.md、所有 SPEC.md、docs/gates.md 中定义一致，无互斥行为
- 严重级别：P0
- 裁决：通过
- 状态：已验证

### ISSUE-C-008
- 类型：C9 过时未标
- 位置：全仓库
- 检查结果：无 `> DEPRECATED` 或 `已废弃` 标记缺少「替代:」的文件；无遗留版本化副本
- 严重级别：P2
- 裁决：通过
- 状态：已验证

## 跨文件审查清单

- [x] 同一规则全仓库唯一权威出处（P0 门禁见 docs/gates.md + SKILL.md）
- [x] 依赖图无环（check_package #5）
- [x] 工作流步骤与六步工作法对齐
- [x] 术语全仓库统一（glossary）
- [x] 所有违规绕行表述在硬门禁上下文中已清除
- [x] 示例通过其所在文件规则自检

## 总结

P0/P1 问题全部已修复并复验通过。C4 重复段落候选（见 docs/content-duplicates.md）中，跨文件重复的 DSL 公式与模板块属有意复用，版本化副本重复已随去壳归零。
