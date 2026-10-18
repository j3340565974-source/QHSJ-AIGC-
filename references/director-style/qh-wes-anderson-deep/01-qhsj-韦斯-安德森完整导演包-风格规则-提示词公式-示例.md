# QHSJ 韦斯·安德森完整导演包（风格规则/提示词公式/示例/负面提示词/检查清单）

# Weisenandesen Skill

这是一个用于生成复古对称电影感图像提示词的 Codex skill。

## 用途

输入一句简短中文画面描述，例如：

```text
画面：一个沙漠里的加油站，9:16 比例
```

它会扩写成包含构图、完整提示词、色彩方案、人物动作、场景道具、氛围、反向限制和比例的完整中文图像生成提示词。

## 风格重点

- 正面平视、相机水平、地平线水平
- 严格中央对称或清晰左右平衡
- 1960s-1970s 明亮复古胶片色彩
- 手工搭建的电影布景感
- 安静、克制、轻微冷幽默
- 避免斜拍、荷兰角、歪地平线、建筑歪斜、AI 塑料感

## 安装

把整个 `weisenandesen` 文件夹复制到你的 Codex skills 目录：

```bash
~/.codex/skills/weisenandesen
```

然后在 Codex 里这样调用：

```text
../../SKILL.md 画面：一个男人在等公交
```

## 文件说明

- ../../SKILL.md：skill 主入口和工作流
- style_rules.md：视觉风格规则
- prompt_formula.md：提示词结构和输出格式
- negative_prompts.md：反向限制
- checklist.md：生成前质量检查
- examples.md：示例提示词
- `agents/openai.yaml`：agent 配置

---

# Weisenandesen

## Overview

Transform brief user ideas into Chinese image prompts that look like quiet retro film stills: strongly symmetrical by default, staged, tactile, carefully arranged, emotionally restrained, and visually playful. Do not invoke a named director as a style shortcut; express the look through concrete visual rules.

## Required References

Before producing prompts, read these files as needed:

- style_rules.md: visual grammar extracted from the reference images.
- prompt_formula.md: construction formula and output contract.
- negative_prompts.md: reusable reverse constraints.
- checklist.md: final quality gate before answering.
- examples.md: sample expansions for common short ideas.

## Workflow

1. Identify the user's core subject: person, animal, object, location, action, and emotional situation.
2. Choose one camera/composition mode from style_rules.md. Default to strict frontal symmetry with a level camera, horizontal horizon, and no tilted perspective, especially for architecture, rooms, counters, vehicles, stations, facades, empty scenes, and single-subject tableaux. Use side-on tableau, overhead stage view, through-window framing, corridor depth, close-up still life with person partly visible, low/waist-level view, or two-plane foreground/background staging only when they still preserve a clear horizontal/vertical order.
3. Build the scene with an implied order: repeated architectural or prop elements, color blocks, frames-within-frames, rows, shelves, tables, windows, stairs, or gift/box/object arrangements. Never create a visible vertical seam, pole, tile line, wire, sign support, or architectural joint that splits a face or body.
4. Expand the scene with tactile period detail: painted walls, practical lamps, numbered signs, luggage, clocks, doors, windows, trays, folded cloth, old machines, shelves, tickets, flowers, boxes, or handwritten labels.
5. Assign a restrained emotional beat plus a small action: reaching, pausing mid-step, looking sideways, sitting on the floor, peeking through a doorway, holding one object, turning away, crouching, leaning, sorting, waiting, or listening.
6. Build a bright retro palette from style_rules.md, keeping colors clean, warm, luminous, slightly vintage, and filmic. Avoid muddy gray haze.
7. Add reverse constraints from negative_prompts.md.
8. Check against checklist.md.

## Output Format

Always answer in this exact structure:

```markdown
画面标题：
构图：
完整提示词：
色彩方案：
人物与动作：
场景与道具：
氛围：
反向限制：
适合比例：
```

## Core Rules

- Write in Chinese unless the user asks otherwise.
- Make the prompt directly usable for image generation.
- Make the result look like a film still, not a poster, illustration, ad, influencer portrait, or concept art.
- Use concrete visual language: lens angle, staging, color, props, surfaces, light, expression, and spacing.
- Preserve the user's subject; enrich the scene without replacing it.
- Avoid copying identifiable characters, plots, costumes, logos, signs, or proprietary elements from references.
- Do not include named-director shorthand in the final prompt.

## Fast Defaults

If the user gives only a short idea, use these defaults:

