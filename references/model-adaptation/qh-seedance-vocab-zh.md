# QHSJ Seedance 中文词表

---
name: seedance-vocab-zh
description: "This skill should be used when the user asks for Chinese Seedance 2.0 prompt wording, Mandarin cinematic vocabulary, Chinese prompt compression, or translation of camera, lighting, action, VFX, audio, and production terms into Chinese."
license: MIT
user-invocable: true
tags:
  - chinese
  - vocabulary
  - seedance-20
metadata:
  version: "6.7.0"
  updated: "2026-08-01"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-vocab-zh

Use Chinese vocabulary when the user asks for Chinese prompts, Mandarin cinematic wording, role binding, first/last-frame workflow, or maximum compactness. Chinese prompt wording is often efficient, but it must still preserve mode, reference tags, action, camera, lighting, audio, and constraints.

## Intent

Chinese production wording can use compact compounds, but compression is useful only when the shot instruction remains explicit. Keep each concise phrase tied to a visible action, camera behavior, light source, sound, or preservation constraint.

## Usage Rule

**Do not translate reference tags.** Keep `@Image1`, `@Video1`, and `@Audio1` unchanged. Use short production phrases instead of abstract adjectives.

## Core Chinese Vocabulary

| Function | Chinese wording |
|---|---|
| **Camera** | `缓慢推镜` (slow push-in), `横向跟拍` (lateral tracking), `固定中景` (locked medium shot), `低角度` (low angle), `特写` (close-up), `从剪影到正面四分之三角度` (silhouette to three-quarter frontal) |
| **Lighting** | `侧逆光` (side backlight), `柔和窗光` (soft window light), `暖色实用灯` (warm practical light), `冷色月光` (cool moonlight), `轮廓光` (rim light), `体积光` (volumetric light) |
| **Motion** | `慢慢转身` (slowly turns), `快速掠过画面` (quickly sweeps across frame), `水珠沿表面下滑` (water droplets slide down surface), `薄雾贴地扩散` (thin mist spreads along ground) |
| **Audio** | `安静环境声` (quiet room tone), `一句短对白` (one brief line of dialogue), `轻微金属声` (slight metallic sound), `无配乐` (no music), `脚步声卡点` (footsteps hit the beat) |
| **First/Last Frame** | `@图片1 为首帧` (@Image1 as first frame), `@图片2 为尾帧` (@Image2 as last frame), `自然过渡到尾帧` (natural transition to final frame), `中间动作连续，不跳切` (continuous motion between, no jump cuts) |
| **Constraints** | `严格保持logo、标签、形状和颜色不变` (strictly preserve logo, label, shape, and color unchanged), `人物面部特征完全一致` (character facial features completely consistent) |

## Compact I2V Pattern

```
@Image1为参考，严格保持[主体/产品/脸部/标志]不变；仅加入[动作/光线/镜头变化]。
镜头：[一个动作]。
声音：[音效或环境声]。
```

**Example:**
```
@Image1为参考，严格保持香水瓶外形、标签、颜色不变；瓶身表面缓慢凝结水珠，沿曲面滑落。
镜头：固定特写，焦点锁定标签。
光线：左侧柔和窗光，右侧冷蓝色轮廓光。
声音：安静环境声，细微水滴声。
```

## Script Variant Rule

When the deliverable targets 台灣, 香港, or any Traditional-script audience:
- Write prompts in **Simplified Chinese** (简体中文)
- Declare the delivery script separately for subtitles and final text
- **Never** convert between scripts using find-and-replace
- Examples of correct conversion:
  - ✅ 头发 → 頭髮 (correct Traditional form)
  - ❌ 头发 → 頭發 (incorrect mechanical conversion)

## De-Slop Rule

**Avoid vague abstract terms.** Decompose them into physical elements:

| Vague Term (要避免) | Physical Elements (用具体描述) |
|---|---|
| `电影感` (cinematic feel) | → 具体的镜头运动 + 光线来源 + 景深 |
| `氛围感` (atmosphere) | → 空气中的雾气/尘埃 + 色温 + 声音环境 |
| `高级感` (premium feel) | → 材质细节 + 柔和光线 + 简洁构图 |
| `大片感` (blockbuster feel) | → 广角镜头 + 运动速度 + 对比度 + 音效设计 |
| `质感` (texture, bare) | → 表面粗糙度 + 反光特性 + 材质类型 |

**Bad example:**
```
一个女人在咖啡馆，很有电影感，氛围感很强
```

**Good example:**
```
咖啡馆靠窗位置，一个女人慢慢搅拌咖啡，视线望向窗外。
镜头：侧面中景，缓慢推进到近景。
光线：右侧柔和窗光照亮半边脸，左侧暗部保留轮廓。
声音：低音量咖啡馆环境声，勺子轻碰杯壁一次。
```

## Key Principles for Chinese Prompts

1. **短而具体** (Short and specific) - not vague and long
2. **保留参考标签** (Preserve reference tags) - `@Image1` not `@图片1`
3. **一个动作** (One action) - not multiple events
4. **具体光源** (Specific light source) - not "美丽的光线" (beautiful lighting)
5. **声音指令清晰** (Clear audio instruction) - or explicitly state silence
6. **字幕后加** (Add subtitles in post) - never ask the model to generate text

## Output Contract

Return concise Chinese prompt text with:
- Preserved reference tags (exact spelling)
- One clear action with timing
- Specific camera behavior
- Physical light sources
- Audio or silence instruction
- Preservation constraints when needed

Optional: Provide English gloss when useful for clarification.
