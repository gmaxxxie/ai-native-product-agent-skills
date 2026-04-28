---
name: ai-native-agent-skill-design
description: 'AI Native 产品方法论——智能体与技能单元设计的实操 Skill。

  用户提供任务场景，Skill 自动执行能力编排设计流程：

  任务拆解 → Agent 角色定义 → Skill 拆分 → Tool 映射 → 边界与回退设计 → 输出能力编排方案。

  基于《AI Native 产品方法论》第12章。

  '
tags: p4, 技能设计, 产品方法论
- ai-product
- methodology
- agent
- skill
- orchestration
- book-skill
author: Max
source_book: AI Native 产品方法论
version: 1.0.0
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p4-agent-skill-design
stage: p4
source_chapter: 第13章 技能单元设计

---


# AI Native 智能体与技能单元设计 Skill

## 使用场景

- 产品需要从单轮问答进化到多步任务推进
- 需要设计可复用的能力模块（Skill）和任务编排层（Agent）
- 需要明确智能体的边界：可以推进到哪里、何时必须停下并把控制权交还给人

## 核心概念

- **智能体（Agent）**：面向目标组织任务、编排能力与调用动作的系统层
- **技能单元（Skill）**：围绕一类任务封装的可复用能力单元
- **工具（Tool）**：可被调用的具体接口、系统能力或外部动作
- **智能体边界**：智能体可以推进到哪里、何时必须停下并把控制权交还给人

## 什么时候真的需要 Agent

不是所有 AI 产品都需要 Agent。以下场景通常需要：

- 用户提出的不是单一问题，而是一项任务
- 任务需要多步骤完成：理解目标 → 拆解任务 → 调用工具 → 组织结果
- 中间步骤可能失败，需要回退、重试或请求补充信息

如果只是单轮问答、单次总结、单次分类，通常 Prompt + RAG 或固定 Workflow 就足够。

## Agent 的基本结构

```
Reason（理解目标）
  → Plan（拆解任务）
    → Act（执行动作）
```

三个动作对应三种难点：

- **Reason**：系统是否真正理解了用户目标
- **Plan**：系统是否能把复杂任务拆成可执行步骤
- **Act**：系统是否能在真实环境中可靠完成动作

任何一环不稳定，Agent 最终都会退化成"说得很多，但做不成事"。

## Agent、Skill 与 Tool 的关系

| 层级 | 定义 | 例子 |
|------|------|------|
| Tool | 具体工具或系统接口 | 查询订单、检索日志、调用 CRM |
| Skill | 围绕某类任务封装的能力模块 | 客服问题归因、运维告警诊断、经营指标解释 |
| Agent | 任务层面编排技能与工具 | 理解用户问题 → 选择 Skill → 调用 Tool → 组织结果 |

### 分工原则

- **Tool** 做具体事：查询、调用、写入
- **Skill** 做一类事：封装任务逻辑、输入输出约束、评估标准
- **Agent** 决定做哪些事：目标理解、任务拆解、Skill 选择、结果组织

## 能力编排流程

```
用户目标
  → Agent 理解与规划
    → Skill 选择
      → Tool 调用
        → 结果组织
          → 用户确认 / 人工接管
```

如果这条链路里任何一层边界不清，Agent 就会退化成大黑盒。

## Skill 设计原则

### 1. 能力可拆分

把复杂任务拆成独立、可复用的能力单元。例如：

- 查询订单 → 解释物流状态 → 判断是否需要升级人工

### 2. 边界可治理

每个 Skill 必须有清晰的：

- 输入范围：接受什么、不接受什么
- 输出约束：返回什么格式、什么精度
- 失败条件：什么情况下必须回退或交还给人

### 3. 执行可回退

每个 Skill 必须有明确的回退机制：

- 失败时如何回退
- 超时时如何处理
- 结果不可信时如何降级

## 技术层 vs 方法层

技术层会持续变化：
n- 单智能体 vs 多智能体
- Planner / Executor / Router 等不同编排结构
- Function Calling vs MCP 等不同动作连接方式
- 提示词技能 vs 代码技能的不同封装方式

方法层更长期稳定：
n- 能力如何拆分
- 调用如何授权
- 执行如何回退
- 过程如何观测
- 责任如何界定

## 输出物：能力编排方案