- Camera: 默认使用正面平视、相机水平、地平线水平的静止电影镜头，尤其适合建筑正立面、房间、柜台、车站、空镜和单人舞台式画面。需要变化时，可使用侧面平视、隔窗/隔门框、长廊纵深、低机位腰平或轻微俯视，但仍必须保持画面不歪、不斜拍、不荷兰角.
- Composition: 默认强中央对称或严格正面对称；也可以是柔性对称、左右重复、框中框、成排道具、走廊纵深或前景/背景两层调度，但必须有清晰水平线、垂直线和左右平衡。中轴由布景暗示而不是画成实体线，不允许竖线穿过脸、头部或身体.
- Set: 手工搭建的电影布景, 可见几何墙面、门框、窗框、台阶、柜台、长廊或舞台纵深.
- Color: 1960s-1970s 复古胶片色, 明亮干净、暖调补光、不发灰, 粉、薄荷绿、湖蓝、芥末黄、奶油白、砖红、暖棕、橙金任选 2-4 色.
- Performance: 表情克制, 安静, 微妙冷幽默, 但动作要有情境：翻看、递出、偷看、坐下、转身、蹲下、停在半步、拿着一个不合时宜的小道具，不要总是正面站立.
- Ratio: 默认 `3:2` 或 `4:3`; 长廊、车厢、柜台可用 `16:9`; 单人、门框、建筑正立面和空镜可用 `2:3` 或 `9:16`.

---

# Checklist

生成前逐项检查：

1. 是否保留了用户原始主体和场景？
2. 是否明确写出具体镜头方式，并默认保证正面平视、相机水平、地平线水平、画面不倾斜？
3. 是否有清晰结构化秩序：严格中央对称、左右平衡、框中框、前景/背景分层、重复道具、正立面、成排陈列或中心消失点纵深构图？
4. 人物或主体是否有更有趣的调度：侧身、坐下、半身入画、背对、探出、偏在三分之一处、被前景部分遮挡、或处在动作进行中？
5. 场景是否像手工搭建的电影布景，而不是普通实拍生活照？
6. 是否有 1960s-1970s 复古胶片色彩感？
7. 色彩是否明亮、干净、温暖、轻微复古，而不是现代霓虹、整体发灰、灰雾、暗沉或恐怖？
8. 是否有成对、重复、整齐、编号或标签化的道具？
9. 人物表情是否克制、安静、带一点冷幽默？
10. 是否避免夸张表情、夸张动作和网红摆拍？
11. 是否避免海报、广告、插画、漫画、概念图语气？
12. 是否加入真实摄影、电影剧照、静止镜头、胶片颗粒等摄影质感？
13. 反向限制是否覆盖商业广告、赛博朋克、恐怖、杂乱背景、漫画插画、AI 塑料感？
14. 输出格式是否完全符合固定 9 个字段？
15. 适合比例是否与场景匹配？
16. 是否明确避免任何可见竖线、墙缝、门缝、柱子、标牌支杆或地砖缝穿过人物脸部、头部、脖子或身体？
17. 如果写了“褪色”“旧胶片”，是否同时写了“明亮干净、不发灰、暖调补光”？
18. 是否避免了斜拍、荷兰角、歪地平线、斜向透视、建筑歪斜和随手抓拍感？
19. 是否避免了证件照式正面站姿、僵硬全身居中摆拍和单调平铺构图？
20. 是否至少加入一个电影化变化：前景道具、框中框、正立面、中心纵深、成排陈列、局部近景或动作瞬间？

如果任一关键项失败，先修正再输出。

关键项：2、3、4、5、6、7、8、9、11、13、14、16、17、18、19、20。

---

# Examples

Use these examples as a range, not a template. When generating new prompts, prefer varied camera modes and small actions over repeating a centered full-body person facing the camera. Good outputs may use side-on tableau, overhead views, foreground objects, frame-within-frame, partial figures, seated poses, or action-in-progress while preserving retro color, staged order, and restrained humor.

## 1. 一个小男孩站在火车站

