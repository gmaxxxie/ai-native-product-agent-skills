---
name: ai-native-pm-agent
version: 1.0.0
description: AI Native 产品经理 Agent — — 五书合一的产品工作流编排器。 用户提供一个产品想法或问题线索，Agent 自动编排七个阶段：
  P1需求发现 → P2方向定界 → P3体验设计 → P4系统构建 → P5商业模式 → P6增长策略 → P7审计投产。 基于五本书：《AI Native 产品方法论》《AI时代的用户体验》《AI确定性商业模式》《AI
  Native 营销与增长》《AI rebuild product needs》。
author: max
tags:
- ai-product
- agent
- orchestrator
- pm
- book-skill
- five-books
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills
---


# AI Native PM Agent

## 使用场景

- 你有一个产品想法，需要从需求发现到生产运行的完整产品方案
- 你需要用系统化方法论管理 AI 产品全生命周期
- 你希望五本书的方法论能在一个 Agent 中自然流转

## 工作流

```text
用户输入
  → [P1] 需求发现 (ai-native-product-needs/*)
    → [P2] 方向定界 (ai-native-direction-framing)
      → [P3] 体验设计 (ai-native-user-experience)
        → [P4] 系统构建 (ai-native-system-building + 子 Skills)
          → [P5] 商业模式 (ai-native-business-model/*)
            → [P6] 增长策略 (ai-native-marketing-growth/*)
              → [P7] 审计投产 (ai-native-audit-release  / 待创建)
                → 输出完整产品方案
```

## 阶段详情

### P1: 需求发现
- **Skill**: `ai-native-product-needs/*`
- **输入**: 用户原始想法
- **输出**: 需求简报 (Needs Brief)
- **关键判断**: 机会评分 >= 60 才进入 P2

### P2: 方向定界
- **Skill**: `ai-native-direction-framing`
- **输入**: P1 需求简报
- **输出**: Direction Brief
- **关键判断**: go/no-go 决策

### P3: 体验设计
- **Skill**: `ai-native-user-experience`
- **输入**: P2 Direction Brief
- **输出**: UX 方案
- **关键判断**: 人机协作模式定义

### P4: 系统构建
- **Skill**: `ai-native-system-building` + 子 Skills
- **输入**: P3 UX 方案
- **输出**: 系统架构方案
- **包含**: Agent/Skill/记忆/上下文/RAG

### P5: 商业模式
- **Skill**: `ai-native-business-model/*`
- **输入**: P4 系统成本估算
- **输出**: 定价策略 + 收入模型
- **关键判断**: 成本-定价匹配

### P6: 增长策略
- **Skill**: `ai-native-marketing-growth/*`
- **输入**: P5 商业模式
- **输出**: 获客/激活/留存方案
- **关键判断**: 增长目标-系统承载匹配

### P7: 审计投产
- **Skill**: `ai-native-audit-release`
- **输入**: P4-P6 全部方案
- **输出**: go/no-go 决策 + 监控方案

## 核心机制

### 上下文传递

每个阶段的输出自动写入 Product Context 的对应字段，下一阶段启动时自动读取。

```yaml
product_context:
  version: "1.0"
  created_at: "2026-04-27T11:00:00+08:00"
  status: "active"  # active / paused / rollback
  current_stage: "p1"  # p1-p7
  
  # 各阶段输出物
  artifacts:
    p1_needs_brief: null       # ai-native-product-needs 产出
    p2_direction_brief: null   # ai-native-direction-framing 产出
    p3_ux_design_brief: null   # ai-native-user-experience 产出
    p4_system_architecture: null  # ai-native-system-building 产出
    p5_business_model_brief: null # ai-native-business-model 产出
    p6_growth_strategy_brief: null # ai-native-marketing-growth 产出
    p7_audit_decision: null    # ai-native-audit-release 产出
  
  # 回溯历史
  history:
    - stage: "p1"
      version: 1
      completed_at: "2026-04-27T11:30:00+08:00"
      artifacts_key: "p1_needs_brief"
  
  # 冲突检测结果
  conflict_checks:
    p4_p5_cost_pricing: null
    p3_p4_ux_latency: null
    p6_p4_growth_capacity: null
```

### 冲突检测
每完成两个阶段，自动运行冲突检测：
- P4 + P5 → 成本-定价匹配
- P3 + P4 → UX-系统延迟匹配
- P6 + P4 → 增长-承载匹配

### 用户交互点
以下节点必须等待用户确认：
1. P2 结束后（方向定界 go/no-go）
2. P4 结束后（系统架构方案确认）
3. P7 结束后（最终投产决策）

### 回溯机制
用户可在任意时刻说：
- "回到 P2 重新看方向" → 保留 P3-P7 为 v1，重新执行 P2 生成 v2
- "P4 的系统成本太高了" → 回溯到 P4，P5-P7 标记为待更新

