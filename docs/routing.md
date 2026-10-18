# 路由匹配与多任务调度算法

## 数据源（唯一权威）

- `routes.json` — 工作流（路由）表：`triggers` / `priority` / `gate_level` / `capabilities` / `capability_dependencies` / `always_run`。
- `capabilities/*/SPEC.md` — 每个能力的标准触发（`## 典型触发`）。
- `capability-routes.json` — 能力机器元数据：`semantic_triggers` / `auto` / `conditional` / `dependencies` / `priority`。

## 匹配算法（唯一权威定义）

实现载体：`backend/app/services/route_matcher.py::match_route`。同一 query 的处理顺序：

1. **排除 deprecated**：跳过 `deprecated: true` 的路由。
2. **能力识别**：按标准触发、语义触发与中文白话线索确定直接能力集合；子句级否定隔离（`phrase_is_negated`）会剔除被否定的触发，且否定不跨分句泄露。
3. **硬约束收敛**：显式排除项（不要提示词 / 不要分镜 / 不要全流程 / 只做音效 / 审计不生成内容等）在依赖闭包前移除对应交付物。
4. **依赖闭包**：按 `capability-routes.json` 的 `dependencies` 递归补齐前置能力；被硬约束禁止的能力不参与闭包。
5. **工作流调度（多任务）**：
   - `intent-analysis` 作为强制入口始终排入计划。
   - 由**显式工作流触发**命中的路由优先于仅由能力自动派生的路由。
   - 其余命中路由按 `priority` 降序、再按 id 排序，**全部**排入执行计划（叠加 / 并行），不因展示上限截断。
   - 整体门禁取最严值 `strictest_gate_level`；`blocks_on_failure_any` 表示任一命中路由为硬门禁。
6. **模糊意图 fallback**：请求含创作线索但无显式交付物时，落入 `intent-analysis` + `general_orchestration`，返回 `matched=true`、`fallback=true`、`error_code=INTENT_ANALYSIS_FALLBACK`。

## 未命中

当请求既无任何命中能力、也无创作线索时，返回 `matched=false`、`error_code=NO_ROUTE_MATCHED`，并按 difflib 相似度给出最接近的 3 条候选路由（`candidates`）。

## 多任务返回字段

`match_route` 返回向后兼容字段（`matched` / `route_id` / `gate_level` / `blocks_on_failure`）以及多任务字段：

- `routes` — 全部命中路由及其 `priority` / `matched_triggers`。
- `workflows` — 命中路由 id 列表（有序）。
- `capabilities` / `direct_capabilities` — 闭包后能力与直接请求能力。
- `multi_task` — 是否命中多条路由。
- `strictest_gate_level` / `blocks_on_failure_any`。

## 复用约束

`run_evals.py`、后端 `/route`、前端展示均复用该实现，禁止出现第二份匹配逻辑。
