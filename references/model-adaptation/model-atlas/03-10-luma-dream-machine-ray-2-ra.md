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
