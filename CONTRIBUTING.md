# 贡献指南

## 前置条件

- Python 3.10+
- Node.js 20+（前端）
- 了解 [AGENTS.md](AGENTS.md) 中的冲突裁决优先级

## 快速开始

```bash
# 后端
pip install -r backend/requirements.txt -r backend/requirements-dev.txt
python3 -m pytest backend/tests/

# 前端
cd frontend && npm install && npm run build
```

## 开发流程

1. 从 `main` 创建分支：`git checkout -b feat/<topic>`
2. 完成变更后运行全部检查：
   ```bash
   make check-all          # 结构 + 内容 + schema + 路由
   python3 -m pytest backend/tests/
   cd frontend && npm run build
   ```
3. 提交前确保 `check_package.py` 16 项检查全部通过。

## 新增内容入口

- **新能力**：在 `capabilities/<name>/` 创建 SPEC.md + inputs.schema.json + outputs.schema.json，更新 capabilities/index.md，运行 scripts/build_routes.py，添加 golden 样例。
- **新工作流**：在 `workflows/<name>/` 创建 WORKFLOW.md，更新 workflows/index.md，运行 build_routes。
- **新知识库**：在 `references/<domain>/` 创建 .md 文件，更新对应域 references/<domain>/index.md。
- 所有变更后运行 `make check-all`。

## 文件大小限制

| 类型 | 行数 | 字节 |
|---|---|---|
| SKILL.md | ≤ 500 | ≤ 24 KB |
| SPEC（能力规格） | ≤ 200 | ≤ 10 KB |
| WORKFLOW（工作流） | ≤ 150 | ≤ 8 KB |
| reference 知识库 | ≤ 300 | ≤ 12 KB |
| index 索引 | ≤ 100 | ≤ 4 KB |

超限文件按 `##` 二级标题拆分为子目录分片。

## 门禁规则

- P0 门禁禁止绕过，违反时返回错误码并停止执行。
- 路由匹配唯一数据源：`backend/app/services/route_matcher.py`。
- 同一规则全仓库只能有一个权威出处，其余仅写"见 `<路径>`"。

## 提交规范

- 使用 [Conventional Commits](https://www.conventionalcommits.org/)：`feat:`、`fix:`、`docs:`、`refactor:`、`chore:`
- 阶段标签格式：`stage/<X>-done`
- 发布标签格式：`v<major>.<minor>.<patch>`

## 联系

- 微信：`C0053224QM`
- QQ 邮箱：`3340565974@qq.com`
- Google 邮箱：`j3340565974@gmail.com`
