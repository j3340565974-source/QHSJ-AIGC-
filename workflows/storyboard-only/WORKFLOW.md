# 专注分镜表制作

> 工作流 ID: `storyboard-only`

**版本**: 8.0.0

**描述**: 专注分镜表制作

## 阶段
### SB0 剧本/素材分析
**输入**: 剧本/故事描述

**输出**: 场次划分、节拍点

**模块**:
- `01-novel-screenplay`

### SB1 空间推演
**输入**: 场, 次

**输出**: 站位、轴线、机位设计

**模块**:
- `04-spatial-continuity`

### SB2 逐镜拆解（并行）
**输入**: 场次 + 空间设计

**输出**: 完整分镜表

**模块**:
- `02-storyboard-directing`
- `03-cinematography`
- `05-character-performance`
- `10-action-choreography（动作戏时）`

**并行**: True

### SB3 节奏优化
**输入**: 分镜表初稿

**输出**: 节奏优化建议、补镜/删镜建议

**模块**:
- `13-quality-gates`

## 最终产物
- 场次表
- 站位声明
- 完整分镜表
- 导演阐述

