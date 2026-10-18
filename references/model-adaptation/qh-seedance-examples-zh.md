# QHSJ Seedance 中文示例库

---
name: seedance-examples-zh
description: "This skill should be used when the user asks for Chinese Seedance 2.0 examples, Chinese prompt patterns, example rewrites, or safe versions of working Chinese video-generation prompts."
license: MIT
user-invocable: true
tags:
  - chinese
  - examples
  - seedance-20
metadata:
  version: "6.7.0"
  updated: "2026-08-01"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-examples-zh

Use examples as language-specific patterns, not content to copy blindly. Chinese prompts should stay compact, concrete, and production-oriented. Keep reference tags such as `@Image1`, `@Video1`, and `@Audio1` unchanged.

## Intent

Some users learn by rule, but the ones who come here learn by seeing. The purpose of these examples is recognition - a working prompt close enough to their idea that they can feel the gap and close it themselves. An example that teaches is worth ten instructions.

## Example Labels

| Label | Meaning |
|---|---|
| `safe` | Original concept, no protected identity. |
| `needs-owned-reference` | Requires user-owned, licensed, public-domain, or authorized asset. |
| `surface-specific` | Depends on the active web, API, or workflow surface. |
| `rewrite-required` | Mentions protected identity, brand, celebrity, exact scene, song, or voice. |

## Safe Example Patterns

### Product I2V
```
@Image1为产品参考，严格保持logo、标签、瓶身形状和颜色不变。镜头缓慢推进到标签特写；左侧暖光扫过玻璃，水珠沿瓶身下滑，背景保持暗色静止。声音：轻微环境声，结尾一声清脆玻璃音。
```
**Label:** safe  
**Mode:** I2V  
**Why it works:** Explicitly locks product identity, adds only motion and light, includes timing and audio.

### Character Drama
```
原创角色A站在狭窄走廊，缓慢放下信封，目光停在紧闭的门上。镜头为稳定中近景并轻微推进。暖色顶灯微微闪烁，墙面有冷色雨光反射。声音：远处雨声，无配乐。
```
**Label:** safe  
**Mode:** T2V  
**Why it works:** One visible beat (lowers envelope, looks at door), motivated light, clear endpoint.

### Action
```
原创快递员在雨夜屋顶奔跑，跃过一道狭窄缝隙，落地后单膝撑住并冲向即将关闭的铁门。低机位手持跟拍，冷色屋顶灯和湿滑地面反光。声音：急促呼吸、雨声、铁门提示音。
```
**Label:** safe  
**Mode:** T2V  
**Why it works:** Clear sequence of physical actions, motivated camera (low handheld for urgency), layered audio.

### Safe Animation
```
原创二维动画沙漠信使，夸张围巾，驾驶小型风力木车穿过浅色沙丘。手绘背景质感，圆润角色造型，柔和粉彩色调，车轮带出细小沙尘。镜头侧向稳定跟拍。
```
**Label:** safe  
**Mode:** T2V  
**Why it works:** Specific visual style without referencing protected properties, clear motion, production-safe descriptors.

### First/Last Frame
```
@图片1为首帧，@图片2为尾帧。保持同一原创角色、服装和房间布局，角色从椅子上缓慢站起，走到窗边并停在尾帧姿势。动作连续自然，不跳切，不改变脸部、衣服或房间结构。镜头固定中景，仅轻微推镜。声音：安静室内环境声。
```
**Label:** safe  
**Mode:** FLF2V (First/Last Frame)  
**Why it works:** Explicitly locks identity and scene, describes continuous motion between frames, prevents drift.

### Sequence Clip 01
```
原创角色A在清晨机场出口停下，手里握着一张折起的纸条。本段只建立"她在等待某人"的线索，不出现重逢或离开。镜头横向稳定跟拍到中景，A看向到达屏并停住。声音：机场环境声、远处广播、无配乐。
```
**Label:** safe  
**Mode:** T2V (sequence beginning)  
**Why it works:** Sets up narrative without completing it, clear endpoint for continuation planning.

### Continuation (Clip 02)
```
从上一段已接受视频的真实结尾继续：A站在到达屏前，纸条仍在右手。本段只让A打开纸条，看到名字后向画面左侧抬头，不重复走出机场的动作，不提前出现对方。镜头固定中近景，轻微推镜。
```
**Label:** safe  
**Mode:** Extend/Continuation  
**Why it works:** Starts from observed state of accepted footage, advances exactly one beat, preserves continuity.

### Camera-Reference R2V
```
@图片1锁定原创角色造型和服装，@视频1仅参考运镜节奏和侧向跟拍方式，不复制人物、场景或品牌。角色在雨夜街道从画面左侧跑入，停在路灯下回头。镜头横向稳定跟拍，最后固定中景。冷色雨光，地面反射霓虹。声音：雨声、脚步声，无配乐。
```
**Label:** needs-owned-reference  
**Mode:** R2V (Reference-to-Video)  
**Why it works:** Separates identity reference from motion reference, explicitly restricts what transfers.

### Dialogue
```
原创角色A坐在厨房桌前，固定中近景。对白期间头部保持稳定，只做轻微表情变化。角色轻声说："我找到钥匙了。"柔和窗光来自画面右侧，背景有暖色台灯。声音：清晰短对白、低室内环境声、无配乐。
```
**Label:** safe  
**Mode:** T2V with dialogue  
**Why it works:** Locks camera to minimize lip-sync drift, brief dialogue, motivated light, clear audio layers.

## Rewrite Pattern

If the prompt contains protected names, translate the intent into original descriptors:

| Protected Reference | Safe Rewrite |
|---|---|
| `知名IP角色` (famous IP character) | → `原创蒙面屋顶信使` (original masked rooftop messenger) |
| `某导演风格` (specific director's style) | → `低饱和胶片质感、硬侧光、长焦压缩空间、静默表演` (low-saturation film texture, hard side light, telephoto compression, silent performance) |
| `品牌logo` (brand logo) | → `几何图案标志` (geometric pattern mark) + requires owned reference |
| `明星A` (celebrity A) | → `原创角色` (original character) + describe appearance without naming |

## Common Mistakes to Avoid

❌ **Too vague:**  
`一个女人在咖啡厅，很美，很有感觉`

✅ **Concrete and directed:**  
`原创角色A坐在咖啡厅靠窗位置，缓慢搅拌咖啡，视线望向窗外雨景。镜头：侧面中景，推进到近景。右侧柔和窗光，左侧保留暗部轮廓。声音：低咖啡厅环境声，勺子轻碰杯壁一次。`

❌ **Asking model to generate text:**  
`屏幕上显示"欢迎回家"字样`

✅ **Add text in post:**  
`手机屏幕亮起显示短信通知，不显示具体文字内容。[后期添加字幕："欢迎回家"]`

## Output Contract

Return:
1. Chinese example prompt
2. Label (safe / needs-owned-reference / rewrite-required)
3. Mode (T2V / I2V / V2V / R2V / FLF2V / Extend)
4. Brief explanation of why the pattern works
5. Safer Chinese variant when the original contains protected references
