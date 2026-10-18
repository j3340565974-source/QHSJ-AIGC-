> DEPRECATED，替代：references/vfx/qh-vfx-parametric-library.md

# QHSJ VFX 参数化特效库（粒子·光效·天气·魔法）

> **QHSJ V3.0.0 全网增量知识库**
> **数据日期**：2026-09-25
> **置信度**：中高：BFL 官方 + 可复用 VFX 模板

---

## 国内来源

> **来源 URL**：
> - https://makeaiprompt.com/blog/battlefield-smoke-and-fire-embers-vfx-prompt/ （战场烟雾与余烬）
> - https://makeaiprompt.com/blog/abandoned-battlefield-fire-sparks-vfx-prompt/ （废墟火星）
> - https://makeaiprompt.com/blog/temple-of-fire-god-lava-surge-vfx-prompt/ （熔岩涌动）
> - https://makeaiprompt.com/blog/chariot-fire-trail-vfx-prompt/ （战车火尾）
> - https://makeaiprompt.com/blog/sandstorm-desert-vfx-prompt/ （沙漠沙暴）
> - https://makeaiprompt.com/blog/crystal-particle-explosion-vfx-prompt/ （水晶粒子爆炸）
> - https://makeaiprompt.com/blog/wolf-running-through-fire-and-smoke-vfx-prompt/ （狼穿火烟）
> - https://awesomevideoprompts.com/tags/vfx/ 与 /tags/particles/ （游戏过场 VFX 案例集）
>
> **数据日期**：2026-09-25
> **置信度**：中高（英文 VFX prompt 工程模板，可直接中文化后用于即梦/Seedance）
> **内容**：把每种特效拆成粒子类型、烟雾特征、热畸变、光源交互四个可填槽位，配合 `13-vfx-motion-physics.md` / `qh-anime-ultimate-vfx-paradigm.md` / `../action/qh-xuanhuan-magic-combat.md` 使用。

## 1. VFX 提示词四槽位结构（通用骨架）

任何 VFX 镜头都按以下四槽位展开，缺槽位 = AI 自由发挥 = 翻车：

```
[粒子类型 Primary Particle] + [次级粒子 Secondary Particle] +
[烟雾/雾气 Smoke & Haze] + [热畸变/光交互 Heat Distortion & Light]
```

每个槽位都要有**可替换变量**，不要写死。

---

## 2. 火焰 / 烟雾 / 余烬类

### 2.1 战场浓烟与余烬（坦克残骸）
```
环境：黄昏/深夜/阴天黎明。
主光源：暖橙色火光，与冷深蓝色暮空形成冷暖对比。
空气：厚重呛人的尘烟，火光穿透形成体积光（volumetric god rays）。
烟雾：从被摧毁的炮塔涌出浓稠、翻卷、油状黑烟，上升到高处渐变为深灰色消散；
      下方烟须扭曲地缠绕地面。
余烬：密密麻麻发光火星、余烬、细灰在空中漂浮，是周围环境的微弱动态光源；
      部分余烬粘在物体表面，滋滋作响爆出小烟团。
热畸变：火光上方可见明显热浪扭曲（heat haze）。
```

### 2.2 废墟火星（慢镜）
```
主体：缓慢、迷人的发光火星/余烬/细灰 cascading 飘落。
光源：火星是周围环境唯一的动态微光来源。
火星来源：[变量：四号坦克残骸 / 燃烧坍塌的木梁 / 火盆]。
粒子质感：超精细细尘形成柔雾；粗沙颗粒反光；混合碎石/瓦砾形成混乱感。
```

### 2.3 狼穿火烟（角色穿越特效）
```
超精细视觉特效。一大团发光余烬、火星、细灰在空中旋转，
像恶意的萤火虫一样反光。部分余烬粘在狼毛上，滋滋爆出小烟团。
可见的热浪扭曲大气，背景被扭曲变形。粗浓烟须卷曲缠绕狼身，
狼穿过时破开烟层。地面是[焦土/雪地/石板]。
```

---

## 3. 魔法 / 能量类

### 3.1 战车火尾（紫色魔法能量）
```
粒子与余烬：
- 初级粒子：密集、锋利、闪闪发光的紫色魔法能量碎片阵雨；
- 次级粒子：细小、发光的紫黑色灰烬，不祥地悬浮在空中。
烟雾：火尾产生浓稠、油状、翻卷的黑烟，像在空气中扭动抓取。
热畸变：尾迹上方有明显热浪扭曲。
```

