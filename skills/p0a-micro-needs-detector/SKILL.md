---
name: p0a-micro-needs-detector
version: 1.0.0
description: 微需求五问检测器。团队天然偏爱"大需求"，这个 Skill 把看起来很小、但可能压得很深的问题重新看见。 基于《AI rebuild product
  needs》工具卡。
author: Max
tags:
- book-skill
- needs-discovery
- micro-needs
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p0a-micro-needs-detector
---

# 微需求五问检测器

## 一句话定位

需求池里全是大词时，用这五个问题检测那些"太小不值得做"的问题，是不是真正的产品起点。

## 何时触发

- 需求池里全是大词（"协作总控台"、"智能化升级"）
- 团队觉得"这个点太碎，不值得做"
- 你怀疑真正的问题藏在系统外补偿动作里

## 输入

一个具体场景描述（不要抽象需求，要具体事件）。

**示例输入**：
```
"项目负责人总要在会后再追一遍责任确认"
```

## 输出

五问检测结果 + 判断建议。

## 五个问题

### Q1: 这个问题是不是每天都在发生，只是每次都很小？

**检测方法**：
- 这个动作是否在不同项目/不同团队重复出现？
- 是否已经成为某些角色的"默认动作"？
- 是否很少被单独讨论，但实际频率很高？

**输出格式**：
```
频率评估: [high/medium/low]
证据: [ju体观察/数据/访谈结果]
```

### Q2: 用户是不是已经为它发展出稳定的 workaround？

**检测方法**：
- 用户是否有固定的"补救步骤"？
- 这些 workaround 是否已经被视为"正常流程"？
- 是否有人专门负责处理这些 workaround？

**输出格式**：
```
workaround 列表:
1. [workaround 描述] - 频率: [x次/天/周]
2. ...

隐性成本: [时间/精力/情绪代价]
```

### Q3: 如果不做，谁会继续默默为它承担代价？

**检测方法**：
- 这个代价是平均分摊还是由某个/某几个角色党底？
- 党底的人是否是组织中最忙或最有价值的人？
- 这种代价是否会影响他们做更重要的事？

**输出格式**：
```
承担角色: [角色名称]
承担内容: [具体代价]
机会成本: [因此错过的更重要事项]
```

### Q4: 这段负担是不是带着羞耻、疲惫或责任风险，因此不容易被主动表达？

**检测方法**：
- 用户是否会在正式场合提出这个问题？
- 是否常常被用"这就是工作"或"习惯了"带过？
- 是否涉及"这不是我该做的"或"我不想让别人知道我在做这个"的心理？

**输出格式**：
```
情绪负担: [shame/fatigue/anxiety/none]
表达障碍: [用户主动提出频率 low/medium/high]
潜台词: [用户实际会说什么来描述这个问题]
```

### Q5: 一旦系统接住它，用户体感会不会明显变轻？

**检测方法**：
- 解决后，那些党底的人是否立刻少背一层心智负担？
- 是否有人会主动说"终于不用再…了"？
- 这个改变是否可以被感知到（而不是只是数据上好看）？

**输出格式**：
```
体感变化: [dramatic/moderate/subtle/none]
关键见证: [用户可能会说的话]
价值密度: [high/medium/low]
```

## 综合输出格式

```yaml
micro_needs_assessment:
  input: "原始场景描述"
  
  q1_frequency:
    score: "high/medium/low"
    evidence: "证据"
  
  q2_workaround:
    workarounds: ["列表"]
    hidden_cost: "隐性成本"
  
  q3_bearer:
    role: "承担角色"
    cost: "具体代价"
    opportunity_cost: "机会成本"
  
  q4_emotion:
    burden: "shame/fatigue/anxiety/none"
    expression_barrier: "low/medium/high"
  
  q5_relief:
   体感_change: "dramatic/moderate/subtle/none"
    value_density: "high/medium/low"
  
  verdict:
    is_micro_need: true/false
    confidence: "high/medium/low"
    reasoning: "判断理由"
  
  recommendation:
    action: "建议动作"
    priority: "P0/P1/P2"
    next_step: "下一步"
```

## 常见误判

- **小 ≠ 深**：问题小不自动等于值得做
- **隐蔽 ≠ 高价值**：隐蔽的问题也需要验证是否真的有人在乎
- **体感变化是必要条件**：如果接住了但用户感觉不到，不是好的微需求

## 一句判断

> 微需求不靠声量成立，靠重复出现的代价成立。
