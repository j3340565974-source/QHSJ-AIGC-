# 路由匹配与冲突算法

## 匹配算法（唯一权威定义）

同一 query 命中多条路由时，按以下顺序裁决：

1. **排除 deprecated**：排除 `deprecated: true` 的路由
2. **score 降序**：score = 大小写不敏感子串命中的 trigger 数量
3. **priority 降序**：score 并列时按 `priority` 降序
4. **冲突返回**：仍并列 → 返回 `ROUTE_CONFLICT`，列出全部并列候选交用户选择，**禁止自动择一**

## 未命中

所有路由 score = 0 时 → 返回 `NO_ROUTE_MATCHED`，按 difflib 相似度给出最接近的 3 条候选。

## 实现载体

本算法唯一实现为 `backend/app/services/route_matcher.py::match_route`。`run_evals.py`、后端 `/route`、前端展示均复用该实现，禁止出现第二份。
