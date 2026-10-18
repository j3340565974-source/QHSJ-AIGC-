# QHSJ 提示词模板金库（国内外工业模板合并）

> **QHSJ V3.0.0 全网增量知识库 · 合并件**
> **数据日期**：2026-09-25
> **置信度**：高：官方文档 + 开源 skill + 多份 2026 从业者指南交叉验证
> **合并说明**：本文件整合国内外同类知识库，保留各自有价值的速查表，按来源分区；URL 与置信度见各分区来源块。
> **贡献来源**：
>   - 国内：cn-prompt-templates（Seedance/Sora2/GPT-Image2 工业模板）
>   - 国外：en-prompt-format-templates（六段/五段/七参数/Veo 公式）

---

## 国内来源

> **来源 URL**：
> - https://seadance.io/zh/guide （Seedance 2.5 官方提示词指南）
> - https://agskills.dev/songguoxs/seedance-prompt-skill/seedance （GitHub: songguoxs/seedance-prompt-skill，1.7k star）
> - https://blog.csdn.net/yuntongliangda/article/details/154990144 （Sora2 导演级提示词框架）
> - https://github.com/freestylefly/awesome-gpt-image-2 （GPT-Image2 工业提示词引擎）
> - 抖音 @AI漫剧教程系列（7611257003109915257 / 7648639938480721178 / 7677906745897858536）
>
> **数据日期**：2026-09-25
> **置信度**：高（官方文档 + 1.7k star 开源 skill + 一线创作者实测技巧）
> **基座去重说明**：本文件聚焦"工业级可粘贴模板 + 平台语法细节"，与基座 `../09-prompt-engineering.md` / `../23-prompt-operator-engineering.md` / `../../model-adaptation/qh-seedance-render-engine.md` 互补，不重复叙事原则。

## 1. Seedance 2.5 基础提示词公式（官方）

### 1.1 六段式骨架
```
[主体] + [运动] + [环境] + [美学] + [镜头] + [音频]
```
- **主体**（必填）：谁 + 做什么动作。逻辑基础。
- **运动**（必填）：动作的时间链条。"谁在做什么"必须落到具体动词。
- **环境**（可选）：空间背景、灯光细节、视觉风格，奠定基调。
- **美学**（可选）：风格流派、色彩倾向、质感。
- **镜头**（可选）：运镜编排、景别切换。
- **音频**（可选）：环境音、旁白、配乐。

### 1.2 民间六步法（即梦创作者实测，比官方更"反翻车"）
1. **锁基础参数**：先写时长、比例、分辨率、画质，避免 AI 跑偏。
2. **加画质+稳定词**（放最前面）：`最高画质，细节丰富，锐度清晰，色彩自然，面部五官清晰稳定不变形，眼睛嘴型不扭曲，人体结构正常比例自然，画面流畅不抖，无闪烁卡顿，人物比例正常`。
3. **写主体与动作链**：用陈述句，禁用比喻/拟人/反问。
4. **加光影氛围**：`水面反光，明暗对比强烈` 这类可落视觉的词。
5. **写镜头指令**：别写"动一下"，写 `缓慢推进，中景视角，轻微手持感，镜头始终跟随人物`。
6. **结尾加稳定约束**：`画面流畅不抖，人脸清晰不变形，无闪烁卡顿，人物比例正常`。

### 1.3 字数与权重纪律
- 提示词总字数控制在 **100 字内**（单次生成），过长会被 AI 截断忽略。
- 权重词单次不超过 **5 个**，数值控制在 **1.0–1.5**，防止画面异常。
- 负面词精简 **3–5 个**核心问题，拒绝堆砌无效否定词。
- 全程用**陈述句**，禁用反问、比喻、拟人等修辞。

---

## 2. @ 多模态参考语法（Seedance 2.0/2.5）

平台硬规格：
- 图片：jpeg/png/webp/bmp/tiff/gif，最多 **9 张**，每张 <30MB
- 视频：mp4/mov，最多 **3 段**，总长 2–15s，每段 <50MB，480p–720p
- 音频：mp3/wav，最多 **3 个**，总长 ≤15s，每个 <15MB
- 文件总数上限 **12 个**（图+视频+音频合计）
- 单段生成时长 4–15 秒，输出最高 2K
- **红线**：禁止上传含真实人脸的图片/视频，会被自动拦截。

