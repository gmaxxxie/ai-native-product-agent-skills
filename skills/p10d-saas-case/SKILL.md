---
name: p10d-saas-case
description: 'AI Native 产品方法论——AI Native SaaS 行业案例模板 Skill。

  用户提供 SaaS 产品场景和业务背景，Skill 自动执行全链路方法论：

  方向定界 → 试验展开 → 系统构建 → 审计放行 → 生产运行，输出 AI Native 化改造方案。

  基于《AI Native 产品方法论》第21章 AI Native SaaS 案例，适用于数据分析、业务洞察、决策支持场景。

  '
tags:
- ai-product
- methodology
- ai-native-saas
- data-analytics
- case-study
- book-skill
author: Max
source_book: AI Native 产品方法论
source_chapter: 第21章 AI Native SaaS 案例
version: 1.0
stage: p10d
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p10d-saas-case
---

# AI Native SaaS 案例模板 Skill

## 使用场景

- 传统 SaaS 产品需要 AI Native 化改造
- 需要设计数据分析类产品的 AI 能力升级路径
- 关注语义层构建、能力护城河和数据飞轮建设场景

## AI Native SaaS 特征与适配性

| SaaS 特征 | 对方法论的影响 |
|-----------|--------------|
| 功能型 → 能力型 | 不是加 AI 功能，而是重写能力入口 |
| 语义层依赖 | 需要构建业务语义理解和指标语义层 |
| 数据积累 | 用户数据形成天然的反馈飞轮 |
| 能力护城河 | 真实使用越多，能力越难被复制 |
| 订阅商业模式 | 适合用价值信号驱动续费 |

## AI Native SaaS 方法论路径

```
@ai-native-direction-framing
  → 选择最值得 AI Native 化的功能层
  → 输出：Direction Brief

@p2a-experiment-overview + @p2b-product-form-exploration
  → 验证语义理解、数据解释、洞察生成能力
  → 输出：产品形态建议

@p2c-process-redesign
  → 分析流程重构：问答 → 追问 → 下钻 → 行动
  → 输出：交互工作流

@ai-native-context-engineering
  → 业务上下文构建：指标语义、维度关系、权限语义
  → 输出：上下文架构

@ai-native-knowledge-rag
  → 领域知识 RAG：行业术语、口径定义、业务规则
  → 输出：语义层设计

@ai-native-agent-skill-design
  → 分析 Agent：指标查询、趋势解读、异常归因
  → 输出：Agent 和 Skill 设计

@ai-native-ux-design
  → 自然语言交互设计
  → 输出：信任分级和渐进式透明

@ai-native-audit-release
  → 数据准确性和洞察可靠性审计
  → 输出：放行决策

@ai-native-production-ops
  → 用户行为观测和数据飞轮建设
  → 输出：生产运行方案
```

## SaaS AI Native 化分层

### 第一层：增强型（最常见）
- 自然语言查询替代下拉筛选
- AI 解读取代固定报表
- 异常自动发现和推送
- → 适合：加在现有产品上，快速验证

### 第二层：重构型
- 问答即分析（NL to SQL / API）
- 主动洞察推送（不只是被动查询）
- 预测性建议（而非历史数据展示）
- → 适合：产品全面 AI Native 化

### 第三层：自主型
- AI 自动执行业务动作（数据录入、报告生成、任务派发）
- 跨系统自动化工作流
- → 适合：有强集成能力的高阶产品

## SaaS 案例 Skill 输出模板

\`\`\`yaml
# AI Native SaaS 案例方案

方向定界:
  核心问题: [哪个功能层最值得 AI Native 化]
  当前产品: [现有 SaaS 产品类型]
  AI Native 化层次: [增强型 / 重构型 / 自主型]
  Direction Brief: [输出]

试验展开:
  能力实验:
    - 语义理解: [自然语言解析准确率]
    - 指标计算: [SQL生成准确率 / 误差率]
    - 异常检测: [误报率 / 漏报率]
  产品实验:
    - 形态: [问答式 / 推送式 / 自主式]
    - 用户接受度测试
  商业实验:
    - 付费意愿提升测试
    - 续费率对比

系统构建:
  语义层:
    - 指标定义: [原子指标 / 派生指标]
    - 维度关系: [业务口径]
    - 权限语义: [行级 / 列级权限]
  Agent 设计:
    - 查询理解 Agent
    - 指标计算 Agent
    - 异常归因 Agent
    - 报告生成 Agent
  Memory: [用户偏好 / 分析历史 / 常用指标]
  Context: [数据库Schema / 业务口径 / 权限上下文]
  RAG: [指标口径文档 / 行业知识 / 使用指南]
  UX: [自然语言输入 / 信任分级展示 / 可解释输出]

审计放行:
  数据准确性: [误差容忍标准]
  洞察可靠性: [置信度展示标准]
  权限安全: [数据隔离验证]

生产运行:
  数据飞轮: [用户查询 → 反馈 → 能力优化]
  指标监控: [查询成功率 / 准确率 / 用户满意度]
  价值发现: [使用频率 / 功能依赖度 / 续费相关性]
\`\`\`

## 与其他 Skill 的关系

- **核心协同**：@ai-native-context-engineering（语义层），@ai-native-agent-skill-design（分析Agent），@ai-native-ux-design（自然语言交互）
- **配套**：@ai-native-production-ops（数据飞轮），@p10a-value-discovery-loop（价值发现）
- **案例 Skill**：@p10b-aiops-case（AIOps场景），@p10c-customer-service-case（客服场景）

## 适用边界

- ✅ 数据分析类 SaaS（BI、CRM、ERP、分析平台）
- ✅ 需要自然语言查询能力的工具型 SaaS
- ✅ 可以形成数据飞轮的订阅型产品
- ❌ 数据质量极差、指标口径混乱的产品（先做数据治理）
- ❌ 强事务性、低分析价值的工具型 SaaS
