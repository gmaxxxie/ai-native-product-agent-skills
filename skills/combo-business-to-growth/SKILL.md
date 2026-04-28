---
skill:
  name: combo-business-to-growth
  version: 1.0.0
  description: >-
    商业模式 → 增长策略 组合 Skill。将确定性溢价定价策略与 AI Native 增长飞轮匹配，
    输出定价-增长联动策略，确保商业模式和增长方式自洽。
  author: Max
  tags: [book-skill, combo, business-model, growth, pricing, ai-product]
  requires: [p6-business-model, p7-marketing-growth]
---

# 商业模式 → 增长策略

## 一句话定位

商业模式和增长策略必须自洽——确定性溢价定价 × AI Native 增长飞轮 = 可持续增长。

## 何时触发

- 商业模式和增长策略不一致（如高价低增长、低价高流失）
- 需要确保定价方式和获客方式匹配
- 需要从商业模式推导增长策略，而不是反过来

## 输入

商业模式方案 + 当前增长数据。

**示例输入**：
```
商业模式: 保险模式 - 按成功解决次数收费，失败不收费
当前增长: 月新增 200 用户，月流失 150 用户
问题: 增长覆盖不了流失
```

## 匹配逻辑

### 匹配 1: 定价方式 × 获客方式

```
定价方式          最佳获客方式             不匹配的获客方式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
按结果收费        案例驱动、口碑传播        广告投放（解释成本高）
订阅制            产品体验驱动、免费试用     电话销售（CAC太高）
部署费+维护       销售驱动、POC验证         自助注册（信任不足）
按准确度分成      数据驱动、效果展示         品牌广告（无法量化）
```

### 匹配 2: 收入结构 × 增长飞轮

```
收入结构          需要的飞轮类型
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
按结果收费        需要数据飞轮：更多使用→更好结果→更多使用
订阅制            需要预测性留存：降低流失→提升LTV→覆盖CAC
部署费+维护       需要口碑飞轮：成功案例→信任→更多客户
按准确度分成      需要意图预测飞轮：更准预测→更高分成→更多数据
```

### 匹配 3: 确定性维度 × 营销策略

```
确定性维度        营销策略重点
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
事实确定性        展示验证方法、公开准确率测试
合规确定性        展示认证、审计报告、安全白皮书
结果确定性        展示成功案例、效果对比、退款承诺
```

## 综合输出格式

```yaml
business_growth_alignment:
  input:
    business_model: "商业模式"
    pricing: "定价方式"
    current_growth: "当前增长数据"
  
  alignment_check:
    pricing_vs_acquisition:
      match: true/false
      current: "当前获客方式"
      recommended: "推荐获客方式"
      gap: "差距分析"
    
    revenue_vs_flywheel:
      match: true/false
      current_flywheel: "当前飞轮"
      needed_flywheel: "需要的飞轮"
      gap: "差距分析"
    
    certainty_vs_marketing:
      match: true/false
      certainty_dimension: "确定性维度"
      marketing_focus: "营销重点"
      gap: "差距分析"
  
  action_plan:
    immediate: ["立即调整"]
    short_term: ["30天内"]
    medium_term: ["90天内"]
  
  metrics:
    business_metrics: ["商业模式指标"]
    growth_metrics: ["增长指标"]
    alignment_metrics: ["一致性指标"]
```

## 一句判断

> 商业模式和增长策略是一枚硬币的两面。定价方式决定了获客方式，收入结构决定了飞轮类型。
