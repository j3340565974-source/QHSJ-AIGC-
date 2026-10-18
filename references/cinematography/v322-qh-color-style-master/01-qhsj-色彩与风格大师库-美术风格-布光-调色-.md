# QHSJ 色彩与风格大师库（美术风格·布光·调色）

> **QHSJ V3.0.0 全网增量知识库**
> **数据日期**：2026-09-25
> **置信度**：高：开源风格库 + BFL 官方 + 经典色彩理论教材

---

## 国内来源

> **来源 URL**：
> - https://github.com/freestylefly/awesome-gpt-image-2 （GPT-Image2 Style Library，工业级风格标签库）
> - https://www.studiobinder.com/blog/how-to-use-color-in-film-50-examples-of-movie-color-palettes/ （StudioBinder 电影配色 50 例）
> - https://www.requiemforadream.com/how-color-theory-shapes-mood-in-cinema/ （60/30/10 法则）
> - https://pixflow.net/blog/the-ultimate-guide-to-film-color-theory-and-palettes/ （电影色彩理论终极指南）
> - https://floniks.com/learn/cinematography/color-contrast-in-cinematography （色彩对比与互补色）
> - https://cinenoir.net/style/colorful/mastering-the-palette-10-exemplary-films-in-cinematic-color-theory/ （10 部电影配色大师课）
>
> **数据日期**：2026-09-25
> **置信度**：高（工业开源风格库 + 经典电影色彩理论教材）
> **内容**：可粘贴的风格标签词 + 色彩配方比例 + 经典影片色卡，用于 AI 出图/出视频的风格锁定；与 `../../aesthetics/08-aesthetics-art-direction.md` / `../../core/14-style-cultural-knowledge.md` / `../../aesthetics/21-style-genome.md` / `../../audio/qh-audiovisual-aesthetic-presets.md` 配套。

## 1. 视觉风格标签词库（GPT-Image2 工业级）

### 1.1 大类
```
realistic / 3D / illustration / classical / brand / poster / UI /
photography / architecture / character / infographic
```

### 1.2 细分风格流派词
| 类别 | 可粘贴中文标签 |
|---|---|
| **写实摄影** | 纪实感、电影感写实、浅景深、自然光、胶片颗粒、可信的小瑕疵（增强真实感） |
| **3D 渲染** | C4D 风格、Blender 渲染、Octane 光追、材质真实、产品级打光、UE5 引擎 |
| **插画** | 水彩、水墨、扁平矢量、赛璐璐动漫、吉卜力风、美式漫画、装饰艺术 Art Deco |
| **古典** | 文艺复兴油画、巴洛克、浮世绘、浮世绘怪谈、国风水墨、青绿山水、工笔重彩 |
| **品牌** | 极简品牌感、VI 视觉板、高级灰、留白克制、无衬线字体 |
| **海报** | 赛博朋克霓虹、波普艺术、瑞士国际主义排版、日系海报风、港风复古 |

### 1.3 质感 / 材质词
```
磨砂金属 / 拉丝不锈钢 / 镜面反射 / 木纹 / 大理石 / 织物纹理 /
皮肤质感 / 湿润光泽 / 干燥颗粒 / 做旧磨损 / 崭新亮面 / 半透明玻璃
```

---

## 2. 色彩理论基础（可直接转 prompt）

### 2.1 色轮关系
| 配色方案 | 色轮位置 | 心理效果 | 典型案例 |
|---|---|---|---|
| **互补色** | 色轮正对（红↔绿、蓝↔橙、黄↔紫） | 高对比、视觉张力、冲突 | 《疯狂的麦克斯：狂暴之路》橙蓝对冲；《天使爱美丽》红绿 |
| **类比色** | 色轮相邻三色（红↔橙↔黄 / 蓝↔青↔绿） | 和谐、舒缓、自然 | 风景、外景、宁静段落 |
| **三分色** | 色轮上等距三色 | 丰富但不冲突 | 卡通、儿童向、活泼 |
| **单色** | 同一色相不同明度/饱和度 | 统一、高级、压抑 | 单色电影、特定情绪段落 |

