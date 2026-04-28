---
name: p6a-certainty-premium-calculator
version: 1.0.0
description: 确定性溢价计算器。基于《AI确定性商业模式》核心公式， 帮助产品团队计算 AI 产品的确定性溢价，从而设计更高价值的收费模式。
author: Max
tags: p6, 商业模式, 确定性溢价计算
- book-skill
- business-model
- pricing
- certainty-premium
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p6a-certainty-premium-calculator
stage: p6a
source_book: AI确定性商业模式
source_chapter: 第02章 确定性溢价

---


# 确定性溢价计算器

## 一句话定位

计算你的 AI 产品能为用户提供多少确定性价值，从而设计更高的收费模式。

## 核心公式

```
确定性溢价 = 用户的恐惧程度 × 出错的代价 × 替代成本
```

## 何时触发

- 需要为 AI 产品设计定价策略
- 现有定价模式遇到瓶颈
- 想要从"卖功能"升级为"卖确定性"
- 需要证明 AI 产品的高价值

## 输入

产品场景 + 用户描述 + 当前定价。

**示例输入**：
```
产品: AI 合同审查助手
用户: 企业法务团队
场景: 审查供应商合同，确保没有风险条款
当前定价: 按用户数订阅，每人每月 99 元
```

## 计算步骤

### Step 1: 评估用户的恐惧程度

**定义**：用户对不确定性的敏感度（不是害怕情绪，而是对不确定性的耐受阈值）

**评估问题**：
- 用户对这个任务的准确性要求有多高？
- 出错了会有什么后果？
- 用户是否愿意为"更高的确定性"付更多钱？

**评分标准**：
```
恐惧程度评分:
  1-3: "低 - 用户对不确定性耐受度高，出错也没什么大不了"
  4-6: "中 - 用户希望准确，但能接受一定误差"
  7-10: "高 - 用户对准确性极度敏感，出错代价巨大"
```

### Step 2: 评估出错的代价

**定义**：AI 出错时用户会损失多少（金钱、职业风险、机会成本）

**评估问题**：
- 如果 AI 给错了答案，用户会损失多少钱？
- 是否会影响用户的职业发展或声誉？
- 是否会导致法律或合规风险？

**量化方法**：
```
出错代价:
  direct_cost: "直接金钱损失 (元)"
  career_risk: "职业风险 (低/中/高)"
  legal_risk: "法律风险 (低/中/高)"
  opportunity_cost: "错过的机会 (元)"
  total_estimated: "估算总代价 (元)"
```

### Step 3: 评估替代成本

**定义**：用户找到另一个同等确定性解决方案的代价

**评估问题**：
- 如果不用 AI，用户现在怎么解决这个问题？
- 现有解决方案的成本是多少？
- 市面上有没有替代品？价格如何？

**量化方法**：
```
替代成本:
  current_solution: "当前解决方式"
  current_cost: "当前成本 (元/次)"
  alternative_solutions: ["替代方案及价格"]
  switching_cost: "转换成本 (元)"
  total_alternative: "替代方案总成本 (元)"
```

### Step 4: 计算确定性溢价

**计算公式**：
```
确定性溢价 = 恐惧程度(1-10) × 出错代价(元) × 替代成本系数

替代成本系数:
  - 替代方案很多: 0.5
  - 替代方案一般: 1.0
  - 替代方案很少: 2.0
  - 几乎没有替代方案: 3.0
```

## 综合输出格式

```yaml
certainty_premium_calculation:
  input:
    product: "产品名称"
    user: "目标用户"
    scenario: "使用场景"
    current_pricing: "当前定价"
  
  fear_assessment:
    score: "1-10"
    reasoning: "评估理由"
    evidence: "支持证据"
  
  error_cost:
    direct: "直接金钱损失"
    career: "职业风险等级"
    legal: "法律风险等级"
    opportunity: "机会成本"
    total: "估算总代价"
  
  alternative_cost:
    current_solution: "当前解决方式"
    current_cost: "当前成本"
    alternatives: ["替代方案"]
    coefficient: "0.5/1.0/2.0/3.0"
  
  calculation:
    formula: "恐惧程度 × 出错代价 × 替代系数"
    certainty_premium: "确定性溢价 (元)"
    price_ceiling: "价格上限 (元)"
    price_floor: "价格下限 (元)"
    optimal_price: "建议定价 (元)"
  
  recommendation:
    pricing_model: "推荐定价模式"
    value_proposition: "核心价值主张"
    justification: "定价依据"
```

## 示例：AI 合同审查助手

**输入**：
- 产品: AI 合同审查助手
- 用户: 企业法务
- 当前定价: 每人每月 99 元

**计算**：
- 恐惧程度: 8/10（合同出错可能导致重大损失）
- 出错代价: 每次错误可能损失 10-100 万元
- 替代成本: 人工审查 500-2000 元/份，系数 2.0

**结果**：
- 确定性溢价: 8 × 50,000 × 2.0 = 800,000 元
- 建议定价: 按合同份数或风险金额比例收费，而非订阅制

## 常见误判

- **低估出错代价**：只看直接成本，忽视职业和法律风险
- **忽视替代成本**：不考虑用户现有解决方案，高估自己的价值
- **恐惧程度主观**：用自己的感受代替用户的实际恐惧

## 一句判断

> 确定性是 AI 产品最珍贵的资产，因为它直接对应着用户的恐惧。
