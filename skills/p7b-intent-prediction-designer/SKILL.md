---
name: p7b-intent-prediction-designer
version: 1.0.0
description: 意图预测营销设计器。基于《AI Native 营销与增长》意图预测营销概念卡， 帮助产品从"人群定向"升级为"个体预见"——在用户明确表达之前就提供相关内容。
author: Max
tags: p7, 营销增长, 意图预测
- book-skill
- intent-prediction
- marketing
- personalization
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p7b-intent-prediction-designer
stage: p7b
source_book: AI Native 营销与增长
source_chapter: 第03章 意图预测营销

---


# 意图预测营销设计器

## 一句话定位

从"人群定向"到"个体预见"——在用户明确表达之前，就预测他们需要什么并主动提供。

## 何时触发

- 用户转化率低，内容触达不精准
- 想从"用户搜索了什么"升级为"用户可能需要什么"
- 需要设计 AI 驱动的个性化推荐系统
- 获客成本持续上升

## 输入

产品场景 + 用户行为数据 + 当前触达方式。

**示例输入**：
```
产品: 在线教育平台
当前触达: 邮件推送课程推荐（基于浏览历史）
问题: 打开率 2%，转化率 0.1%
```

## 设计流程

### Step 1: 意图信号识别

**任务**：识别哪些用户行为可以预测意图。

**信号类型**：
```
显性信号:
  - 搜索关键词
  - 浏览路径
  - 加购行为
  - 直接询问

隐性信号:
  - 停留时长
  - 重复访问
  - 对比行为
  - 时间规律（如每月月底看某类内容）

上下文信号:
  - 时间（工作日/周末/深夜）
  - 地点
  - 设备类型
  - 上一动作
```

### Step 2: 意图分层

**任务**：将用户意图分层，匹配不同的响应策略。

```
意图分层:
  L0 无意图: 用户在漫无目的浏览 → 做好内容展示，不打扰
  L1 弱意图: 用户在探索某个方向 → 提供引导性内容
  L2 中意图: 用户在比较/评估 → 提供对比/评测内容
  L3 强意图: 用户即将决策 → 提供促成决策的内容（案例/优惠/限时）
  L4 行动意图: 用户正在执行 → 提供辅助/加速内容
```

### Step 3: 触达策略设计

**任务**：为每个意图层级设计触达策略。

```
触达策略:
  L0: 做好推荐位，不打扰
  L1: 侧边栏/推送卡片，轻量引导
  L2: 内容弹窗/对比工具，主动帮助
  L3: 定制化方案/限时优惠，促成决策
  L4: 一键操作/自动填充，减少摩擦
```

### Step 4: 反馈闭环

**任务**：设计从触达到模型更新的反馈闭环。

```
闭环:
  用户行为变化 → 更新意图评分 → 调整触达策略 → 观察效果 → 更新模型
```

## 综合输出格式

```yaml
intent_prediction_design:
  input:
    product: "产品名称"
    current_approach: "当前触达方式"
    problems: ["当前问题"]
  
  signals:
    explicit: ["显性信号"]
    implicit: ["隐性信号"]
    contextual: ["上下文信号"]
    available_now: ["当前可用的信号"]
    need_to_collect: ["需要额外收集的信号"]
  
  intent_layers:
    L0: { name: "无意图", strategy: "不打扰" }
    L1: { name: "弱意图", strategy: "轻引导" }
    L2: { name: "中意图", strategy: "主动帮助" }
    L3: { name: "强意图", strategy: "促成决策" }
    L4: { name: "行动意图", strategy: "减少摩擦" }
  
  feedback_loop:
    data_collection: "数据收集方式"
    model_update: "模型更新频率"
    strategy_adjust: "策略调整机制"
  
  implementation:
    phase1: "第一阶段（30天）"
    phase2: "第二阶段（90天）"
    phase3: "第三阶段（180天）"
  
  metrics:
    primary: "意图预测准确率"
    secondary: ["转化率", "触达响应率", "用户满意度"]
```

## 常见误判

- **过度预测**：预测太激进，用户感觉被监视
- **信号不足**：只依赖显性信号，忽视隐性信号
- **忽视隐私**：意图预测需要行为数据，必须注意隐私合规

## 一句判断

> 意图预测不是猜用户想要什么，而是在用户需要的时候恰好出现。