### 2.2 好莱坞橙青调（Teal & Orange）
- 肤色是暖橙色，阴影/环境推成青蓝色。
- 原理：互补色并置时，**彼此会让对方显得更饱和**（歌德/Albers 色彩交互定律）。
- 这是好莱坞大片默认调色：让人物从背景中"跳"出来。
- Prompt 写法：`暖色肤色高光，青蓝色阴影，好莱坞电影级调色，高对比互补色对冲`。

---

## 3. 60/30/10 配色法则（构图级色彩分布）

画面色彩面积比：
- **60%**：主色调，中性色（背景、墙面、大地、灰/白/米）。
- **30%**：次要色，奠定情绪基调（服装、家具、大面积道具）。
- **10%**：点缀色，吸引视线（关键道具、标志、口红、火光）。

Prompt 写法：
```
画面 60% 是冷灰蓝色调的城市背景，30% 是女主的红色大衣，
10% 是手中金色打火机的反光。
```
这个比例制造视觉和谐，同时把视线锁在 10% 点缀上。

---

## 4. 经典影片色卡（可直接模仿）

| 影片 | 色彩策略 | Prompt 关键词 |
|---|---|---|
| **《布达佩斯大饭店》** | 严格粉彩色码：1930s 用特定粉/紫，不同时代不同调色 | 对称构图、马卡龙粉紫、复古粉彩、韦斯·安德森式 |
| **《疯狂的麦克斯：狂暴之路》** | 橙红沙漠 vs 冷蓝天空，互补色对冲 | 橙黄沙暴、青蓝天空、高饱和互补、末日废土 |
| **《天使爱美丽》** | 红绿互补，绿色调贯穿 | 墨绿墙、正红外套、暖黄灯光、法式复古 |
| **《封神第一部》** | 东方美学：元明道教水陆画 + 永乐宫壁画 + 北宋山水 + 商周青铜巫元素 | 金红卧榻、蟠龙雕刻、饕餮纹、水陆画神仙谱、青绿山水气韵 |
| **《我不是药神》** | 现实主义低饱和冷调，还原 2000 年代中国 | 灰蓝冷调、低饱和、年代质感、粗糙纪实 |
| **《飞驰人生》** | 西部大地的苍黄 vs 城市的灰蓝 | 西部戈壁土黄、雪原冷蓝、赛车橙红点缀 |

---

## 5. 色彩—情绪对照速查

| 颜色倾向 | 情绪/叙事用途 |
|---|---|
| **暖橙/金黄** | 温暖、怀旧、家、黄昏、回忆 |
| **冷蓝/青** | 孤独、理性、科技、夜晚、忧郁 |
| **正红** | 危险、欲望、血、激情、警告 |
| **墨绿** | 自然、诡异、法式复古、嫉妒 |
| **紫/品红** | 魔法、神秘、超自然、赛博朋克 |
| **金/琥珀** | 华贵、神性、佛教、仙侠 |
| **黑白灰** | 纪实、严肃、极简、克制 |
| **高饱和撞色** | 狂欢、荒诞、波普、混乱 |
| **低饱和灰调** | 压抑、现实、时代感、悲剧 |

---

## 6. 提示词中的风格锁定模板

### 6.1 单图风格锁定
```
[主体]，[构图]，[主色 60%] + [次色 30%] + [点缀色 10%]，
[光影]，[质感]，[参考影片/画家风格]，[比例]
```
例：
```
一个穿红风衣的女人站在雨夜街头，中景，
60% 冷蓝霓虹反射，30% 潮湿深色路面，10% 她大衣的正红色，
路灯轮廓光，湿润皮肤质感，《银翼杀手2049》式电影调色，2.39:1
```

