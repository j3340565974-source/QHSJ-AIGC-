# 闭源模型与 Canvas 工作流自动化对接引擎 (Cloud Models & Canvas Workflow Engine)

本引擎专门面向闭源云端视频模型及 Canvas 协作画布，提供提示词解耦注入、资产图映射与批量任务调度规范，实现“AI 自动完成参数装配，导演仅在关键节点审核确认”。具体模型可用功能、时长、画幅、参考图数量、API 端点和字段名称均属于供应商契约，必须在实际调用时核验官方文档；下文时长示例仅用于估算，不视为当前能力保证。

---

## 一、 闭源云端模型三层对接架构

```text
[分镜动力学与解耦提示词组] 
       │
       ├──> 1. 资产图/4 View 资产板绑定 (@asset_name -> 平台参考图输入)
       ├──> 2. 提示词解耦投喂 (主体层 + 环境层 + 镜头动态层)
       └──> 3. 平台参数契约 (生成时长随模型契约: Seedance 2.0 ≤15s / 即梦 5s~10s, 运镜强度, 提示词相关性, 风格预设)
       │
       ▼
[目标视频模型 / Canvas 画布 API（按官方契约适配）]
```

---

## 二、 Canvas / 云端 API 批量调度模版示例 (Python)

```python
"""QHSJ provider-adapter template.

Install: python -m pip install requests
Configure QHSJ_VIDEO_API_URL, QHSJ_VIDEO_API_KEY and QHSJ_VIDEO_MODEL from the
actual provider's official API documentation before calling this function.
The generic payload below is only a starting contract: providers often use different
field names and reference-image formats, so adapt build_provider_payload() per provider.
"""
from __future__ import annotations

import os
from typing import Any, Mapping

import requests


def build_provider_payload(shot_data: Mapping[str, Any]) -> dict[str, Any]:
    """Map a QHSJ shot record to the target provider's documented request schema."""
    model = shot_data.get("model") or os.getenv("QHSJ_VIDEO_MODEL")
    prompt = shot_data.get("positive_prompt") or shot_data.get("prompt")
    if not model:
        raise ValueError("缺少模型名称：请提供 shot_data['model'] 或设置 QHSJ_VIDEO_MODEL")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("缺少正向提示词：需要 positive_prompt 或 prompt")

    # Keep only fields documented by the selected provider. Rename/remove fields in
    # this adapter when its official API contract differs; do not assume cross-provider parity.
    payload: dict[str, Any] = {"model": model, "prompt": prompt.strip()}
    optional_map = {
        "negative_prompt": "negative_prompt",
        "duration": "duration",
        "aspect_ratio": "aspect_ratio",
        "ref_images": "ref_images",
        "camera_motion": "camera_motion",
        "motion_intensity": "motion_intensity",
    }
    for source_key, provider_key in optional_map.items():
        if source_key in shot_data and shot_data[source_key] is not None:
            payload[provider_key] = shot_data[source_key]
    return payload


def inject_shot_payload(
    shot_data: Mapping[str, Any],
    api_endpoint: str | None = None,
    api_key: str | None = None,
    timeout_seconds: float = 60.0,
    session: requests.Session | None = None,
) -> dict[str, Any]:
    """Submit one shot payload and return a decoded JSON response, or raise a clear error."""
    endpoint = api_endpoint or os.getenv("QHSJ_VIDEO_API_URL")
    token = api_key or os.getenv("QHSJ_VIDEO_API_KEY")
    if not endpoint:
        raise ValueError("缺少 API 地址：请核验供应商文档并设置 QHSJ_VIDEO_API_URL")
    if not token:
        raise ValueError("缺少 API 凭证：请通过安全环境变量设置 QHSJ_VIDEO_API_KEY")
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds 必须大于 0")

    payload = build_provider_payload(shot_data)
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    client = session or requests.Session()
    try:
        response = client.post(endpoint, headers=headers, json=payload, timeout=timeout_seconds)
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError as exc:
            raise RuntimeError("供应商返回的响应不是有效 JSON；请按官方契约检查响应格式") from exc
        if not isinstance(data, dict):
            raise RuntimeError("供应商响应 JSON 顶层不是对象；请在适配器中处理实际响应结构")
        return data
    finally:
        if session is None:
            client.close()
```

---

## 三、 平台生成批次与资产前置预估规范

每组输出提示词与分镜时，系统将自动汇总闭源平台任务资产清单：
- **视频生成任务组数**：如标准 3 分钟剧本输出 14 组视频单元（每组 12s~15s）；
- **前置参考图需求**：角色资产 4 View 板（CHR-）+ 场景氛围参考图（SCN-）；
- **任务轮次预估**：按闭源平台标准生成批次统计，辅助团队高效规划生成批次与点数预算。
