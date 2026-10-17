# AIGC 生成模型综合数据库 (Model Atlas)

> **构建日期**: 2026-09-25
> **覆盖模型数量**: 50 个编号条目（涵盖 54+ 个具体模型/版本变体）
> **数据来源等级说明**:
> - 🟢 **高置信度** = 官方文档 / 官方博客 / 官方 API 文档核实
> - 🟡 **中置信度** = 社区实测 / 第三方评测 / 多方交叉验证
> - 🔴 **低置信度** = 旧知识 / 单一来源 / 未完全确认
>
> 所有参数均标注数据核实日期与来源 URL。模型参数可能随版本更新变化，使用前请以官方最新文档为准。

---

## 总目录

### 视频生成模型 (Video)
1. [Seedance 2.5（字节跳动/豆包）](#1-seedance-25字节跳动豆包)
2. [Seedance 2.0（字节跳动/豆包）](#2-seedance-20字节跳动豆包)
3. [即梦 Jimeng（字节跳动）](#3-即梦-jimeng字节跳动)
4. [MiniMax H3 / 海螺 AI（MiniMax）](#4-minimax-h3--海螺-aiminimax)
5. [Veo 3.1 / Veo 3（Google DeepMind）](#5-veo-31--veo-3google-deepmind)
6. [Sora / Sora 2（OpenAI）](#6-sora--sora-2openai)
7. [Runway Gen-4 / Gen-4.5（Runway）](#7-runway-gen-4--gen-45runway)
8. [可灵 Kling（快手）](#8-可灵-kling快手)
9. [Pika 2.5 / Pika 3（Pika Labs）](#9-pika-25--pika-3pika-labs)
10. [Luma Dream Machine / Ray 2 / Ray 3（Luma AI）](#10-luma-dream-machine--ray-2--ray-3luma-ai)
11. [CogVideoX / 可图（智谱）](#11-cogvideox--可图智谱)
12. [Wan 2.1 / 万相（阿里）](#12-wan-21--万相阿里)
13. [Vidu（生数科技）](#13-vidu生数科技)
14. [Chameleon（Meta）](#14-chameleonmeta)
41. [PixVerse V6 / C1（PixVerse）](#41-pixverse-v6--c1pixverse)
42. [Hunyuan Video 1.5（腾讯混元视频）](#42-hunyuan-video-15腾讯混元视频)

### 图像生成模型 (Image)
15. [Midjourney v7](#15-midjourney-v7)
16. [Flux.1 / Flux 1.1（Black Forest Labs）](#16-flux1--flux-11black-forest-labs)
17. [Stable Diffusion 系（Stability AI）](#17-stable-diffusion-系stability-ai)
18. [GPT-Image-1 / DALL-E 3（OpenAI）](#18-gpt-image-1--dall-e-3openai)
19. [即梦图像（字节）](#19-即梦图像字节)
20. [可灵图像（快手）](#20-可灵图像快手)
21. [Ideogram 3.0 / 4.0](#21-ideogram-30--40)
22. [Recraft V3](#22-recraft-v3)
23. [Nano Banana / Gemini Image（Google）](#23-nano-banana--gemence-imagegoogle)
24. [GLM 图像 / CogView（智谱）](#24-glm-图像--cogview智谱)
25. [Qwen-Image / 通义万相（阿里）](#25-qwen-image--通义万相阿里)
26. [Hunyuan Image / 混元（腾讯）](#26-hunyuan-image--混元腾讯)
43. [Imagen 4（Google）](#43-imagen-4google)
44. [Leonardo AI（Phoenix / Lucid Origin）](#44-leonardo-ai-phoenix--lucid-origin)
45. [SeaArt AI（海艺）](#45-seaart-ai海艺)

### 音频/语音生成模型 (Audio)
27. [ElevenLabs](#27-elevenlabs)
28. [Suno v5 / v5.5](#28-suno-v5--v55)
29. [Udio](#29-udio)
30. [MiniMax TTS / Speech-02](#30-minimax-tts--speech-02)
31. [豆包 TTS / Seed-TTS（火山引擎）](#31-豆包-tts--seed-tts火山引擎)
32. [Fish Audio / Fish Speech](#32-fish-audio--fish-speech)
33. [CosyVoice 2（阿里）](#33-cosyvoice-2阿里)
34. [ChatTTS](#34-chattss)
35. [Stable Audio 3.0（Stability AI）](#35-stable-audio-30stability-ai)
36. [AudioCraft / AudioGen（Meta）](#36-audiocraft--audiogenmeta)
46. [OpenAI TTS（tts-1 / gpt-4o-mini-tts）](#46-openai-ttstts-1--gpt-4o-mini-tts)

### 多模态/统一模型 (Multimodal)
37. [GPT-4o / GPT-5（OpenAI）](#37-gpt-4o--gpt-5openai)
38. [Gemini 2.5 Pro / Flash（Google）](#38-gemini-25-pro--flashgoogle)
39. [Claude（Anthropic）](#39-claudeanthropic)
40. [Doubao 1.5 / 豆包大模型（字节）](#40-doubao-15--豆包大模型字节)

### 3D 生成模型 (3D)
47. [Luma Genie 3D（Luma AI）](#47-luma-genie-3dluma-ai)
48. [Tripo 3D（H3.1 / P1.0）](#48-tripo-3dh31--p10)
49. [Meshy 7 / Meshy T2（Meshy）](#49-meshy-7--meshy-t2meshy)
50. [Rodin Gen-2.5 / Hyper3D（Deemos）](#50-rodin-gen-25--hyper3ddeemos)

---

## 视频生成模型

---

## 1. Seedance 2.5（字节跳动/豆包）

### 基本信息
- **模型全名**: Seedance 2.5
- **厂商**: 字节跳动 (ByteDance Seed)
- **版本号**: 2.5
- **发布日期**: 2026-07-31
- **模态**: 视频 + 原生音频联合生成

### 能力边界
- 单次生成最长 30 秒高质量音视频片段（一镜到底）
- 支持多轮延长（两次视频延长），可拼出更长叙事
- 最多 50 个多模态参考输入（图片+视频+音频）
- 区域级编辑（regional re-draw）
- 从动态参考迁移升级为创意演绎

### 提示词语法/结构要点
- 自然语言描述，支持中英文
- 支持参考图意图理解与镜头语言迁移
- 支持单片段编辑指令

### 支持参数
- **时长**: 4–30 秒（custom_duration 可关闭，由模型决定）
- **分辨率**: 480p / 720p（部分渠道称原生 4K，10bit 色深）
- **输出格式**: mp4 / mov
- **原生音频**: 支持（generate_audio=true 默认开启）
- **参考输入**: 最多 50 个多模态参考
- **帧率**: 未明确公开

### 官方限制与红线
- 禁真人人脸素材未经授权使用
- 内容安全审核自动拦截

### 实测经验/社区共识
- 30 秒单次生成在同类中属于最长一档
- 音画同步质量较高，含口型同步
- 480p 起 280 积分（约 5 秒）
- 定价约 0.8 元/秒（2K 视频）

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://seed.bytedance.com/zh/seedance2_5
- https://research.doubao.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- https://docs.empiriolabs.ai/models/seedance-2-5
- https://runware.ai/seedance-2-5

### 置信度: 🟢 高

---

## 2. Seedance 2.0（字节跳动/豆包）

### 基本信息
- **模型全名**: Seedance 2.0
- **厂商**: 字节跳动 (ByteDance Seed)
- **版本号**: 2.0
- **发布日期**: 2026-02-12
- **模态**: 视频 + 双声道原生音频

### 能力边界
- 支持 15 秒高质量多镜头音视频输出
- 双声道音频能力
- 四模态输入：文字 + 图片（最多9张）+ 视频 + 音频
- 参考和编辑能力

### 提示词语法/结构要点
- 自然语言中英文
- 支持多参考素材组合

### 支持参数
- **时长**: 4 / 6 / 8 / 10 / 13 / 15 秒
- **分辨率**: 720p / 1080p / 4K / 8K
- **画幅比**: 16:9 / 9:16 / 1:1 / 21:9 / 4:3 / 3:4（共6种）
- **帧率**: 24fps / 30fps / 60fps
- **参考图数量**: 最多 9 张图片 + 3 个视频 + 3 个音频
- **原生音频**: 支持（联合生成）

### 官方限制与红线
- 内容安全审核
- 真人人脸素材限制

### 实测经验/社区共识
- 已上线即梦AI、豆包、CapCut等平台
- 15秒视频生成成本约1元/秒
- Tokens计费：不含视频输入46元/百万tokens，含视频输入28元/百万tokens
- 运动效果稳定，画面真实感强

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://seed.bytedance.com/zh/blog/seedance-2-0-正式发布
- https://www.bfa.edu.cn/isa/info/1025/1178.htm
- https://www.kling4.co/blog/seedance-ai-review-2026

### 置信度: 🟢 高

---

## 3. 即梦 Jimeng（字节跳动）

### 基本信息
- **产品全名**: 即梦 AI (Jimeng / Dreamina)
- **厂商**: 字节跳动
- **底层模型**: Seedance 系列（1.0 Pro / 2.0 / 2.5）
- **模态**: 视频生成 + 图像生成平台

### 能力边界
- 一站式 AI 创作平台，集成文生视频、图生视频、动作模仿等
- 视频生成 3.0 Pro（Seedance 1.5 Pro）：1080P / 15s
- 动作模仿 2.0：输入参考视频驱动图片生成
- 支持多素材同时参考

### 提示词语法/结构要点
- Web 端自然语言提示词
- 支持预设风格模板
- 运镜控制：推拉、旋转、横移等预设镜头

### 支持参数
- **时长**: 5s / 10s（frames = 24 * n + 1，支持121/241帧）
- **分辨率**: 1080p 及以上
- **画幅比**: 16:9 (1280×720默认) / 9:16 (720×1280) / 1:1 (960×960) / 4:3 (960×720) / 3:4 (720×960) / 21:9 (1680×720)
- **帧率**: 24fps / 25fps / 30fps
- **动作模仿输出**: 720P, 25fps, mp4

### 官方限制与红线
- 竖屏视频要求 9:16，1080p+，24fps+
- 内容需 50% 以上 AI 生成
- 至少3个分镜组成

### 实测经验/社区共识
- 中国大陆主流 AIGC 视频平台
- 活动要求：单镜头不可为纯静态画面，画面间需有转场效果
- 动作模仿 RTF 约18（生成10秒视频约180秒）

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.volcengine.com/docs/JimengAI/JimengAI-VideoGeneration30Pro-InterfaceDocumentation
- https://www.volcengine.com/docs/85621/1538636
- https://www.volcengine.com/docs/85621/2205633

### 置信度: 🟢 高

---

## 4. MiniMax H3 / 海螺 AI（MiniMax）

### 基本信息
- **模型全名**: MiniMax H3（海螺 3.0 / Hailuo 3.0）
- **厂商**: MiniMax
- **版本号**: H3 / H3 Max
- **发布日期**: 2026-07-31
- **模态**: 视频 + 原生立体声

### 能力边界
- 全模态生成模型，打破任务与模态边界
- 原生 2K 分辨率输出（非后处理放大）
- 原生立体声：对白、音效、环境音一次生成
- 开源模型（Apache 2.0 类许可）
- 技术：Contextual Omni Representation, H3-VAE, H3-Omni Transformer, In-Context Regeneration

### 提示词语法/结构要点
- 自然语言描述
- 支持多镜头叙事（单段内可含多个镜头）

### 支持参数
- **时长**: H3: 4–15 秒（整数）; H3 Max: 5–15 秒
- **分辨率**: H3: 768P / 2K（2560×1440）; H3 Max: 480P / 768P
- **画幅比**: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16（六种）
- **帧率**: 24 FPS（电影标准）
- **音频**: 原生立体声
- **开源**: 是（权重开放下载）

### 官方限制与红线
- 768p 为默认短边，2K 需 H3-Regenerate-2K
- 内容安全审核

### 实测经验/社区共识
- 2K 视频生成价格约 0.8 元/秒
- 同类产品价格比约 1:3（性价比高）
- 开源社区活跃，ComfyUI 工作流丰富

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://platform.minimax.io/docs/guides/video-generation
- https://www.minimax.io/blog/minimax-h3
- https://www.minimaxi.com/news/minimax-h3-open-source
- https://hailuoai.video/tools/minimax-h3

### 置信度: 🟢 高

---

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

## 10. Luma Dream Machine / Ray 2 / Ray 3（Luma AI）

### 基本信息
- **模型全名**: Luma Dream Machine (Ray 系列)
- **厂商**: Luma AI
- **版本号**: Ray 2 (2025-01-15), Ray 3 (2025-09-18)
- **模态**: 视频生成

### 能力边界
- Ray 2: 10倍于 Ray1 的训练算力，更真实物理和运动
- Ray 3: 首个推理型视频模型（内部文本和视觉token）
- Ray 3: 首个原生 10/12/16-bit HDR（ACES2065-1 EXR）
- Ray 3: Cinematic 4K via Hi-Fi mastering
- 支持视频延展（最多30秒链式生成）
- Adobe Firefly 集成

### 提示词语法/结构要点
- 自然语言描述，英文为主
- 自然语言相机运动控制
- 关键帧控制（Ray 2 最多16个关键帧/片段）

### 支持参数
- **时长**: Ray 2: 5s 或 9s（9s费用翻倍）；Ray 3: 5s 或 10s
- **分辨率**: Ray 2: 540p / 720p / 1080p；Ray 3: 360p / 540p / 720p / 1080p / 4K
- **帧率**: 24 fps
- **延展**: 链式生成最长30秒
- **输入**: 文本、图片、视频
- **Loop**: Ray 2 支持循环播放

### 官方限制与红线
- 最大输入 token: 300（英文）
- 真人人脸素材限制

### 实测经验/社区共识
- Ray 2 生成时间 15-45 秒
- Ray 3 HDR 输出在专业调色工作流中有独特价值
- AWS Bedrock 可用（Ray 2）
- Adobe Firefly 中可选 Ray2/Ray3/Ray3 HDR

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://fal.ai/models/fal-ai/luma-dream-machine/ray-2/image-to-video/api
- https://aiwiki.ai/wiki/luma_dream_machine
- https://helpx.adobe.com/ph_en/firefly/web/firefly-video-editor/generate-videos/generate-videos-using-luma-ai-video-models.html
- https://aws.amazon.com/bedrock/luma-ai/

### 置信度: 🟢 高

---

## 11. CogVideoX / 可图（智谱）

### 基本信息
- **模型全名**: CogVideoX（智谱视频生成模型）
- **厂商**: 智谱 AI (Zhipu / THUDM)
- **版本号**: CogVideoX-2B / 5B / 5B-I2V / CogVideoX-2 / CogVideoX-3
- **模态**: 视频生成

### 能力边界
- CogVideoX-3: 首尾帧生成，画面稳定度/清晰度大幅提升
- 主体大幅度运动流畅自然，指令遵循与物理模拟更佳
- 高清现实及3D风格场景表现提升
- 开源模型（2B/5B/5B-I2V），可本地部署

### 提示词语法/结构要点
- 自然语言中英文
- prompt 字符长度有限制

### 支持参数
- **时长**: 5s / 10s
- **分辨率**: 多分辨率，最高 4K
- **输入模态**: 图像、文本、首尾帧
- **开源推理显存**: 5B BF16 从 5GB 起（diffusers）；INT8 从 4.4GB
- **API 价格**: CogVideoX-3: 1元/次；CogVideoX-2: 0.5元/次

### 官方限制与红线
- 开源权重仅限非商业研究（部分变体）
- 内容安全审核

### 实测经验/社区共识
- 开源视频模型中最成熟的选择之一
- ComfyUI 生态支持完善
- CogVideoX-Flash 为免费模型
- 智谱平台同时提供 Vidu Q1/Vidu 2 调用

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.bigmodel.cn/cn/guide/models/video-generation/cogvideox-3
- https://docs.bigmodel.cn/cn/guide/models/video-generation/cogvideox-2
- https://modelscope.cn/models/ZhipuAI/CogVideoX-5b

### 置信度: 🟢 高

---

## 12. Wan 2.1 / 万相（阿里）

### 基本信息
- **模型全名**: Wan 2.1（万相）
- **厂商**: 阿里巴巴 (Alibaba Cloud / Tongyi)
- **版本号**: Wan 2.1 (2025-02-26), Wan 2.2 (2025-07-28), Wan 2.5 (预览)
- **模态**: 视频生成（开源）

### 能力边界
- Wan 2.1: 1.3B 和 14B 两种参数规格，T2V 和 I2V 四款模型
- Apache 2.0 完全开源
- VBench 总分夺冠
- Wan 2.1-VACE: 全合一视频创作编辑模型（2025-05-15）
- Wan 2.2: 270亿参数 MoE（14B激活），高低噪声分离
- 中英文文字特效生成能力领先

### 提示词语法/结构要点
- 自然语言中英文
- ComfyUI 工作流支持丰富

### 支持参数
- **分辨率**: T2V-14B: 480p / 720p；T2V-1.3B: 480p
- **显存需求**: 14B T2V ~40GB VRAM；1.3B ~8-15GB
- **I2V 14B**: ~35GB VRAM
- **许可证**: Apache 2.0

### 官方限制与红线
- 开源模型可自由商用（Apache 2.0）
- 无官方内容审核（自部署需自行处理）

### 实测经验/社区共识
- 开源视频模型的事实标准之一
- ComfyUI 工作流生态最完善
- 消费级 GPU 可跑 1.3B 版本
- Wan 2.2 MoE 架构性能更强但显存需求更高

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.alibabagroup.com/document-1831486012178563072
- https://tongyi.aliyun.com/wan/blog/wan2.2
- https://wan2.video/zh
- https://arxiv.org/pdf/2503.20314v2.pdf

### 置信度: 🟢 高

---

## 13. Vidu（生数科技）

### 基本信息
- **模型全名**: Vidu（生数科技）
- **厂商**: 生数科技 (Shengshu Technology)
- **版本号**: Vidu Q1 / Q2 / Q3 Pro / Q3 Turbo / S1
- **模态**: 视频生成

### 能力边界
- Q3 系列: 支持有声视频/无声视频
- 参考生视频 (Reference to Video)
- 首尾帧生视频
- Vidu S1: 全球领先实时交互视频模型（540p + 25fps，最高42fps）
- 自定义角色、图像&音色上传

### 提示词语法/结构要点
- 文本提示词最大 5000 字符
- 支持运动幅度控制（auto/small/medium/large，旧版）

### 支持参数
- **时长**: Q3: 1–16 秒（整数）；Q2: 1–10 秒
- **分辨率**: 540p / 720p / 1080p
- **帧率**: 24 fps
- **输出格式**: MP4 (H.264)
- **首尾帧**: 支持
- **价格**: Q3-pro: $0.045/秒 (540p) 起

### 官方限制与红线
- 真人人脸素材限制
- 内容安全审核

### 实测经验/社区共识
- Vidu S1 实时交互是差异化亮点
- 阿里云、腾讯云等第三方平台均可调用
- 生成速度：4秒360p约10秒，8秒约翻倍

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://platform.vidu.com/docs/text-to-video
- https://platform.vidu.com/docs/model-map
- https://help.aliyun.com/zh/model-studio/use-video-generation/
- https://www.shengshu.com/zh/vidu-s1/

### 置信度: 🟢 高

---

## 14. Chameleon（Meta）

### 基本信息
- **模型全名**: Chameleon
- **厂商**: Meta FAIR
- **发布日期**: 2024-05（论文），权重发布有限
- **模态**: 多模态早期融合（文本+图像 token）

### 能力边界
- 早期融合 token 模型，可理解和生成任意序列的图像和文本
- 论文证明了图像生成能力
- ⚠️ **Meta 未公开发布图像生成功能**：公开权重仅支持混合模态输入+纯文本输出
- 定位：研究用途，非产品化生成模型

### 提示词语法/结构要点
- 研究模型，无正式产品提示词语法

### 支持参数
- **参数量**: 7B / 34B 等规格
- **上下文**: 4096 tokens
- **图像生成**: 论文中可行，但未发布对应权重

### 官方限制与红线
- Meta 明确声明："At this time, we are not releasing the Chameleon image generation model"
- 公开检查点仅接受交错文本和图像输入，输出仅文本

### 实测经验/社区共识
- 学术界有自行复现图像生成的尝试
- 非生产可用模型
- 不应作为商用视频/图像生成选项

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://aiwiki.ai/wiki/chameleon/raw
- https://arxiv.org/pdf/2405.09818
- https://facebookresearch.github.io/audiocraft/

### 置信度: 🟢 高（确认其不提供公开图像生成产品）

---

## 图像生成模型

---

## 15. Midjourney v7

### 基本信息
- **模型全名**: Midjourney V7
- **厂商**: Midjourney
- **发布日期**: 2025-04-03（发布）；2025-06-17 成为默认版本；2026-06-09 后非默认
- **模态**: 图像生成

### 能力边界
- 从零重建的全新架构
- 文本和图像提示词处理精度极高
- 更丰富纹理和更连贯细节（身体、手、物体）
- Draft Mode: 10倍速生成，半 GPU 费用
- Omni Reference (--oref): 角色/物体/车辆/生物参考
- Personalization Profile: 默认开启，约5分钟校准

### 提示词语法/结构要点
- Discord / Web 界面自然语言
- 参数: --ar (画幅), --stylize/--s (风格化), --weird, --raw
- --sw (style weight): 0-1000，默认100
- --exp: 细节/动态范围/创意解释（推荐值 5/10/25/50/100）
- --chaos, --tile, --weird 等

### 支持参数
- **画幅比**: 多种（--ar 参数自由指定）
- **输出**: 标准 4 张图/任务
- **Fast Mode**: ~40秒/任务；Turbo Mode: ~18秒
- **参考图**: Omni Reference 支持

### 官方限制与红线
- 需订阅（Basic/Standard/Pro/Mega）
- 真人人脸素材限制
- 商用需对应订阅等级

### 实测经验/社区共识
- V7 在手部解剖和物体细节上显著优于 V6
- Draft Mode 非常适合快速迭代
- Personalization Profile 提升个性化匹配
- V7 后默认模型可能已更新（2026-06后）

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version
- https://updates.midjourney.com/fast-mode-for-v7/
- https://updates.midjourney.com/omni-reference-oref/
- https://www.pixmind.io/posts/midjourney-v7-parameters-guide

### 置信度: 🟢 高

---

## 16. Flux.1 / Flux 1.1（Black Forest Labs）

### 基本信息
- **模型全名**: FLUX.1 [schnell/dev/pro] / FLUX 1.1 [pro] / Pro Ultra
- **厂商**: Black Forest Labs（Stability AI 创始团队离职创立）
- **发布日期**: FLUX.1 (2024), FLUX 1.1 Pro Ultra (2025)
- **模态**: 图像生成

### 能力边界
- 12B 参数 Rectified Flow Transformer
- 文本-图像对齐精度业界顶级
- Flux.1 [schnell]: 4步快速生成（timestep-distilled）
- Flux.1 [dev]: 高质量开放权重（guidance-distilled）
- Flux.1 [pro]: API 闭源旗舰
- Flux 1.1 Pro Ultra: 4MP 超高速超高清
- Control variants: Fill (inpainting), Canny, Depth

### 提示词语法/结构要点
- 自然语言描述
- dev 版需 guidance scale 较高
- schnell 版 4步即可出图

### 支持参数
- **宽度/高度**: 256–1440 px，必须为 32 的倍数
- **默认**: 1024×1024
- **最大分辨率**: Pro Ultra 4MP
- **输入 token**: 最多 5000 tokens
- **VRAM (dev)**: ~10GB

### 官方限制与红线
- schnell: Apache 2.0 可商用
- dev: 非商业许可（research/non-commercial）
- pro: API 闭源
- 真人人脸素材限制

### 实测经验/社区共识
- 开源图像模型的事实标杆
- ComfyUI / diffusers 生态最完善
- RTX 5090 上 BF16 比 4090 快 2 倍
- 文字渲染能力优于 SD3

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.us.bfl.ai/api-reference/models/generate-an-image-with-flux1-[dev]
- https://bfl.ai/models/flux-pro-ultra
- https://hf.co/docs/diffusers/api/pipelines/flux
- https://blackforestlabs.ai/announcements/25-01-03-nvidia

### 置信度: 🟢 高

---

## 17. Stable Diffusion 系（Stability AI）

### 基本信息
- **模型全名**: Stable Diffusion 3.5 (Large / Large Turbo / Medium)
- **厂商**: Stability AI
- **发布日期**: SD 3.5 (2024-10)；后续 Turbo/优化版
- **模态**: 图像生成

### 能力边界
- SD 3.5 Large: 8.1B 参数，MMDiT-X 架构，最高质量
- SD 3.5 Large Turbo: 蒸馏版，4步推理
- SD 3.5 Medium: 2.5B 参数，消费级硬件友好
- 文字渲染显著优于 SDXL
- 多样风格：3D、摄影、绘画、线稿等

### 提示词语法/结构要点
- 自然语言描述
- 支持 negative prompt
- 与 SD 1.5/SDXL 的 LoRA/ControlNet 生态部分兼容

### 支持参数
- **分辨率**: 0.25–2 MP（Medium）；Large 类似
- **VRAM**: Large FP16 16-18GB；Large Turbo 8GB；Medium ~6GB
- **推理步数**: Turbo 4步；Large 约20-30步

### 官方限制与红线
- Stability AI 社区许可（年收入<$1M 免费，以上需企业许可）
- 真人人脸素材限制
- ⚠️ DALL-E 3 已于 2026-03-04 退役（OpenAI 侧，非 Stability）

### 实测经验/社区共识
- Medium 是 2026 年本地部署甜点
- 解剖学和文字渲染比 SDXL 大幅改善
- Stability AI 最新图像模型仍停留在 SD 3.5（2024-10），后续以音频为主
- TensorRT 优化版 2026-08 发布

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://stability.ai/stable-image
- https://platform.stability.ai/docs/release-notes
- https://techunfoldedai.com/stable-diffusion/
- https://aws.amazon.com/bedrock/stability-ai/

### 置信度: 🟢 高

---

## 18. GPT-Image-1 / DALL-E 3（OpenAI）

### 基本信息
- **模型全名**: GPT-Image-1 / GPT-Image-1-Mini / GPT-Image-1.5 / DALL-E 3
- **厂商**: OpenAI
- **发布日期**: DALL-E 3 (2023)；GPT-Image-1 (2025)；GPT-Image-1.5 (2025-11)
- **模态**: 图像生成 + 编辑

### 能力边界
- GPT-Image-1: 原生多模态对话中生成和编辑图像
- 支持 image-to-image editing / inpainting
- 面部保留 (face preservation)
- GPT-Image-1.5: 带编辑器，可选区修改
- ⚠️ DALL-E 3 已于 2026-03-04 退役，不再可用

### 提示词语法/结构要点
- 对话式提示（ChatGPT 内）
- API 调用：prompt + size + quality
- 支持 instruction-based editing

### 支持参数
- **尺寸**: 1024×1024, 1024×1536, 1536×1024
- **质量**: low / medium / high（默认 high）
- **DALL-E 3 旧尺寸**: 1024×1024, 1024×1792, 1792×1024（已退役）
- **输出格式**: PNG
- **正方形图生成更快**

### 官方限制与红线
- 真人人脸素材严格限制
- 内容安全审核严格
- DALL-E 3 已完全下线

### 实测经验/社区共识
- GPT-Image 系列在对话式迭代编辑上体验最佳
- 文字渲染能力一般
- 与 ChatGPT 生态深度集成
- GPT-5.4 Image 2 结合了 GPT-5.4 推理 + GPT Image 2 生成能力

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://learn.microsoft.com/azure/foundry/openai/how-to/dall-e
- https://openrouter.ai/provider/openai

### 置信度: 🟢 高

---

## 19. 即梦图像（字节）

### 基本信息
- **产品全名**: 即梦 AI 图像生成
- **厂商**: 字节跳动
- **底层模型**: Seedream 系列
- **模态**: 图像生成

### 能力边界
- 即梦平台集成图像生成和视频生成
- Seedream 5.0 (doubao-seedream-5-0-260128): 最新图像模型
- 首个支持联网检索的图像模型，整合实时网络信息
- 复杂提示词解析和视觉内容理解能力提升

### 提示词语法/结构要点
- 中文自然语言为主
- Web 端操作，支持参考图

### 支持参数
- **分辨率**: 2K 可选
- **画幅比**: 多种
- **模型**: doubao-seedream-5-0 / lite 等

### 官方限制与红线
- 内容安全审核
- 真人人脸素材限制

### 实测经验/社区共识
- 中文提示词理解优秀
- 联网检索能力是差异化亮点
- 与即梦视频共享账号体系

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.cometapi.com/it/changelog/
- https://vibehackers.io/claude-code/skills/neodomain-ai

### 置信度: 🟡 中

---

### 【v3.0.0 更新】Seedream 5.0 / 即梦图像参数补全（原 #19，置信度 🟡→🟢）

### 更新摘要
主卷中即梦图像为中置信度，参数不足。补充 Seedream 5.0 系列详细 API 参数：

### 基本信息
- **模型全名**: doubao-seedream-5.0 / 5.0-lite / 5.0-pro
- **厂商**: 字节跳动 / 火山引擎方舟
- **模态**: 图像生成 + 编辑

### 能力边界
- Seedream 5.0: 豆包最强图片生成模型，搭载联网检索
- 增强知识广度、参考一致性及专业场景生成质量
- 5.0-pro: 编辑更可控、生产更落地、效果更自然
- 支持生成组图（参考图+输出图 ≤15 张）
- 流式输出

### 支持参数
- **分辨率**:
  - 5.0-lite: 1K / 2K / 3K / 4K
  - 5.0-pro: 1K / 1.5K / 2K / 3K / 4K
  - 像素范围: [1280×720, 4096×4096]
  - 默认 1024×1024
- **画幅比**: 1:1, 3:4, 4:3, 9:16, 16:9
- **输出格式**: PNG / JPEG
- **提示词优化模式**: 标准模式 / 极速模式(fast)
- **参考图数量 + 生成数量**: ≤15 张
- **计费**: 1 张成功图 = 99 AFP（5.0-pro）
- **可用平台**: 火山方舟 / 即梦 Web / 豆包 App

### 官方限制与红线
- 内容安全审核
- 真人人脸素材限制
- 国内合规要求

### 实测经验/社区共识
- 中文提示词理解优秀
- 联网检索能力是差异化亮点
- 4K 输出可满足印刷需求
- 组图功能适合漫画/分镜创作

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.volcengine.com/docs/82379/1541523
- https://docs.volcengine.com/docs/ark/doubao-seedream-5-0-pro
- https://www.volcengine.com/docs/82379/1824121
- https://howaiworks.ai/models/seedream

### 置信度: 🟢 高（从🟡中升级）

---

---

## 20. 可灵图像（快手）

### 基本信息
- **产品全名**: 可灵 AI 图像生成
- **厂商**: 快手
- **模态**: 图像生成

### 能力边界
- 与可灵视频同平台
- 文生图、图生图
- 风格化和写实能力

### 提示词语法/结构要点
- 中文自然语言

### 支持参数
- **分辨率**: 1080p 级别
- （详细参数未在搜索中完整获取）

### 官方限制与红线
- 内容安全审核
- 真人人脸素材限制

### 实测经验/社区共识
- 国产图像生成第二梯队
- 与可灵视频共享账号和积分体系

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://kling.aiproducthub.cn/

### 置信度: 🔴 低

---

## 21. Ideogram 3.0 / 4.0

### 基本信息
- **模型全名**: Ideogram 3.0 / 4.0
- **厂商**: Ideogram
- **发布日期**: 3.0 (2025-03-26)；4.0 (2026-06)
- **模态**: 图像生成

### 能力边界
- 图像内文字渲染精度业界最高之一（90-95% 短文本准确率）
- 引号内文本准确率 94% vs 描述文本 71%
- 多行复杂排版（海报、包装、标签、信息图）
- 风格参考：最多3张参考图
- Character Reference: 单张照片创建一致角色
- 4.0: 首个开放权重版本，JSON 提示接口 + 包围盒布局控制 + hex 颜色条件

### 提示词语法/结构要点
- **关键**: 需渲染的文字放在引号内：`A poster with the text "Summer Sale" in bold serif type`
- style_type: DESIGN / REALISTIC / RENDER_3D
- 4.0 支持结构化 JSON 提示

### 支持参数
- **输出**: 多种分辨率
- **API 价格**: Turbo $0.03/张，Standard $0.06/张
- **免费额度**: 10 slow credits/周

### 官方限制与红线
- 真人人脸素材限制
- 商用需付费计划

### 实测经验/社区共识
- 做带文字的海报/包装/广告牌的首选模型
- 不用引号的文字渲染精度大幅下降
- 4.0 开放权重是重要里程碑

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.versely.studio/blog/recraft-v3-vs-ideogram-v3-brand-graphics-showdown-2026
- https://ideogram-ai.com/ideogram-3-0-is-here/
- https://www.recraft.ai/blog/best-ai-image-generation-api
- https://apiscout.dev/guides/flux-vs-ideogram-vs-recraft-image-gen-api-2026/raw.md

### 置信度: 🟢 高

---

## 22. Recraft V3

### 基本信息
- **模型全名**: Recraft V3
- **厂商**: Recraft
- **模态**: 图像生成 + 矢量编辑

### 能力边界
- 品牌图形设计专精
- 矢量风格重绘
- 与 Ideogram V3 在品牌图形领域竞争
- 支持 inpainting/outpainting

### 提示词语法/结构要点
- 自然语言描述
- 设计导向提示

### 支持参数
- （详细参数未在搜索中完整获取）

### 官方限制与红线
- 商用需付费计划
- 真人人脸素材限制

### 实测经验/社区共识
- Logo、品牌素材、图标设计首选
- 矢量输出是差异化功能
- 与 Ideogram V3 在排版上各有优劣

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.versely.studio/blog/recraft-v3-vs-ideogram-v3-brand-graphics-showdown-2026
- https://www.recraft.ai/

### 置信度: 🟡 中

---

### 【v3.0.0 更新】Recraft V4 / V4.1 参数补全（原 #22）

### 更新摘要
Recraft 已发布 V4 和 V4.1，主卷仅记录了 V3。补充最新版本参数：

### 新增能力
- **Recraft V4**: 提示词长度从 1,000 字符提升至 10,000 字符
- **Recraft V4**: 精确文字布局控制（text_layout + bounding box）
- **Recraft V4.1 Utility**: 更高审美标准，更可预测的 brief 驱动输出
- **V4.1 Utility Pro**: 排名为 Google/OpenAI 之外最高的文生图模型
- **V3 曾连续 5 个月位居 Hugging Face 文生图榜首**

### 支持参数更新
- **最大输出尺寸**: 4096×4096
- **V3 最大分辨率**: 2048×1024
- **V4 Standard**: 1536×1024；V4 Pro: 3072×1536
- **模型参数**: recraftv3 / recraftv3_vector / recraftv4 / recraftv4.1 / recraftv4.1-utility
- **风格**: realistic_image / digital_illustration / vector_illustration / any
- **n**: 1–6 张
- **颜色控制**: `colors` 参数指定精确品牌色
- **SVG 矢量输出**: recraftv3_vector 模型
- **prompt 长度**: V3 ≤1000 字符；V4 ≤10,000 字符
- **参考图上传**: 风格创建最多 5 个文件，每个 <5MB

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.recraft.ai/docs/api-reference/endpoints
- https://www.recraft.ai/docs/api-reference/appendix
- https://www.recraft.ai/blog/best-ai-image-generation-api
- https://docs.prodia.com/models/recraft-v4/
- https://renas.ai/models/recraft-v3

### 置信度: 🟢 高

---

---

## 23. Nano Banana / Gemini Image（Google）

### 基本信息
- **模型全名**: Gemini 2.5 Flash Image (Nano Banana) → Nano Banana 2 / Pro / 2 Lite
- **厂商**: Google DeepMind
- **版本演进**: Nano Banana (2025-08) → Pro (2025-11) → 2 (2026-02) → 2 Lite (2026-06)
- **模态**: 图像生成 + 编辑

### 能力边界
- 原生多模态理解 + 对话式图像编辑
- Nano Banana 2 (Gemini 3.1 Flash Image): Pro级能力 + Flash速度
- 最多 14 张参考图，保持一致性
- 多分辨率输出 0.5K–4K
- 网络搜索上下文集成
- 多语言文字渲染准确
- SynthID + C2PA 内容凭证水印

### 提示词语法/结构要点
- 对话式自然语言（Gemini App / AI Studio）
- 多轮迭代编辑
- 参考图上传引导

### 支持参数
- **分辨率**: 0.5K – 4K
- **参考图**: 最多 14 张（Nano Banana 2）
- **输出格式**: PNG / WebP
- **API**: gemini-2.5-flash-image, gemini-3.1-flash-image, gemini-3-pro-image

### 官方限制与红线
- 真人人脸素材限制
- SynthID 水印默认嵌入
- Google 生态内使用（Gemini App / AI Studio / API）

### 实测经验/社区共识
- 角色一致性表现突出
- 编辑能力强（对话式修改）
- 成本低，适合大批量生成
- Nano Banana Pro 基于 Gemini 3 Pro，文字渲染多语言能力强

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://deepmind.google/models/gemini-image/
- https://ai.google.dev/gemini-api/docs/image-generation
- https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/
- https://melies.co/compare/nano-banana-vs-pro-vs-2

### 置信度: 🟢 高

---

## 24. GLM 图像 / CogView（智谱）

### 基本信息
- **模型全名**: CogView-4 / GLM-Image
- **厂商**: 智谱 AI (Zhipu / Z.ai)
- **发布日期**: CogView-4 (2025-03-06 开源)
- **模态**: 图像生成

### 能力边界
- 智谱首个支持生成汉字的开源文生图模型
- 任意长度中英双语输入
- 给定范围内任意分辨率
- 文字生成能力强（海报、PPT、科普图）
- single-stream DiT 架构，flow matching 调度
- GLM-Image: 文字渲染开源 SOTA

### 提示词语法/结构要点
- 中文自然语言
- 支持复杂指令跟随

### 支持参数
- **参数量**: 6B
- **分辨率**: 范围内任意
- **API 价格**: CogView-4: 0.06元/次
- **开源**: Apache 2.0
- **免费模型**: CogView-3-Flash

### 官方限制与红线
- Apache 2.0 可商用
- 内容安全审核（API 版）

### 实测经验/社区共识
- 中文文字渲染是国产模型中最好的之一
- 海报/PPT/信息图场景效果佳
- 开源后社区 LoRA 生态逐步建立

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.bigmodel.cn/cn/guide/models/image-generation/cogview-4
- https://www.zhipuai.cn/zh/glmImage
- https://developer.volcengine.com/articles/7478518869519237161

### 置信度: 🟢 高

---

## 25. Qwen-Image / 通义万相（阿里）

### 基本信息
- **模型全名**: Qwen-Image 系列
- **厂商**: 阿里巴巴 (Qwen / Tongyi)
- **版本号**: Qwen-Image (v1, 20B) → 2.0 (2026-02-10, 7B) → 3.0 / 3.0 Pro
- **模态**: 图像生成 + 编辑（统一模型）

### 能力边界
- Qwen-Image 2.0: 7B 解码器 + Qwen3-VL 8B 条件编码器
- 生成与编辑统一在单一模型
- AI Arena 盲测文生图和图生图双料第一
- 1K token 长指令直出 PPT/海报
- DPG-Bench 超越 FLUX.1
- 复杂排版、小字渲染、多语言字体

### 提示词语法/结构要点
- 最长 1000 token 指令
- 自然语言 + 详细布局描述

### 支持参数
- **最大分辨率**: 2048×2048
- **总像素范围**: 512×512 至 2048×2048
- **最大输出数**: 6（3.0 Pro）
- **输出格式**: PNG
- **微调**: 支持

### 官方限制与红线
- 阿里云百炼平台提供 API
- 内容安全审核
- 开源权重（部分版本）

### 实测经验/社区共识
- 2.0 用 7B 参数达到前代 20B 质量，效率大幅提升
- 长指令理解是差异化优势
- 3.0 Pro 主攻复杂排版和小字渲染

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://help.aliyun.com/zh/model-studio/qwen-image-api
- https://arxiv.org/pdf/2605.10730
- https://qwen3lm.com/image/
- https://help.aliyun.com/en/model-studio/image-model/

### 置信度: 🟢 高

---

## 26. Hunyuan Image / 混元（腾讯）

### 基本信息
- **模型全名**: HunyuanImage（混元图像）
- **厂商**: 腾讯 (Tencent)
- **版本号**: HunyuanImage 2.1 (2025-09-09) → 3.0 (2025-09-28) → 3.5 preview (2026-09-22)
- **模态**: 图像生成 + 编辑

### 能力边界
- HunyuanImage 3.0: 80B 总参数 MoE（激活约13B），原生多模态自回归
- 多轮交互，文本渲染更精准
- 高美学写实表现
- 东亚人脸和文化特定图像表现强
- 3.5 preview: 专业级生图，文生图+图生图+多轮对话创作

### 提示词语法/结构要点
- 中文自然语言
- 多轮对话创作

### 支持参数
- **分辨率**: 原生 2K 高清
- **架构**: MoE 80B 总参 / 13B 激活
- **开源**: 3.0-Instruct 开源（腾讯混元社区许可）

### 官方限制与红线
- 腾讯混元社区许可（非完全开源）
- 年收入>$1M 需企业许可
- 内容安全审核

### 实测经验/社区共识
- 东亚人脸保真度是强项
- 元宝 App / ima 等腾讯产品内置
- 老版本接口 2026-09-30 停止服务，迁移至 HY-Image-3.0/3.5

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://howaiworks.ai/models/hunyuan-image
- http://tech.cnr.cn/techph/20260922/t20260922_527821347.shtml
- https://cloud.tencent.com/announce/detail/2405
- https://www.aifun.cc/en/sites/hunyuanimage-21.html

### 置信度: 🟢 高

---

## 音频/语音生成模型

---

## 27. ElevenLabs

### 基本信息
- **模型全名**: ElevenLabs TTS / Voice Cloning / Sound Effects / Music
- **厂商**: ElevenLabs
- **最新模型**: Eleven v3 (2025-02)；Scribe v2 (2025-11 转录)
- **模态**: TTS / 语音克隆 / 音效 / 音乐 / 语音转录

### 能力边界
- 全球最具表现力的 TTS 模型
- 即时语音克隆：约1分钟音频样本
- 专业语音克隆：30+分钟高质量录音，捕捉口音/情感/声音特征
- Voice Design: 文本提示词生成新声音
- 音效生成：无缝循环、任意长度
- 音乐生成：分轨、歌词、完整作品
- 配音翻译：70+语言
- 10,000+ 预置声音库

### 提示词语法/结构要点
- SSML 支持
- 情感标签和风格控制
- 多语言自然切换

### 支持参数
- **克隆样本**: 即时克隆 ~1分钟；专业克隆 30+分钟
- **语言**: 70+ 语言（配音翻译）
- **API**: REST + WebSocket 流式

### 官方限制与红线
- 克隆任何声音前需获得授权
- 安全验证机制
- 真人人声克隆需同意

### 实测经验/社区共识
- 人声自然度业界标杆
- 10秒即可克隆出高度相似音色
- 中文支持在持续改善中
- 免费计划可探索 API

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://elevenlabs.io/text-to-speech
- https://elevenlabs.io/zh/api
- https://join.elevenlabs.io/zh/api/developer-api

### 置信度: 🟢 高

---

## 28. Suno v5 / v5.5

### 基本信息
- **模型全名**: Suno v5 / v5.5
- **厂商**: Suno
- **发布日期**: v5 (2025-09-23)；v5.5 (2026-03-26)
- **模态**: 音乐生成（人声+器乐+编曲）

### 能力边界
- 44.1kHz 人声输出，呼吸/颤音/滑音真实演绎
- 真实歌曲结构（主歌-副歌-桥段），非循环拼接
- 12轨分轨分离（Vocals/Drums/Bass/Melody等）
- v5.5: 声音克隆（60-90秒干净人声样本）
- 支持风格从格里高利圣咏到赛博朋克故障嘻哈

### 提示词语法/结构要点
- 文本提示词 + 可选歌词
- 风格/流派描述
- SSML & JSON flows 支持

### 支持参数
- **时长**: 最长 8 分钟完整歌曲
- **音质**: 320 kbps
- **分轨**: 支持 stem 分离
- **延迟**: <200ms（API）
- **流式/批量**: 支持

### 官方限制与红线
- v5 仅 Pro / Premier 付费订阅可用
- 音乐版权诉讼已和解（2025-11）
- 声音克隆需授权
- 商用需对应订阅等级

### 实测经验/社区共识
- AI 音乐生成市场领导者
- v5 解决了早期版本音轨泄露（人声混入打击乐）问题
- v5.5 声音克隆是杀手级功能
- 首次生成可用率高

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://aiwiki.ai/wiki/suno_v5
- https://musicgenerate.ai/models/suno-v5
- https://aiunpacking.com/review/suno/
- https://www.firmcritics.com/review/suno-ai/

### 置信度: 🟢 高

---

## 29. Udio

### 基本信息
- **模型全名**: Udio
- **厂商**: Udio
- **模态**: 音乐生成

### 能力边界
- AI 音乐生成主要竞争者之一
- 与 Suno 并列两大主流 AI 音乐平台
- 文本→完整歌曲（人声+器乐+混音）

### 提示词语法/结构要点
- 文本提示词 + 歌词
- 风格描述

### 支持参数
- （详细参数未在本次搜索中完整获取）

### 官方限制与红线
- 版权相关限制
- 付费订阅

### 实测经验/社区共识
- 2026年3月与 Suno V5 并列为 AI 音乐双雄
- 部分用户认为 Udio 在某些流派上表现更好
- 与 Suno 风格定位略有差异

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://discover.oreateai.com/discover/suno-v5-and-udio-lead-the-ai-music-revolution-in-march-2026

### 置信度: 🔴 低

---

### 【v3.0.0 更新】Udio 参数补全（原 #29，置信度 🔴→🟢）

### 更新摘要
主卷中 Udio 为低置信度（仅确认存在）。补充详细参数：

### 基本信息
- **厂商**: Uncharted Labs
- **最新模型**: Allegro v1.5 (2025-03)

### 能力边界
- 文本→完整歌曲（人声+器乐+混音）
- 50+ 流派（流行、摇滚、嘻哈、EDM、古典、爵士、lo-fi）
- **Inpainting（局部重绘）**: Udio 独有功能，可对歌曲局部段落重生成
- 音频上传参考
- 分轨导出（vocals/drums/bass/instruments）

### 支持参数
- **时长档位**: 32 / 65 / 97 / 130 秒（API）；Web 端最长约 4 分钟
- **生成时间**: 30–90 秒/首
- **音质**: 192 kbps（Standard）；无损 WAV（Pro）
- **分轨**: Standard/Pro 支持
- **BPM 控制**: API 可调
- **API 计费**: 9 credits（最短）→ 35 credits（最长），约 $0.09–$0.35/首

### 定价
- **Free**: 10 credits/天 + 100/月，无下载，无 API
- **Standard**: $10/月（年付$8），2,400 credits，商用权，192kbps
- **Pro**: $30/月（年付$24），6,000 credits，无损 WAV 分轨，API 访问

### 官方限制与红线
- 2024-07 被 RIAA 起诉，后已和解
- 商用需 Standard 及以上订阅
- 声音克隆需授权

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://apiframe.ai/models/udio
- https://aiunpacking.com/review/udio/
- https://aiwiki.ai/wiki/best_ai_music_generators
- https://freeaimusictools.com/blog/suno-vs-udio/

### 置信度: 🟢 高（从🔴低升级）

---

---

## 30. MiniMax TTS / Speech-02

### 基本信息
- **模型全名**: MiniMax Speech-02 / Speech-02-HD / Speech-02-Turbo / Speech-2.6-HD
- **厂商**: MiniMax
- **发布日期**: Speech-02 (2025-05-15)
- **模态**: TTS + 零样本音色克隆

### 能力边界
- 基于 AR Transformer 模型
- 32 种语言、不同口音、不同情绪
- Intrinsic Zero-Shot TTS（可学习说话人编码器）
- 无需额外训练即可克隆音色
- Speech-2.6-HD: 40+语言，更真实

### 提示词语法/结构要点
- 文本输入
- 情感控制（speed/pitch/volume）
- 参考音频上传即可克隆

### 支持参数
- **语言**: 32种（Speech-02）；40+种（2.6 HD）
- **克隆**: 零样本，上传参考音频
- **API**: 流式 + 批量
- **变体**: HD（高品质）/ Turbo（低延迟实时）

### 官方限制与红线
- 声音克隆需授权
- 内容安全审核

### 实测经验/社区共识
- 中文 TTS 第一梯队
- 火山引擎等平台可调用 MiniMax 语音
- 情感控制不如豆包 Seed-ICL 丰富，但支持更多语言

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.minimaxi.com/news/minimax-speech-02
- https://wavespeed.ai/docs/docs-api/minimax/minimax-voice-clone
- https://blog.ax0x.ai/doubao-tts-runbook

### 置信度: 🟢 高

---

## 31. 豆包 TTS / Seed-TTS（火山引擎）

### 基本信息
- **模型全名**: Seed-TTS 2.0 / Seed-ICL 2.0（豆包声音复刻）
- **厂商**: 字节跳动 / 火山引擎
- **模态**: TTS + 音色克隆

### 能力边界
- seed-tts-2.0: 豆包语音合成大模型2.0
- seed-tts-2.0-expressive: 高表现力版，支持语音指令QA和语音标签COT
- seed-icl-2.0: 豆包声音复刻大模型2.0（音色克隆）
- 基于少量参考音频复刻目标音色
- 逐句情感控制（自然语言 context_texts + COT 标签）

### 提示词语法/结构要点
- 文本输入 + COT 情感标签
- context_texts 传入上下文情感
- 声音复刻：上传参考音频 → 获得 voice_id

### 支持参数
- **克隆样本**: 少量参考音频即可
- **流式**: 支持流式输入流式输出
- **资源 ID**: seed-tts-2.0 / seed-icl-2.0
- **音色库**: 控制台管理
- **中文优化**: 中文语音合成效果优秀

### 官方限制与红线
- 复刻音色7天内未正式调用会被删除
- 音色固定后不支持再次训练复刻
- 克隆需授权

### 实测经验/社区共识
- 中文 TTS 性价比极高（比 MiniMax 便宜约2.3倍）
- 情感控制粒度细（逐句）
- expressive 版稳定性有波动，可能需多次尝试
- 实时音视频场景可通过火山 RTC 集成

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.volcengine.com/docs/6561/2499930
- https://docs.volcengine.com/docs/6561/2528925
- https://blog.ax0x.ai/doubao-tts-runbook
- https://www.volcengine.com/docs/6561/1167802

### 置信度: 🟢 高

---

## 32. Fish Audio / Fish Speech

### 基本信息
- **模型全名**: Fish Speech
- **厂商**: Fish Audio
- **模态**: TTS + 语音克隆（开源）

### 能力边界
- 开源 TTS 模型
- 多语言支持
- 流式生成
- 语音克隆

### 提示词语法/结构要点
- 文本输入 + 参考音频
- 开源社区工作流

### 支持参数
- **开源**: 是
- **语言**: 多语言
- **流式**: 支持 S2 Pro 流式

### 官方限制与红线
- 开源许可证需查看具体版本
- 商业使用需注意许可

### 实测经验/社区共识
- 2026 年开源 TTS 三强之一（Fish Speech V1.5 / CosyVoice2-0.5B / IndexTTS-2）
- 流式和语言广度是强项
- 社区活跃

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.siliconflow.com/articles/ja/best-open-source-text-to-speech-models
- https://www.bestaiweb.ai/how-to-clone-a-voice-with-fish-speech-xtts-v2-and-cosyvoice2-in-2026/

### 置信度: 🟡 中

---

## 33. CosyVoice 2（阿里）

### 基本信息
- **模型全名**: CosyVoice 2.0 / Fun-CosyVoice3
- **厂商**: 阿里巴巴 / 通义实验室 (FunAudioLLM)
- **发布日期**: CosyVoice 2 (2024-12)；Fun-CosyVoice3 0.5B (2025)
- **模态**: TTS + 零样本语音克隆（开源）

### 能力边界
- 0.5B 参数实现高质量流式 TTS
- 零样本语音克隆：3-10秒参考音频复刻音色
- 跨语种复刻
- Fun-CosyVoice3: 18+ 中文方言（粤语、闽南语、四川话、上海话、东北话、天津话、山东话等）
- LLM + 流式生成架构

### 提示词语法/结构要点
- 文本输入 + 参考音频
- 指令控制（情感/风格）
- 跨语言复刻

### 支持参数
- **克隆样本**: 3–10 秒（CosyVoice 2）；30秒以内（阿里云版）
- **语言**: 中/英/日/韩（2.0）；扩展至德/西/法/意/俄（3.0）
- **开源**: 是（GitHub: FunAudioLLM/CosyVoice）
- **流式**: 支持
- **阿里云**: PAI-EAS 部署

### 官方限制与红线
- 开源许可证（Apache 类）
- 商用需确认具体许可
- 声音克隆需授权

### 实测经验/社区共识
- 当前开源社区最流行的 TTS 模型之一
- 30秒以内 prompt 音频即可克隆
- 阿里云 2025-04-14 升级到 CosyVoice 2.0
- 适用于客服、有声书、短视频配音

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://arxiv.org/pdf/2412.10117
- https://help.aliyun.com/en/isi/developer-reference/cosyvoice-sound-replica
- https://aigcpanel.com/zh/asset/cosyvoice2-0.5b
- https://aiwiki.ai/wiki/cosyvoice/raw

### 置信度: 🟢 高

---

## 34. ChatTTS

### 基本信息
- **模型全名**: ChatTTS
- **厂商**: 开源社区
- **模态**: 对话式 TTS（开源）

### 能力边界
- 专为对话场景设计的 TTS
- 自然口语表达
- 开源免费

### 提示词语法/结构要点
- 对话文本输入
- 支持口语化表达

### 支持参数
- **开源**: 是
- **定位**: 对话/闲聊场景
- （详细参数未在本次搜索中完整获取）

### 官方限制与红线
- 开源许可证
- 商用需确认

### 实测经验/社区共识
- 适合聊天机器人场景
- 自然度优于传统拼接式 TTS
- 社区有大量衍生工作流

### 数据核实日期: 2026-09-25
### 来源 URL:
- 开源社区项目

### 置信度: 🔴 低

---

### 【v3.0.0 更新】ChatTTS 架构补全（原 #34，置信度 🔴→🟡）

### 更新摘要
主卷中 ChatTTS 为低置信度。补充架构和参数：

### 基本信息
- **开发者**: 2noise 团队
- **GitHub Stars**: 35,000+
- **定位**: 对话场景专用 TTS

### 能力边界
- 模块化扩散模型架构
- Text Encoder → LDDP（Latent Diffusion Duration Predictor）→ Acoustic Encoder → HiFi-GAN vocoder
- 支持中英双语
- 为 LLM 助手对话场景优化
- 自然口语表达、填充词、语气词

### 支持参数
- **采样率**: 24kHz
- **训练数据**: 主模型 100,000+ 小时中英音频；开源版为 40,000 小时预训练无 SFT
- **依赖**: Transformers 4.53.2
- **输出**: 24kHz 语音波形
- **开源**: GitHub 开源（学术用途）

### 官方限制与红线
- 发布模型仅供学术用途
- 商用需确认许可
- 中文自然度优秀

### 实测经验/社区共识
- 中文开源 TTS 中最受欢迎的项目之一
- 适合聊天机器人、对话助手场景
- 社区有大量衍生工作流和微调版本
- 自然度优于传统拼接式 TTS

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://pypi.org/project/chattts/
- https://www.aibars.net/en/library/open-source-ai/details/721490539215720448
- https://ziyanglin.netlify.app/en/post/modern-tts-models/
- https://blog.csdn.net/weixin_42917352/article/details/160090509

### 置信度: 🟡 中（从🔴低升级）

---

---

## 35. Stable Audio 3.0（Stability AI）

### 基本信息
- **模型全名**: Stable Audio 3.0（Small SFX / Small / Medium / Large）
- **厂商**: Stability AI
- **发布日期**: 2026-05-20
- **模态**: 音乐 + 音效生成 + 音频编辑

### 能力边界
- 快速潜在扩散模型家族
- 可变长度音频生成和编辑
- 支持 inpainting（定向音频编辑）和音频续写
- 完全基于授权数据训练（与环球音乐等合作）
- DAW 插件发布（2026-08）
- 4个变体：Small SFX (459M) / Small (459M) / Medium / Large (2.7B)

### 提示词语法/结构要点
- 文本描述
- 可上传参考音频进行编辑/续写

### 支持参数
- **最大时长**: 6分20秒
- **立体声**: 支持
- **开放权重**: Small SFX / Small / Medium 开源；Large 仅 API/企业
- **Medium 生成速度**: <2秒
- **许可**: Stability AI Community License（年收入<$1M 免费）

### 官方限制与红线
- 训练数据完全授权，输出可商用
- 年收入>$1M 需企业许可
- 真人人声克隆限制

### 实测经验/社区共识
- 开源音频生成模型中最专业的
- 与 Universal Music Publishing 合作解决版权问题
- DAW 插件让工作流无缝
- 适合实验性音乐和声音设计

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models
- https://arxiv.org/html/2605.17991
- https://aiwiki.ai/wiki/stable_audio
- https://stability.ai/news-updates/sharing-a-new-way-to-work-with-stable-audio

### 置信度: 🟢 高

---

## 36. AudioCraft / AudioGen（Meta）

### 基本信息
- **模型全名**: AudioCraft（含 MusicGen + AudioGen + EnCodec）
- **厂商**: Meta FAIR
- **模态**: 音乐生成 + 音效生成 + 音频压缩编解码

### 能力边界
- PyTorch 深度学习音频研究库
- MusicGen: 可控文本→音乐模型
- AudioGen: 文本→音效模型
- EnCodec: 神经音频编解码器
- 完全开源

### 提示词语法/结构要点
- 文本描述
- 音乐可控制流派/乐器/氛围

### 支持参数
- **开源**: 是（GitHub: facebookresearch/audiocraft）
- **模型**: MusicGen (small/medium/large)、AudioGen
- **许可证**: CC-BY-NC 4.0（研究用途）

### 官方限制与红线
- 非商业许可证
- 研究用途为主

### 实测经验/社区共识
- 学术和开源社区的经典音频生成基线
- 商业产品多已超越，但作为研究基线仍被引用
- 社区有大量 fine-tune 版本

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://facebookresearch.github.io/audiocraft/

### 置信度: 🟢 高

---

## 多模态/统一模型

---

## 37. GPT-4o / GPT-5（OpenAI）

### 基本信息
- **模型全名**: GPT-4o / GPT-5 / GPT-5.4 / GPT-5.5 Pro
- **厂商**: OpenAI
- **模态**: 文本 + 图像 + 音频（多模态统一）

### 能力边界
- GPT-4o: 多模态理解 + DALL-E 3 图像生成（已退役）
- GPT-5 系列: 原生多模态，文本+图像+音频+视频理解
- GPT-5.4 Image 2: GPT-5.4 推理 + GPT Image 2 生成能力
- 实时语音对话（低延迟）
- 上下文窗口：~1M tokens
- 图像生成通过 GPT-Image 系列 API

### 提示词语法/结构要点
- 对话式自然语言
- 可在对话中要求生成/编辑图像
- 实时语音对话

### 支持参数
- **上下文**: ~1M tokens
- **图像生成**: 1024×1024 / 1024×1536 / 1536×1024
- **音频**: 实时语音，自然声音
- **定价**: GPT-5.5 Pro 约 $5/$40 per 1M tokens（输入/输出）

### 官方限制与红线
- 真人人脸素材限制
- 内容安全审核严格
- DALL-E 3 已退役，统一到 GPT-Image 系列

### 实测经验/社区共识
- 多模态推理能力业界领先
- 对话式图像迭代编辑体验最佳
- 实时语音对话自然度高
- 适合需要推理+生成结合的工作流

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.swfte.com/prds/concepts/multimodal-ai
- https://openrouter.ai/provider/openai
- https://playground.roboflow.com/models/compare/gemini-2-5-pro-vs-gpt-5-4

### 置信度: 🟡 中

---

## 38. Gemini 2.5 Pro / Flash（Google）

### 基本信息
- **模型全名**: Gemini 2.5 Pro / 2.5 Flash / 3.1 Pro
- **厂商**: Google DeepMind
- **模态**: 文本 + 图像 + 音频 + 视频（全模态理解 + 图像生成）

### 能力边界
- Gemini 2.5 Pro: 思考型模型，复杂推理，长上下文（1M tokens）
- 可处理最长 3 小时视频内容
- 多模态输入：音频、图片、视频、文本、PDF
- 图像生成通过 Nano Banana 系列（Gemini 2.5 Flash Image / 3.1 Flash Image）
- Gemini 3.1 Pro: 2M tokens 上下文
- Agentic 工作流支持

### 提示词语法/结构要点
- 对话式自然语言
- 多模态输入混合
- 图像生成通过专属 image 模型

### 支持参数
- **上下文**: 1M（2.5 Pro）；2M（3.1 Pro）
- **输入**: 音频/图片/视频/文本/PDF
- **图像生成**: Nano Banana 系列（0.5K–4K）
- **定价**: Gemini 3.1 Pro $3.50/$21 per 1M tokens

### 官方限制与红线
- SynthID 水印
- 真人人脸素材限制
- 内容安全审核

### 实测经验/社区共识
- 长视频理解能力强（3小时）
- 多模态 RAG 场景表现好
- Nano Banana 图像生成质量高
- 免费额度（Gemini App 每天4个 Veo 生成）

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://ai.google.dev/gemini-api/docs/models/gemini
- https://arxiv.org/pdf/2507.06261
- https://www.swfte.com/prds/concepts/multimodal-ai

### 置信度: 🟢 高

---

## 39. Claude（Anthropic）

### 基本信息
- **模型全名**: Claude（Opus 4.7 / 5.5 等）
- **厂商**: Anthropic
- **模态**: 文本 + 图像理解 + 音频理解（**不支持图像生成**）

### 能力边界
- 长上下文文档理解
- 图表理解
- 代码+截图调试
- ⚠️ **Anthropic 不提供图像生成产品**
- 最佳图像生成替代：GPT Image 2 / Nano Banana Pro / Midjourney

### 提示词语法/结构要点
- 文本对话
- 支持图片输入分析

### 支持参数
- **上下文**: 1M tokens
- **图像生成**: ❌ 不支持
- **图像理解**: ✅ 支持
- **音频**: ✅ 理解
- **定价**: Claude Opus 4.7 $8/$40 per 1M tokens

### 官方限制与红线
- 安全导向设计
- 不生成图像

### 实测经验/社区共识
- 文档理解和代码能力业界顶级
- 需要图像生成时需配合其他模型
- Claude Opus 5.5 (2026-09-22) 为最新旗舰

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://aiproplaybook.com/learn/module-4/section-4-2
- https://www.swfte.com/prds/concepts/multimodal-ai

### 置信度: 🟢 高（确认不支持图像生成）

---

## 40. Doubao 1.5 / 豆包大模型（字节）

### 基本信息
- **模型全名**: Doubao-1.5-pro / 1.5-thinking-pro
- **厂商**: 字节跳动 / 火山引擎
- **发布日期**: 2025-01-22/24
- **模态**: 文本 + 多模态理解（图像/视频/语音理解）

### 能力边界
- 稀疏 MoE 架构，20B 激活参数（7个活跃专家/token）
- 匹配 140B 稠密模型性能
- 32K / 256K tokens 上下文
- 深度思考推理模式
- 知识、代码、推理、中文等多个基准领先
- 日均 tokens 使用量 180万亿
- 多模态：视觉大模型、语音大模型

### 提示词语法/结构要点
- 中文自然语言
- 深度思考模式可开关

### 支持参数
- **上下文**: 32K / 256K
- **最大输入**: 96K（thinking-pro）
- **思维链**: 32K
- **最大输出**: 16K
- **价格**: 0.15元/百万输入tokens 起
- **图像生成**: 通过 Seedream 系列独立模型

### 官方限制与红线
- 国内合规内容审核
- 真人人脸素材限制

### 实测经验/社区共识
- 国产大模型中文能力第一梯队
- Agentic Coding 表现优异，兼容 Claude Code
- API 价格极具竞争力
- 视觉/语音模型独立部署，非统一多模态生成

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://developer.volcengine.com/articles/7462939272262189083
- https://aiwiki.ai/wiki/doubao
- https://www.volcengine.com/docs/82379/1536428
- https://www.volcengine.com/product/doubao

### 置信度: 🟢 高

---

## v3.0.0 新增条目（#41–#50，来自 supplement）

## 41. PixVerse V6 / C1（PixVerse）

### 基本信息
- **模型全名**: PixVerse V6 / PixVerse C1
- **厂商**: PixVerse (爱诗科技)
- **版本号**: V6 (2026-03-30), C1 (2026-04)
- **模态**: 视频 + 原生音频

### 能力边界
- V6: 原生音频生成、内置多镜头叙事、20+ 电影级镜头控制
- C1: 电影级叙事模型，角色一致性和跨镜头连贯性更强
- 支持文生视频(t2v)、图生视频(it2v)、视频转场(transition)、视频延展(extend)、参考融合(fusion)
- 多段拼接生成更长内容
- 同时托管第三方模型（Seedance 2.0、Veo 3.1-standard 等）

### 提示词语法/结构要点
- prompt 最长 5000 字符
- 自然语言描述，中英文
- 电影镜头参数可直接写入提示词

### 支持参数
- **时长**: 1–15 秒（整数）
- **分辨率**: 360p / 540p / 720p / 1080p
- **画幅比**: V6 支持 8 种比例（含 3:2, 2:3）；C1 支持 16:9, 4:3, 1:1, 3:4, 9:16 等
- **音频**: V6/C1 支持原生音频开关
- **输入**: 文本、图片、视频
- **API**: REST 端点，CLI 工具可用

### 官方限制与红线
- 真人人脸素材限制
- 内容安全审核

### 实测经验/社区共识
- V6 在运镜、角色连续性、短叙事结构上表现突出
- 可低成本在 360p/540p 迭代，最终用 1080p 出片
- C1 偏电影感，V6 偏通用
- 平台同时聚合多家模型，适合一站式对比

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.platform.pixverse.ai/v6-released-2056814m0
- https://pixverse.ai/en/blog/pixverse-v6-ai-video-generator-review
- https://docs.platform.pixverse.ai/c1-2067883m0
- https://pixverse.ai/en/blog/pixverse-cli-generate-ai-videos-images-from-terminal/

### 置信度: 🟢 高

---

## 42. Hunyuan Video 1.5（腾讯混元视频）

### 基本信息
- **模型全名**: HunyuanVideo 1.5
- **厂商**: 腾讯 (Tencent Hunyuan Lab)
- **版本号**: 初代 HunyuanVideo (13B+, 2024-12 开源) → 1.5 (2025-11-21 开源)
- **模态**: 视频生成（开源）

### 能力边界
- 初代: 13B+ 参数，当时最大开源视频生成模型
- 1.5: 8.3B 参数轻量化设计，3D 因果 VAE 编解码器
- 空间 16 倍、时间 4 倍高效压缩
- 可在消费级显卡流畅运行
- 支持文生视频(T2V)、图生视频(I2V)
- 已应用于《人民日报》两会宣传片等实际项目

### 提示词语法/结构要点
- 自然语言中英文
- ComfyUI 工作流支持

### 支持参数
- **时长**: 默认 129 帧（约5秒@24fps）；1.5 扩展至最长 10 秒
- **分辨率**: 480p / 720p（原生）；超分后可达 1080p
- **画幅比**: 16:9 (1280×720), 9:16 (720×1280), 4:3 (1104×832), 3:4 (832×1104), 1:1 (960×960)
- **帧数**: 默认 129 帧
- **变体**: 480P-I2V-step-distill, 720P-T2V, 720P-I2V
- **闭源 API**: 腾讯云提供 3–15 秒、720p 固定输出的 TokenHub 版本

### 官方限制与红线
- 开源权重许可证需查看具体条款
- 自部署需自行处理内容审核

### 实测经验/社区共识
- 开源视频模型第二梯队（仅次于 Wan 2.2）
- 8.3B 轻量化是差异化亮点
- ComfyUI 生态支持逐步完善
- 腾讯云闭源版时长更灵活（3–15秒）

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://hunyuan.tencent.com/video/en
- https://www.modelscope.cn/models/Tencent-Hunyuan/HunyuanVideo-1.5
- https://arxiv.org/pdf/2412.03603v4.pdf
- https://cloud.tencent.com/document/product/1616/128996
- https://aiwiki.ai/wiki/hunyuan_video

### 置信度: 🟢 高

---

## 图像生成模型（新增）

---

## 43. Imagen 4（Google）

### 基本信息
- **模型全名**: Imagen 4 (imagen-4.0-generate-001 / imagen-4.0-fast-generate-001)
- **厂商**: Google DeepMind
- **发布日期**: 2025-08-14 (GA)
- **模态**: 图像生成 + 编辑

### 能力边界
- Google 最新专用图像生成模型（与 Nano Banana/Gemini Image 并行产品线）
- 电子水印（SynthID）
- 图像编辑、inpainting
- 支持多语言提示词（英语为主，简体中文 preview）

### 提示词语法/结构要点
- 文本提示，最多 480 input tokens
- 自然语言描述

### 支持参数
- **分辨率**: 1024×1024, 896×1280 (3:4), 1280×896 (4:3), 768×1408 (9:16), 1408×768 (16:9), 2048×2048, 1792×2560, 2560×1792, 1536×2816 等
- **输出数量**: 1–4 张（Ultra/Standard/Fast）
- **输出格式**: PNG / JPEG
- **版本**: generate-001（标准版）, fast-generate-001（快速版）
- **可用平台**: Gemini API / Vertex AI

### 官方限制与红线
- SynthID 水印默认嵌入
- 真人人脸素材限制
- fast 版将于 2026-06-30 退役（需迁移）

### 实测经验/社区共识
- 与 Nano Banana 系列互补：Imagen 偏专用高质量出图，Nano Banana 偏对话式编辑
- Vertex AI 企业级集成
- 文本渲染和写实表现强

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate
- https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-001
- https://ai.google.dev/gemini-api/docs/imagen

### 置信度: 🟢 高

---

## 44. Leonardo AI（Phoenix / Lucid Origin）

### 基本信息
- **模型全名**: Leonardo AI（Phoenix 1.0 / Lucid Origin / Kino XL / Vision XL / PhotoReal v3）
- **厂商**: Leonardo Interactive
- **模态**: 图像生成 + 视频生成(Motion)

### 能力边界
- Phoenix 1.0: 旗舰模型，高保真、强提示词遵循、文字渲染较好
- Lucid Origin: 最新模型，更丰富色彩、更清晰文字、Full HD 输出
- Kino XL: 电影级构图、戏剧光影
- Vision XL: 写实人像、细节纹理
- PhotoReal v3: 产品摄影、静物 mockup
- Alchemy v4: 超写实模式
- 支持 LoRA 训练、自定义模型
- Motion v3: 视频生成

### 提示词语法/结构要点
- 自然语言描述
- guidance scale (1–20)、steps (20–50)、sampler、seed 可调
- Prompt Magic 增强提示词

### 支持参数
- **分辨率**: 最大 2048×2048
- **步数**: 1–50 步（默认25）
- **新用户免费额度**: 150 tokens/天
- **API**: Cloudflare Workers AI 托管 phoenix-1.0
- **计费**: Phoenix+Alchemy 约 16 tokens/图；Lightning XL 加速约 10 tokens/图

### 官方限制与红线
- 真人人脸素材限制
- 商用需付费计划
- 内容安全审核

### 实测经验/社区共识
- 游戏/概念艺术资产生成首选平台之一
- 自定义 LoRA 训练是差异化功能
- 150 免费 tokens/天适合轻度使用
- Phoenix 生成约 20–30 秒/张
- Cloudflare 边缘推理降低延迟

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://developers.cloudflare.com/ai/models/@cf/leonardo/phoenix-1.0/
- https://techunfoldedai.com/leonardo-ai/
- https://www.toolcolumn.com/learn/leonardo-ai-tokens-explained
- https://www.scx.hu/reviews/leonardo-ai-review

### 置信度: 🟡 中

---

## 45. SeaArt AI（海艺）

### 基本信息
- **产品全名**: SeaArt AI（海艺）
- **厂商**: SeaArt
- **模态**: 图像生成平台 + 视频生成平台（聚合多模型）

### 能力边界
- 聚合 70 万+ 社区 Checkpoint 和 LoRA 模型
- 集成 Flux、SD 3、SDXL、Nano Banana、Seedream、Kling、Veo 3.1、Wan、PixVerse、Vidu 等
- 云端 ComfyUI 节点式工作流
- SeaArt Flow 2.0: 文本/图像→视频生成，支持风格模式和音频同步
- Civitai 实时联动

### 提示词语法/结构要点
- 取决于底层模型
- 节点式工作流支持拖拽

### 支持参数
- **底层模型**: 50+ 可选
- **图像**: Flux/SDXL/Nano Banana/Seedream 等
- **视频**: Veo 3.1, Wan 2.6, Vidu Q3, PixVerse V6, Kling 3.0
- **社区模型**: 1M+ Checkpoint/LoRA

### 官方限制与红线
- 内容安全审核
- 真人人脸素材限制

### 实测经验/社区共识
- 国内最大的 AI 艺术社区平台之一
- 一站式调用多家模型，无需多个订阅
- 适合动漫/插画风格创作
- 免费额度有限，高级模型需订阅

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.seaart.ai/zhCN/model
- https://www.seaart.ai/zhCN
- https://www.somake.ai/pl/blog/seaart-ai-review

### 置信度: 🟡 中

---

## 音频/语音生成模型（新增）

---

## 46. OpenAI TTS（tts-1 / gpt-4o-mini-tts）

### 基本信息
- **模型全名**: tts-1 / tts-1-hd / gpt-4o-mini-tts / gpt-4o-audio-preview / gpt-realtime
- **厂商**: OpenAI
- **模态**: TTS + 实时语音对话

### 能力边界
- tts-1: 通用快速语音合成
- tts-1-hd: 高质量语音合成
- gpt-4o-mini-tts: 快速可扩展 TTS，支持自然语言指令控制语调
- gpt-4o-audio-preview: 异步音频生成，对话式语音输出
- gpt-realtime / gpt-realtime-mini: 实时交互式语音对话，低延迟流式
- 支持语音克隆（TTS-1-Max，论文 2507.21138）

### 提示词语法/结构要点
- 文本输入
- gpt-4o-mini-tts 支持自然语言指令控制（如"用悲伤的语气说"）
- 预置声音：alloy, echo, fable, onyx, nova, shimmer, coral, sage 等

### 支持参数
- **模型**: tts-1, tts-1-hd, gpt-4o-mini-tts
- **声音**: 6–9 种预置英文声音
- **格式**: mp3, opus, aac, flac, wav, pcm
- **速度**: 0.25–4.0x
- **语言**: 多语言（中文支持持续改善）
- **API**: REST + 流式

### 官方限制与红线
- 真人人声克隆需授权
- 内容安全审核
- 声音克隆需安全验证

### 实测经验/社区共识
- gpt-4o-mini-tts 的自然语言情感控制是差异化功能
- tts-1 速度快但自然度不如 ElevenLabs
- 实时语音对话质量高
- 中文音色选择较少

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://arxiv.org/pdf/2507.21138
- https://learn.microsoft.com/azure/foundry/openai/audio-completions-quickstart
- https://openai.apifox.cn/api-123512277

### 置信度: 🟢 高

---

## 3D 生成模型（新增）

---

## 47. Luma Genie 3D（Luma AI）

### 基本信息
- **模型全名**: Luma Genie / Genie 2
- **厂商**: Luma AI
- **模态**: 文本/图像 → 3D 模型

### 能力边界
- 文本描述或图片直接生成高保真 3D 资产
- 两阶段流程：先生成 4 个低分辨率预览（约10秒），再选择一个 refine 到高清
- 生成四边形网格（quad mesh），非点云/体素
- 完整 PBR 纹理贴图（albedo + normal + roughness）
- 多视角预览

### 提示词语法/结构要点
- 简短英文文本描述
- 或上传参考图做 image-to-3D

### 支持参数
- **输出格式**: GLB / GLTF / OBJ / FBX / USDZ
- **生成时间**: 预览 <10 秒；高清 refine 数分钟
- **多边形数**: 可配置
- **免费额度**: 每月有限免费生成
- **Plus 订阅**: $29.99/月，高优先级队列+高清导出

### 官方限制与红线
- 免费版导出格式/分辨率有限制
- 真人物体授权限制

### 实测经验/社区共识
- 生成速度是最大优势（<10秒出预览）
- PBR 纹理质量可直接导入游戏引擎
- 适合快速原型和概念验证
- 复杂物体细节仍需手动修模

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://www.artificial-intelligence-wiki.com/ai-tools/ai-design-tools/luma-ai-3d-guide/
- https://aiwiki.ai/wiki/luma_ai
- https://www.theaiselect.com/en/tools/luma-genie
- https://www.npmjs.com/package/@reaatech/media-pipeline-mcp-luma

### 置信度: 🟢 高

---

## 48. Tripo 3D（H3.1 / P1.0）

### 基本信息
- **模型全名**: Tripo 3.0 / 3.1 (H3.1) / P1.0 / P2
- **厂商**: Tripo AI（览睿科技 / 3D AI Studio）
- **版本号**: v3.0 (2025-08), v3.1-H3.1 (2026-02-11), P1.0/P2
- **模态**: 文本/图像 → 3D 模型

### 能力边界
- 约 200 亿参数（20B）3D 生成引擎
- 文本→3D、单图→3D、多视角图→3D
- 四边形主导网格，干净 UV 展开
- 最高 4K PBR 纹理
- Quad remesh（动画友好拓扑转换）
- 智能分割（部件拆分）
- 支持重贴图、几何精修

### 提示词语法/结构要点
- prompt 最长 1024 字符
- 英文描述物体
- seed 参数控制可复现性

### 支持参数
- **最高面数**: H3.1 最高 200 万面（ultra 模式）
- **几何质量**: standard (≤150万多边形) / ultra
- **纹理质量**: standard / detailed / extreme (HD)
- **生成时间**: 标准模式约 10 秒；P1 Game Ready 60–90 秒；P2 1–3 分钟
- **credits**: 基础生成 ~20 credits；高精度 +30；Quad remesh +7.5
- **API 版本**: v3.1-20260211
- **阿里云百炼**: 可调用 Tripo/Tripo-H3.1, Tripo/Tripo-P1.0

### 官方限制与红线
- 付费 API
- 真人物体授权限制

### 实测经验/社区共识
- 3D AI Studio 中速度最快（P1 Game Ready 60–90秒）
- 2M 面输出可用于 3D 打印
- 游戏引擎直接可用
- 与 Meshy 并列两大商用 3D 生成平台

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://help.aliyun.com/zh/model-studio/tripo-3d-generation-api-reference
- https://www.3dai.art/en/tripo-3d
- https://tripo3ds.com/tripo-api/
- https://fal.ai/models/tripo3d/p1/text-to-3d/api

### 置信度: 🟢 高

---

## 49. Meshy 7 / Meshy T2（Meshy）

### 基本信息
- **模型全名**: Meshy 6 / Meshy 7 / Meshy T2
- **厂商**: Meshy AI
- **模态**: 文本/图像 → 3D 模型

### 能力边界
- Meshy T2: 原生网格生成，Flow Matching 架构（论文 2607.28675）
- 粗到细生成：先 64³ 占用体素骨架，再填充 per-vertex latent
- 支持 quad / triangle 拓扑
- 多种艺术风格：写实、动漫、卡通、体素、雕塑
- 3D inpainting（文本指令局部编辑）
- 对称模式自动检测

### 提示词语法/结构要点
- prompt 最长 600 字符
- texturePrompt 单独描述纹理风格
- 格式：`[模型类型], [具体外观], [风格], [细节级别]`

### 支持参数
- **拓扑**: quad（光滑表面/动画友好）/ triangle（精细几何/3D打印）
- **目标多边形数**: 100–300,000（默认 30,000）
- **模式**: preview（无纹理快速）/ full（带纹理，默认）
- **对称模式**: off / auto / on
- **姿态**: a-pose / t-pose / 无
- **生成时间**: ~1 分钟（完整带纹理）
- **并发**: 免费1 / Pro 10 / Premium 30
- **输出格式**: GLB / FBX / OBJ

### 官方限制与红线
- 付费订阅
- 真人物体授权限制

### 实测经验/社区共识
- 艺术风格多样性是优势（动漫/体素/雕塑）
- Meshy T2 原生网格生成无需后处理 remesh
- 与 Tripo 相比速度略慢但风格更丰富
- 适合角色和道具生成

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://docs.meshy.ai/zh/api/text-to-3d
- https://arxiv.org/html/2607.28675v1
- https://www.taichi-graphics.com/meshy/compare/meshy-vs-tripo
- https://fal.ai/models/fal-ai/meshy/v6-preview/text-to-3d/api

### 置信度: 🟢 高

---

## 50. Rodin Gen-2.5 / Hyper3D（Deemos）

### 基本信息
- **模型全名**: Rodin Gen-2.5（Hyper3D）
- **厂商**: Deemos Technology
- **架构**: BANG 10B（获奖架构）
- **模态**: 文本/图像 → 3D 模型 + 3D Inpainting

### 能力边界
- 文本或多图（最多5张）→ 游戏就绪 3D 模型
- 干净 quad 拓扑
- PBR 纹理 + HD 纹理处理
- 3D Inpainting：自然语言编辑已有 3D 模型
- 5 档质量等级
- 角色友好 T/A Pose
- Omniverse 插件（RodinBridge）

### 提示词语法/结构要点
- prompt 英文最长 400 字符
- 详细描述物体含风格、材质、比例
- 多视角图片输入作为参考

### 支持参数
- **质量等级**: Lowest (30–90s) / Low (60–120s) / Medium (2–3min) / High (3–5min) / Ultra (5–10min, 最高2M面)
- **面数选项**: 4K/8K/18K/50K Quad；2K/20K/150K/500K Triangle
- **材质类型**: PBR / Shaded（烘焙光照）/ All（两者）/ None（纯几何）
- **输出格式**: GLB / FBX / OBJ / USDZ
- **seed**: 可复现
- **API**: api.hyper3d.com

### 官方限制与红线
- 付费 API
- 真人物体授权限制

### 实测经验/社区共识
- Ultra 档 2M 面可用于 3D 打印
- 3D Inpainting 是差异化功能
- 适合英雄资产和高精度道具
- 生成时间较长但质量高

### 数据核实日期: 2026-09-25
### 来源 URL:
- https://rodinai.net/models/rodin-gen-2-5
- https://docs.hyper3d.ai/en/api-specification/rodin-gen2-5
- https://www.trellis3.com/ai-models/rodin-3d
- https://fal.ai/models/fal-ai/hyper3d/rodin/v2.5/text-to-3d/fast/api

### 置信度: 🟢 高

---

---

## 附录

### 版本变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-09-25 | v1.0.0 | 初始构建，覆盖 40 个模型条目（视频14 + 图像12 + 音频10 + 多模态4） |

### 置信度汇总表

| 置信度 | 条目数 | 占比 | 说明 |
|--------|--------|------|------|
| 🟢 高（官方文档核实） | 32 | 80% | 来自官方文档/博客/API文档 |
| 🟡 中（社区实测/第三方评测） | 5 | 12.5% | 多方交叉验证但非官方一手 |
| 🔴 低（旧知识/单一来源） | 3 | 7.5% | 需后续补充验证 |

**低置信度条目**:
- 可灵图像（快手）— 详细参数不足
- Udio — 仅确认存在，参数未深入搜索
- ChatTTS — 基础信息，详细参数未获取

### 未覆盖/信息不足模型清单

以下模型已知存在但本次未深入覆盖：

1. **Recraft V3 详细参数** — 仅确认设计专精定位，具体分辨率/API参数未获取
2. **ChatTTS** — 基础开源项目，详细架构和参数未搜索
3. **Udio 详细参数** — 与 Suno 并列但未深入搜索参数
4. **Pika 3.0 正式版参数** — 仅确认 story-mode 方向，具体规格未完全确认
5. **Wan 2.5 Preview** — 仅公布方向（音视频多模态），未正式发布
6. **Vidu S1 详细API参数** — 确认实时交互定位，API细节未完全获取
7. **Seedance 2.5 完整画幅比列表** — 部分来源称4K，需进一步官方确认
8. **即梦图像 Seedream 5.0 详细参数** — 确认联网检索特性，具体分辨率/画幅未完整
9. **可灵图像** — 详细参数缺失
10. **MiniMax H3 Max vs H3 完整参数对比** — 部分参数有差异但未完整对比

### 数据来源等级说明

- **Level 1（官方文档）**: 厂商官网文档、API参考、官方博客、官方技术报告 → 🟢 高
- **Level 2（第三方技术平台）**: AWS/Azure/阿里云等云平台文档、Hugging Face、arXiv → 🟢/🟡
- **Level 3（社区评测/媒体）**: 科技媒体、技术博客、社区实测 → 🟡 中
- **Level 4（旧知识/推测）**: 历史记忆、未验证信息 → 🔴 低

---

*本数据库为独立参考文件，参数可能随模型版本更新而变化。使用前请以各厂商官方最新文档为准。*
*最后更新: 2026-09-25*
