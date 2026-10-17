# QHSJ Seedance 导演公式（模式门控·特效合同·13配方）

> **QHSJ V3.0.0 全网增量知识库**
> **数据日期**：2026-09-25
> **置信度**：高：Seedance 2.0 工程规范

---

## 一、导演公式与模式门控

### Director Formula（槽位顺序）
```
Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints
```
主体和主要动作放最前面，因为前几个从句决定镜头层级。

| 槽位 | 用途 | 模式 |
|---|---|---|
| Subject | 模型必须追踪的锚点 | `Original ceramic perfume bottle on black acrylic, label preserved exactly` |
| Action | 可见的变化 | `condensation beads form and slide down the glass over five seconds` |
| Scene | 参考图里没有的才写 | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | 一个主移动带端点 | `slow dolly-in from medium product shot to macro label detail` |
| Light/style | 物理光源+安全视觉语言 | `warm practical key from frame left, cool blue rim, clean commercial realism` |
| Audio | 环境床/SFX/对白/静默 | `Sound: low room tone, soft glass chime on final frame` |
| Constraints | 保留与排除 | `do not alter logo, shape, label, or cap geometry` |

### 模式门控（Mode Gate）

| 模式 | 起草重点 | 常见错误 | 修正 |
|---|---|---|---|
| T2V | 全片完整构建 | 一个clip太多事件 | 保持一个可见beat一个端点 |
| I2V | 保留可见身份，加动作 | 重复描述图片导致产品/脸漂移 | 写`preserve @Image1 exactly`，只加动态变化 |
| V2V | 转移动作/镜头/节奏 | 转移了未授权的长相/场景 | 用已授权素材，限制转移角色 |
| R2V | 每个参考分配独立角色 | 一个参考同时控制长相/姿势/场景/风格 | 拆分角色或优先最重要的 |
| FLF2V | 从首帧到尾帧连续过渡 | 把尾帧当模糊氛围而非端点 | 声明`@Image2 is the final visual target` |
| Edit | 保留源clip只改一层 | 重写整个场景丢失连续性 | `@Video1 is the source clip; change only...` |
| Extend | 从已接受素材继续 | 从计划结尾而非实际结尾开始 | 用观察到的实际结尾状态 |

## 二、延续深度管理（Extension Depth）

```
Depth 0: 从标准参考图开（T2V）
Depth 1: 从上一clip尾帧开（I2V）
Depth 2: 从depth-1 clip尾帧开（I2V from I2V）
Max safe depth: 2（硬顶: 3）
```

到max depth时必须从标准参考重新锚定（T2V），重置depth到0，防止累积漂移。

### 五种延续类型

| 类型 | 用途 | 关键 |
|---|---|---|
| 无缝延续 | 同镜头同地点持续动作 | 必须从已接受素材做I2V，同机位 |
| 有意下一个镜头 | 剪辑点合适 | 故事连续但不承诺无缝 |
| 已知状态桥接 | 定义首尾帧连接 | 清晰start state + end state |
| 尾部修复 | 上一clip最后几秒崩了 | 用最后好帧做I2V种子，只重新生成失败部分 |
| 漂移后重新锚定 | 跨多clip身份/服装漂移 | 从原始角色参考图重新T2V |

**Canon规则**：已接受的观察素材覆盖计划状态。如果计划说到了车但素材结束在离车两步处，下个提示词从两步处开始。拒绝的素材永远不更新canon。

## 三、特效五要素合同（VFX Contract）

每个特效必须指定：
1. **Source**（从哪发源）
2. **Material**（什么材质：粒子/烟/电/液体/碎片）
3. **Motion path**（方向/速度/弧线/旋转）
4. **Light/object interaction**（发光？catch光？投影？碰撞/粘附/反弹/穿透？）
5. **Dissipation**（怎么结束：沉降/消散/蒸发/冻结/坍塌）

### 七类特效速查

| 类型 | 提示词模式 | 稳定性注意 |
|---|---|---|
| 粒子 | `[type] particles [spawn from source], [path], [light], [settle/fade]` | 源物体稳定，粒子动源不变形 |
| 能量 | `[energy type] [color] [along/from source], [surface interaction], [brightness change], [fade]` | 能量附着源，弧线沿电缆 |
| 烟/蒸汽 | `[smoke type] [color] [source], [density], [direction], [gravity/wind], [dissipate]` | 描述密度方向，"thin wispy" vs "thick rolling" |
| 火/热 | `[fire type] [color], [source], [motion], [light cast], [smoke], [extinguish]` | 火发光，指定哪些表面接受光晕 |
| 水/流体 | `[liquid] [source], [arc], [splash/ripple], [surface interaction], [settle]` | 水绑到表面，落在哪怎么交互 |
| 变形 | `[object] [transform verb] [A→B], [which parts change first], [preserved elements], [endpoint]` | 保护身份锚，logo/脸周围变形 |
| 天气 | `[weather] [intensity], [direction], [interaction with characters], [surface effects]` | 天气影响画面内一切，显示多交互点 |