1. **任务拆解图**：复杂任务如何拆成子任务
2. **Agent 角色定义**：目标理解、任务规划、Skill 选择、结果组织
3. **Skill 清单**：每个 Skill 的输入、输出、失败条件
4. **Tool 映射**：每个 Skill 调用哪些 Tool
5. **边界与回退设计**：什么情况下必须停下并交还给人

## 使用方式

当用户提供任务场景时，自动执行：

1. 判断是否真的需要 Agent（还是单轮问答就足够）
2. 将复杂任务拆解为子任务
3. 为每个子任务设计 Skill（输入、输出、失败条件）
4. 映射 Skill 到具体 Tool
5. 设计 Agent 的任务编排逻辑
6. 设计边界与回退机制
7. 输出能力编排方案

## 示例

### 示例1：AI 客服任务编排设计

**场景描述**：
用户说"我的订单怎么还没到货"，系统需要完成多步骤任务。

**用户输入**：
"我的订单怎么还没到货？已经等了5天了"

**Skill 执行流程**：

1. **判断是否需要 Agent**
   - ❌ 单轮问答：只回答"一般配送时间是3-7天"
   - ✅ 需要 Agent：查询订单→查物流→判断异常→提供解决方案

2. **任务拆解**

```
用户目标：了解订单未到货原因并解决
  ├─ 步骤1：识别用户身份和订单号
  ├─ 步骤2：查询订单状态
  ├─ 步骤3：查询物流轨迹
  ├─ 步骤4：判断异常类型
  └─ 步骤5：提供解决方案或升级
```

3. **Skill 设计**

| Skill | 输入 | 输出 | Tool | 失败条件 |
|-------|------|------|------|----------|
| IdentifyUser | 会话上下文 | 用户ID、身份置信度 | CRM查询 | 置信度<0.8时请求确认 |
| QueryOrder | 用户ID、时间范围 | 订单列表 | 订单系统 | 无订单时给出引导 |
| TrackLogistics | 订单号 | 物流状态、轨迹 | 物流系统 | 超时未返回时降级 |
| AnalyzeException | 物流状态 | 异常类型、原因 | 规则引擎 | 无法归类时标记"未知" |
| GenerateResponse | 异常类型 | 回复内容、建议动作 | - | 高风险时转人工 |

4. **Agent 编排逻辑**

```yaml
Agent: CustomerServiceAgent
目标理解: "用户询问订单未到货原因"
任务规划:
  - 先执行 IdentifyUser（若失败则请求确认）
  - 再执行 QueryOrder（若多订单则请用户选择）
  - 然后执行 TrackLogistics
  - 根据物流状态决定后续:
      - 正常运输中 → GenerateResponse(解释预计时间)
      - 物流异常 → GenerateResponse(说明异常+解决方案)
      - 丢件/破损 → 标记升级人工
技能选择策略: 按依赖顺序串行执行，每步检查失败条件
结果组织: 结构化回复 + 可选操作按钮
```

5. **边界与回退设计**

| 场景 | 边界规则 | 回退动作 |
|------|----------|----------|
| 用户身份不确定 | 置信度<0.8 | 请求提供手机号/订单号 |
| 订单查询失败 | 系统超时 | 告知"系统繁忙"并提供自助链接 |
| 物流信息缺失 | 3PL未返回 | 提供官方物流查询方式 |
| 涉及赔付/退款 | 高风险承诺 | 必须人工确认 |
| 用户情绪升级 | 检测到负面情绪 | 自动转人工 |

**输出结果**：

