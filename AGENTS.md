# AGENTS.md

## 冲突裁决优先级

```
1. SKILL.md 中的硬门禁（Asset-First、P0 门禁不可绕过）
2. docs/adr/ 中的架构决策
3. capabilities/*/SPEC.md
4. workflows/*/WORKFLOW.md
5. references/**/*.md
6. examples/
```

**铁律**：同一规则全仓库只能有一个权威出处，其余仅写"见 `<路径>`"。

## 新增内容入口

- 新能力：在 capabilities/对应目录 创建 SPEC.md + inputs.schema.json + outputs.schema.json，更新 capabilities/index.md，运行 scripts/build_routes.py，添加 golden 样例
- 新工作流：在 workflows/对应目录 创建 WORKFLOW.md，更新 workflows/index.md，运行 build_routes
- 新知识库：在 references/对应域 创建 .md，更新对应域索引
- 所有变更后运行 make check-all

## 上下文预算摘要

- 单次加载 ≤ 4 个文件
- 先读 index，再读命中的 1 个 SPEC/WORKFLOW
- 禁止批量读取 SPEC、递归读取目录
- 详见 SKILL.md「加载协议」与「上下文预算」
