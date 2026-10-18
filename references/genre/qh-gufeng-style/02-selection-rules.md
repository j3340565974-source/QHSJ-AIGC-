## Selection rules

- Select by light behavior and exposure, not dynasty or clothing color.
- If the anchor shows bright subjects against a dark room with crisp reflections, choose near-axis flash.
- If the anchor shows warm, soft close faces and glowing jewelry, choose low-light soft key with diffusion.
- If the anchor shows visible patterned sunlight, choose hard side-back light.
- If full robe mass and dark negative space dominate, choose ceremonial tableau.
- If translucent fabric visibly encloses the scene, choose gauze-enclosed backlight.
- If the scene is outdoors, choose the closest engine first, then apply exactly one exterior adapter from [outdoor-translation.md](#outdoor-style-translation).

---

# Outdoor Style Translation

Apply one exterior adapter after selecting the primary reference anchor and photographic engine. The exterior changes the physical light source and layering, not the underlying style.

## Shared exterior invariants

- Keep the face, pale fabric, metal, snow, water, or mist locally brighter than the environment by about 1.5–2.5 stops.
- Keep only 10–30 percent of the frame in direct or near-direct light. Let the rest retain deep colored shadow.
- Use a foreground obstruction with recognizable physical origin: foliage, doorway, fabric, rock, snow, reeds, smoke, terrain, or water reflection.
- Use one dominant color field, one warm or saturated anchor, and deep blacks. Do not default to teal-orange separation.
- Preserve the anchor's optical softness. Bloom bright edges and specular highlights; do not blur the entire scene.
- Avoid “高动态范围、超写实高细节、人物全身清晰锐利” unless the user explicitly prioritizes technical clarity over this style.

## Adapter A: shaded grove or bamboo forest

Use for bamboo, dense woodland, garden shade, reeds, or overgrown paths.

- Place the subject mainly in shade or broken shade.
- Let one side-back sun patch catch the cheek, hat, hair, sleeve, sword edge, or translucent fabric—not the full body.
- Keep trunks and leaves as dark graphic masses rather than fully resolved scenery.
- Use foreground leaves at different distances; at least one layer should partially cover the body or frame edge.
- Mist must be thin, irregular, and visible only where light touches it. Avoid evenly milky air.

## Adapter B: courtyard or architectural exterior

Use for temple gates, corridors, palace courtyards, stone steps, walls, or bridges.

- Use eaves, doors, columns, screens, or walls to divide sun and shadow.
- Keep the face near a shadow boundary rather than centered in open sun.
- Allow pale clothing or a wall edge to clip slightly while the doorway, hall, or eaves remain near-black.
- Prefer doorframe or column obstruction and a slightly tilted or compressed composition over a clean establishing shot.

## Adapter C: overcast, snow, or pale landscape

Use for snowfields, cloudy mountains, foggy water, pale stone, or overcast gardens.

- Treat snow, sky, water, or mist as a large luminous surface, not an excuse to lift the subject's shadows.
- Keep faces one half to one stop below the brightest landscape and preserve dark hair, eyes, belts, weapons, or trees as strong anchors.
- Use a small warm skin, red, gold, amber, or dark green accent to prevent grey collapse.
- Reduce atmospheric detail behind the subject while maintaining one sharp physical foreground edge.

## Adapter D: dusk or night exterior

Use for lantern courtyards, wet streets, moonlit gardens, night forests, or temple steps.

- Choose either near-axis flash or one local warm key; do not combine moonlight, lanterns, rim lights, and broad fill equally.
- Let lanterns, wet stone, metal, silk, and eyes create small highlight blooms against near-black space.
- Preserve rapid falloff and imperfect flash reflections. Avoid bright blue fantasy moonlight and luminous fog everywhere.

## Action intensity

Choose one level deliberately:

1. **Still presence** — standing, sitting, waiting, looking back, hand near sword; best match for the intimate editorial DNA.
2. **Transitional action** — turning, stepping, drawing or returning a sword, catching a sleeve; preferred default for wuxia.
3. **Explosive action** — leaping, spinning, striking, falling; use only when requested. Require 15–30 percent physical foreground occlusion and at least one natural crop among the feet, sword tip, outer sleeve, hat edge, or trailing hem. Keep one functional action line and blur secondary motion. Never preserve the complete head-to-toe silhouette and full weapon together.

For levels 2–3, keep the nearest eye, one main hand, and the weapon direction readable. Let sleeves, hems, hair tips, leaves, dust, rain, or snow move together. Avoid a perfectly isolated silhouette, centered full-body pose, or every airborne element frozen sharp.

## Exterior failure signatures

Classify the result as an exterior style mismatch when three or more appear:

- standard teal-orange cinematic grading;
- strong rays crossing most of the frame;
- every tree, leaf, costume fold, and hair strand is resolved;
- full-body rim light creates a clean hero silhouette;
- the pose reads as a game skill or character poster;
- the landscape is brighter or more important than the face and gesture;
- fog is evenly distributed and grey;
- foreground leaves act only as decoration and do not create spatial obstruction;
- skin is digitally crisp while the background is generic bokeh;
- action is fully explained rather than caught mid-transition.
- a large action prompt asks to preserve the complete hat, head, torso, both legs, trailing fabric, and full weapon.

Correct by changing no more than three variables: background exposure, action completeness, and optical/selective-focus behavior usually have the highest impact.

---

# Prompt Templates

Use these blocks selectively. Do not append every block to one prompt.

## Reference-led master structure

```text
以参考图[编号]作为唯一主锚点，只提取其摄影机位、人物占比、光线机制、环境曝光、柔焦程度和色彩关系；参考图[可选编号]只用于服装／动作。人物必须为不同的原创成年面孔，不复制参考人物，不生成参考图中的文字、水印或品牌。

[画幅]，真实古风时尚摄影。[摄影机距离、焦段、倾斜、景别和裁切]。[人物数量]位原创成年人物。[单人时写姿态、视线、手势与自我沉浸；多人时写身体关系、未完成动作与错开视线]。[服装体量、袖子、裙摆、冠饰和材质]。

前景[身体、衣袖、镜框、帘子或器物]形成[遮挡比例和虚实]；人物主体占[比例]；背景保持[暗环境、镜面、木质空间或仪式大厅]，道具只作为纹理，不承担解释剧情的作用。

采用[唯一摄影机制]：主光或闪光位于[方向]，环境比人物低[档位]；[皮肤、锦缎、金属、珍珠、玻璃]产生不同高光。允许[局部过曝、闪光反射、斑驳光或烛光]，但保留面部结构和深色背景。

使用[柔焦强度]的旧镜头扩散，高光在[金饰、珍珠、灯、丝绸、镜面]周围产生奶油色晕染，降低数字边缘锐度；眼睛、睫毛、鼻翼、唇线和主要手势仍可读。整体色彩采用[主色洗＋一到两个色彩锚点＋深黑背景]，真实时尚杂志摄影，不生成文字和水印。
```

## Near-axis flash block

```text
室内环境曝光压低约1.5—2.5档，一枚靠近镜头轴线的小型闪光灯直接提亮人物皮肤、浅色衣料、玻璃、珍珠与金属；保留轻微闪光衰减和针尖反射，背景灯具与深色木器仍沉入近黑。闪光高光经过轻度光学扩散产生柔和晕圈，但不能变成大面积柔光箱效果。画面具有夜间时尚杂志抓拍感，而不是均匀通透的日光写真。
```

## Low-light bloom block

```text
使用一盏靠近正面或前侧的低照度柔光照亮脸部，背景保持深红木色、酒红黑或近黑；侧后方只有极少量暖色轮廓光。金冠、珍珠、眼睛水光、嘴唇、烛火和锦缎高光产生明显但克制的奶油金晕染，人物轮廓柔软，主要五官仍然可读。允许画面统一偏桃金、琥珀或赤金，但黑位必须深，不能漂成灰褐色。
```

## Dappled hard-light block

```text
一束方向明确的侧逆硬光穿过建筑格栅或帘隙，只在衣袖、头冠、墙面和局部脸侧留下不规则亮斑；其余空间保持深暗。允许亮色锦缎和近镜头边缘局部接近过曝，正面仅以微弱反射光保留眼睛和五官，不将整个房间补亮。
```

## Exterior style-translation block

Use for bamboo forests, gardens, courtyards, snow, mountains, ruins, or wilderness. Combine it with one capture engine rather than replacing that engine:

```text
外景只改变空间，不改变主锚点的摄影机制。环境曝光比人物局部受光面低约1.5—2.5档，阳光、天光或雪地反射只照亮脸侧、衣料边缘、发丝、武器或少量雾气，树林、建筑、地形和天空不能全部清楚。以前景竹叶、门框、岩石、衣袖、薄雾、雪片或地面形成不规则遮挡，主体不是完整展示在干净背景前。暗部保留墨绿、青黑、炭灰、深土色或近黑的颜色密度，不采用灰绿色雾霾或青橙商业调色。光学柔化集中在透光纱边、金属、雪、雾、水面和逆光叶片，眼睛、唇线、主要手势与动作方向仍然可读。
```

## Exterior action block

```text
动作停在转折、失衡或尚未完成的一瞬，不使用完整英雄定格。面部、近侧眼睛、一只主要手和武器作用线位于清楚焦平面；高速运动的远侧衣袖、衣摆、发梢、落叶、雪或尘土保留方向一致的轻微运动模糊。必须让前景织物、竹叶、门框、岩石、薄雾或雪实际遮挡人物约15%—30%，并让脚部、剑尖、外侧衣袖、斗笠边缘或拖尾中至少一项自然切出画面。禁止同时写“完整保留全身、双腿、头部与整把武器”。即使是腾空、旋身或挥剑，也要像被偶然截取的时尚电影瞬间，而不是游戏角色技能展示。
```

## Exterior anti-poster correction

Append when the output looks like a game character, commercial wuxia poster, or generic cinematic hero shot:

```text
保持人物身份、服装和动作方向不变，取消HDR阴影恢复、青橙调色、完整轮廓光、标准体积光柱、全身英雄式展示与所有飞扬元素同时锐利。背景整体压暗约1.5档，只保留少量方向明确的斑驳亮区；收紧或倾斜构图，以竹叶、衣袖、门框、岩石、薄雾或雪形成真实前景遮挡。人物只让近侧眼睛、脸部、一只手和武器作用线清楚，其余运动部分自然柔化。降低皮肤、衣纹、头发与树林的数字微反差，高光仅在纱边、剑刃、发丝、雾或雪周围产生局部旧镜头晕染。
```

## Ceremonial full-body block

```text
稳定竖幅全身构图。单人版本让人物独坐、侧立或缓步，完整保留头冠、宽袖、长袍与拖地裙摆，以手势、视线和衣摆方向形成张力；双人版本可一人坐、一人站，以高低差和轻微触碰建立关系。单一宽幅暖光从高位前侧落下，人物比大厅亮约2档，背景形成大面积有层次的近黑；金色织锦保持厚重体量，深红内层成为主要色彩锚点，柔焦克制，不使用明亮窗光和杂乱前景。
```

## Gauze-enclosed block

Use only when literal curtains or canopy fabric are visible in the anchor:

```text
半透明粉色或香槟色纱帐真实包围人物，并在镜头前形成大面积但不规则的透光层；暖色逆光或烛光从纱后穿透，使褶皱、纤维和边缘发亮。人物通过纱缝或弱正面反射光保持可读，允许一张脸、肩膀或前景织物轻微失焦。整幅画面统一在桃粉、玫瑰与琥珀色中，但保留深红棕阴影和金色亮点。不要将纱帐变成洁白窗帘或明亮日光房。
```

## Anti-commercial correction

Append when the output looks like a clean hanfu advertisement:

```text
保持人物、服装与动作不变，取消明亮均匀的自然日光、完整阴影恢复、清楚分离的所有颜色和商品目录式锐度。环境整体压暗约1.5档，人物改由靠近镜头方向的单一光源或近轴闪光提亮；收紧画面并增加少量衣袖、身体、镜框或柔焦前景遮挡。降低数字边缘锐度，让金饰、珍珠、灯光和丝绸高光产生奶油色晕染；删除过度解释剧情的纸条、茶杯、花枝或扇子，单人只保留一个有情绪的未完成手势，多人只保留身体关系与一个未完成互动。
```

## Skin correction

```text
面部保持可读而非临床锐利：眼睛、睫毛、鼻翼、唇线、眉毛和主要轮廓清楚，皮肤保留轻微毛孔、眼下过渡和色泽变化；降低数字微反差与美容广告锐度。柔焦优先扩散金属、珍珠、烛火、镜面和丝绸高光，其次轻微软化皮肤边缘，不能把瞳孔、鼻孔和嘴唇磨成一片。
```

## Compact negative block

```text
避免明亮均匀的古装商业写真、清新日光生活照、武侠角色海报、游戏技能展示、青橙商业调色、标准体积光柱、完整全身轮廓光、超高动态范围、所有阴影被补亮、商品目录锐度、每种颜色都鲜明分离、空旷干净背景、正中对称摆拍、无意义增加第二个人物、多人面孔同样正面同样清晰、解释剧情的突出道具、所有飞扬元素同时锐利、全局灰雾、全局高斯模糊、塑料皮肤、相同面孔、廉价亮金、CGI、手指与首饰融合、文字、品牌和水印。
```

Keep the negative block focused. Use the selected engine's avoid list instead of combining every possible failure.

---

# Reference Cluster Guide

Use this guide for reference sets resembling ornate two-woman guofeng editorials. Select one cluster as the primary anchor; do not blend all clusters.

## A. Red-gold close face cluster

**Visual cues:** two faces pressed close, oversized gold crowns, red brocade filling the lower frame, one face looking outward and the other lowered, warm blooming highlights.

**Engine:** low-light soft key with highlight diffusion.

**Prompt priorities:** 50–85 mm close distance, faces and crowns occupy most of the frame, red sleeves form foreground mass, dark background, warm frontal light, strong gold halation, one primary face and one softer face.

**Do not add:** windows, outdoor scenery, explanatory hand props, clean garment separation, or bright neutral daylight.

## B. Gold ceremonial full-body cluster

**Visual cues:** one seated and one standing, long gold robes over deep red inner garments, full crowns, large dark hall, still hand contact.

**Engine:** low-key ceremonial tableau.

**Prompt priorities:** complete garment silhouette, stable vertical framing, broad warm key, deep black negative space, gold texture with restrained bloom, red inner layer as the chromatic anchor.

**Do not add:** strong lens flare, cluttered dressing-table props, casual smiles, or high-key pastel light.

## C. Dappled gold architectural cluster

**Visual cues:** pale gold robes, one woman leaning toward the other, hard bright patches on fabric or wall, dark architecture, a blown soft foreground edge.

**Engine:** hard side-back or dappled sunlight.

**Prompt priorities:** directional patterned light, deep shadow, slight off-axis crop, selective highlight clipping, architectural edge or near-camera obstruction, intimate lean.

**Do not add:** evenly filled faces, bright outdoor garden exposure, or whole-frame gauze.

## D. Pale Song-style editorial cluster

**Visual cues:** ivory, pale blue, pale blush, simple floral hairpieces, dark wood interiors, whispering or walking pair, occasional tilt, movement or mirror edge.

**Engine:** choose from near-axis flash, low-light soft key, or hard daylight according to the individual anchor. The clothing does not determine the engine.

**Prompt priorities:** light fabric against dark wood, asymmetrical two-person arrangement, restrained jewelry, one gesture, mild optical softness, controlled foreground or frame edge.

**Do not add:** generic high-key “清新汉服写真,” fully even daylight, or strict historical catalog posing.

## E. Modern opulent flash cluster

**Visual cues:** dark luxury room, mirrors, chrome, black lacquer, glassware, long legs or body silhouettes, pale embroidered clothing, reflected practical lights.

**Engine:** near-axis flash with dark ambient.

**Prompt priorities:** 28–45 mm, room underexposed, subjects lifted by flash, bright skin and glossy materials, mirror repetition, snapshot immediacy, dense objects around the edges.

**Do not add:** pastoral architecture, clean studio backdrop, broad window light, or vintage haze that erases flash reflections.

## F. Pink canopy boudoir cluster

**Visual cues:** translucent pink curtains, candlelight, flowers, vanity objects, overhead or layered viewpoints, foreground body or fabric out of focus, warm rose-amber enclosure.

**Engine:** gauze-enclosed backlight or low-light soft key with diffusion.

**Prompt priorities:** fabric physically surrounds the scene, warm backlight passes through it, candle or vanity practicals, high or oblique camera, bodies at different depths, localized haze and reflective jewelry.

**Do not add:** bright white window curtains, clean daylight, minimal empty backgrounds, or separately saturated pastel color blocks.

## Anchor selection examples

- “像第一张红衣双人特写” → choose A only.
- “金色礼服全身对视” → choose B only.
- “像透过帘子看床边闺阁” → choose F, not generic window light.
- “淡色汉服但要奢靡夜景” → choose D for wardrobe and E for the primary capture engine.
- “随意发挥，保持这组味道” → choose one cluster deliberately and disclose it briefly before generation; do not average all six.

---

# Shared Visual DNA

These traits recur across the reference family even when lighting and costume change.

## Editorial relationship

- Usually feature two adult women in close emotional or physical proximity.
- Use whispering, crown adjustment, hand contact, leaning, mirrored grooming, or one figure resting against another.
- Freeze the gesture before completion; avoid explicit narrative exposition.
- Keep eye-lines unequal: one looks outward, one looks down, one watches the other, or one face turns away.
- Allow sensual or ceremonial tension without copying a real celebrity or existing character.
