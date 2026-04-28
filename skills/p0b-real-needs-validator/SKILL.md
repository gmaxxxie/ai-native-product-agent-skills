---
name: p0b-real-needs-validator
version: 1.0.0
description: 真需求判断五问验车器。AI 时代最危险的不是没有需求，而是伪需求太容易长得像真需求。 基于《AI rebuild product needs》工具卡。
author: Max
tags:
- book-skill
- needs-discovery
- validation
- fake-needs
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p0b-real-needs-validator
---

# 真需求判断五问

## 一句话定位

在需求评审前，用这五个问题给团队装上刹车系统——三问答不扎实，先不要做方案。

## 何时触发

- 需求评审会之前
- 团队情绪高涨，觉得"这个功能一定火"
- 需要区分"高频表达"和"真实需求"

## 输入

一条具体需求描述（不要抽象，要有主语）。

**示例输入**：
```
"希望系统支持一键催办"
```

## 输出

五问检测结果 + 真/伪需求判断 + 建议方向。

## 五个问题

### Q1: 它是不是长期存在？

**检测方法**：
- 这个问题是否在不同项目/不同团队/不同时期都出现？
- 是否已经持续了一段时间（而不是最近才被提出）？
- 如果没有 AI，这个问题是否仍然存在？

**输出格式**：
```
存续性: [long-term/medium-term/recent/fad]
跨场景验证: [yes/no/partial]
无 AI 时仍然存在: [yes/no]
```

### Q2: 它让谁持续付出了什么代价？

**检测方法**：
- 具体是哪些角色在付代价？
- 代价是时间、金钱、精力、情绪，还是职业风险？
- 这个代价是否被量化过（每次 X 分钟，每月 Y 元）？

**输出格式**：
```
付出角色: [角色列表]
代价类型: [time/money/energy/emotion/career_risk]
量化估算: [具体数字或范围]
```

### Q3: 用户有没有为它发展出补偿行为？

**检测方法**：
- 用户是否已经有固定的解决方式（即使很厘赞）？
- 这些补偿行为是否已经被视为"正常流程"？
- 是否有人专门负责处理这些补偿行为？

**输出格式**：
```
补偿行为: [列表]
已常态化: [yes/no]
专职处理人: [yes/no - 角色名]
```

### Q4: 它背后是不是有结构，而不只是偏好？

**检测方法**：
- 这个需求是否连着更大的流程缺口？
- 是否涉及角色权责、信息流、决策权的结构性问题？
- 如果解决了这个，是否会带动其他问题的解决？

**输出格式**：
```
结构性: [structural/situational/preference]
流程缺口: [具体缺口描述]
连锁效应: [yes/no - 如果有，列出]
```

### Q5: 即使没人讨论，它还会不会继续存在？

**检测方法**：
- 如果今天没人提出，这个问题是否明天仍然在？
- 是否是组织/行业/人性的常态，而不是某个人的一时想法？
- 如果不做任何处理，问题是会恶化、保持还是消失？

**输出格式**：
```
自然存续: [yes/no]
常态类型: [organizational/industry/human_nature/situational]
不处理的趋势: [worsen/stable/diminish]
```

## 综合输出格式

```yaml
real_needs_validation:
  input: "原始需求描述"
  
  q1_longevity:
    duration: "long-term/medium-term/recent/fad"
    cross_scenario: "yes/no/partial"
    exists_without_ai: "yes/no"
  
  q2_cost:
    bearers: ["角色列表"]
    cost_type: "time/money/energy/emotion/career_risk"
    quantified: "具体数字"
  
  q3_compensation:
    behaviors: ["补偿行为列表"]
    normalized: "yes/no"
    dedicated_handler: "yes/no - 角色"
  
  q4_structure:
    structural: "structural/situational/preference"
    process_gap: "流程缺口描述"
    chain_effect: "yes/no"
  
  q5_persistence:
    natural_existence: "yes/no"
    nature_type: "organizational/industry/human_nature/situational"
    trend_if_ignored: "worsen/stable/diminish"
  
  verdict:
    is_real_need: true/false
    confidence: "high/medium/low"
    pass_count: "X/5"
    reasoning: "判断理由"
  
  recommendation:
    action: "建议动作"
    priority: "P0/P1/P2"
    if_fake: "如果是伪需求，真正的问题可能是什么"
    next_step: "下一步"
```

## 使用规则

- **三问不过先停**：五问中如果有三问答不扎实，先不要做方案
- **分开记录**：把"高频表达"和"五问结果"分开记录，避免讨论被热度带跑
- **定期复盘**：已通过的需求，上线 30 天后再跑一次五问验证

## 常见误判

- **高频 ≠ 真实**：被多次提出的需求可能只是某个人的偏好
- **整齐 ≠ 可靠**：需求描述很清晰不代表问题真实存在
- **可做 ≠ 该做**：技术上能做不代表产品上该做

## 一句判断

> 真需求靠现实反复支付，伪需求靠热度和顺滑感成立。
