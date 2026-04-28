---
name: p6c-insurance-mode-designer
version: 1.0.0
description: 保险模式设计器。设计以"结果担保"为核心的商业模式： 为 AI 的输出结果提供担保，出错则赔偿或免费。 基于《AI确定性商业模式》概念卡。
author: Max
tags: p6, 商业模式, 保险模式
- book-skill
- business-model
- insurance-mode
- result-guarantee
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p6c-insurance-mode-designer
stage: p6c
source_book: AI确定性商业模式
source_chapter: 第04章 保险模式

---


# 保险模式设计器

## 一句话定位

为 AI 的结果提供担保：成功才收费，失败不收费。

## 何时触发

- AI 产品的结果可以明确定义
- 用户愿意为"确定的结果"付费
- 出错的代价可以量化
- 有能力承担偶然的失败

## 输入

产品场景 + 成功标准 + 失败成本。

**示例输入**：
```
产品: AI 税务申报助手
场景: 帮助个人和企业申请税收退回
成功标准: 成功帮助用户获得税收退回
失败成本: 每次失败损失人工审核成本约 50 元
```

## 设计步骤

### Step 1: 定义"成功"标准

**任务**：明确什么算"成功"，什么算"失败"。

**输出**：
```
成功标准:
  definition: "成功的明确定义"
  measurable: "是否可量化"
  verification: "如何验证成功"
  edge_cases: ["边界情况"]
```

### Step 2: 评估风险与成本

**任务**：计算每次失败的成本和发生概率。

**输出**：
```
风险评估:
  failure_rate: "失败率估算"
  cost_per_failure: "每次失败成本"
  expected_cost: "预期成本"
  risk_mitigation: ["风险缓解措施"]
```

### Step 3: 设计收费模式

**任务**：将风险转化为可持续的收费策略。

**收费方式**：
```
收费模式:
  - 成功费: "按成功次数收费（如 $0.99/次解决）"
  - 成果分成: "按结果价值比例收费（如退税额的 10%）"
  - 保底 + 分成: "基础费 + 超额分成"
  - 订阅保险: "月费保证最大次数的成功"
```

### Step 4: 设计风险控制

**任务**：确保失败在可控范围内。

**输出**：
```
风险控制:
  max_exposure: "最大风险暴露"
  stop_loss: "止损线"
  escalation: "风险上升处理"
  insurance_pool: "是否需要风险准备金"
```

## 综合输出格式

```yaml
insurance_mode_design:
  input:
    product: "产品名称"
    scenario: "使用场景"
    success_criteria: "成功标准"
    failure_cost: "失败成本"
  
  success_definition:
    definition: "成功定义"
    measurable: "可量化"
    verification: "验证方法"
    edge_cases: ["边界情况"]
  
  risk_assessment:
    failure_rate: "失败率"
    cost_per_failure: "每次失败成本"
    expected_cost: "预期成本"
    mitigation: ["缓解措施"]
  
  pricing:
    model: "收费模式"
    unit: "计费单位"
    rate: "费率"
    example: "计算示例"
  
  risk_control:
    max_exposure: "最大暴露"
    stop_loss: "止损线"
    escalation: "上升处理"
    reserve: "风险准备金"
  
  unit_economics:
    revenue_per_success: "每次成功收入"
    cost_per_failure: "每次失败成本"
    break_even_rate: "盈亏平衡点"
    margin_at_target: "目标利润率"
```

## 示例：AI 税务申报助手

**设计**：
- 成功标准：帮助用户获得税收退回
- 收费：退税额的 10-20%
- 风险控制：最高保证 50 万元/单
- 盈亏平衡：成功率 > 60% 即可盈利

## 常见误判

- **成功标准不清**："成功"定义模糊，导致收费争议
- **低估失败率**：实际失败率高于预估，导致亏损
- **风险暴露过大**：没有设置止损线，一次大失败就倒闭

## 一句判断

> 保险模式的核心不是承担风险，而是精确计算风险并将其转化为价值。