### 3.2 水晶粒子爆炸（紫水晶洞爆发）
```
电影静帧，照片级 VFX，动态低角度镜头：
巨大的古代紫水晶簇在黑暗洞穴虚空中猛烈爆炸。
爆炸源自内部纯能量涌动，爆发前先出现复杂的蛛网状裂纹，
裂纹中透出强烈电光青色光芒，随后 catastrophic burst。
水晶碎裂成混合体：大块锋利碎片 + 细碎闪光晶尘，
全部向外高速喷射，在空中旋转反射光芒。
```

### 3.3 火焰环 / 火球（修行/施法）
```
Frame 5: 巨大火球缓慢向四周膨胀，面部可见恐慌，火焰吞噬周围，
火星余烬慢镜飘出，冲击波可见，电影级混乱慢动作，4K。
Frame 6: 火焰环在双手间缓慢旋转扩大，闭眼深度专注，
脸上有汗珠，火焰能量有节奏地脉动，暖色戏剧光缓慢增强，
电影级修行瞬间，4K。
```

### 3.4 记忆碎片（抽象艺术粒子）
```
慢镜头特写：数千片不规则水晶碎片悬浮在虚空中。
每片碎片都是完美微型棱镜，反射不同的超写实绝美日落或星空。
碎片缓慢旋转、闪烁、聚合、离散。抽象电影感 / 装置艺术风格，10秒。
```

---

## 4. 天气 / 自然现象类

### 4.1 沙漠沙暴
```
粒子质感：
- 超细粉沙/尘，形成柔雾；
- 粗沙颗粒，捕捉光线；
- 混合沙、卵石、大碎片，混乱感；
- 闪烁、近乎魔法的微尘。
风的行为：
- 优雅可见的螺旋卷须与涡旋；
- 强力、定向的风流线；
- 湍流、不可预测的阵风与涡流；
- 缓慢滚动的厚重尘云。
```

### 4.2 游戏过场 / 神庙逃亡（体积光+尘埃）
```
游戏过场，史诗奇幻动作，戏剧化体积神光（volumetric god rays），
厚重尘埃与瓦砾，照片级+风格化游戏光照，强物理感。
0-4s：低角度宽镜头跟拍主角冲刺穿过古老石廊，身后突然大面积坍塌，
镜头加速进入快速跟拍，地面开裂塌陷。
4-8s：极端推轨变焦（vertigo effect）在主角脸上……
```

---

## 5. 熔岩 / 地火类

### 5.1 神庙熔岩涌动
```
熔岩黏度：[变量：稀薄如水 / 浓稠如沥青 / 中等岩浆]。
熔岩核心：[变量：亮黄白炽 / 橙红 / 暗红冷却]，表面有[变量：龟裂纹壳 / 流动光泽 / 泡沫翻涌]。
喷发物：移动时猛烈喷出[碎石 / 火星 / 有毒气体 / 蒸汽]。
环境交互：熔岩与神庙环境剧烈反应，[石面沸腾 / 水汽爆炸 / 金属扭曲]。
```

---

## 6. VFX 提示词选词速查表

### 6.1 粒子
| 类别 | 中文词库 |
|---|---|
| 火星/余烬 | 发光余烬、火星、细灰、炭屑、闪烁光斑、恶意萤火虫般的火星 |
| 烟雾 | 浓稠黑烟、油状烟、卷须烟、薄暮雾、尘霾、蒸汽、烟圈 |
| 魔法粒子 | 紫色能量碎片、晶尘、金光粒子、电光电弧、蓝色星尘、符文光粒 |
| 自然粒子 | 雪花、雨滴、落叶、花瓣、沙尘、花粉、萤火虫 |

### 6.2 光效
```
体积光 / 丁达尔光 / 神光（god rays）/ 轮廓光（rim light）/
镜头眩光（lens flare）/  bloom 光晕 / 霓虹反射 / 电光爆闪 /
熔岩自发光 / 月光冷辉 / 火光暖橙
```

### 6.3 空气透视
```
空气里厚浓烟霭 / 可见热浪扭曲 / 大气雾感 / 丁达尔光柱 /
浮尘反光 / 水汽弥漫 / 尘埃在光束中翻滚
```

