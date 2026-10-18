## 5. Veo 3.1 / Veo 3（Google DeepMind）

### 基本信息
- **模型全名**: Veo 3.1 / Veo 3
- **厂商**: Google DeepMind
- **版本号**: Veo 3 (2025-05-21), Veo 3.1 (2025-10-16)
- **模态**: 视频 + 原生音频

### 能力边界
- Veo 3: 首个原生音画同步的主流 AI 视频模型
- Veo 3.1: 更丰富音频、更强叙事控制、增强真实感
- "Ingredients to Video"：多参考图控制角色、物体、风格
- Flow 电影制作平台集成
- Gemini API / Vertex AI 可用

### 提示词语法/结构要点
- 详细场景描述 + 相机运动 + 光线氛围
- 支持多参考图引导风格和内容
- 对话和音效可通过提示词引导

### 支持参数
- **时长**: 4 / 6 / 8 秒（单段）；Veo 3.1 支持最长 148 秒（通过 Flow 延展）
- **分辨率**: 720p / 1080p / 4K
- **画幅比**: 16:9 或 9:16
- **帧率**: 未明确公开（电影级）
- **参考图**: 支持（Veo 3.1，referenceImages）
- **音频**: 原生生成（对话、环境音、音效）
- **输入**: 文本、图片、视频

### 官方限制与红线
- 参考图功能在 API 早期有不一致（文档说支持但 API 报不支持）
- 真人人脸素材限制

### 实测经验/社区共识
- Veo 3.1 在纹理真实感、输入保真度和音频质量上比 Veo 3 提升
- Gemini 中每天免费生成 4 个
- Flow 中可编辑视频：延长片段、拼接场景
- 生成速度约 1 分钟+
- 唇形同步质量高

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://deepmind.google/models/veo/
- https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- https://ai.google.dev/gemini-api/docs/veo
- https://blog.google/innovation-and-ai/products/veo-updates-flow/

### 置信度: 🟢 高

---

## 6. Sora / Sora 2（OpenAI）

### 基本信息
- **模型全名**: Sora / Sora 2
- **厂商**: OpenAI
- **版本号**: Sora (初代), Sora 2 (2025-09-30)
- **模态**: 视频 + 同步音频

### 能力边界
- Sora 2: 物理精度更高、更真实、更可控
- 同步对话和音效
- 可完成奥运体操、浮力滑板后空翻、三周半跳等极难物理动作
- 文本→视频、图片→视频、视频→视频（生成后编辑）

### 提示词语法/结构要点
- 自然语言详细描述
- 支持相机参数模拟（180°快门、大画幅传感器模拟）

### 支持参数
- **时长**: 1–20 秒（Sora 2）
- **分辨率**: 720p / 1080p / 4K
- **音频**: 支持（同步对话+音效）
- **变体**: 720p 最多可生成 2 个变体，1080p 不支持多变体

### 官方限制与红线
- ⚠️ **重要变更**: Sora 产品已于 2026-04-26 停止面向消费者服务
- Sora 2 通过 Azure OpenAI (Foundry) 预览可用
- 真人人脸素材严格限制

### 实测经验/社区共识
- Sora 2 在物理模拟上显著优于初代
- 4K 输出质量高，但生成时间较长
- 消费者端 Sora App 已下线，企业端通过 Azure 提供

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://openai.com/index/sora/
- https://learn.microsoft.com/azure/foundry/openai/concepts/video-generation
- OpenAI Sora 2 System Card

### 置信度: 🟢 高

---

## 7. Runway Gen-4 / Gen-4.5（Runway）

### 基本信息
- **模型全名**: Runway Gen-4 / Gen-4.5 / Gen-4 Turbo
- **厂商**: Runway ML
- **版本号**: Gen-4 (2025-03), Gen-4.5 (2025-12)
- **模态**: 视频生成

### 能力边界
- Gen-4: 角色/场景/物体跨镜头一致性（单张参考图即可）
- Motion Brush: 在画面特定区域"画"运动方向（独家功能）
- Director Mode: 节点式相机控制（zoom/pan/tracking/俯仰）
- Gen-4.5: 视觉编程接口（Node Graph），解耦式潜在控制
- 保持 Video Arena Elo 排行榜前列

### 提示词语法/结构要点
- 自然语言 + Motion Brush 区域控制
- Director Mode 相机路径关键帧
- 参考图设定 look and feel

### 支持参数
- **时长**: 最长 10 秒
- **分辨率**: 720p（基础），最高 4K（Gen-4）
- **画幅比**: 16:9, 9:16, 4:3, 1:1, 3:4, 21:9
- **帧率**: 24 fps
- **输入**: 文本、图片
- **Turbo 模式**: ~30秒生成10秒视频

