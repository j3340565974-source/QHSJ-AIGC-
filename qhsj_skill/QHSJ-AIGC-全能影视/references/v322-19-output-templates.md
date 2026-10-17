# 输出模板

## A. 小说项目卡

```yaml
project:
  title:
  genre:
  audience:
  target_length:
  voice:
canon:
world:
characters:
series_arc:
current_state:
open_threads:
style_lock:
forbidden_future_reveals:
```

## B. 场景空间护照

```yaml
scene_id:
location:
time:
anchors:
characters:
objects:
axis:
light:
sound:
camera_access:
continuity_notes:
```

## C. 分镜卡

| 镜号 | 时长 | 功能 | 景别/构图 | 机位/运动 | 主体动作 | 反应 | 空间状态 | 光 | 声 | 终帧 |
|---|---|---|---|---|---|---|---|---|---|---|

## D. 图片 Prompt

> ⚠️ 以下为旧版通用占位提纲，已被 `qh-output-frame-protocol.md` 双区框内协议取代。框内图片必须以【风格】开头，按【风格】【材质】【光影】【渲染】【物理锁定】【场景锁定】【角色锁定】【空间】【负向】固定结构输出；禁止使用【主体】【服装与细节】【构图与摄影】【光影与色调】【质量标签】等旧标签。本提纲仅作字段参考，禁止直接按此格式出框内提示词。

```text
【风格】
【材质】
【光影】
【渲染】
【空间】
【构图】
【摄影】
【动作/姿态】
【色彩】
【视觉风格】
【参考】
【输出】
【负向/约束（仅在模型支持时）】
```

## E. 视频 Prompt

> ⚠️ 以下为旧版通用占位提纲，已被 `qh-output-frame-protocol.md` 双区框内协议取代。框内视频必须以【风格】开头，依次包含【材质】【光影】【渲染】【角色+音色】【物理锁定】，并以【镜N（Xs）】承载镜头；禁止使用【主体】等非协议旧标签。本提纲仅作字段参考。

```text
【风格】
【场景】
【动作】
【环境运动】
【摄影机】
【表演】
【光影】
【声音】
【连续性】
【终帧】
```

## F. QA

```text
QG0 输入：PASS/FAIL
QG1 叙事：PASS/FAIL
QG2 资产：PASS/FAIL
QG3 空间：PASS/FAIL
QG4 表演：PASS/FAIL
QG5 物理：PASS/FAIL
QG6 Prompt：PASS/FAIL
QG7 连续性：PASS/FAIL
QG8 交付：PASS/FAIL
残留风险：
修复建议：
```
