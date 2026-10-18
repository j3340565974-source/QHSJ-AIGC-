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
