---
skill:
  name: ai-native-pm-agent
  version: 1.0.0
  description: >-
    AI Native 产品经理 Agent — — 五书合一的产品工作流编排器。
    用户提供一个产品想法或问题线索，Agent 自动编排七个阶段：
    P1需求发现 → P2方向定界 → P3体验设计 → P4系统构建 → P5商业模式 → P6增长策略 → P7审计投产。
    基于五本书：《AI Native 产品方法论》《AI时代的用户体验》《AI确定性商业模式》《AI Native 营销与增长》《AI rebuild product needs》。
  author: max
  tags: [ai-product, agent, orchestrator, pm, book-skill, five-books]
  requires: []
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
