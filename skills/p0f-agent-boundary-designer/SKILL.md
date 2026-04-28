---
skill:
  name: p0f-agent-boundary-designer
  version: 1.0.0
  description: >-
    Agent 边界清单。AI 产品最危险的不是做不到，而是做过头。
    这个 Skill 帮你系统性地定义 AI 应该做什么、不应该做什么、什么时候必须停下来等人。
    基于《AI rebuild product needs》工具卡。
  author: Max
  tags: [book-skill, agent-design, boundary, safety, ai-product]
  requires: []
---

# Agent 边界清单

## 一句话定位

AI 产品最危险的不是做不到，而是做过头。这个清单帮你系统性地定义 AI 的边界。

## 何时触发

- 设计 AI Agent 或 Copilot 产品
- 需要明确 AI 的权限范围
- 高风险场景（医疗、金融、法律、安全）
- 需要设计"人工接管"机制

## 输入

产品场景描述 + 行业 + 风险等级。

**示例输入**：
```
产品: AI 合同审查助手
行业: 法律科技
风险等级: high
主要用户: 企业法务团队
```

## 输出

完整的边界设计文档，包括自动执行区、人工接管区、禁用区。

## 边界清单

### 类别 1: 决策权边界（AI 能不能做决定）

**检查项**：
- [ ] AI 可以提供建议，但不能做最终决定
- [ ] AI 可以做初筛，但高风险项必须人工复核
- [ ] AI 可以自动执行的动作有明确清单
- [ ] 每个自动执行动作都有回滚机制
- [ ] 用户可以随时取消 AI 的决定

**示例**：
```
合同审查助手:
  可以: 标注风险条款、提供模板建议、检查格式一致性
  不可以: 判断合同是否有效、决定是否签署、修改法律条款
  人工复核: 所有高风险条款、金额 > 100万的合同
```

### 类别 2: 数据边界（AI 能不能访问什么数据）

**检查项**：
- [ ] AI 可以访问的数据有明确清单
- [ ] 敏感数据的处理方式已定义
- [ ] 数据使用有审计日志
- [ ] 用户数据不会用于训练模型（除非明确授权）
- [ ] 数据删除和忘记机制已定义

**示例**：
```
合同审查助手:
  可以访问: 合同文本、公司模板库、公开法规
  不可以访问: 其他客户的合同、员工个人信息、第三方数据
  脱敏要求: 合同中的对方名称需要脱敏处理
```

### 类别 3: 行为边界（AI 能不能做什么行为）

**检查项**：
- [ ] AI 不会主动联系第三方
- [ ] AI 不会在未授权的情况下执行金钱操作
- [ ] AI 不会做出永久性、不可逆的改变
- [ ] AI 的行为有完整日志记录
- [ ] AI 的行为可以被用户审计和追溯

**示例**：
```
合同审查助手:
  可以: 生成审查报告、标注风险点、对比模板
  不可以: 自动发送给对方、自动修改合同、自动签署
  日志要求: 所有审查操作必须记录
```

### 类别 4: 责任边界（出了问题谁负责）

**检查项**：
- [ ] 每个 AI 决策都有明确的责任人
- [ ] AI 出错时的责任分配已定义
- [ ] 有明确的赔偿或回滚机制
- [ ] 用户已被明确告知 AI 的限制
- [ ] 有上升通道处理投诉和纠正

**示例**：
```
合同审查助手:
  责任人: 使用系统的律师
  AI错误: 系统提供「不构成法律建议」免责声明
  回滚: 可以重新生成审查报告
  用户告知: 首次使用时显示能力范围和限制
```

### 类别 5: 人机协作边界（什么时候 AI 停下来等人）

**检查项**：
- [ ] 明确定义了"人工接管触发条件"
- [ ] AI 在不确定时会主动请求人工确认
- [ ] 有明确的"人在回路"设计
- [ ] 人工接管的响应时间已定义
- [ ] AI 的自主性可以根据场景调整

**示例**：
```
合同审查助手:
  自动执行: 格式检查、标准条款匹配
  人工接管: 非标准条款、高风险标识、金额超阈值
  请求确认: "这个条款与标准模板不一致，请确认是否接受"
  响应时间: 人工接管请求 2 小时内响应
```

## 综合输出格式

```yaml
agent_boundary_design:
  input:
    product: "产品名称"
    industry: "行业"
    risk_level: "low/medium/high/critical"
    users: ["主要用户"]
  
  decision_boundary:
    can_decide: ["AI 可以做出的决定"]
    cannot_decide: ["AI 不能做的决定"]
    human_review_required: ["必须人工复核的情况"]
    rollback_available: "yes/no"
    user_can_override: "yes/no"
  
  data_boundary:
    can_access: ["可访问数据"]
    cannot_access: ["不可访问数据"]
    sensitive_handling: "敏感数据处理方式"
    audit_logging: "yes/no"
    training_consent: "yes/no"
  
  action_boundary:
    can_do: ["可以的行为"]
    cannot_do: ["不可以的行为"]
    irreversible_actions: ["不可逆行为"]
    action_logging: "yes/no"
    action_traceable: "yes/no"
  
  responsibility_boundary:
    owner: "责任人"
    ai_error_handling: "AI 错误处理"
    compensation: "赔偿机制"
    user_disclosure: "用户告知内容"
    escalation_path: "上升通道"
  
  human_ai_boundary:
    auto_execute: ["自动执行场景"]
    human_handoff: ["人工接管触发条件"]
    confirmation_requests: ["需要确认的场景"]
    response_time: "人工响应时间"
    autonomy_level: "full/partial/none"
  
  risk_assessment:
    highest_risk: "最高风险场景"
    mitigation: "缓解措施"
    residual_risk: "残留风险"
    review_frequency: "审查频率"
```

## 快速使用法

1. 填写产品、行业、风险等级
2. 逐个类别走清单
3. 确保每个"不能"都有对应的"如果发生了怎么办"
4. 让法务/合规/安全团队审核

## 常见误判

- **边界过于保守**：AI 什么都不能做，失去了价值
- **边界过于放宽**：AI 什么都能做，风险不可控
- **只定义能力，不定义责任**：出了问题不知道谁负责
- **忽视用户告知**：用户不知道 AI 的限制

## 一句判断

> 好的 Agent 边界不是限制 AI 能力，而是让 AI 在安全的范围内发挥最大价值。