### 2.1 引用模板
```
参考/提取/组合 + [@ImageN] 的 [主体]，生成 [场景描述]，并保持 [主体] 特征一致。
```
- `@Image1`–`@Image9`：角色参考、场景背景、首帧/尾帧控制
- `@Video1`–`@Video3`：运镜参考、动作参考、节奏参考
- `@Audio1`–`@Audio3`：BGM、音色、音效参考

### 2.2 一镜到底多图接力模板
```
@图片1作为首帧画面，镜头正面跟拍穿着红风衣的女特工向前走，镜头全景跟随，
不断有路人遮挡红衣女子，走到一个拐角处，参考@图片2的拐角建筑，
固定镜头红衣女子离开画面……一个戴面具的女孩在拐角处躲着，形象参考@图片3。
镜头往前摇向红衣女特工，她走进一座豪宅消失不见，豪宅参考@图片4。
全程不要切镜头，一镜到底。
```

---

## 3. 时间戳分镜（Timestamp Storyboarding）— 15 秒长片控制法

### 3.1 标准写法
```
0-3s：[画面/动作/台词/音效]
4-8s：[画面/动作/台词/音效]
9-12s：[画面/动作/台词/音效]
13-15s：[画面/动作/台词/音效]
```

### 3.2 实战范例：仙侠高燃战斗（15s，横屏）
```
15秒仙侠高燃战斗镜头，金红暖色调，
0-3秒：低角度特写主角蓝袍衣摆被热浪吹得猎猎飘动，双手紧握雷纹巨剑，
       剑刃赤红电光持续爆闪，地面熔岩翻涌冒泡，远处魔兵嘶吼着冲锋逼近，
       主角低喝"今日，便以这柄剑，镇尔等邪祟！"，伴随剑鸣与熔岩咕嘟声；
4-8秒：环绕摇镜快切，主角旋身挥剑，剑刃撕裂空气迸射红色冲击波，
       前排魔兵被击飞碎裂成灰烬，伴随剑气破空声与魔兵惨嚎；
9-12秒：仰拍拉远定格慢放，主角跃起腾空，剑刃凝聚巨型雷光电弧劈向魔兵群；
13-15秒：缓推特写主角落地收剑的姿态，衣摆余波微动，冷声道"此界之门，不容踏越"，
       音效收束为余音震颤与渐弱风声。
```

### 3.3 超长视频（>15s）多段拼接法
- 总时长拆成 N 段，每段 15s。
- 第 1 段正常生成；第 2 段起，把上一段成片作为 `@视频1` 上传，提示词写 `将@视频1延长15秒。0-5秒：接上段……`。
- **衔接点必须显式写**："本段结尾画面：剑修正面持剑站在山巅，目光前视，远方魔气翻涌。" —— 这段描述就是下一段的起点锚。

---

## 4. 短剧/对话场景提示词模板

### 4.1 霸总反杀名场面（15s）
```
画面（0-5秒）：特写女主撕契约镜头，纸屑飘落，总裁单膝跪地伸手阻拦，
眼神慌乱，女主侧身躲开，嘴角挂着冷漠笑意。
台词1（总裁，卑微慌乱）："苏晚！契约还没结束，你不能走！我给你钱，给你地位！"
画面（6-10秒）：女主抬脚避开他的手，将撕碎的契约纸扔在他脸上，
镜头扫过周围宾客的窃窃私语。
台词2（女主，冷漠反杀）："契约？顾总，当初是你说，我连给你提鞋都不配，现在求我？晚了！"
画面（11-15秒）：总裁僵在原地，脸上沾着纸屑，女主转身昂首离开，红裙裙摆飘动。
音效：华丽又带张力的背景音，契约撕碎的声响，宾客轻微的窃窃私语声。
```

### 4.2 情绪描写纪律（Seedance 2.5 实测）
- ❌ 不要写"凶狠""冷静"这类抽象情绪词，AI 读不懂。
- ✅ 用动作演绎：`锦衣卫率先快步冲锋抽出剑向前突袭，刺客灵巧地闪避、顺势挥剑反击`。
- **情绪在视频生成里靠动作烘托，不靠形容词概括。**