### 6.4 运动状态
```
缓慢翻涌 / 猛烈喷发 / 螺旋上升 / 漂浮悬浮 / 高速喷射 /
慢镜飘散 / 脉动闪烁 / 旋转扩大 / 蛛网状蔓延
```

---

## 7. 使用纪律
- 每个 VFX 镜头至少写满四槽位（粒子/次级粒子/烟雾/热畸变），缺槽位 = AI 瞎编。
- 粒子要区分**初级（密集、主导）**和**次级（稀疏、氛围）**，只写一类会显得单薄。
- 火焰/能量必须写**光源颜色**，因为它会反过来照亮环境——这是 VFX 真实感的关键。
- 慢镜（slow motion）要显式标注，否则 AI 会用正常速度爆炸。

---

## 国外来源

> **来源 URL**：
> - https://docs.bfl.ai/guides/prompting_video_camera_terms （BFL FLUX 3 官方 VFX & Transformation / Shutter & Time 章节，2026-09-24）
> - https://makeaiprompt.com/blog/sandstorm-desert-vfx-prompt/ （Sandstorm Desert VFX Master Template，2025-10-06）
> - https://makeaiprompt.com/blog/snowfall-and-blizzard-vfx-prompt/ （Snowfall/Blizzard VFX，2025-10-06）
> - https://awesomevideoprompts.com/tags/vfx/ （Awesome Video Prompts VFX 标签库，2026-06-14）
>
> **数据日期**：2026-09-25 抓取
> **置信度**：中高（BFL 官方 + 可复用 VFX 模板，部分为社区 prompt 库）

## 一、BFL 官方 VFX 与变形特效（可直接复用整句）

| 特效类型 | 英文 Prompt 示例 | 视觉说明 |
|---|---|---|
| Double exposure 双重曝光 | `Elegant double exposure blends a pensive man's profile portrait with a misty pine forest, treetops and fog drifting inside his silhouette against white sky.` | 人像剪影里叠森林/雾，诗意忧郁 |
| Datamosh 数据挤压 | `A dancer hits the beat drop and the frame erupts in datamosh corruption, pixels smearing and melting into glitched motion trails, colors bleeding chaotically.` | 像素糊化、色彩乱溢、数字故障 |
| Kaleidoscope 万花筒 | `Overhead kaleidoscope symmetry multiplies a troupe of dancers into shifting mirrored mandala patterns, costumes blooming like folding flowers.` | 镜面对称曼陀罗，Busby Berkeley 式 |
| Morphing 形变 | `Seamless morphing transforms one face through four generations, child to teenager to mother to grandmother, features fluidly reshaping.` | 跨年龄无缝变形 |
| Slit scan 狭缝扫描 | `A galloping horse stretches into slit-scan time distortion, its body smeared into flowing temporal ribbons across the frame.` | 主体拉成时间光带，超现实速度感 |
| X-ray 透视 | `An x-ray view reveals the inner skeleton of a mechanical hand flexing, gears and pistons glowing blue-white against black.` | 半透明解剖视图 |
| Levitation 悬浮 | `Quiet levitation lifts books, teacups and a floor lamp drifting slowly through a sunlit living room, objects rotating weightlessly.` | 日常 Domestic Magic |

## 二、天气与大气粒子模板（MakeAIPrompt 大气粒子参数模板）

沙尘暴 VFX 模板展示了一个**可迁移到任意天气特效**的八段结构。用户按段选填即可：

### 段 1：核心主体
- Primary Subject 选项：`apocalyptic sandstorm` / `colossal haboob`（哈布沙暴）/ `swirling dust devil`（尘卷）/ `gritty desert gale` / `supernatural sand vortex`
- Secondary Elements：`engulfing ancient ruins` / `obscuring a lone traveler` / `revealing a hidden oasis` / `battering an off-road vehicle`

### 段 2：环境
- Location：`endless erg of Sahara dunes` / `rocky wadi` / `salt pans` / `Martian cratered landscape` / `post-apocalyptic wasteland`
- Geological：`towering sandstone mesas and buttes` / `sharp volcanic spires` / `cracked arid earth` / `deep narrow canyon`

### 段 3：强度与情绪
- Intensity：`light hazy breeze kicking up fine dust` → `steady blinding gale with horizontal sheets of sand` → `turbulent chaotic vortex` → `monstrous towering wall of dust consuming the horizon`
- Emotional impact：`oppressive dread` / `awe-inspiring power` / `isolated loneliness` / `thrilling danger` / `mysterious wonder`

