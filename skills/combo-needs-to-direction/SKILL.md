---
name: combo-needs-to-direction
version: 1.0.0
description: 需求发现 → 方向定界 组合 Skill。从用户痛点出发，系统跑完微需求检测、 真需求验证、四层拆解，输出可直接进入方向定界的 Direction
  Brief。
author: Max
tags: 编排器, 需求到方向
- book-skill
- combo
- needs
- direction
- ai-product
requires:
- p0a-micro-needs-detector
- p0b-real-needs-validator
- p0c-needs-decomposer
- ai-native-direction-framing
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/combo-needs-to-direction
stage: combo
source_book: AI Native 产品方法论
source_chapter: 编排器

---


# 需求发现 → 方向定界

## 一句话定位

从一个模糊的痛点线索出发，跑完需求发现全流程，直接输出 Direction Brief。

## 何时触发

- 你有一个产品想法，需要快速验证并进入方向定界
- 不想分别调用多个工具卡，需要一站式输出
- 需要从"我有一个想法"到"方向定界简报"的最短路径

## 输入

一个模糊的产品想法或痛点描述。

**示例输入**：
```
"我想做一个帮律师自动审查合同的 AI 产品"
```

## 编排流程

```
输入: 模糊想法
  ↓
【Step 1】微需求检测 (p0a)
  → 是否存在被忽视的微需求？
  → 是否需要重新定义问题？
  ↓
【Step 2】需求四层拆解 (p0c)
  → 表达层：用户说了什么
  → 场景层：问题发生在哪里
  → 处境层：谁被困住了
  → 代价层：不解决会怎样
  ↓
【Step 3】真需求验证 (p0b)
  → 5问验证：长期性、代价、补偿行为、结构性、自然存续
  → 真/伪判定
  ↓
【Step 4】方向定界准备
  → 将需求发现结果转化为 Direction Brief 输入
  → 明确问题定义、场景切入、资料条件
  ↓
输出: Direction Brief（可直接进入 p1）
```

## 综合输出格式

```yaml
direction_brief_input:
  source: "原始想法"
  
  problem_definition:
    surface_problem: "表面问题"
    deep_problem: "深层问题"
    why_different: "为什么不同"
  
  scenario_entry:
    user: "目标用户"
    scenario: "使用场景"
    pain_point: "核心痛点"
  
  evidence:
    micro_needs: ["微需求发现"]
    real_need_validation: "真需求验证结果"
    cost_evidence: "代价证据"
    compensation_behaviors: ["补偿行为"]
  
  data_readiness:
    available_data: "可获取的数据"
    data_sensitivity: "数据敏感度"
    access_difficulty: "获取难度"
  
  preliminary_judgment:
    worth_pursuing: true/false
    confidence: "high/medium/low"
    key_risks: ["风险列表"]
    next_step: "进入方向定界 (p1)"
```

## 一句判断

> 好的方向定界，始于好的需求发现。不要带着假设进入方向定界，要带着证据。