## 使用方式

当用户提供一个产品想法时，自动执行：

1. 初始化 Product Context
2. 按阶段路由依次执行各阶段 Skill
3. 每阶段完成后进行冲突检测
4. 用户可在任意节点确认/修改/回溯
5. 最终输出完整产品方案

## 核心概念

### 概念一：总编排器的本质——不是串行流水线，而是智能路由

AI Native PM Agent 不是把七个阶段串起来跑一遍。它的核心能力是：
1. **智能路由**：根据当前阶段的输出决定下一步走哪条路径
2. **冲突检测**：自动发现跨阶段的矛盾
3. **回溯管理**：支持在任意节点回溯修改
4. **上下文传递**：确保每个阶段都能获取前序阶段的完整上下文

```
用户输入
  → 初始化 Product Context
    → P1 需求发现 → [go/no-go]
      → P2 方向定界 → [用户确认]
        → P3 体验设计
          → P4 系统构建 → [用户确认] → [冲突检测: P4 vs P5]
            → P5 商业模式 → [冲突检测: P5 vs P6]
              → P6 增长策略 → [冲突检测: P4 vs P6]
                → P7 审计投产 → [用户确认] → 输出完整方案
```

> 总编排器的价值不是"帮你跑完七个阶段"，而是"在每个阶段告诉你该不该继续、有没有冲突"。

### 概念二：Product Context——贯穿七阶段的共享状态

Product Context 是总编排器的核心数据结构，记录了每个阶段的产出物和状态：

```yaml
product_context:
  version: "1.0"
  status: "active"  # active / paused / rollback
  current_stage: "p1"
  
  artifacts:
    p1_needs_brief: null       # 需求发现产出
    p2_direction_brief: null   # 方向定界定产
    p3_ux_design_brief: null   # 体验设计产出
    p4_system_architecture: null  # 系统构建产出
    p5_business_model_brief: null # 商业模式产出
    p6_growth_strategy_brief: null # 增长策略产出
    p7_audit_decision: null    # 审计投产产出
```

每个阶段启动时自动读取前序阶段的产出，完成后自动写入自己的产出。

### 概念三：三个冲突检测点

每完成两个阶段，自动运行冲突检测：

| 冲突检测 | 检查内容 | 典型问题 |
|----------|----------|----------|
| P4 + P5 | 成本-定价匹配 | 系统成本太高，定价无法覆盖 |
| P3 + P4 | UX-系统延迟匹配 | UX 设计要求实时响应，系统架构做不到 |
| P6 + P4 | 增长-承载匹配 | 增长目标超出系统承载能力 |

> 冲突检测不是"发现问题"，而是"在投入更多资源之前发现矛盾"。

### 概念四：三个用户交互点

以下节点必须等待用户确认，不能自动继续：

| 交互点 | 确认内容 | 不确认则 |
|--------|----------|----------|
| P2 结束后 | 方向定界 go/no-go | 暂停或回溯到 P1 |
| P4 结束后 | 系统架构方案确认 | 回溯到 P3 或 P4 |
| P7 结束后 | 最终投产决策 | 暂停或回溯 |

### 概念五回溯机制

用户可在任意时刻说：
- "回到 P2 重新看方向" → 保留 P3-P7 为 v1，重新执行 P2 生成 v2
- "P4 的系统成本太高了" → 回溯到 P4，P5-P7 标记为待更新
- "P6 的增长策略和 P5 的商业模式不匹配" → 回溯到 P5 重新设计

回溯不是失败，而是迭代。

## 分步执行

### Step 1：初始化 Product Context

**输入**：用户原始想法

**处理**：
1. 创建 Product Context 数据结构
2. 记录原始输入
3. 设置 current_stage = p1
4. 初始化所有 artifacts 为 null

**输出**：Product Context（已初始化）

---

### Step 2：P1 需求发现

**输入**：用户原始想法

**处理**：
1. 调用 p0-product-needs 或 p0-needs-orchestrator
2. 执行微需求检测、四层拆解、真需求验证
3. 输出 Needs Brief
4. 检查机会评分：≥ 60 才进入 P2

**输出**：Needs Brief → 写入 Product Context

---

### Step 3：P2 方向定界

**输入**：P1 Needs Brief

**处理**：
1. 调用 ai-native-direction-framing
2. 执行五维度判断 + 资料审查 + 能力评估
3. 输出 Direction Brief
4. **等待用户确认 go/no-go**

**输出**：Direction Brief → 写入 Product Context

---

### Step 4：P3 体验设计

**输入**：P2 Direction Brief

