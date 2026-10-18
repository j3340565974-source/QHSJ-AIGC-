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
