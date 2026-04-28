---
skill:
  name: p8a-rax-risk-assessor
  version: 1.0.0
  description: >-
    RAX 风险评估器。基于《AI时代的用户体验》RAX 框架（Risk, Ambiguity, eXposure），
    系统性评估 AI 产品的风险、模糊性和暴露程度，帮助产品团队识别和管理用户体验风险。
  author: Max
  tags: [book-skill, risk-assessment, RAX, user-experience, ai-product]
  requires: []
---

# RAX 风险评估器

## 一句话定位

系统性评估 AI 产品的风险（Risk）、模糊性（Ambiguity）和暴露程度（eXposure），找出用户体验的弱点。

## 何时触发

- AI 产品即将上线或已上线，需要评估用户体验风险
- 用户反馈产品"不可靠"或"不透明"
- 需要优先级排序风险修复
- 需要向利益相关者展示风险管理能力

## 输入

产品描述 + 用户场景 + 已知问题。

**示例输入**：
```
产品: AI 医疗诊断助手
场景: 帮助医生诊断疾病
用户: 临床医生
已知问题: 医生担心 AI 诊断错误导致误诊
```

## RAX 框架

### R - Risk（风险）

**定义**：AI 出错时用户要承担什么后果？

**评估项**：
- [ ] 出错的概率是多少？
- [ ] 出错的代价是多少（金钱、职业、健康、法律）？
- [ ] 出错是否可逆？
- [ ] 是否有回滚机制？

**输出格式**：
```
Risk 评估:
  error_probability: "出错概率"
  error_cost:
    financial: "金钱损失"
    career: "职业风险"
    health: "健康风险"
    legal: "法律风险"
    reputation: "声誉风险"
  reversibility: "是否可逆"
  rollback: "回滚机制"
  risk_level: "低/中/高/极高"
```

### A - Ambiguity（模糊性）

**定义**：用户能不能理解 AI 在做什么？

**评估项**：
- [ ] AI 的行为是否可解释？
- [ ] 用户是否知道 AI 的能力边界？
- [ ] 系统的输出是否一致可预测？
- [ ] 用户是否知道什么时候应该不信任 AI？

**输出格式**：
```
Ambiguity 评估:
  explainability: "可解释性"
  boundary_clarity: "能力边界清晰度"
  output_consistency: "输出一致性"
  trust_boundary: "信任边界"
  ambiguity_level: "低/中/高"
```

### X - eXposure（暴露程度）

**定义**：用户在多大程度上依赖 AI 的输出？

**评估项**：
- [ ] 用户是否可以选择不使用 AI？
- [ ] 用户是否可以审核 AI 的输出？
- [ ] AI 是辅助还是决策？
- [ ] 用户有没有退出机制？

**输出格式**：
```
eXposure 评估:
  optional_usage: "使用是否可选"
  output_review: "输出是否可审核"
  ai_role: "辅助/决策"
  exit_option: "退出机制"
  exposure_level: "低/中/高"
```

## 综合评估

### RAX 矩阵

```
        低暴露        中暴露        高暴露
低风险  ✓ 安全      ✓ 可接受    ⚠ 需要监控
中风险  ✓ 可接受    ⚠ 需要监控  ⚠ 需要改进
高风险  ⚠ 需要监控  ⚠ 需要改进  ✗ 危险
```

### 优先级排序

**高优先级**：
- 高风险 + 高暴露：立即停止使用，重新设计
- 高模糊性 + 高暴露：用户不知道在信什么，危险

**中优先级**：
- 中风险 + 高暴露：需要改进
- 高风险 + 中暴露：需要改进

**低优先级**：
- 低风险 + 低暴露：可以接受
- 低模糊性 + 低暴露：可以接受

## 综合输出格式

```yaml
rax_assessment:
  input:
    product: "产品名称"
    scenario: "使用场景"
    user: "目标用户"
    known_issues: ["已知问题"]
  
  risk:
    error_probability: "出错概率"
    error_cost: "出错代价"
    reversibility: "可逆性"
    rollback: "回滚机制"
    level: "低/中/高/极高"
  
  ambiguity:
    explainability: "可解释性"
    boundary_clarity: "能力边界"
    output_consistency: "输出一致性"
    trust_boundary: "信任边界"
    level: "低/中/高"
  
  exposure:
    optional_usage: "使用可选性"
    output_review: "输出可审核性"
    ai_role: "辅助/决策"
    exit_option: "退出机制"
    level: "低/中/高"
  
  matrix:
    risk_level: "风险等级"
    exposure_level: "暴露等级"
    ambiguity_level: "模糊等级"
    overall_status: "安全/可接受/需改进/危险"
  
  recommendations:
    critical: ["立即要做的"]
    high: ["高优先级改进"]
    medium: ["中优先级改进"]
    low: ["低优先级改进"]
```

## 示例：AI 医疗诊断助手

| 维度 | 评估 | 等级 |
|------|------|------|
| Risk | 出错可能导致误诊，代价极高 | 高 |
| Ambiguity | 医生不太理解 AI 的判断逻辑 | 中 |
| eXposure | AI 只是辅助，最终诊断权在医生 | 中 |

**综合判断**：需要改进

**建议**：
- 立即：加强错误检测和告警机制
- 短期：提升可解释性，让医生理解 AI 的判断依据
- 长期：建立人机协同诊断流程

## 常见误判

- **只关注准确率**：高准确率不等于低风险，出错代价更重要
- **忽视模糊性**：用户不理解 AI 的行为，即使结果正确也会不信任
- **高估用户能力**：假设用户能够判断 AI 是否出错

## 一句判断

> RAX 的核心不是消除风险，而是让风险可见、可管理、可接受。
