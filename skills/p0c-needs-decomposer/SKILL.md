---
name: p0c-needs-decomposer
version: 1.0.0
description: 需求四层拆解卡。很多团队一听到用户表达，就直接拆功能。 这张卡强迫团队先把"用户说了什么"和"用户真正被什么困住"分开。 基于《AI rebuild
  product needs》工具卡。
author: Max
tags:
- book-skill
- needs-discovery
- decomposition
- user-research
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p0c-needs-decomposer
---

# 需求四层拆解卡

## 一句话定位

把一条用户原话，逐层拆到表达、场景、处境、代价四层，找到真正该解决的问题。

## 何时触发

- 用户提出了一个需求，团队准备直接进入方案讨论
- 需要区分"用户说的"和"用户真正需要的"
- 需求评审时发现只有表达层，缺少深度

## 输入

用户的原始表达（一句话或一段话）。

**示例输入**：
```
"希望自动把消费分类做得更准"
```

## 输出

四层拆解结果 + 问题重定义 + 方案方向建议。

## 四层拆解

### Layer 1: 表达层（用户原话是什么）

**任务**：原汁原味记录用户的表达，不加工、不翻译、不推断。

**输出格式**：
```
用户原话: "..."
表达方式: [direct/indirect/complaint/wish/compliment]
表达场景: [where/when/how this was expressed]
```

### Layer 2: 场景层（问题发生在什么时候、哪一步、和谁有关）

**任务**：描绘问题发生的具体场景，包括时间、地点、角色、流程位置。

**输出格式**：
```
时间节点: [when it happens]
地点/界面: [where it happens]
涉及角色: [who is involved]
流程位置: [which step in the workflow]
频率: [how often]
```

### Layer 3: 处境层（他为什么在这里被困住，谁在补位，谁在党底）

**任务**：探索用户被困住的深层原因，找出系统性缺失和隐性代价。

**输出格式**：
```
被困原因: [why the user is stuck]
系统缺失: [what the system fails to provide]
补位角色: [who is filling the gap]
党底角色: [who bears the cost]
隐性劳动: [unseen work being done]
```

### Layer 4: 代价层（如果系统不接住，这个人会持续损失什么）

**任务**：量化用户因此承受的持续损失，包括可见和不可见的。

**输出格式**：
```
时间代价: [minutes/hours per occurrence]
金钱代价: [direct cost]
情绪代价: [frustration/anxiety/shame/etc]
机会代价: [what they miss out on]
长期损失: [churn/disengagement/etc]
```

## 综合输出格式

```yaml
needs_decomposition:
  input: "用户原始表达"
  
  layer1_expression:
    verbatim: "用户原话"
    expression_type: "direct/indirect/complaint/wish/compliment"
    context: "表达场景"
  
  layer2_scenario:
    timing: "时间节点"
    location: "地点/界面"
    roles: ["涉及角色"]
    workflow_step: "流程位置"
    frequency: "频率"
  
  layer3_situation:
    stuck_reason: "被困原因"
    system_gap: "系统缺失"
    filler_role: "补位角色"
    bearer_role: "党底角色"
    hidden_labor: "隐性劳动"
  
  layer4_cost:
    time_cost: "时间代价"
    money_cost: "金钱代价"
    emotion_cost: "情绪代价"
    opportunity_cost: "机会代价"
    long_term_loss: "长期损失"
  
  reframed_problem:
    original: "用户表面上说的"
    actual: "真正该解决的"
    why_different: "为什么不同"
  
  solution_direction:
    dont_do: "不要做的（表达层方案）"
    should_do: "该做的（处境层方案）"
    key_metric: "怎么证明做对了"
```

## 快速使用法

1. 把一条需求写在白板/文档最上面
2. 要求团队逐层补全四层内容
3. **任何一层说不出来，先不要进入方案讨论**

## 示例：完整走一遍

**原始需求**：
> "希望自动把消费分类做得更准"

**四层拆解**：

| 层次 | 内容 |
|------|------|
| 表达层 | 用户说"不想每次都手动改分类" |
| 场景层 | 通常发生在下班后、睡前或月底对账时，想快速看懂钱花去了哪里 |
| 处境层 | 他并不只是嫌麻烦，而是本来就对支出有点失控感；一旦分类不断出错，他还得重新回忆每笔钱为什么花，越改越想逃避 |
| 代价层 | 如果产品长期接不住，用户失去的不只是几次修正动作，而是对财务状况的掌握感，最后很可能直接放弃记账 |

**重定义**：
- 不要做：只是提高分类准确率
- 该做：帮助用户重新建立生活秩序感
- 关键指标：不是"分类准确率"，而是"月底对账时的焦虑程度下降"

## 常见误判

- **只有表达层**：变成功能愿望清单
- **只有场景层**：误把麻烦当成真问题
- **缺少处境层**：无法区分"想要更快"和"真的困扰"
- **缺少代价层**：无法判断优先级

## 一句判断

> 如果一条需求说不清处境和代价，它通常还不够成熟。
