# 统一对白、表演节拍、环境音、拟音、配乐与混音层次

> 工作流 ID: `audio-design`

**版本**: 3.0.0

**描述**: 统一对白、表演节拍、环境音、拟音、配乐与混音层次

## 触发条件
- 声音设计
- 音效设计
- 配音设计
- 旁白设计
- 声音分层

## 阶段
### AU0 声音意图与媒介识别
**输入**: 剧, 本, 、, 分, 镜, 、, 视, 频, 提, 示, 词, 或, 声, 音, 需, 求

**输出**: 声, 音, 目, 标, 、, 声, 音, 来, 源, 、, 对, 白, 语, 言, 和, 限, 制

**模块**:
- 模块: `../../references/audio/13-audio-sound.md`, `../../references/audio/11-audio-voice.md`

### AU1 对白与表演同步
**输入**: 声, 音, 意, 图, 、, 角, 色, 状, 态, 、, 时, 长

**输出**: 台, 词, 节, 拍, 、, 停, 顿, 、, 语, 速, 、, 气, 口, 和, 表, 演, 锚, 点

**模块**:
- 模块: `../../references/novel-screenwriting/qh-dialogue-speed-check.md`, `../../references/novel-screenwriting/qh-dialogue-doctor-7d.md`, `../../references/audio/qh-vo-os-weaving.md`

### AU2 环境音与音效分层（并行）
**输入**: 场, 景, 、, 动, 作, 、, 材, 质, 与, 空, 间

**输出**: 环, 境, 底, 噪, 、, 动, 作, 拟, 音, 、, 重, 点, 音, 效, 和, 空, 间, 混, 响

**模块**:
- 模块: `../../references/audio/11-audio-sound.md`, `../../references/model-adaptation/qh-seedance-audio.md`

**并行**: True

### AU3 同步与质量检查
**输入**: 对, 白, 、, 环, 境, 音, 、, 音, 效, 、, 时, 长

**输出**: 声, 音, 时, 间, 轴, 、, 冲, 突, 与, 缺, 口, 清, 单

**模块**:
- 模块: `../../references/quality-safety/13-quality-gates.md`, `../../references/quality-safety/qa-checklist-320.md`

## 最终产物
- 声音设计说明
- 台词/音效时间轴
- 混音层次建议
- 同步检查清单