### 官方限制与红线
- 真人人脸素材需授权
- Motion Brush 为 Runway 核心差异化功能

### 实测经验/社区共识
- Motion Brush 3.0 是竞品难以匹配的独家能力
- 角色一致性是 Gen-4 最大卖点
- 专业影视制作首选工具之一
- Gen-4.5 在物理真实感、运动连贯性、提示词遵循上提升

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://runway.com/research/introducing-runway-gen-4
- https://dev.runwayml.com/
- https://chatforest.com/reviews/runway-gen4-gen45-ai-video-world-consistency-character-reference/

### 置信度: 🟢 高

---

## 8. 可灵 Kling（快手）

### 基本信息
- **模型全名**: Kling Video（可灵）
- **厂商**: 快手 (Kuaishou)
- **版本号**: 2.0 / 2.1 / 2.5 / 2.6 / 3.0
- **模态**: 视频生成（含原生音频）

### 能力边界
- Kling 2.0 (2025-04-15): 多模态视觉语言(MVL)框架，多模态视频编辑
- Kling 2.1 (2025-05-26): Standard/Professional/Master 三档，角色一致性提升，首尾帧关键帧
- Kling 2.6 (2025-12-03): 原生音频生成（英语优先），48fps
- Kling 3.0 (2026-02-05): 原生4K，60fps，15秒，多语言音频

### 提示词语法/结构要点
- 自然语言中英文
- 运镜控制：推拉、旋转、横移，Web端支持自定义方位角/俯仰角
- 风格模板内置多种艺术风格

### 支持参数（以最新 Kling 3.0 为准）
- **时长**: 5 / 10 秒（2.x系列）；15秒（3.0）
- **分辨率**: 720p / 1080p（2.x）；原生 4K（3.0）
- **画幅比**: 16:9, 9:16, 1:1
- **帧率**: 24fps（2.x）；48fps（2.6）；60fps（3.0）
- **首尾帧**: 支持
- **音频**: Kling 2.6+ 支持原生音频

### 官方限制与红线
- 免费版默认 720P，会员解锁 1080P
- "高表现"生成模式每日有限次
- 真人人脸素材限制

### 实测经验/社区共识
- 国产视频生成第一梯队
- 内部测试 Kling 2.0 vs Veo 2 胜率 182%
- API 成熟，腾讯云等第三方平台可调用
- 3.0 系列时长上限 15 秒，30-60fps

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://app.klingai.com/cn/dev/document-api/apiReference/model/videoModels
- https://aiwiki.ai/wiki/kling
- https://lorphic.com/what-is-kling-ai-full-guide/
- https://cloud.tencent.com/document/product/1823/135742

### 置信度: 🟢 高

---

## 9. Pika 2.5 / Pika 3（Pika Labs）

### 基本信息
- **模型全名**: Pika（Pika 2.5 / Pika 3.0）
- **厂商**: Pika Labs
- **版本号**: 2.2 → 2.5 → 3.0
- **模态**: 视频生成

### 能力边界
- Pika 2.5: 更清晰视觉、更平滑相机运动、场景延展至25秒
- Lip Sync: 从图片+音频生成说话人脸视频（VTuber/虚拟主播）
- Pikaswaps: 文本指令替换视频中任意物体
- Pikadditions: 在场景中插入新角色/道具/特效
- Pika 3.0: Story-mode 生成，输入脚本/系列提示词输出多场景一致角色视频
- PikaStream 1.0: 实时流式视频（24fps, 1.5s延迟, 9B DiT参数）

### 提示词语法/结构要点
- 自然语言描述
- 支持 Motion Intensity (1-4)、Guidance Scale (8-24)、Negative Prompt
- FPS 可调（默认24）

### 支持参数
- **时长**: 单段约 10s；Pikaframes 关键帧可延展至 25s
- **分辨率**: 1080p
- **画幅比**: 7种比例
- **帧率**: 24 FPS（可调）
- **输入**: 文本、图片、视频

### 官方限制与红线
- 真人人脸素材限制
- 内容安全审核

### 实测经验/社区共识
- Pika 2.5 被公认为"迄今最佳"通用模型，物理更稳定、变形更少
- Pika 3.0 主打 Story-mode，直接对标 Runway Gen-4
- API 提供 Pika 2.5 等工具 REST 端点
- 生成时间约60秒

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://pikaslabs.com/pika-2.5/
- https://pikaslabs.com/api/
- https://resource.digen.ai/runway-ml-vs-pika-labs-2026-comparison/
- https://pikaslabs.com/pikastream/

### 置信度: 🟡 中

---
