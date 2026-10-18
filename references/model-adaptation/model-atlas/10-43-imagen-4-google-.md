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
