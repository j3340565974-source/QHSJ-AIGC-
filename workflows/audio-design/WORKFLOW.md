# 统一对白、表演节拍、环境音、拟音、配乐与混音层次

> 工作流 ID: `audio-design`

**版本**: 7.0.0

**描述**: 统一对白、表演节拍、环境音、拟音、配乐与混音层次

## 触发条件
- 声音设计
- 音效设计
- 配音设计
- 旁白设计
- 声音分层

## 阶段
### AU0 声音意图与媒介识别
**输入**: 剧本、分镜、视频提示词或声音需求

**输出**: 声音目标、声音来源、对白语言和限制

**模块**:
- 模块: `../../references/audio/13-audio-sound.md`, `../../references/audio/11-audio-voice.md`

### AU1 对白与表演同步
**输入**: 声音意图、角色状态、时长

**输出**: 台词节拍、停顿、语速、气口和表演锚点

**模块**:
- 模块: `../../references/novel-screenwriting/qh-dialogue-speed-check.md`, `../../references/novel-screenwriting/qh-dialogue-doctor-7d.md`, `../../references/audio/qh-vo-os-weaving.md`

### AU2 环境音与音效分层（并行）
**输入**: 场景、动作、材质与空间

**输出**: 环境底噪、动作拟音、重点音效和空间混响

**模块**:
- 模块: `../../references/audio/11-audio-sound.md`, `../../references/model-adaptation/qh-seedance-audio.md`

**并行**: True

### AU3 同步与质量检查
**输入**: 对白、环境音、音效、时长

**输出**: 声音时间轴、冲突与缺口清单

**模块**:
- 模块: `../../references/quality-safety/13-quality-gates.md`, `../../references/quality-safety/qa-checklist-320.md`

## 最终产物
- 声音设计说明
- 台词/音效时间轴
- 混音层次建议
- 同步检查清单

