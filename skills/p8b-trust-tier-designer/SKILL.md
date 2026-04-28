---
name: p8b-trust-tier-designer
version: 1.0.0
description: 信任度分级设计器。基于《AI时代的用户体验》信任分级理论， 设计 AI 产品的信任度分级体系，让用户渐进式地建立对 AI 的信任。
author: Max
tags: p8, 用户体验, 信任分级
- book-skill
- trust-design
- tier-system
- user-experience
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p8b-trust-tier-designer
stage: p8b
source_book: ai-agent-ux
source_chapter: 第02章 信任分级设计

---


# 信任度分级设计器

## 一句话定位

设计一套信任度分级体系，让用户从"尝试"到"依赖"渐进式地建立对 AI 的信任。

## 何时触发

- AI 产品需要用户从不信任到信任
- 想要设计渐进式的 AI 交付策略
- 需要匹配用户的信任水平与 AI 的自主程度
- 需要避免用户过度依赖或拒绝使用

## 输入

产品场景 + 用户类型 + AI 能力边界。

**示例输入**：
```
产品: AI 写作助手
场景: 帮助用户写作业务邮件
用户: 职场人士，对 AI 写作质量有疑虑
AI能力: 能写出合格邮件，但可能缺乏个性
```

## 信任度分级

### 第一级：尝试（Trial）

**特征**：用户第一次接触 AI，持怀疑态度

**产品设计**：
```
尝试级:
  ai_autonomy: "低 - AI 只提供建议，不自动执行"
  user_control: "高 - 用户完全控制"
  transparency: "高 - 详细解释 AI 的建议逻辑"
  rollback: "简单 - 一键撤销"
  verification: "用户可以轻松验证 AI 建议的正确性"
```

### 第二级：验证（Validation）

**特征**：用户已经验证过 AI 的能力，开始建立信任

**产品设计**：
```
验证级:
  ai_autonomy: "中 - AI 可以执行简单任务，复杂任务需要确认"
  user_control: "中 - 用户可以设置规则和限制"
  transparency: "中 - 关键决策提供解释"
  rollback: "可用 - 可以回滚到上一版"
  verification: "抽样验证，关键决策必须确认"
```

### 第三级：委托（Delegation）

**特征**：用户已经充分信任 AI，愿意委托给 AI 处理

**产品设计**：
```
委托级:
  ai_autonomy: "高 - AI 可以自主执行，只在异常时通知用户"
  user_control: "低 - 用户设置策略，不干预执行"
  transparency: "低 - 只在异常时提供解释"
  rollback: "复杂 - 可以回滚到任意历史版本"
  verification: "定期审查，异常通知"
```

### 第四级：协作（Collaboration）

**特征**：AI 和用户形成高度协作关系

**产品设计**：
```
协作级:
  ai_autonomy: "适应 - 根据任务自动调整"
  user_control: "智能 - AI 学习用户偏好，自动调整"
  transparency: "适应 - 根据用户偏好调整透明度"
  rollback: "智能 - 预测性回滚"
  verification: "智能 - AI 主动提醒异常"
```

## 分级过渡设计

### 过渡触发条件

```
过渡条件:
  尝试 → 验证:
    - 用户完成了 X 次任务
    - 用户对 AI 建议的接受率 > 80%
    - 用户主动调整过 AI 的建议
  
  验证 → 委托:
    - 用户完成了 Y 次复杂任务
    - 用户对 AI 自动执行的满意度 > 90%
    - 用户开始设置高级规则
  
  委托 → 协作:
    - 用户与 AI 有长期互动历史
    - AI 已经学习了用户的工作模式
    - 用户表达了对 AI 的高度信任
```

### 过渡保护

```
过渡保护:
  - 用户可以手动调整信任等级
  - 升级时默认保留回滚选项
  - 降级时保持历史设置
  - 异常情况自动降级
```

## 综合输出格式

```yaml
trust_tier_design:
  input:
    product: "产品名称"
    scenario: "使用场景"
    user: "目标用户"
    ai_capability: "AI 能力边界"
  
  tiers:
    trial:
      name: "尝试级"
      autonomy: "低"
      control: "高"
      transparency: "高"
      rollback: "简单"
      verification: "完全验证"
    
    validation:
      name: "验证级"
      autonomy: "中"
      control: "中"
      transparency: "中"
      rollback: "可用"
      verification: "抽样验证"
    
    delegation:
      name: "委托级"
      autonomy: "高"
      control: "低"
      transparency: "低"
      rollback: "复杂"
      verification: "定期审查"
    
    collaboration:
      name: "协作级"
      autonomy: "适应"
      control: "智能"
      transparency: "适应"
      rollback: "智能"
      verification: "智能"
  
  transitions:
    trial_to_validation:
      conditions: ["过渡条件"]
      protections: ["保护机制"]
    validation_to_delegation:
      conditions: ["过渡条件"]
      protections: ["保护机制"]
    delegation_to_collaboration:
      conditions: ["过渡条件"]
      protections: ["保护机制"]
  
  implementation:
    default_tier: "默认等级"
    user_override: "用户可手动调整"
    auto_adjust: "是否自动调整"
    rollback_always: "是否始终保留回滚"
```

## 示例：AI 写作助手

**设计**：
- 尝试级：AI 提供多个写作建议，用户选择并修改
- 验证级：AI 可以自动生成草稿，用户确认后发送
- 委托级：AI 自动处理常规邮件，只在异常时通知
- 协作级：AI 学习用户写作风格，自动调整语气和用词

## 常见误判

- **一开始就高自主**：用户还没建立信任就给 AI 高自主权
- **过渡太快**：信任建立需要时间，急不得
- **忽视降级**：只设计升级，不设计降级机制

## 一句判断

> 信任不是一个开关，而是一个渐进的过程。好的设计让用户自己决定什么时候信任 AI。