**处理**：
1. 调用 ai-native-user-experience
2. 执行任务分析、人机分工、状态可见性、纠偏机制、信任设计
3. 输出 UX 方案

**输出**：UX Design Brief → 写入 Product Context

---

### Step 5：P4 系统构建 + P5 商业模式

**输入**：P3 UX 方案 + P4 系统成本估算

**处理**：
1. P4：调用 ai-native-system-building，输出系统架构方案
2. **冲突检测 P4 + P5**：系统成本 vs 定价是否匹配
3. P5：调用 ai-native-business-model，输出定价策略 + 收入模型
4. **等待用户确认系统架构方案**

**输出**：System Architecture + Business Model Brief → 写入 Product Context

---

### Step 6：P6 增长策略 + P7 审计投产

**输入**：P5 商业模式 + P4 系统架构

**处理**：
1. **冲突检测 P6 + P4**：增长目标 vs 系统承载是否匹配
2. P6：调用 ai-native-marketing-growth，输出增长策略
3. P7：调用 ai-native-audit-release，执行六类审计
4. **等待用户确认最终投产决策**

**输出**：Growth Strategy + Audit Decision → 写入 Product Context

---

### Step 7：输出完整产品方案

**输入**：Product Context（全部 artifacts）

**处理**：
1. 整合七个阶段的产出物
2. 标注所有冲突检测结果
3. 标注所有用户确认点的状态
4. 输出完整产品方案文档

**输出**：完整产品方案（含需求发现、方向定界、体验设计、系统构建、商业模式、增长策略、审计投产）

### 示例 1：AI 客服产品的完整编排

**场景描述**：用户说"我想做一个 AI 客服产品，帮企业自动回复客户问题"。

**Step 1 初始化**：
```yaml
product_context:
  current_stage: "p1"
  artifacts:
    p1_needs_brief: null
    # ... 全部 null
```

**Step 2 P1 需求发现**：
- 微需求检测：发现新人客服的"不敢问"微需求
- 四层拆解：表达层→场景层→处境层→代价层
- 真需求验证：5/5 通过
- 机会评分：85/100 → 进入 P2
- **产出**：Needs Brief（核心问题：新人知识辅助，而非自动回复）

**Step 3 P2 方向定界**：
- 五维度判断：全部通过
- 资料审查：FAQ + 历史工单可用
- 能力评估：AI 辅助回复可行
- **用户确认**：✅ go
- **产出**：Direction Brief（聚焦新人客服知识辅助场景）

**Step 4 P3 体验设计**：
- 人机分工：AI 生成候选回复，人工确认后发送
- 状态可见：展示 AI 置信度和引用来源
- 纠偏机制：快速编辑、重新生成、完全拒绝
- **产出**：UX Design Brief

**Step 5 P4 + P5 冲突检测**：
- P4 系统架构：RAG + 历史工单检索 + 候选回复生成
- **冲突检测 P4 + P5**：✅ 成本可控（单次调用 < $0.01）
- P5 商业模式：SaaS 订阅 + 按坐席收费
- **用户确认**：✅ 系统架构方案通过
- **产出**：System Architecture + Business Model Brief

**Step 6 P6 + P7**：
- **冲突检测 P6 + P4**：✅ 增长目标（月增 50 坐席）在系统承载范围内
- P6 增长策略：PLG（免费试用 → 团队邀请 → 付费转化）
- P7 审计投产：go（条件放行）
- **用户确认**：✅ 最终投产
- **产出**：Growth Strategy + Audit Decision

**最终输出**：完整产品方案，从需求发现到投产的七个阶段全部完成。

---

### 示例 2：回溯场景——P4 系统成本过高

**场景描述**：在执行到 P5 时，发现 P4 的系统架构方案成本过高，无法匹配 P5 的定价策略。

**冲突检测触发**：
```yaml
conflict_check:
  p4_p5_cost_pricing:
    status: "CONFLICT"
    detail: "P4 系统方案的月运行成本 $50,000，但 P5 定价策略的月收入预期 $30,000"
    recommendation: "回溯到 P4 优化系统架构，或回溯到 P5 调整定价"
```

**用户决策**："回到 P4 重新设计系统架构"

**回溯处理**：
1. 保留 P1-P3 的产出不变
2. P4 标记为 v2，重新执行
3. P5-P7 标记为"待更新"
4. P4 v2 输出后，重新运行冲突检测
5. 如果通过，继续执行 P5-P7 v2

**P4 v2 优化**：
- 将 RAG 检索从实时改为批量预处理
- 将 LLM 调用从 GPT-4 降级为 GPT-3.5-turbo
- 月运行成本从 $50,000 降至 $15,000

**重新冲突检测**：✅ 成本-定价匹配

> 回溯不是失败，而是迭代。好的编排器让回溯的成本最低。
