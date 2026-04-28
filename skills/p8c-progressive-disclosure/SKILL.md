---
skill:
  name: p8c-progressive-disclosure
  version: 1.0.0
  description: >-
    渐进式披露清单。基于《AI时代的用户体验》渐进式披露理论，
    提供 AI 产品逐步展示功能和能力的设计清单，避免一次性向用户交付过多信息。
  author: Max
  tags: [book-skill, progressive-disclosure, ux-design, onboarding, ai-product]
  requires: []
---

# 渐进式披露清单

## 一句话定位

不要一次性把 AI 的所有能力都展示给用户，而是按照用户的成熟度逐步披露。

## 何时触发

- AI 产品功能复杂，需要分阶段展示
- 用户新手期流失率高
- 需要设计入门体验和功能发现机制
- 想要避免用户被复杂功能吓跑

## 输入

产品功能列表 + 用户成熟度阶段 + 核心价值路径。

**示例输入**：
```
产品: AI 数据分析工具
功能:
  - 基础数据导入
  - 自动图表生成
  - 智能分析建议
  - 高级建模
  - 自定义报告
  - API 接口
  - 团队协作
  - 自动化工作流
核心价值: 快速从数据中获得洞察
```

## 渐进式披露框架

### 阶段 1: 第一次价值（First Value）

**目标**：让用户在 5 分钟内体验到第一个"啊哈"时刻

**披露内容**：
```
第一次价值:
  features: ["最核心的 1-2 个功能"]
  complexity: "极低"
  setup: "零设置或自动设置"
  time_to_value: "< 5 分钟"
  guidance: "手把手引导"
```

### 阶段 2: 核心使用（Core Usage）

**目标**：让用户掌握日常使用的核心功能

**披露内容**：
```
核心使用:
  features: ["日常使用的 3-5 个功能"]
  complexity: "低"
  setup: "简单设置"
  time_to_value: "< 30 分钟"
  guidance: "上手教程 + 工具提示"
```

### 阶段 3: 高级功能（Advanced Features）

**目标**：让有需求的用户发现更多能力

**披露内容**：
```
高级功能:
  features: ["进阶功能"]
  complexity: "中"
  setup: "需要一定配置"
  discovery: "在用户需要时自然展示"
  guidance: "高级教程 + 示例"
```

### 阶段 4: 专家模式（Expert Mode）

**目标**：让高级用户充分发挥 AI 潜力

**披露内容**：
```
专家模式:
  features: ["全部功能"]
  complexity: "高"
  setup: "完全可配置"
  discovery: "需要主动探索"
  guidance: "文档 + 社区"
```

## 披露触发机制

### 触发方式

```
触发方式:
  - 时间触发: "使用 X 天后解锁"
  - 行为触发: "完成 X 次操作后解锁"
  - 需求触发: "用户表达某种需求时展示"
  - 上下文触发: "在特定场景下自动展示"
  - 手动触发: "用户主动点击解锁"
```

### 触发时机

```
触发时机:
  - 不要在用户第一次使用时展示所有功能
  - 在用户需要时展示，而不是你觉得用户需要时
  - 给用户选择权："想了解更多"
  - 避免弹窗干扰
```

## 综合输出格式

```yaml
progressive_disclosure_plan:
  input:
    product: "产品名称"
    features: ["全部功能列表"]
    core_value: "核心价值"
    user_journey: "用户主要使用路径"
  
  stages:
    first_value:
      name: "第一次价值"
      features: ["第一次展示的功能"]
      complexity: "极低"
      setup: "零设置"
      time_to_value: "< 5 分钟"
      guidance: "手把手引导"
    
    core_usage:
      name: "核心使用"
      features: ["核心功能"]
      complexity: "低"
      setup: "简单设置"
      time_to_value: "< 30 分钟"
      guidance: "上手教程"
    
    advanced:
      name: "高级功能"
      features: ["进阶功能"]
      complexity: "中"
      setup: "需要配置"
      discovery: "需求触发"
      guidance: "高级教程"
    
    expert:
      name: "专家模式"
      features: ["全部功能"]
      complexity: "高"
      setup: "完全可配置"
      discovery: "主动探索"
      guidance: "文档 + 社区"
  
  triggers:
    - type: "触发类型"
      condition: "触发条件"
      stage: "触发阶段"
  
  anti_patterns:
    - "避免的反模式1"
    - "避免的反模式2"
  
  metrics:
    - "新手完成率"
    - "功能发现率"
    - "用户活跃度"
    - "功能使用深度"
```

## 示例：AI 数据分析工具

**阶段设计**：
- 第一次价值：上传 CSV → 自动生成一个图表
- 核心使用：选择图表类型、添加筛选条件、导出报告
- 高级功能：联合分析、趋势预测、异常检测
- 专家模式：自定义建模、API 调用、自动化工作流

**触发机制**：
- 高级功能在用户试图做复杂操作时自动展示
- 专家模式需要主动点击"高级设置"

## 常见误判

- **一次性展示所有**：导致用户信息过载
- **披露太慢**：用户不知道产品还有更多能力
- **强制引导**：不给用户跳过教程的选择

## 一句判断

> 好的产品不是让用户知道你有多少功能，而是让用户在需要的时候自然地发现这些功能。
