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
