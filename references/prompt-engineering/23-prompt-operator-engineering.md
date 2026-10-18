# Prompt 编程、AI 算子与自动编译工程

## 1. 目的

把自然语言创意变成可验证的“提示词程序”。这些算子是内部 IR，不应机械原样输出给不支持该语法的模型。

## 2. 基础算子

```text
LOCK(subject, property)
SET(scene, property)
PLACE(entity, relation)
MOVE(actor, path, speed, duration)
ACT(actor, action, phase)
REACT(actor, response, duration)
CAM(position, target, motion, lens)
FOCUS(from, to, timing)
LIGHT(source, direction, quality, temperature)
MATERIAL(object, property)
SOUND(source, position, timing)
KEEP(property)
CHANGE(property, from, to, timing)
CUT(reason)
MATCH(previous_state, next_state)
END(frame_state)
ASSERT(condition)
```

## 3. 示例

```text
LOCK(A, red_coat)
PLACE(A, left_of=B, 2m)
ACT(A, raise_right_hand, 1.0s)
REACT(B, eyes_shift_to_A, 0.4s)
CAM(side, A+B, slow_dolly_in, normal_lens)
LIGHT(key_left_back, warm, soft)
END(A_left_B_right, hands_unchanged)
```

然后编译为模型自然语言：

`画面左侧的A与画面右侧的B保持两米距离，A缓慢抬起右手……`

## 4. 算子检查

每个算子至少验证：

- Actor 唯一
- 时间有序
- 空间关系有来源
- 动作有可执行对象
- 终态可传递
- 没有互相冲突的 KEEP/CHANGE

## 5. Prompt 编译器

`用户白话 → 语义解析 → IR → 空间/表演/物理检查 → 模型 Adapter → 自然语言 Prompt → 反编译检查`

反编译检查：从最终 Prompt 再次提取主体、动作、位置、相机、时间，与原 IR 比较。差异超过阈值就重新编译。

## 6. 编程模式

用户说：

- “把这个镜头换成夜景” → CHANGE(light/time)
- “人物别动，只让镜头动” → KEEP(subject_state) + CAM(move)
- “上一镜结束在门边，这镜从门边开始” → MATCH(end_state, start_state)
- “只改衣服，其他不动” → CHANGE(costume) + KEEP(all_other_assets)

## 7. 自动测试

每个复杂 Prompt 至少测试：

1. 主体是否唯一
2. 主要动作是否唯一
3. 左右/前后是否明确
4. 时间是否闭合
5. 终态是否能传递
6. 模型语法是否支持