---

## 5. 视频内文字三模板

### 5.1 口号/标题文字
```
[文字内容] + [出现时机] + [位置] + [出现方式]，[文字样式（颜色、字体）]
```
例：`随后画面逐渐虚化，屏幕中央出现文字"Joy is in Seedance"。`

### 5.2 字幕
```
字幕出现在画面底部，内容为"..."，并与音频节奏同步。
```
例：`低沉平静的男声说："..."。字幕跟随旁白出现在画面底部。`

### 5.3 对话气泡
```
[角色] 说："..."，对话气泡出现在角色周围并显示对应台词。
```

> 文字纪律：尽量用常见字符，避免生僻字/特殊符号；严格指定拼写，否则 AI 会错字。

---

## 6. GPT-Image2 图像提示词模板选择规则

### 6.1 匹配优先级
1. **产品类型** → 模板类目（product / poster / UI / infographic / brand / photo / character / scene / document）
2. **视觉词** → 风格标签（realistic / 3D / illustration / classical / brand / poster / UI）
3. **场景词** → 场景标签（commerce / education / social / food / travel / story / history / tech / creative）
4. 模糊请求 → 给 2–3 个方向让用户选，不要直接开写。

### 6.2 最终 Prompt 六块结构
```
[主体与任务] + [构图与版式] + [视觉风格与材质] + [文字与标签要求] + [比例与输出格式] + [约束与负面细节]
```

### 6.3 高频模板 ID（可直接调用）
| 模板 ID | 用途 | 关键约束 |
|---|---|---|
| `ui-screenshot-system` | App 截图/仪表盘/直播界面 | 锁平台、比例、状态栏/Tab/操作区、文字可读性 |
| `infographic-engine` | 解释图/时间线/知识卡 | 3–5 模块，色块+箭头+图标+留白，禁止长段正文 |
| `scientific-scale-diagram` | 微观→宏观尺度对比 | 6–8 个尺度框，每框标签短句，标注单位与倍率 |
| `poster-layout-system` | 活动/电影海报 | 锁主体、标题层级、配色、比例；禁止拼贴板 |
| `conceptual-typography-poster` | 标题字即主视觉 | 标题拼写必须逐字正确，配色克制 |
| `ink-double-exposure-poster` | 水墨氛围人像 | 人像剪影+墨色质感+留白，非必要不加文字 |
| `product-commerce-visual` | 商品主图/详情页 | 主商品+卖点标签+辅助道具分层，禁无关道具 |
| `architecture-space` | 室内/建筑/地图 | 锁视角、尺度、材质、光线；地图锁标签语言 |
| `realistic-photography` | 人像/街拍/写实 | 指定机位、镜头、光源、质感；加可信小瑕疵 |
| `character-design-sheet` | 角色设定表 | 锁角色身份，定义构图/配色/笔触/完成度 |

---

## 7. 负面提示词清单（通用）
```
no watermarks, no subtitles, no text overlays, 多余手指, 解剖错误,
面部畸变, 闪烁, 抖动, 伪文字, 错字, 过度磨皮塑料感
```
- 负面词 3–5 个核心即可，堆砌无效否定词会反噬画质。

---

## 国外来源

> **来源 URL**：
> - https://lzyprompt.com/blog/ai-video-prompt-structure-formula/ （LzyPrompt 6-Part Formula，2026-03-03）
> - https://www.imagetoprompt.dev/blog/video-prompt-guide-2026/ （ImageToPrompt 5-Part Formula，2026-03-01）
> - https://skillmd.ai/skills/video-generator/SKILL.md （Video Generator SKILL.md，2026-04-06）
> - https://iseoai.com/veo-3-1-video-prompt-formula/ （iSEO AI 7-Param Veo/Sora Formula，2026-09-19）
> - https://promptsmint.com/prompts/the-ai-video-director-sora-veo-runway/ （AI Video Director Shot Sheet，2026-03-23）
> - https://miraflow.ai/blog/how-to-write-effective-prompts-veo3-veo3-1-sora2 （Miraflow，2025-12-10）
>
> **数据日期**：2026-09-25 抓取
> **置信度**：高（多份 2026 年从业者指南交叉验证同一套结构）

