---
name: p0-needs-orchestrator
version: 1.0.0
description: 需求发现编排器。协调微需求检测、真需求验证、需求拆解、需求考古、好问题生成、Agent 边界设计六个工具卡， 按顺序执行并输出完整的需求发现报告。
  基于《AI rebuild product needs》读者工具箱。
author: Max
tags: p0, 需求发现, 编排器
- book-skill
- needs-discovery
- orchestrator
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p0-needs-orchestrator
stage: p0
source_book: AI rebuild product needs
source_chapter: 编排器

---


# 需求发现编排器

## 一句话定位

从一个模糊的痛点线索出发，系统性地跑完六个工具卡，输出可直接进入方向定界的需求发现报告。

## 何时触发

- 你有一个产品想法或痛点线索，需要系统性验证
- 需要从需求发现到方向定界的完整过程
- 想要确保需求判断有结构化依据

## 输入

一个模糊的产品想法或痛点描述。

**示例输入**：
```
"我想做一个 AI 客服产品，帮企业自动回复客户问题"
```

## 编排流程

```
用户输入
  ↓
【Step 1: 微需求检测】p0a-micro-needs-detector
  → 输出: 是否存在被忽视的微需求
  ↓
【Step 2: 需求四层拆解】p0c-needs-decomposer
  → 输出: 表达层/场景层/处境层/代价层
  ↓
【Step 3: 真需求验证】p0b-real-needs-validator
  → 输出: 真/伪需求判断
  ↓
【Step 4: 需求考古】p0d-needs-archaeologist
  → 输出: 深层需求 + 历史约束
  ↓
【Step 5: 好问题生成】p0e-good-question-generator
  → 输出: 六维度研究问题
  ↓
【Step 6: Agent 边界设计】p0f-agent-boundary-designer
  → 输出: 完整边界文档
  ↓
输出: 需求发现报告
```

## 每个 Step 的输入输出

### Step 1: 微需求检测

**输入**：用户原始想法
**输出**：
```yaml
micro_needs:
  found: true/false
  needs: ["发现的微需求列表"]
  recommendation: "是否需要重新定义问题"
```

### Step 2: 需求四层拆解

**输入**：用户原始想法
**输出**：
```yaml
decomposition:
  layer1: "表达层"
  layer2: "场景层"
  layer3: "处境层"
  layer4: "代价层"
  reframed_problem: "重定义的问题"
```

### Step 3: 真需求验证

**输入**：重定义后的需求
**输出**：
```yaml
validation:
  is_real: true/false
  pass_count: "X/5"
  confidence: "high/medium/low"
  if_fake: "如果是伪需求，真正的问题可能是"
```

### Step 4: 需求考古

**输入**：已验证的需求
**输出**：
```yaml
archaeology:
  deep_need: "深层需求"
  constraints: ["约束条件"]
  historical_attempts: ["历史尝试"]
  productizable: "yes/no"
```

### Step 5: 好问题生成

**输入**：深层需求
**输出**：
```yaml
good_questions:
  dimensions: ["六个维度的问题"]
  best_question: "最佳研究问题"
  research_direction: "研究方向"
```

### Step 6: Agent 边界设计

**输入**：产品场景
**输出**：
```yaml
boundary:
  decision: "决策权边界"
  data: "数据边界"
  action: "行为边界"
  responsibility: "责任边界"
  human_ai: "人机协作边界"
```

## 综合输出格式

```yaml
needs_discovery_report:
  input: "原始想法"
  
  executive_summary:
    verdict: "需求是否成立"
    confidence: "high/medium/low"
    key_finding: "最重要的发现"
    recommendation: "建议动作"
  
  detailed_findings:
    micro_needs: "Step 1 结果"
    decomposition: "Step 2 结果"
    validation: "Step 3 结果"
    archaeology: "Step 4 结果"
    good_questions: "Step 5 结果"
    boundary: "Step 6 结果"
  
  next_steps:
    if_proceed: "如果继续，进入方向定界的准备"
    if_revisit: "如果需要回顾，重新定义的方向"
    if_stop: "如果停止，为什么"
  
  artifacts:
    direction_brief_input: "可以直接作为 p1-direction-framing 输入的内容"
```

## 使用方式

### 方式一：完整流程

```
我有一个想法: [描述]
帮我跑完需求发现流程
```

### 方式二：单独调用某个工具卡

```
帮我用微需求五问检测这个场景: [描述]
帮我做需求四层拆解: [需求]
帮我验证这个需求是不是真需求: [需求]
```

### 方式三：跳过某些步骤

```
需求已经验证过了，直接进入需求考古
边界设计已经有了，跳过 Step 6
```

## 与其他 Skill 的关系

- **上游输入**：用户的灵感、痛点、市场观察
- **下游输出**：p1-direction-framing（方向定界）
- **并行使用**：可以在 p1 过程中反复调用验证

## 一句判断

> 需求发现不是一次性活动，而是持续验证的过程。每个工具卡都是一个检查点，而不是最终答案。
