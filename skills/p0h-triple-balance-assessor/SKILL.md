---
skill:
  name: p0h-triple-balance-assessor
  version: 1.0.0
  description: >-
    AI 产品三重平衡表。当团队讨论 AI 产品方向时，最容易只看增长和效率。
    这个 Skill 帮团队同时看商业、人性、文化三层。
    基于《AI rebuild product needs》工具卡。
  author: Max
  tags: [book-skill, ethics, balance, product-direction, ai-product]
  requires: []
---

# AI 产品三重平衡表

## 一句话定位

不要只看商业指标，用三层判断确保 AI 产品赢得长期信任。

## 何时触发

- 大方向评审会
- 评估新功能/新产品方向
- 觉得团队只在追求增长和效率
- 需要平衡短期收益与长期价值

## 输入

一个 AI 产品方向或功能描述。

**示例输入**：
```
方向: "做一个默认全自动帮用户安排日程、催办任务、对外发确认消息的 AI 助手"
```

## 输出

三层评估 + 综合判断 + 调整建议。

## 三层判断

### 层 1: 商业层（Business）

**核心问题**：这个能力能不能赚钱？能不能持续？

**三个检查点**：

1. **这个能力的长期成本是什么？**
   - Token/算力成本
   - 运维成本
   - 错误兌底成本
   - 人工复核成本

2. **它带来的价值能不能覆盖持续消耗？**
   - 单位用户价值
   - 增值服务收费潜力
   - 用户留存提升

3. **它是不是靠高成本堆出"看起来很聪明"？**
   - 是否需要持续高成本维护才能保持体验？
   - 如果成本下降 50%，体验会不会大打折扣？
   - 是否是"资金密集型"而非"结构优势型"？

**输出格式**：
```
商业层评估:
  long_term_cost: "长期成本估算"
  value_coverage: "价值是否覆盖成本"
  smart_illusion: "是否靠高成本堆出"
  viability: "viable/marginal/not_viable"
```

### 层 2: 人性层（Humanity）

**核心问题**：这个能力是不是真正帮助了人？

**三个检查点**：

1. **它是否真的减轻了用户的长期负担？**
   - 减轻的是执行负担还是决策负担？
   - 是否把负担从用户转移到了其他地方？
   - 用户是否感觉更轻松了？

2. **它是否保留了人的主体性和判断感？**
   - 用户是否还能做出自己的选择？
   - 系统是在"帮助判断"还是"替代判断"？
   - 用户是否还能感觉到"这是我的决定"？

3. **它是在帮助人生活，还是让人更依赖系统？**
   - 用户是否变得更独立了，还是更依赖了？
   - 如果系统没了，用户是更强了还是更弱了？
   - 这个依赖是健康的还是不健康的？

**输出格式**：
```
人性层评估:
  burden_reduction: "是否减轻长期负担"
  agency_preservation: "是否保留主体性"
  dependency_type: "healthy/unhealthy/neutral"
  human_flourishing: "是否促进人的成长"
```

### 层 3: 文化层（Culture）

**核心问题**：这个产品在训练什么？扩散什么？

**三个检查点**：

1. **它在训练用户怎么理解效率、关系和责任？**
   - 效率是否变成了唯一标准？
   - 关系是否被简化成了交易？
   - 责任是否被外包了？

2. **它是在扩大人的现实感，还是在鼓励更浅的自动化依赖？**
   - 用户是否更关注现实世界了？
   - 还是更沉迷于系统优化的虚拟体验？
   - 产品是否在"放大"还是"缩小"人的能力？

3. **这种产品逻辑是否值得被扩散？**
   - 如果所有产品都这么做，世界会变得更好吗？
   - 这种逻辑能否被复制到其他领域？
   - 如果被复制，结果是什么？

**输出格式**：
```
文化层评估:
  value_training: "训练了什么价值观"
  reality_expansion: "扩大还是缩小现实感"
  worth_spreading: "是否值得扩散"
  cultural_impact: "positive/neutral/negative"
```

## 综合输出格式

```yaml
triple_balance_assessment:
  input:
    direction: "产品方向描述"
    context: "业务背景"
  
  business_layer:
    long_term_cost: "长期成本"
    value_coverage: "价值覆盖"
    smart_illusion: "是否高成本堆出"
    viability: "viable/marginal/not_viable"
    score: "1-10"
  
  humanity_layer:
    burden_reduction: "减轻负担"
    agency_preservation: "保留主体性"
    dependency_type: "healthy/unhealthy/neutral"
    flourishing: "促进成长"
    score: "1-10"
  
  culture_layer:
    value_training: "训练价值观"
    reality_expansion: "扩大/缩小现实感"
    worth_spreading: "值得扩散"
    impact: "positive/neutral/negative"
    score: "1-10"
  
  balance_analysis:
    strongest_layer: "最强的一层"
    weakest_layer: "最弱的一层"
    imbalance_risk: "失衡风险"
    
  verdict:
    overall_score: "1-10"
    recommendation: "proceed_with_caution/adjust/stop"
    key_adjustments: ["关键调整建议"]
    
  next_steps:
    if_proceed: "如果继续，需要补强的方面"
    if_adjust: "具体调整方案"
    if_stop: "如果停止，替代方向"
```

## 快速使用法

1. 填写产品方向
2. 逐层过三个层次，每层回答三个问题
3. **如果只有商业层有答案，先不要轻易下结论**
4. 看哪一层最弱，调整方案补强这一层

## 示例：完整走一遍

**方向**：
> "做一个默认全自动帮用户安排日程、催办任务、对外发确认消息的 AI 助手"

**三层评估**：

| 层次 | 评估 | 分数 |
|------|------|------|
| 商业层 | 容易讲增长故事，能提高效率感和付费想象。但长期运行成本、错误兌底成本、对外沟通失误成本会一起上升。 | 6/10 |
| 人性层 | 可能减轻执行负担，但会吞掉很多本该由用户自己保留的判断。系统在"替代判断"而不是"帮助判断"。 | 4/10 |
| 文化层 | 如果系统越来越默认替人表达、替人确认、替人推进，最后训练出来的不是更成熟的协作，而是更舒服的判断外包。 | 3/10 |

**综合判断**：
- 总分：13/30 —— 不建议原样实施
- 关键调整：
  1. 保留一部分自动化
  2. 高风险动作改为待确认
  3. 把"替用户落锤"改成"替用户暴露风险和整理上下文"
  4. 让产品从"更强"变成"更可信"

## 常见误判

- **商业层一票否决**：只看能不能赚钱，忽视长期信任
- **人性层变成道德说教**：不是不做，而是找到平衡点
- **文化层太抽象**：要具体到"如果所有产品都这么做会怎样"

## 一句判断

> 下一代 AI 产品，不该只赢得指标，还要赢得长期信任。
