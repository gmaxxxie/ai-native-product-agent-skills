# AI Native PM Agent — 架构设计文档

> 版本: 1.0
> 日期: 2026-04-27
> 作者: Max

---

## 项目概述

将五本书的方法论整合为一个端到端的 AI Native 产品经理 Agent，支持从需求发现到生产运行的完整产品工作流。

### 五本书构成的工作流

| 阶段 | 来源书籍 | 状态 | Skill 数 |
|------|---------|------|---------|
| P1 需求发现 | 《AI rebuild product needs》 | 待创建 | 3-4 |
| P2 方向定界 | 《AI Native 产品方法论》 | ✅ 就绪 | 1 |
| P3 体验设计 | 《AI时代的用户体验》 | 待创建 | 3-4 |
| P4 系统构建 | 《AI Native 产品方法论》 | ✅ 就绪 | 4 |
| P5 商业模式 | 《AI确定性商业模式》 | 待创建 | 2-3 |
| P6 增长策略 | 《AI Native 营销与增长》 | 待创建 | 3-4 |
| P7 审计投产 | 《AI Native 产品方法论》 | ✅ 就绪 | 1 |

---

## 核心架构

### 单 Agent + 七阶段流 + 共享 Product Context

```
┌─────────────────────────────────────────────────────────────┐
│                    ai-native-pm-agent                        │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ P1 需求   │→│ P2 方向   │→│ P3 体验   │→│ P4 系统   │   │
│  │ 发现     │  │ 定界     │  │ 设计     │  │ 构建     │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│       ↑           ↑           ↑           ↑                │
│       └───────────┴───────────┴───────────┘                │
│              共享产品上下文 (Product Context)                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                 │
│  │ P5 商业   │→│ P6 增长   │→│ P7 审计   │                 │
│  │ 模式     │  │ 策略     │  │ 投产     │                 │
│  └──────────┘  └──────────┘  └──────────┘                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Product Context Schema

```yaml
product_id: uuid          # 产品唯一标识
stage: string             # 当前阶段
completed_stages: []      # 已完成阶段
artifacts:                # 各阶段输出物
  p1_needs: {}            # 需求简报
  p2_direction: {}        # 方向定界简报
  p3_ux: {}               # UX 方案
  p4_system: {}           # 系统架构方案
  p5_business: {}         # 商业模式方案
  p6_growth: {}           # 增长策略方案
  p7_audit: {}            # 审计放行方案
decisions: []             # 关键决策记录
flags:                    # 状态标记
  needs_revisit: []       # 需要回溯的阶段
  blockers: []            # 阻塞项
  user_approvals: []      # 用户确认点
```

---

## 阶段路由规则

### 默认流
```
p1 → p2 → p3 → p4 → p5 → p6 → p7
```

### 关键路由决策

| 条件 | 动作 |
|------|------|
| p1.opportunity_score < 60 | 暂停，提示重新审视需求 |
| p2.go_no_go == "no-go" | 终止，输出方向定界结论 |
| p2.go_no_go == "conditional" | 标记条件，进入 p3 但附加约束 |
| 用户说"跳过商业模式" | p4 → p6，跳过 p5 |
| p7.audit == "no-go" | 回溯到 p4 |

---

## 冲突检测规则

| 检测 | 触发条件 | 规则 |
|------|---------|------|
| 成本-定价匹配 | p4 + p5 完成 | system_cost * 3 < pricing_floor |
| UX-系统延迟匹配 | p3 + p4 完成 | ux_requires_realtime AND latency > 2s |
| 增长-承载匹配 | p6 + p4 完成 | target_mau / 30 > system_capacity |

---

## 实施路线图

### Phase 1: 核心工作流验证（2-3周）
- P2 → P4 → P7 跑通
- 验证 Skill 编排和上下文传递

### Phase 2: 前端补强（2周）
- 接入 P1（需求发现）和 P3（体验设计）

### Phase 3: 商业闭环（2周）
- 接入 P5（商业模式）和 P6（增长策略）

### Phase 4: 智能化（持续）
- 自动推荐、冲突检测、决策回溯

---

## 文件结构

```
ai-native-pm-agent/
├── SKILL.md                           # Agent 主入口
├── ARCHITECTURE.md                    # 本架构文档
├── references/
│   ├── product-context-schema.md      # 共享上下文协议
│   ├── stage-routing.md               # 阶段路由规则
│   └── conflict-detection.md          # 冲突检测规则
├── scripts/
│   ├── init_product_context.py        # 初始化上下文
│   └── test_orchestrator.py           # 编排逻辑测试
└── templates/
    └── report-template.md             # 输出报告模板
```