```yaml
# 能力编排方案：AI 客服 Agent

Agent:
  name: CustomerServiceAgent
  role: 客服任务编排与协调
  objectives:
    - 理解用户问题
    - 查询相关信息
    - 提供准确回答
    - 控制服务风险

Skills:
  - name: IdentifyUser
    input: [user_message, session_id]
    output: 
      user_id: string
      confidence: float
    failure: confidence < 0.8
    fallback: request_explicit_identification

  - name: QueryOrder  
    input: [user_id, time_range="30d"]
    output:
      orders: [{id, status, amount, items}]
    failure: orders.length == 0
    fallback: guide_no_order

  - name: TrackLogistics
    input: [order_id]
    output:
      status: enum[运输中,已签收,异常]
      events: [{time, location, status}]
    failure: timeout > 5s
    fallback: provide_official_tracking_link

  - name: AnalyzeException
    input: [logistics_status, events]
    output:
      exception_type: enum[延迟,丢件,破损,其他]
      severity: enum[低,中,高]
    failure: exception_type == "其他"
    fallback: mark_unknown_escalate

  - name: GenerateResponse
    input: [analysis_result, user_intent]
    output:
      message: string
      actions: [{type, label, payload}]
      risk_level: enum[低,中,高]
    failure: risk_level == "高"
    fallback: escalate_to_human

Tools:
  CRM.query: 用户信息查询
  OrderSystem.query: 订单状态查询
  Logistics.track: 物流轨迹查询
  RuleEngine.classify: 异常类型判断

边界控制:
  max_turns: 10
  escalation_triggers:
    - risk_level == "高"
    - user_sentiment < -0.5
    - mention_keywords: ["投诉", "法院", "媒体"]
    - 连续3次未能解决问题
```

---

### 示例2：AIOps 故障诊断编排

**场景描述**：
告警系统收到多条告警，需要自动诊断并提供分诊建议。

**用户输入**：
"收到告警：服务A响应超时、数据库连接池耗尽、CPU使用率95%"

**Skill 执行流程**：

1. **任务拆解**

```
目标：分析告警并给出故障分诊建议
  ├─ 步骤1：聚类告警（识别相关性）
  ├─ 步骤2：查询服务依赖拓扑
  ├─ 步骤3：检索相关日志
  ├─ 步骤4：召回历史相似案例
  ├─ 步骤5：生成故障摘要
  └─ 步骤6：推荐处置优先级
```

2. **Skill 清单**

| Skill | 功能 | 输入 | 输出 | Tool |
|-------|------|------|------|------|
| ClusterAlerts | 告警聚类 | 告警列表 | 告警组、根因候选 | 聚类算法 |
| QueryDependency | 依赖查询 | 服务名 | 上下游服务图 | CMDB |
| FetchLogs | 日志检索 | 服务+时间窗口 | 相关日志片段 | ELK |
| RecallCases | 案例召回 | 告警特征 | 相似历史案例 | 向量检索 |
| SummarizeFault | 故障摘要 | 多源信息 | 故障描述 | LLM |
| RecommendAction | 处置建议 | 故障类型 | 优先级+建议 | 规则引擎 |

3. **关键边界设计**

```yaml
高风险边界:
  - 禁止技能: 任何直接操作生产的动作
  - 输出性质: 永远是建议，不是命令
  - 置信度阈值: <70% 时必须标注"不确定，需人工确认"
  
回退机制:
  - 案例召回为空时: 标记"无历史参考，依赖专家判断"
  - 日志查询失败时: 降级为"基于告警的初步判断"
  - 多源信息冲突时: 列出矛盾点，不强行统一
```

**输出结果**：

```yaml
# 能力编排方案：AIOps 诊断 Agent

Agent:
  name: AIOpsDiagnosisAgent  
  type: Observation-Only（仅观察，不执行）
  principles:
    - 只组织信息，不下达指令
    - 只提供建议，不做决策
    - 所有输出供参考，必须由工程师确认

Skills:
  ClusterAlerts:
    input: [alerts, correlation_rules]
    output: 
      clusters: [{root_alert, related_alerts}]
      timeline: [event_sequence]

  QueryDependency:
    input: [service_name]
    output:
      upstream: [services]
      downstream: [services]
      impact_radius: string

  FetchLogs:
    input: [services, time_window="-30m,+5m"]
    output:
      log_snippets: [text]
      error_patterns: [{pattern, count}]

  RecallCases:
    input: [alert_signature, vectors]
    output:
      similar_cases: [{case_id, similarity, resolution}]
      top_recommendation: string

  SummarizeFault:
    input: [clusters, logs, cases]
    output:
      summary: string
      confidence: float
      evidence_chain: [sources]

  RecommendAction:
    input: [fault_type, severity]
    output:
      priority: enum[P0,P1,P2]
      suggested_actions: [strings]
      escalation_path: string

边界协议:
  no_execution: true
  confidence_threshold: 0.7
  uncertainty_handling: explicit_flag
  audit_required: true
```
