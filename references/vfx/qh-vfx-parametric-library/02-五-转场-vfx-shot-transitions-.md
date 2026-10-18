## 五、转场 VFX（Shot Transitions）

- `match cut`：桌上旋转硬币 → 太空旋转行星。
- `whip transition`：急摇模糊厨房 → 蜡烛餐厅。
- `foreground wipe`：公交车驶过遮住画面，露出新街道。
- `jump cut`：同机位跳切，vlog 忏悔感。
- `object portal`：镜头钻进咖啡杯，棕色液体溶解成秋日森林。
- `pass-through`：穿过钥匙孔进书房，再从窗户穿出雨夜街，一个连续不可能镜头。
- `quick cuts`：早餐拆成 8 个快切，节奏打击乐。
- `screen-in-screen`：无限递归，女人看电视里自己又在看电视。

## 六、常用大气/粒子关键词库

从多源汇总，可直接拼接：
- **雾/霾**：`atmospheric haze`, `dense fog`, `volumetric fog`, `mist rolling`, `steam rising from grates`, `dust motes drifting`, `embers floating`, `ash falling`
- **雨**：`rain-slicked streets`, `rain reflections`, `drops on taxi window`, `heavy rain`, `umbrella droplets`, `rain streaks on lens`
- **雪**：`falling snow`, `blizzard`, `gentle snowfall`, `snow drifting on wind`
- **烟/尘**：`cigarette smoke drifting`, `gunsmoke`, `dust kicked up by footsteps`, `smoke billowing`, `explosion mushroom cloud`, `embers glowing`
- **火/火花**：`candle flames trembling`, `firelight dancing`, `sparks flying`, `embers as eyes`, `flames flaring from kitchen wok`, `fire dragon emerging from cracks`
- **能量/魔法**：`golden energy blade trail`, `semi-transparent holographic phantom`, `blue-white spiritual glow`, `energy shockwave rippling ground`, `particles converging into text`
- **光效**：`god rays through dust`, `lens flare`, `halation bloom`, `volumetric light cones`, `projected light patterns`

## 七、实战经验

- 粒子描述必须带**物理**：`chaotic mix of granular sand and fine dust, visible swirling tendrils` 比 `a sandstorm` 出片率高一个量级。
- 天气特效要同时写**遮挡度**（opaque wall / translucent veil）和**光线穿透**（god rays piercing through），两者对比才有体积感。
- 爆炸/火焰必须配**动态点光源**：`instant point light source during each explosion, illuminating surrounding area`——否则火光没有照亮环境，看起来像贴图。
- 不要在一个 prompt 里塞两种以上天气（`rain and snow and fog`），模型会乱。
