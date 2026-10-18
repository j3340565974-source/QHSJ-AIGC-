# 产物落盘约定

## 目录结构

```
runs/
  <run_id>/
    meta.json        # 符合 schemas/run-meta.schema.json
    prompts/*.md     # 可直接投喂图生视频模型的结构化提示词
    outputs/*.md     # 生成产物
    summary.md       # ≤ 5 行摘要
```

## run_id 格式

`run_id = YYYYMMDD-HHMMSS-<slug>`

## 规则

- 任何 > 20 行生成内容必须写入 `runs/<run_id>/` 下文件
- 上下文只保留 ≤ 5 行摘要 + 路径
- 跨阶段引用前序产物：只写 `runs/<run_id>/...` 路径，禁止复制全文回上下文
- 产物不存在时返回 `ARTIFACT_NOT_FOUND`
- `runs/` 整体 gitignore，回溯靠本地

## meta.json 字段

- `run_id`：符合格式
- `query`：用户原始请求
- `route_id`：命中的路由
- `gate_level`：门禁级别
- `timestamp`：ISO 时间戳
- `artifacts`：产物文件路径列表