### 6.2 视频风格锁定
```
[类型] + [视觉质感] + [镜头语言] + [情绪张力]
```
例：
```
武侠剧，电影级光影，极致面部特写，金红暖色调，仙侠高燃氛围
```
（出自即梦 Seedance 创作者实测公式）

---

## 国外来源 · 美术风格

> **来源 URL**：
> - https://seanbair.ai/artistic-style-prompt-library.html （Sean Bair Artistic Style Prompt Library，36 风格 / 144 prompts，2026-09-15 更新）
> - https://docs.bfl.ai/guides/prompting_video_camera_terms （BFL FLUX 3 Art Direction 章节，2026-09-24）
> - https://prompt-architects.com/blog/33-midjourney-style-modifiers-reference （Prompt Architects 33 Style Modifiers，2026-06-27）
> - https://www.promptspace.in/blog/midjourney-prompts-ultimate-guide-2026 （PromptSpace 200 Examples，2026-03-27）
>
> **数据日期**：2026-09-25 抓取
> **置信度**：高（36 风格库 + BFL 官方风格短语，可直接拼用）

## 一、BFL 官方 Art Direction 五种世界观风格（整段复用）

| 风格 | 英文 Prompt 示例 |
|---|---|
| **Dreamcore 梦境核心** | `Dreamcore emptiness fills endless pastel hallways under a blown-out overexposed sky, doors leading nowhere, a lone swing swaying without wind, liminal dream logic, quietly unsettling nostalgia.` |
| **Dystopian 反乌托邦** | `A dystopian megacity glistens under relentless rain, surveillance drones sweeping searchlights across neon-soaked crowds and towering propaganda screens, steam rising from grates, oppressive cyberpunk gloom.` |
| **Magical realism 魔幻现实主义** | `Gentle magical realism fills an ordinary corner café where paper lanterns float freely above chatting customers, drifting between tables as waiters ignore them, warm everyday enchantment.` |
| **Maximalism 极繁主义** | `Opulent maximalism crowds a baroque salon with gilded mirrors, stacked oil paintings, velvet drapes, marble busts and cascading flowers, camera slowly gliding through ornate sensory overload.` |
| **Diorama 微缩模型** | `A charming diorama miniature small town awakens, tilt-shift model railways, tiny felt cars and handcrafted houses under warm lamp lighting, whimsical.` |

## 二、BFL 动画/媒介风格

- `stop motion claymation`：定格黏土动画，`plasticine toast hopping onto plates, jerky handmade frames, fingerprint textures visible`
- `pixel art`：复古像素，`16-bit city at sunset, dithered orange gradients, blocky skyscrapers, tiny sprite pedestrians, SNES atmosphere`
- `zoetrope`：走马盘，`spinning zoetrope drum flickers galloping horse sprites, Victorian pre-cinema wonder`
- `kinetic typography`：动态字体，`city skyline built from animated words, letters stacking into skyscrapers`

## 三、Sean Bair 36 风格库——可直接套用的"风格包"

每个风格包的套路：**视觉描述 + 调色板 + 代表作参照 + MJ/DALL·E/SD 三端 prompt**。

### 01 AI-Futuristic / Cyberpunk 赛博朋克
- 视觉：`neon-drenched cityscapes, holographic interfaces floating mid-air, chrome and glass architecture, autonomous drones, neural-link implants glowing on temples`
- 调色：`electric blue, deep purple, cyan against dark backgrounds, rain-slicked streets reflecting digital billboards`
- MJ 短语：`futuristic AI cityscape, neon holographic displays, cyberpunk aesthetic, chrome architecture, glowing neural interfaces, rain-slicked streets reflecting cyan and purple neon, volumetric fog, cinematic lighting, ultra-detailed, 8k --ar 16:9 --v 6.1 --style raw`
- 关键词：`holographic, neural, neon-lit, chrome, volumetric fog, bioluminescent, circuitry, data streams`

