---
name: p6b-arbiter-mode-designer
version: 1.0.0
description: 仲裁者模式设计器。设计以"真相即服务"为核心的商业模式： 提供可验证的真实信息和判断，让用户相信每个数字都是真的。 基于《AI确定性商业模式》概念卡。
author: Max
tags: p6, 商业模式, 仲裁者模式
- book-skill
- business-model
- arbiter-mode
- truth-service
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p6b-arbiter-mode-designer
stage: p6b
source_book: AI确定性商业模式
source_chapter: 第03章 仲裁者模式

---


# 仲裁者模式设计器

## 一句话定位

设计一个"每个数字都是真的"的产品，让用户为可验证的真实信息付费。

## 何时触发

- 产品的核心价值是提供可验证的信息
- 用户为"信息准确性"有明确痛点
- 行业存在大量不确定或虚假信息
- 需要建立权威背书和追溯机制

## 输入

行业 + 用户痛点 + 可验证的信息类型。

**示例输入**：
```
行业: 金融投资
用户: 个人投资者
痛点: "市面上太多虚假信息，不知道该信谁"
可验证信息: 公司财务数据、监管文件、行业报告
```

## 设计步骤

### Step 1: 定义真相范围

**任务**：明确产品承诺提供哪些类型的可验证信息。

**输出**：
```
真相范围:
  information_types: ["可提供的信息类型"]
  verification_methods: ["验证方法"]
  sources: ["信息来源"]
  limitations: ["不能保证的范围"]
```

### Step 2: 设计可验证机制

**任务**：让用户能够验证每个信息的真实性。

**输出**：
```
验证机制:
  transparency_level: "透明度等级"
  traceability: "是否可追溯到原始来源"
  third_party_verification: "是否有第三方验证"
  user_audit: "用户是否可以自己验证"
  update_frequency: "信息更新频率"
```

### Step 3: 设计权威背书

**任务**：建立产品的可信度和权威性。

**输出**：
```
权威背书:
  data_sources: ["数据来源及其权威性"]
  partnerships: ["合作伙伴"]
  certifications: ["认证和合规"]
  expert_review: "是否有专家审核"
  methodology: "信息处理方法论"
```

### Step 4: 设计收费模式

**任务**：将真相服务转化为可持续的收入。

**收费方式**：
```
收费模式:
  - 订阅制: "无限次验证服务"
  - 按次计费: "每次验证收费"
  - 分级服务: "基础信息免费，深度验证付费"
  - 企业服务: "定制化验证解决方案"
```

## 综合输出格式

```yaml
arbiter_mode_design:
  input:
    industry: "行业"
    user_pain: "用户痛点"
    verifiable_info: ["可验证信息类型"]
  
  truth_scope:
    types: ["信息类型"]
    methods: ["验证方法"]
    sources: ["来源"]
    limits: ["限制"]
  
  verification:
    transparency: "透明度"
    traceability: "可追溯性"
    third_party: "第三方验证"
    user_audit: "用户自审"
    update_freq: "更新频率"
  
  authority:
    sources: ["数据来源"]
    partners: ["合作伙伴"]
    certifications: ["认证"]
    experts: "专家审核"
    methodology: "方法论"
  
  pricing:
    model: "收费模式"
    tiers: ["服务等级"]
    unit: "计费单位"
    value_proposition: "价值主张"
  
  moat:
    data_flywheel: "数据飞轮"
    brand_trust: "品牌信任"
    network_effects: "网络效应"
    switching_cost: "转换成本"
```

## 示例：金融信息平台

**设计**：
- 真相范围：公司财务数据、监管处罚、行业排名
- 验证机制：每个数据点都可追溯到原始公开文件
- 权威背书：与主流金融数据提供商合作
- 收费：基础查询免费，深度分析订阅制

## 常见误判

- **过度承诺**：保证了不能保证的东西，一旦出错信任崩塌
- **验证不足**：声称可验证但用户无法实际验证
- **数据渠道单一**：依赖单一数据源，风险集中

## 一句判断

> 仲裁者模式的核心不是信息本身，而是信息的可验证性。