**五条铁律**：一个clip只一个英雄特效；特效必须锚定可见源；尊重物理（重力/风/碰撞/反射/遮挡）；特效必须有端点（forms→travels→dissipates）；保护核心身份（脸/手/logo/文字周围放特效，不穿过）。

## 四、动作合同（Motion Contract）

```
State: actor/object + action + force level + timing + physical consequence + continuity + endpoint
```

| 动作类型 | 强写法 | 弱写法 |
|---|---|---|
| 细微表演 | `Character A inhales, grips the cup tighter, then sets it down without looking away` | `she feels nervous` |
| 产品材质 | `condensation beads gather, merge, and slide down the bottle neck` | `the product looks refreshing` |
| 编排动作 | `Character B ducks under the swinging bag, pivots left, and stops in a guarded stance` | `fast action fight scene` |
| 物体物理 | `paper receipt lifts in the fan breeze, flips once, and lands face-up` | `papers move dynamically` |
| 环境运动 | `rain streaks diagonally across the backlight while puddle ripples spread from footsteps` | `stormy weather atmosphere` |

**物理前置模式**：写质量+力+材质，然后命名一个相机可见的后果：`the heavy oak door swings shut and the candle flames bend toward it`。

## 五、分层风格法（Layered Style）

不要用一个宽泛标签，拆成五层：
1. **媒介**：真人/定格/2D动画/3D渲染/微缩摄影
2. **表面纹理**：胶片颗粒/水彩晕染/纸张纹理/拉丝金属/磨砂玻璃/布料织纹
3. **调色板**：暖(橙黄红)/冷(蓝青)/低饱和粉/高对比/单色
4. **相机/渲染行为**：浅景深/微距/正交投影/手持/鱼眼
5. **运动节奏**：平滑真实/弹性挤压拉伸/断续定格动画/慢镜优雅

**源片质感锁定**：写手机日常UGC就锁`vertical handheld phone footage, slight grip sway, auto-exposure shifts`；写安全摄像头就锁`locked high-angle camera, timestamp burn-in feel, low-light noise`。缺陷词汇就是风格本身——太干净的伪UGC读起来假两遍。

## 六、去废话规则（Anti-Slop）

| 模糊词 | 替换为 |
|---|---|
| `cinematic feel`（电影感） | 具体镜头运动+光源+景深 |
| `atmosphere`（氛围感） | 空气中雾气/尘埃+色温+声音环境 |
| `premium feel`（高级感） | 材质细节+柔和光线+简洁构图 |
| `blockbuster feel`（大片感） | 广角镜头+运动速度+对比度+音效设计 |
| `texture`（质感，裸用） | 表面粗糙度+反光特性+材质类型 |

**可见性测试**：每个词必须能在画面上看到。看不到的词删掉。

## 七、13配方家族

| 家族 | 最佳用途 | 核心模式 |
|---|---|---|
| Product | 广告/电商/hero shot | 产品锚点+一个材质变化+受控镜头+logo保留 |
| Lifestyle | 生活方式/美食/旅行 | 简单动作+生活环境+手持/自然光+环境声 |
| Drama | 情绪/对白/短叙事 | 角色标签+手势+动机镜头+静默/稀疏声 |
| Music video | 节拍同步/舞蹈 | 节奏参考+可见节拍变化+光脉冲+明确站位 |
| Landscape | 定场/自然/氛围 | 慢镜头+天气运动+层次纵深+自然声 |
| Commercial | 品牌安全 | 问题/使用/结果节拍+精确产品约束+干净光 |
| Animation | 原创角色+风格化动作 | 媒介+形状语言+调色板+弹性/加权运动 |
| VFX | 变形/粒子/天气/能量 | Source+材质行为+交互+消散端点 |
| First/last frame | 中间过渡 | 首帧+尾帧+连续过渡+身份锁定 |
| Commercial campaign | 6/10/15/30s变体 | 钩子+产品证明+终态+裁切矩阵 |
| Short drama | 快切竖屏短剧 | Setup+反转+悬念+held reaction close |
| Talking head | 口播/讲解 | 锁定中近景+短引语+最小头部运动+字幕安全框 |
| Home/space tour | 空间漫游 | 单条连续take+稳定前进路径+每区光变+仅环境声 |

## 八、故障诊断树

| 症状 | 可能原因 | 首选修复 |
|---|---|---|
| 产品/脸变了 | I2V重复描述了可见身份或动作过载 | 加保留约束；删除重复静态细节 |
| 镜头跳 | 多个不兼容移动或没有端点 | 选一个移动带起止 |
| 输出泛 | 空洞风格词和弱动作 | 替换为物理动作/源光/材质/声音 |
| 动作被忽略 | 静态提示或无可见后果 | 加主体/动词/时序/改变后的终态 |
| 口型差 | 说话时头/镜头动，对白太长，未分配说话者 | 锁定构图，缩短台词，分配说话者 |
| VFX乱 | 特效无源/物理/消散 | 加source/material/path/interaction/endpoint |
| 提示词被拦 | 受保护IP/真人/图形/绕过措辞 | 用安全制作语言重写意图 |
| 延伸质量降 | 无尾帧锚点或延续中太多新变量 | 用上clip实际尾帧做首帧，每次只改一个变量 |