### 02 Anime / Manga 日系动画
- 视觉：`large expressive eyes, dynamic poses, vibrant saturated colors, cel shading, clean bold linework, wind-blown hair, cherry blossom petals, speed lines`
- MJ：`anime style illustration, expressive eyes, dynamic pose, vibrant saturated colors, cel shading, clean linework, cherry blossom petals, dramatic lighting, studio quality anime, in the style of Makoto Shinkai --ar 16:9 --niji 6`
- 子风格：`shonen`（热血动作）、`shoujo`（少女浪漫）、`chibi`（Q 版）、`mecha`（机甲）
- 工作室参照：`Ghibli`、`Trigger`、`MAPPA`、`Ufotable`

### 03 Vintage Americana / Norman Rockwell 复古美式
- 视觉：`warm nostalgic mid-century American illustration, rich oil-painting textures, soft golden lighting, idealized everyday life`
- 调色：`warm earth tones — amber, cream, russet, sage green`

### 其他高频风格包（PromptSpace 汇总）
- **摄影风**：`editorial photography`, `street photography`, `fashion photography`, `documentary photography`, `macro photography`, `aerial drone photography`, `film noir cinematography`, `Kodak Portra 400 film`, `tintype photography`, `infrared photography`
- **艺术运动**：`art nouveau`, `art deco`, `baroque`, `renaissance`, `impressionism`, `surrealism`, `minimalism`, `brutalism`, `vaporwave`, `synthwave`, `cottagecore`, `dark academia`, `solarpunk`, `ukiyo-e`（浮世绘）
- **漫画**：`comic book art style, bold black ink outlines, dynamic action pose, halftone dot shading, vibrant primary colors, dramatic perspective, speed lines`

## 四、Midjourney 风格修饰词三大类（Prompt Architects）

最稳的组合方式：**媒介 + 光感 + 情绪**，各取 1–2 个。

- **媒介/质感**：`cinematic photography`, `Studio Ghibli watercolor`, `1970s film grain`, `Art Deco illustration`, `35mm film`, `polaroid`, `oil painting`, `concept art`, `matte painting`
- **导演/电影参照**：`by Wes Anderson`（对称、粉彩色、deadpan）、`Wong Kar-wai mood`（王家卫）、`Christopher Nolan anamorphic`、`Blade Runner`、`in the style of Roger Deakins`
- **艺术家/摄影师参照**：`Annie Leibovitz portrait`, `Ansel Adams landscape`, `Makoto Shinkai sky`, `Gustav Klimt`, `Moebius`, `Beksinski`

**质量词注意**（Midjourney Cheat Sheet）：
- `8k` → 光比更极端，颜色更饱和、更 CG 感
- `cinematic` → 阴影更重（但画面不一定更暗），物体更厚，更海报感
- `color grading` → 色相偏移剧烈，鲜艳但不过饱和

## 五、调色/影调风格包（从实战 prompt 提炼）

| 风格名 | 关键词组合 |
|---|---|
| 青橙好莱坞 | `teal and orange color grading, teal shadows, amber highlights, contemporary crime drama film aesthetic, shot on Arri Alexa 32mm` |
| 韩国复仇片 | `desaturated teal-green color grade, harsh fluorescent and sodium vapor lighting, 35mm film grain` |
| 王家卫 | `step printing effect, ghostly motion trails, warm red bloom, neon alley, dreamy Wong Kar-wai mood` |
| 赛博朋克 | `neon-lit, pink and cyan, rain reflections, volumetric fog, cold tones` |
| 温馨治愈 | `soft light, warm tones, slow pace, comforting, pastel palette` |
| 奢华极简 | `rim light, metallic, minimal composition, negative space` |
| 复古胶片 | `film grain, faded colors, nostalgic halation bloom, soft vintage 35mm` |
| 黑色电影 | `high contrast, hard light, deep shadows, venetian blind shadows, cigarette smoke, monochrome` |
| 梦境 | `dreamcore, overexposed pastel sky, liminal space, soft focus, nostalgic unease` |
| 末日废土 | `desaturated browns and greys, dust, cracked earth, overcast sky` |