### 段 4：粒子与风动物理（VFX 核心）
- Particle Quality：`hyper-detailed fine silt creating soft haze` / `granular coarse sand that catches light` / `mix of sand, pebbles and debris` / `shimmering magical motes`
- Wind Behavior：`visible elegant swirling tendrils and vortices` / `powerful directional streamlines` / `turbulent unpredictable gusts and eddies` / `slow-rolling heavy dust clouds`
- Atmospheric Obscuration：`thick low-visibility sand fog` / `dense opaque wall of sand` / `translucent veils partially obscuring background` / `dynamic god rays piercing through breaks`

### 段 5：光与色
- Light Source：`harsh scorching midday sun` / `low warm sunset light` / `cold eerie full moon glow` / `internal lightning flashes within the storm` / `vehicle headlights`
- Time：`high noon` / `golden hour` / `twilight` / `dead of night`
- Palette：`monochromatic ochre/sepia/beige` / `fiery deep oranges, burning reds, dark umber` / `desaturated gritty browns and greys` / `unnatural sci-fi teal/purple dust`

### 段 6：构图
- Shot：`extreme wide shot` / `wide shot` / `medium shot` / `close-up on particle effects`
- Angle：`eye-level` / `dramatic low-angle` / `high-angle aerial drone POV` / `Dutch angle`
- Focal point：`immense scale of the storm wall` / `texture of sand hitting a surface` / `subject struggling against wind` / `sun being blotted out`

### 段 7：渲染
- Style：`hyperrealistic` / `photorealistic` / `cinematic film still` / `epic concept art` / `atmospheric matte painting`
- Quality：`8K UHD` / `ultra-detailed` / `volumetric lighting` / `ray tracing` / `PBR`
- Finishing：`anamorphic lens flare` / `motion blur on fast particles` / `subtle film grain` / `dramatic color grading` / `HDR`

### 段 8：负向
`blurry, out of focus, cartoony, low-resolution, watermark, text, signature, oversaturated colors, static, flat lighting`

**实战组装示例**：
> *Cinematic film still of an apocalyptic haboob engulfing a rugged off-road vehicle in an endless erg of Sahara dunes, towering undulating dunes. Overwhelming turbulent intensity, awe-inspiring natural power and oppressive dread. VFX focus on chaotic mix of granular sand and fine dust, visible powerful swirling tendrils and vortices, dense opaque wall of sand, dynamic god rays piercing through. Lit by low warm sunset light, fiery spectrum of deep oranges, burning reds, dark umber shadows. Extreme wide shot, dramatic low-angle, emphasizing immense scale. Hyperrealistic, 8K, volumetric lighting, ray tracing, anamorphic flare, motion blur on fastest particles.*

## 三、雪/暴风雪 VFX 关键短语

参考 Snowfall/Blizzard 模板提炼：
- `heavy blizzard conditions, dense horizontally blowing snow, near-zero visibility`
- `long dramatic shadows cast by low winter sun through blowing snow`
- `anamorphic lens, leading line of road disappearing into the storm, significant motion blur on fast-moving foreground flakes`
- `photorealistic, Unreal Engine 5 render quality`
- Negative：`cartoon, illustration, painting, sunlight, green vegetation`

## 四、BFL 时间/快门类动态效果（常被忽视但极有用）

这些既是时间特效也是 VFX：
- `bullet time`：彩带/水滴悬停，镜头环绕穿过悬浮粒子。
- `speed ramp`：出拳命中瞬间变慢再弹回，汗水飞溅。
- `step printing`：霓虹巷里舞者留下鬼影拖尾，王家卫梦呓感。
- `long exposure look`：夜骑者车灯拖成光轨。
- `boomerang loop`：香槟塞弹出又缩回瓶中，无限循环。
- `cinemagraph`：整间 diner 全冻结，只有咖啡蒸汽上升。

## 五、转场 VFX（Shot Transitions）

- `match cut`：桌上旋转硬币 → 太空旋转行星。
- `whip transition`：急摇模糊厨房 → 蜡烛餐厅。
- `foreground wipe`：公交车驶过遮住画面，露出新街道。
- `jump cut`：同机位跳切，vlog 忏悔感。
- `object portal`：镜头钻进咖啡杯，棕色液体溶解成秋日森林。
- `pass-through`：穿过钥匙孔进书房，再从窗户穿出雨夜街，一个连续不可能镜头。