## 一、通用六段式公式（跨模型最稳）

**公式**：`Camera + Subject + Action + Setting + Lighting + Style`

每个模型都在找这六个组件，缺一个模型就瞎猜一个。

### 1. Camera and Cinematography
- Shot types：`wide shot`, `medium shot`, `close-up`, `extreme close-up`, `bird's eye`, `low angle`, `Dutch angle`
- Movement：`dolly forward`, `pan left`, `tracking shot`, `whip pan`, `slow push-in`, `crane up`, `Steadicam follow`
- Lens：`shot on 24mm anamorphic lens, f/2.8, shallow depth of field`
- **必须写速度**：`slow dolly` 和 `rapid pan` 完全不同。不写 camera，模型默认静态中景。

### 2. Subject and Character
- 前 20–30 个词权重最高，**主体必须前置**。
- 差：`a woman`
- 好：`a woman in her late twenties with wavy brown hair, light freckles, wearing a tailored navy blazer over a white t-shirt`

### 3. Action and Motion
- 用具体动词：`sprints`, `drifts`, `pivots`, `reaches`；不要用 `moves`, `goes`。
- 写物理：`water sloshes with visible surface tension as the glass tilts` 而不是 `water moves`。

### 4. Environment and Setting
- 用感官词，不只地名：`a smoky jazz club at 2 AM, amber light filtering through haze, half-empty tables with candles guttering, exposed brick walls`。
- 交代前/中/后景层次：`a crowded market stretches behind him, out of focus`。

### 5. Lighting
- 点名光源和行为：`golden hour, warm backlight creating rim-lit silhouettes`。
- 不要写 `good lighting` / `bright`。

### 6. Style and Mood
- Medium：`realistic`, `stop-motion`, `claymation`, `film noir`, `VHS aesthetic`, `anime`
- Color：`muted desaturated tones`, `vibrant saturated`, `teal and orange`, `black and white`
- Quality：`cinematic 4K`, `shallow DoF`, `ultra-realistic textures`, `35mm film grain`
- Reference：`Wes Anderson symmetry`, `Netflix documentary quality`, `music video pacing`

### 完整组装示例
> **Close-up, slow push-in.** A weathered fisherman in his sixties, deep sun-creased skin, salt-stained cap, **mends a torn net with practiced hands** on a wooden dock. **Early morning fog rolls across a still harbor behind him. Warm golden sidelight from the rising sun, cool blue shadows.** **Documentary realism, 35mm film grain, shallow depth of field.**

6 个元素，3 句话，每个句子覆盖 1–2 个组件。

## 二、五段式公式（ImageToPrompt）

`Scene Description + Motion + Camera Work + Duration + Style/Atmosphere`

1. Scene Description：主体+环境，要具体。
2. Motion：主体怎么动、环境元素怎么动。
3. Camera Work：景别+运动+焦段。
4. Duration：`10 seconds, 16:9`（时长+画幅）。
5. Style/Atmosphere：影调/参考导演/胶片。

## 三、五层结构（SkillMD video-generator）

```
1. Shot Specification   — 机位、景别、运动
2. Setting & Atmosphere — 地点、时间、天气、光
3. Subject & Action     — 谁/做什么，按 beats 写
4. Audio Layer          — 对白/音效/环境声（仅 Veo）
5. Style/Grade          — 美术处理、镜头、调色
```

模板：`[Shot type + camera movement]. [Setting and atmosphere]. [Subject and action beats]. [Audio]. [Style/grade].`

## 四、七参数 Veo 3.1 / Sora 2 专业公式（iSEO AI）

1. **Character**：`charID_[Character Name]`，角色一致性锚点。
2. **Tone**：整体情绪基调。
3. **Visuals**：画面描述。
4. **Camera**：镜头调度。
5. **Action/Choreography**：动作编排。
6. **Sound Design**：环境音/对白/音乐（Veo 原生音频）。
7. **Constraints**：必须保留/必须排除。
