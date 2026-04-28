---
name: p10b-aiops-case
description: 'AI Native 产品方法论——AIOps 行业案例模板 Skill。

  用户提供 AIOps 场景和业务背景，Skill 自动执行全链路方法论：

  方向定界 → 试验展开 → 系统构建 → 审计放行 → 生产运行，输出完整案例方案。

  基于《AI Native 产品方法论》第19章 AIOps 案例，适用于高风险、强约束、重责任场景。

  '
tags:
- ai-product
- methodology
- aiops
- case-study
- high-risk
- book-skill
author: Max
source_book: AI Native 产品方法论
source_chapter: 第19章 AIOps 案例
version: 1.0
stage: p10b
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p10b-aiops-case
---

# AIOps 案例模板 Skill

## 使用场景

- 运维团队希望引入 AI 能力，需要系统性方法论指导
- 需要为 AIOps 产品设计从方向到生产的完整路径
- 关注高风险、强约束、重责任场景的 AI 化方法

## AIOps 特征与适配性

| AIOps 特征 | 对方法论的影响 |
|------------|--------------|
| 高风险：错误建议直接导致故障扩大 | 必须有强审计放行和人在回路机制 |
| 知识密集：依赖专家经验 | 需要知识沉淀和检索增强 |
| 实时性强：响应时间要求高 | 模型延迟必须纳入评估 |
| 可解释性：决策必须可追溯 | 上下文工程和日志是基础设施 |
| 责任边界清晰：谁决策谁负责 | Agent 边界设计是核心 |

## AIOps 方法论路径

```
@ai-native-direction-framing
  → 选择最值得先 AI 化的运维节点
  → 输出：Direction Brief

@p2a-experiment-overview + @p2b-experiment-engine
  → 验证日志解释、告警聚类、案例召回能力
  → 输出：实验结论报告

@p2c-process-redesign
  → 值班升级链设计
  → 输出：人机协作矩阵

@p2e-shadow-validation
  → 影子系统并行验证
  → 输出：影子验证报告

@ai-native-audit-release
  → 高风险场景审计放行
  → 输出：放行决策

@ai-native-production-ops
  → 值班面板和生产观测
  → 输出：生产运行方案

@p10a-value-discovery-loop
  → 价值信号识别与反馈
  → 输出：价值发现方案
```

## 典型 AIOps 能力分层

### 第一层：值班辅助（低风险）
- 日志解释与摘要
- 告警聚类与去重
- 案例召回与相似故障推荐
- → 适合：自动 + 人在回路中

### 第二层：分诊辅助（中风险）
- 故障影响范围判断
- 根因概率排序
- 处置建议推荐
- → 适合：Copilot + 人在回路中

### 第三层：自动处置（高风险）
- 自动扩缩容
- 自动切流
- 自动补丁
- → 适合：人在监督中，且需强审计

## AIOps 案例 Skill 输出模板

\`\`\`yaml
# AIOps 案例方案

方向定界:
  核心问题: [选择最值得先 AI 化的运维节点]
  目标场景: [故障分诊 / 告警处理 / 日志分析 / 容量规划]
  约束条件: [响应时间要求 / 风险边界 / 可解释性要求]
  Direction Brief: [输出]

试验展开:
  能力实验:
    - 日志解释: [模型/准确率/结论]
    - 告警聚类: [模型/准确率/结论]
    - 案例召回: [模型/准确率/结论]
  产品实验:
    - 值班面板原型
    - 采纳率/满意度
  商业实验:
    - MTTR 缩短目标
    - ROI 测算

系统构建:
  Agent 设计:
    - 值班 Agent
    - 分诊 Agent
    - 知识库 Agent
  Memory: [会话状态 / 故障上下文 / 历史案例]
  Context: [告警上下文 / 服务拓扑 / 业务影响]
  RAG: [运维知识库 / SOP / 历史故障库]
  审计规则: [风险等级 / 升级条件 / 人工接管点]

审计放行:
  RAX 评估: [风险/接受度/体验评分]
  放行条件: [通过/附条件/拒绝]
  约束: [高风险动作必须人工确认]

生产运行:
  可观测性: [五层观测设计]
  反馈回灌: [故障案例 → 知识库更新]
  循环优化: [月度复盘 + 季度能力沉淀]
\`\`\`

## 与其他 Skill 的关系

- **核心协同**：@ai-native-direction-framing, @p2a-experiment-overview, @ai-native-audit-release, @ai-native-production-ops
- **配套**：@ai-native-memory-system（会话状态管理），@ai-native-knowledge-rag（运维知识沉淀），@p10a-value-discovery-loop（价值发现）
- **案例 Skill**：@p10c-customer-service-case（客服场景），@p10d-saas-case（数据分析场景）

## 适用边界

- ✅ 故障分诊、告警处理、日志分析、容量预测等场景
- ✅ 高风险、强约束、重责任的运维环境
- ❌ 需要直接自动执行高危操作（建议用人在监督中 + 强审计）
- ❌ 实时性要求极高的交易系统（延迟和准确率难以兼顾）