画面标题：迟到的站台
构图：正面平视静止镜头，站台时钟和远处铁轨形成中央轴线，小男孩站在画面正中，两侧长椅、行李箱和站牌成对排列。
完整提示词：一个小男孩独自站在复古火车站站台中央，正面平视静止镜头，中央对称构图，像手工搭建的电影布景，背后是一只圆形大钟、两排奶油色长椅和整齐摆放的旧皮箱，站台墙面有编号牌、旧车票窗口、黄铜灯和红色木门，小男孩穿整洁短外套，双手拿着过大的纸质车票，表情安静克制，像在礼貌地等待一列永远晚点的火车，1960s-1970s 复古胶片色彩，明亮干净、轻微复古褪色但不发灰，真实电影剧照质感，细腻胶片颗粒，人物脸部和身体前方没有任何竖线遮挡或切割，童话感、书本感、剧场感。
色彩方案：奶油白墙面和淡蓝站牌为主，芥末黄灯光、旧木棕长椅和砖红色门框点缀。
人物与动作：小男孩站在画面中心，身体笔直，低头看车票，表情认真但有一点冷幽默。
场景与道具：圆形大钟、旧皮箱、纸质车票、长椅、黄铜壁灯、编号站牌、售票窗口、铁轨。
氛围：安静、怀旧、童话式等待，像定格在电影中的一秒。
反向限制：不要商业广告感、海报排版、插画风、漫画风、赛博朋克、恐怖片、普通网红摄影、杂乱背景、夸张表情、现代霓虹灯、塑料质感、AI 生成感、错误透视、畸形手指、文字水印、logo。
适合比例：3:2

## 2. 一个女孩在酒店走廊

画面标题：第三间房门
构图：正面平视镜头，长走廊的地毯、吊灯和门牌形成纵深中轴，女孩站在走廊正中，两侧房门完全对称。
完整提示词：一个女孩站在复古酒店走廊中央，正面平视静止镜头，中央对称构图，长走廊像舞台布景一样向后延伸，两侧排列相同的粉色房门、黄铜门牌、壁灯和细长地毯，女孩穿简洁旧式连衣裙，手里拿着一把过大的铜钥匙，表情平静克制，像刚听见一件很荒唐但必须保持礼貌的事情，手工搭建的电影场景，1960s-1970s 复古胶片色彩，明亮干净、轻微复古褪色但不发灰，真实摄影质感，安静冷幽默，童话剧场感。
色彩方案：珊瑚粉墙面为主，黄铜金属、奶油白门框、深红地毯和少量薄荷绿装饰。
人物与动作：女孩站在画面中心，轻握钥匙，目视镜头，表情冷静。
场景与道具：对称房门、铜钥匙、门牌、壁灯、走廊地毯、清洁车、窄窗、旧电话。
氛围：礼貌的尴尬、安静、剧场感、旧酒店童话。
反向限制：不要广告图、不要海报字体、不要插画漫画、不要网红写真、不要恐怖酒店、不要杂乱走廊、不要夸张表情、不要现代极简酒店、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：16:9

## 3. 一家人在餐桌前沉默

画面标题：晚餐没有问题
构图：正面平视，餐桌长边与画面水平线平行，餐桌中央花瓶作为中轴，一家人左右对称坐开。
完整提示词：一家人沉默地坐在复古餐厅的长餐桌前，正面平视静止镜头，中央对称构图，桌中央只有一只细长花瓶和一颗橘子，两侧餐盘、银器、水杯和烛台严格对称排列，墙上挂着小幅风景画和成对壁灯，房间像手工搭建的电影布景，人物穿整洁旧式家居服，所有人表情克制安静，像一场非常正式但没人知道为什么正式的晚餐，1960s-1970s 复古胶片色彩，温暖明亮，细腻真实电影剧照，轻微颗粒，冷幽默、书本感、剧场感。
色彩方案：芥末黄墙面、奶油白桌布、橄榄绿餐椅、砖红色地毯，少量银色餐具反光。
人物与动作：一家人均匀坐在两侧，手放在桌边，互相不说话，表情礼貌而僵硬。
场景与道具：长餐桌、花瓶、橘子、餐盘、银器、烛台、壁灯、风景画、旧钟。
氛围：安静、家庭冷幽默、礼貌尴尬、像舞台上一场暂停的晚餐。
反向限制：不要广告餐桌、不要美食摄影、不要插画风、不要恐怖晚宴、不要杂乱餐具、不要夸张表演、不要网红滤镜、不要现代豪宅、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：16:9

## 4. 一只狗坐在邮局门口

