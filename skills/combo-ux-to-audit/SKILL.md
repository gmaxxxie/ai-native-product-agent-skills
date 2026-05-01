---
name: combo-ux-to-audit
version: 1.0.0
description: UX 设计 → 审计放行 组合 Skill。将 RAX 风险评估、信任度分级、渐进式披露 与审计放行流程打通，输出 UX 审计报告 + 放行建议。
author: Max
tags: 编排器, UX到审计
- book-skill
- combo
- ux
- audit
- risk
- trust
- ai-product
requires:
- p8a-rax-risk-assessor
- p8b-trust-tier-designer
- p8c-progressive-disclosure
- ai-native-audit-release
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/combo-ux-to-audit
stage: combo
source_book: AI Native 产品方法论
source_chapter: 编排器

---


# UX 设计 → 审计放行

## 一句话定位

UX 设计完成后，用 RAX 评估风险、用信任分级验证设计、用渐进式披露检查引导——确保 UX 可以安全放行。

## 何时触发

- UX 设计完成，准备进入开发
- 需要验证 UX 设计是否满足审计要求
- 高风险场景上线前的最后检查
- 需要向合规/安全团队提供 UX 审计报告

## 输入

UX 设计方案 + 产品场景 + 风险等级。

**示例输入**：
```
产品: AI 医疗诊断助手
UX 设计: 医生输入症状 → AI 给出诊断建议 → 医生确认或修改
风险等级: 高
```

## 编排流程

```
输入: UX 设计方案
  ↓
【Step 1】RAX 风险评估 (p8a)
  → Risk: AI 出错时用户承担什么后果
  → Ambiguity: 用户能否理解 AI 在做什么
  → eXposure: 用户在多大程度依赖 AI 输出
  → 输出: RAX 矩阵评分
  ↓
【Step 2】信任度分级验证 (p8b)
  → 当前设计对应哪个信任等级
  → 信任等级是否匹配用户成熟度
  → 升级/降级路径是否设计
  → 输出: 信任分级评估
  ↓
【Step 3】渐进式披露检查 (p8c)
  → 功能披露是否符合渐进式原则
  → 新手引导是否充分
  → 高级功能是否在需要时展示
  → 输出: 披露合规检查
  ↓
【Step 4】放行建议生成
  → 综合 RAX + 信任分级 + 披露检查
  → 生成放行建议: go / conditional-go / no-go
  → 标注放行条件和监控指标
  ↓
输出: UX 审计报告 + 放行建议
```

## 综合输出格式

```yaml
ux_audit_report:
  input:
    product: "产品名称"
    ux_design: "UX 设计方案"
    risk_level: "低/中/高/极高"
  
  rax_assessment:
    risk: { level: "低/中/高/极高", issues: ["问题"] }
    ambiguity: { level: "低/中/高", issues: ["问题"] }
    exposure: { level: "低/中/高", issues: ["问题"] }
    overall: "安全/可接受/需改进/危险"
  
  trust_tier:
    current_design_tier: "尝试/验证/委托/协作"
    user_maturity_tier: "尝试/验证/委托/协作"
    match: true/false
    upgrade_path: "升级路径"
    downgrade_trigger: "降级触发条件"
  
  disclosure_check:
    first_value_clear: true/false
    complexity_appropriate: true/false
    advanced_features_hidden: true/false
    expert_mode_available: true/false
  
  verdict:
    decision: "go / conditional-go / no-go"
    conditions: ["放行条件（如果是 conditional-go）"]
    blockers: ["阻塞项（如果是 no-go）"]
  
  monitoring:
    must_watch: ["上线后必须监控的指标"]
    warning_thresholds: ["告警阈值"]
    rollback_triggers: ["回滚触发条件"]
```

## 示例：AI 医疗诊断助手

| 检查项 | 结果 | 等级 |
|--------|------|------|
| RAX Risk | 诊断错误可能导致误诊 | 高 |
| RAX Ambiguity | 医生不理解 AI 判断逻辑 | 中 |
| RAX eXposure | AI 只是辅助，医生有最终决定权 | 中 |
| 信任分级 | 设计在"验证级"，但用户还在"尝试级" | 不匹配 |
| 渐进式披露 | 首次使用缺少充分引导 | 需改进 |

**放行建议**: conditional-go
**条件**：
1. 增加诊断建议的可解释性（降低 Ambiguity）
2. 增加新手引导流程（匹配"尝试级"信任）
3. 设置异常检测告警（降低 Risk）

## 一句判断

> UX 审计不是找设计的问题，而是确保设计在真实使用场景下安全可靠。
