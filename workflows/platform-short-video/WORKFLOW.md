# 从受众与平台目标到短视频脚本、镜头节奏、声音和发布包装

> 工作流 ID: `platform-short-video`

**版本**: 8.0.0

**描述**: 从受众与平台目标到短视频脚本、镜头节奏、声音和发布包装

## 触发条件
- 短视频平台方案
- 平台短视频脚本
- 抖音短剧
- 小红书视频文案
- 视频号脚本

## 阶段
### SV0 平台和受众约束
**输入**: 用户目标、目标平台、受众、时长

**输出**: 内容目标、平台硬限制、需核实的时效性假设

**模块**:
- 模块: `../../references/platform/platform-algorithm-evidence.md`, `../../references/platform/platform-playbooks.md`

### SV1 钩子与叙事脚本
**输入**: 内容目标和用户创意

**输出**: 开场钩子、冲突节拍、完整脚本

**模块**:
- 模块: `../../references/platform/hook-library/index.md`, `../../references/platform/platform-script-patterns-180/index.md`, `../../references/platform/03-short-video.md`

### SV2 视觉节奏与声音设计（并行）
**输入**: 脚本和目标时长

**输出**: 镜头分配、屏幕动作、对白/环境音节拍

**模块**:
- 模块: `../../references/storyboard/08-storyboard-directing.md`, `../../references/cinematography/03-cinematography.md`, `../../references/audio/13-audio-sound.md`

**并行**: True

### SV3 平台交付包装与质检
**输入**: 脚本、视觉节奏、声音节拍

**输出**: 发布文案、标题候选、交付格式和风险清单

**模块**:
- 模块: `../../references/platform/platform-playbooks.md`, `../../references/quality-safety/13-quality-gates.md`, `../../references/quality-safety/15-safety-compliance.md`

## 最终产物
- 短视频脚本
- 分镜/时长分配
- 声音建议
- 平台包装建议
- 质量与合规清单