画面标题：没有寄出的狗
构图：正面平视，邮局正门是中轴，狗坐在门口中央，两侧邮箱、包裹和告示牌对称排列。
完整提示词：一只狗端正地坐在复古邮局门口中央，正面平视静止镜头，中央对称构图，邮局立面像手工搭建的电影布景，奶油色门框、红色双开门、两排绿色邮箱、整齐堆放的纸包裹和写着号码的小木牌形成秩序，狗脖子上挂着一个小信封，表情安静严肃，像正在等待一封非常重要的信，1960s-1970s 复古胶片色彩，明亮干净、轻微复古褪色但不发灰，真实电影剧照质感，童话感、冷幽默、旧欧洲小镇气。
色彩方案：奶油白墙面、邮政红门、薄荷绿邮箱、旧纸棕包裹、黄铜门把手。
人物与动作：狗坐在画面中心，身体端正，目视镜头，信封垂在胸前。
场景与道具：双开门、邮箱、包裹、邮戳、木牌、黄铜门把、台阶、小地毯。
氛围：安静、可爱但不幼稚、一本正经的冷幽默。
反向限制：不要宠物广告、不要萌宠海报、不要插画漫画、不要网红宠物照、不要杂乱街景、不要夸张表情、不要现代商业招牌、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：3:2

## 5. 两个孩子在图书馆对视

画面标题：第七排书架
构图：正面平视，书架通道形成中轴，两个孩子在中轴两侧对称站立，书桌和台灯重复排列。
完整提示词：两个孩子在复古图书馆的书架通道里安静对视，正面平视静止镜头，中央对称构图，长长的书架通道像舞台布景一样延伸，左右两侧是同样高度的木书架、绿色台灯、编号抽屉和整齐书脊，两个孩子分别站在中轴两侧，手里各拿一本过大的硬壳书，表情克制严肃，像刚发现一条只有他们知道的图书馆规则，1960s-1970s 复古胶片色彩，明亮柔和，真实电影剧照质感，书本感、童话感、安静冷幽默。
色彩方案：旧木棕为主，台灯绿、奶油白纸张、暗红书脊、黄铜编号牌点缀。
人物与动作：两个孩子左右对称站立，身体笔直，互相对视，动作很小。
场景与道具：木书架、绿色台灯、编号抽屉、硬壳书、借书卡、梯子、地毯、黄铜书挡。
氛围：安静、神秘但不恐怖、书本童话感、冷幽默。
反向限制：不要魔法大片特效、不要恐怖图书馆、不要插画漫画、不要杂乱书堆、不要网红摄影、不要夸张惊讶、不要现代 LED 灯、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：16:9

## 6. 一个男人坐在洗衣房

画面标题：旋转之前
构图：正面平视，洗衣机通道形成中轴，男人坐在正中，两侧洗衣机圆门重复排列。
完整提示词：一个男人坐在复古自助洗衣房中央的木椅上，正面平视静止镜头，中央对称构图，两侧薄荷绿洗衣机圆门整齐重复，墙面是黄油黄色，天花板荧光灯沿中轴排列，男人穿红色旧式工作服，双手放在膝盖上，表情平静严肃，怀里抱着一篮叠得过分整齐的白袜子，手工搭建的电影布景，1960s-1970s 胶片色彩，真实电影剧照，明亮干净、不发灰，冷幽默、安静、剧场感。
色彩方案：薄荷绿洗衣机、黄油黄墙面、红色工作服、奶油白地砖、少量银色金属。
人物与动作：男人坐在画面中心，姿势端正，目视镜头，表情没有波动。
场景与道具：洗衣机、木椅、洗衣篮、叠好的袜子、肥皂售卖机、墙上营业时间牌、折叠桌。
氛围：平静、荒诞、机械秩序、日常小剧场。
反向限制：不要广告大片、不要现代洗衣品牌图、不要插画漫画、不要脏乱洗衣房、不要恐怖冷光、不要夸张表情、不要网红打卡照、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：16:9

## 7. 一个厨师站在粉色甜品店

画面标题：最后一块蛋糕
构图：正面平视，玻璃甜品柜和中央柜台构成中轴，厨师站在正中，两侧粉色盒子堆成对称塔。
完整提示词：一个厨师站在复古粉色甜品店中央，正面平视静止镜头，中央对称构图，玻璃甜品柜、黑白棋盘地砖和两侧粉色蛋糕盒形成舞台式秩序，厨师穿白色制服，双手托着一块小蛋糕，表情克制安静，像在宣布一件非常严肃的甜品事件，手工搭建电影场景，1960s-1970s 复古胶片色彩，明亮干净、轻微复古褪色但不发灰，真实摄影质感，童话感、书本感、冷幽默。
色彩方案：玫瑰粉墙面和蛋糕盒为主，奶油白制服、黑白棋盘地砖、少量樱桃红和黄铜灯光点缀。
人物与动作：厨师站在画面中心，托着小蛋糕，身体笔直，目视镜头。
场景与道具：甜品柜、蛋糕盒、托盘、玻璃罩、价签、壁钟、吊灯、棋盘地砖。
氛围：甜美但严肃、童话商店、安静冷幽默。
反向限制：不要食品广告、不要商业海报、不要插画漫画、不要网红甜品店、不要过度闪亮、不要杂乱柜台、不要夸张笑容、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：4:3

