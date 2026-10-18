## 五、Shot Sheet 分镜表（PromptSmith "AI Video Director"）

每个场景输出一张 Shot Sheet：
1. **Scene Description（What）**
   - Subject：外貌、服装、姿态、表情。
   - Environment：地点、时间、天气。
2. **Camera（How filmed）**：景别、角度、运动、焦段、景深。
3. **Action Beats（Temporal）**：按时间码拆 beats，每个 beat 一个动作。
4. **Lighting Evolution**：光在镜头内怎么变。
5. **Audio**：对白/SFX/环境音。
6. **Style Reference**：导演/影片/调色。

## 六、模型特定调整（关键！）

| 模型 | 特点 | Prompt 策略 |
|---|---|---|
| **Sora 2** | 物理因果驱动 | 写因果链：`the wind catches the fabric, pulling it taut` 而非 `fabric blowing`。支持原生音频。（注：OpenAI 已宣布关闭 Sora，2026-04-26 app 关闭，API 2026-09-24 终止） |
| **Veo 3.1** | 精确理解摄影术语 | `dolly zoom`, `timelapse`, `slow push-in` 直接翻译成机位行为。主体前置要比别的模型更激进。商业级干净画面。 |
| **Runway Gen-4.5** | 重动作轻外观 | 图生视频时，首图已带视觉信息，文字 prompt 专注写力和运动：`wind pulls the curtain toward the open window`。适合快速迭代/社交媒体。 |
| **Kling 3.0** | 支持加权与负向 | `++sleek red convertible++ driving along coastal highway`。多镜头序列最多 6 镜，原生音频+对口型。 |
| **Hailuo 02 Director** | 方括号语法 | `[camera: slow dolly in]` 方括号 token 语法。 |
| **LTX-2** | 几何控制 | 通过 start frame / end frame 的空间 delta 控制运动，原生 4K 50fps。 |
| **Seedance 2.0** | 纯 prompt 写实 | prompt-only 机位控制，运动平滑度好。 |

## 七、最优长度与常见错误

- **甜区**：50–150 词（3–6 句）。单句 prompt 必出泛泛结果；超过 200 词模型开始忽略后半段或融合冲突。
- **负面语言**：大多数模型不处理 `no text overlay` / `don't show buildings`，它会生成你不让它生成的东西。改写成正向描述。（例外：Kling 支持显式 negative prompt。）
- **一场景一 prompt**：需要序列就分多条生成，保持描述一致再剪辑。
- **模糊运动**：`moving` 不是运动描述，`drifting slowly left to right while rotating` 才是。
- **风格冲突**：`golden hour` + `studio lighting` 光源矛盾，选一个。
- **堆形容词**：`epic cinematic dramatic hyperdetailed` 不叠加，选 1–2 个精确词。

## 八、可复制模板（直接填方括号）

### 模板 A：通用视频 prompt
```
[Shot type + camera movement, speed]. [Subject: 外貌+服装].
[Action: 具体动词+物理细节]. [Setting: 前中后景+时间天气].
[Lighting: 光源方向+色温+质感]. [Style/grade: 媒介+调色+胶片颗粒].
[Duration], [aspect ratio].
```

### 模板 B：分镜序列（多镜头）
```
[STYLE] [类型/影调/调色/胶片质感]
[CHARACTERS] [谁/服装/道具/体态]
[LOCATION] [环境/天气]
[TIMELINE]
  [0:00–3] SHOT 1: [景别] [机位] [动作]
  [3–6]   SHOT 2: ...
[SFX] [音效]
[MUSIC] [音乐]
[QUALITY ANCHOR] [质量约束: 写实/重量感/无变形/无闪烁]
[NEGATIVE] [排除项]
```

### 模板 C：Veo 带音频
```
[Shot]. [Subject action]. [Environment]. [Lighting].
[Dialogue: "..."]. [Ambient sound: ...]. [Music style: ...].
[Style/grade]. [Duration], 16:9.
```

## 九、生产力建议

- 建自己的 prompt 库：按风格/主体类型/模型分类，复用已验证的 prompt，改主体而非从零写。
- 失败的 prompt 定位是哪一类模糊（通常是 angle/lens/lighting），从上面词表换一个精确词重跑。
- 10–20 次迭代后词汇会内化，prompt 反而越写越短——这才是目标：不是华丽，是精确。
