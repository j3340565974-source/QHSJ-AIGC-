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