## 8. 一个老人站在温室里

画面标题：浇水时间表
构图：正面平视，温室拱顶和地砖形成中轴，老人站在中央，两侧盆栽等距排列。
完整提示词：一个老人站在复古玻璃温室中央，正面平视静止镜头，中央对称构图，拱形玻璃屋顶、棋盘地砖和两排盆栽形成精确秩序，老人穿橄榄绿色园丁服，手里拿着黄铜喷壶，表情严肃安静，像刚发现所有植物都提前五分钟长大，手工搭建的电影布景，1960s-1970s 复古胶片色彩，薄雾般柔和光线，真实电影剧照质感，童话感、剧场感、冷幽默。
色彩方案：薄荷绿金属框架、橄榄绿植物、奶油白地砖、黄铜喷壶、少量珊瑚花色。
人物与动作：老人站在画面中心，握着喷壶，身体端正，表情冷静。
场景与道具：玻璃拱顶、棋盘地砖、盆栽、喷壶、植物标签、木凳、温度计、旧水管。
氛围：安静、植物剧场、温柔荒诞、旧书页感。
反向限制：不要植物广告、不要现代温室科技感、不要插画漫画、不要杂乱植物堆、不要恐怖雾气、不要夸张表情、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：16:9

## 9. 两个人在火车包厢里喝茶

画面标题：茶杯之间
构图：正面平视，车窗和小桌形成中轴，两个人左右对称坐在沙发上。
完整提示词：两个人在复古火车包厢里相对坐着喝茶，正面平视静止镜头，中央对称构图，中间小桌、茶壶和车窗形成画面中轴，左右两侧是同样的天鹅绒座椅、木质墙板、黄铜阅读灯和行李架，窗外是浅色荒原缓慢掠过，两人穿整洁旧式套装，表情克制，像正在讨论一件无人愿意先说出口的小事，1960s-1970s 复古胶片色彩，温暖明亮，真实电影剧照质感，安静、书本感、礼貌冷幽默。
色彩方案：蜂蜜木色墙板、橄榄黄座椅、奶油白茶具、黄铜灯、窗外浅蓝灰。
人物与动作：两人左右对称坐着，各自端杯，互相看着但动作很小。
场景与道具：茶壶、茶杯、小桌、车窗、天鹅绒座椅、行李架、皮箱、阅读灯。
氛围：礼貌紧张、安静移动感、旧旅行小说气质。
反向限制：不要商业旅行广告、不要海报排版、不要插画漫画、不要现代高铁、不要杂乱包厢、不要夸张表情、不要赛博朋克、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：16:9

## 10. 一个女孩站在电梯口

画面标题：请勿使用电梯
构图：正面平视，电梯门位于中轴，女孩站在电梯门前，左右告示牌、椅子和墙面线条对称。
完整提示词：一个女孩站在复古建筑的电梯口中央，正面平视静止镜头，中央对称构图，电梯门、楼层指示牌和地毯形成中轴，两侧是木质墙板、黑色告示牌、细脚椅、盆栽和旧式按钮，女孩穿整洁短外套，手指停在按钮前但没有按下，表情安静克制，像正在认真遵守一条非常荒唐的规定，手工搭建的电影布景，1960s-1970s 复古胶片色彩，暖橙和旧木色，真实电影剧照质感，冷幽默、剧场感、怀旧。
色彩方案：暖橙电梯门、旧木棕墙板、奶油白线条、黑色告示牌、少量绿色盆栽。
人物与动作：女孩站在画面中心，手指靠近按钮，目视侧方，表情冷静。
场景与道具：电梯门、楼层指示牌、按钮、告示牌、细脚椅、盆栽、地毯、墙面线条。
氛围：荒诞规则、安静等待、旧酒店或旧办公楼的剧场感。
反向限制：不要商业地产广告、不要现代电梯厅、不要插画漫画、不要恐怖电梯、不要杂乱背景、不要夸张惊恐、不要网红拍照、不要 AI 塑料感、不要可见中轴实体线、不要竖线切脸、不要整体发灰。
适合比例：4:3