## 六、CinePrompt 一键风格预设（huihuihui-wq）

| 预设 | Prompt 短语 |
|---|---|
| CINEMATIC | `35mm film, shallow DoF, warm tones` |
| CYBERPUNK | `neon lighting, rainy night, cold tones` |
| GHIBLI | `hand-painted, enhanced saturation` |
| VINTAGE | `film grain, faded, nostalgic` |
| MINIMAL LUXURY | `rim light, metallic, minimal` |
| HEALING | `soft light, slow pace, comforting` |

## 七、风格选择与堆叠建议

1. **一次只锁一个主风格**，再加 1–2 个光感/镜头词。`cinematic photography + Studio Ghibli watercolor` 这种跨媒介堆叠要慎重，容易冲突。
2. **导演参照是快捷键**：`Wes Anderson symmetry` 一个词打包了对称构图+粉彩色+deadpan 表演+4:3 画幅。
3. **摄影胶片型号**能微调质感：`Kodak Portra 400`（暖肤色、宽容度高）、`Fuji Velvia`（高饱和风光）、`Cinestill 800T`（夜景光晕、红溢色）。
4. **不要堆质量词**：`epic cinematic dramatic hyperdetailed beautiful stunning` 不会叠加，选 1–2 个精确词。
5. **色彩对比法**：写 `teal shadows and amber highlights` 比写 `cinematic color` 精确十倍。

---

## 国外来源 · 布光与调色

> **来源 URL**：
> - https://docs.bfl.ai/guides/prompting_video_camera_terms （BFL / FLUX 3 官方 Lighting Styles，2026-09-24）
> - https://freecraftlog.com/comfyui-lighting-prompt-complete-guide/ （FreeCraftLog 50 Lighting Prompts，2026-04-08 更新）
> - https://reezo.ai/blog/cinematography-terms-for-ai-video-prompts （Reezo AI，2026-05-12）
> - https://www.openjourney.art/blog/stable-diffusion-prompts （Open Journey SD Guide，2026-07-05）
>
> **数据日期**：2026-09-25 抓取
> **置信度**：高（官方 cheatsheet + 50 词分类表交叉验证）

## 一、布光三原则（FreeCraftLog）

1. **光源方向决定表情**：正面光扁平，斜侧/逆光戏剧化。
2. **色温控制情绪**：暖色=温暖/怀旧，冷色=紧张/神秘。
3. **明暗对比造纵深**：高对比=冲击力，低对比=柔和。

布光是 AI 视频里"看起来电影感"的第一杠杆——比镜头语言更决定画面是"平"还是"立体"。

## 二、自然光系（Natural Light，8 词）

| 英文 Prompt | 中文 | 视觉特征 |
|---|---|---|
| `golden hour lighting` | 黄金时刻光 | 日出后/日落前约 1 小时，暖橙，长阴影，皮肤发光，肖像绝配 |
| `blue hour lighting` | 蓝调时刻 | 日出前/日落后短暂窗口，冷蓝环境光，都市忧郁感 |
| `harsh sunlight` | 直射硬日光 | 强烈阴影，高对比 |
| `overcast lighting` | 阴天柔光 | 均匀软光，淡阴影 |
| `dappled sunlight` | 林间斑驳光 | 树叶缝隙漏下的光斑，森林纵深 |
| `moonlight` | 月光 | 蓝银冷光，神秘夜景 |
| `dawn lighting` | 黎明天光 | 地平线淡粉色 |
| `sunset lighting` | 夕阳光 | 红到橙的戏剧化光 |

**可直接拼用短语**：`golden hour lighting, warm orange sunlight, long shadows, soft bokeh, cinematic atmosphere`。
