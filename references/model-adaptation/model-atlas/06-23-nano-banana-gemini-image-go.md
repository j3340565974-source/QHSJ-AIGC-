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
