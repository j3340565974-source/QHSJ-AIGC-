# 专门管理人物、场景、道具资产规格、参考图、版本锁与分镜引用，避免跨镜头漂移。

> 工作流 ID: `asset-lock`

**版本**: 3.0.0

**描述**: 专门管理人物、场景、道具资产规格、参考图、版本锁与分镜引用，避免跨镜头漂移。

## 触发条件
- 人物资产锁定
- 角色资产锁定
- 场景资产锁定
- 资产冻结
- 锁定人物和场景
- 先锁定角色和场景
- 分镜资产引用角色图
- 分镜图引用场景图
- 资产版本锁定
- 先做人设和场景再分镜
- 人物场景资产定稿后再分镜
- 分镜图引用已锁定场景图
- 分镜图引用已锁定人物图
- 角色外观不要变化
- 场景布局不要变化

## 准入条件
- 用户提出锁定资产、跨镜引用、版本管理或资产漂移修复。

## 输入
- Canon
- asset_state
- reference assets
- downstream shots

## 输出
- asset specification
- canonical asset versions
- lock ledger
- dependency impact report

## 阶段
### L0 资产来源和版本清点
**输入**: 现有资产文件, Canon, 项目状态

**输出**: 资产目录, 版本冲突表, 缺失文件表

**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/asset/asset-ledger.md`

### L1 锁定字段和可变字段定义
**输入**: 资产目录, 用户约束

**输出**: 不可变字段, 可变字段, 版本策略

**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../examples/templates/asset-lock-ledger.md`

### L2 图像/规格质量核验
**输入**: 资产图和规格

**输出**: 身份一致性、拓扑一致性、来源一致性和材质检查

**模块**:
- 模块: `../../references/asset/p1-asset-validation-cases-500.md`, `../../references/quality-safety/16-quality-gates.md`

### L3 锁定资产引用与下游依赖扫描
**输入**: 通过核验的资产版本, 分镜/提示词/图像产物

**输出**: 锁定台账, asset_dependency_index, needs_recheck 清单

**模块**:
- 模块: `../../references/asset/qhsj-asset-locking-protocol.md`, `../../references/spatial/qhsj-spatial-gaze-distance-ledger.md`, `../../schemas/project-state.schema.json`

### L4 修复与回归
**输入**: 缺陷清单, 受影响产物

**输出**: 修复记录, 相关产物回归报告

**模块**:
- 模块: `../../references/core/qhsj-multiagent-review-protocol.md`, `../../references/quality-safety/16-quality-gates.md`

## 最终产物
- 资产锁定台账
- 规范版本引用清单
- 下游依赖影响报告
- 未解决项

