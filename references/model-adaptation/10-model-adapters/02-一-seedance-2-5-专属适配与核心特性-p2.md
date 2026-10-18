---

### 6. 官方 API 契约（创建任务请求体）

```json
{
  "model": "doubao-seedance-2-5-260628",
  "content": [
    { "type": "text", "text": "……草莓味参考@图像1……" }
  ],
  "generate_audio": true,
  "ratio": "16:9",
  "duration": 15,
  "output_format": "mov"
}
```

| 参数 | 取值与说明 |
|---|---|
| `model` | 固定 `doubao-seedance-2-5-260628` |
| `ratio` | `16:9` / `9:16` / `1:1` / `21:9`；编辑/首尾帧模式用 `adaptive` 自适应 |
| `duration` | **4~30 秒** |
| `generate_audio` | 布尔值，是否生成原生音频 |
| `content` | 数组，可混合 `text` / `image_url` / `video_url` / `audio_url` 多模态素材 |
| 素材 `role` | `reference_image` / `reference_video` / `reference_audio`；首帧 `first_frame`、尾帧 `last_frame`（**仅 2.5 模式②；首/尾帧与参考图互斥**；2.0 不适用） |

---
