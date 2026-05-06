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

## 核心概念

### 1. Trust Threshold（信任阈值）

**定义**：用户愿意"放手"让 AI 自主行动的成功率临界点。这个临界点由三个变量共同决定。

**关键点**：
- 核心公式：**Trust Threshold = f（风险等级，介入成本，替代方案）**
- 风险等级：AI 犯错时用户承受的后果有多严重，决定用户的"容错上限"
- 介入成本：用户干预 AI 时需要付出的代价，介入成本越高，用户越不愿干预，反而要求 AI 更可靠
- 替代方案：AI 不可信时用户还有什么选择，替代方案越多，对 AI 的信任要求越严格
- 信任不是感性的冲动，而是一种理性的风险收益计算

> 来源：书稿 ch07「Trust Threshold 模型：信任决策的量化框架」

### 2. 信任的经济学：边际效益递减

**定义**：在 Trust Threshold 以下，提升 AI 可靠性带来的信任增长剧烈；超过阈值后，继续投入资源提升可靠性是低效的。

**关键点**：
- 60%→70% 的准确率提升用户感知明显，98%→99% 的提升几乎无人察觉
- 后者的技术开发成本可能是前者的十倍以上
- 如果 AI 已越过 Trust Threshold，更明智的做法是把资源分配到降低介入成本、提升透明度等其他维度
- 团队最常见的资源错配：花三个月把准确率从 95% 提升到 99%，而忽视了其他信任变量

> 来源：书稿 ch07「信任的经济学：不是越可靠越好」

### 3. Agency-Control Tradeoff（自主权-控制权权衡）

**定义**：每次赋予 AI 系统更多的自主权（agency），就意味着人类让渡出一部分控制权。自主权必须通过持续的信任积累逐步获得，而非一次性授予。

**关键点**：
- AI 产品与传统软件的根本区别：非确定性 + agency-control tradeoff
- 大多数团队的错误：在测试系统出错时会发生什么之前，就直接跳到完全自主模式
- 信任资本（trust capital）是用户在"赋予 agency"时计算的核心变量
- 渐进式授权设计：从低自主 → 中自主 → 高自主 → 适应性自主

> 来源：书稿 ch07 延伸阅读「CC/CD Framework」及案例库 Smashing Magazine「6大信任设计模式」

### 4. 信任分级的四阶段模型

**定义**：将用户对 AI 的信任发展划分为四个阶段，每个阶段对应不同的 AI 自主程度、用户控制程度和透明度要求。

**关键点**：
- **尝试级（Trial）**：AI 只提供建议，用户完全控制，详细解释逻辑
- **验证级（Validation）**：AI 可执行简单任务，关键决策需确认，抽样验证
- **委托级（Delegation）**：AI 自主执行，只在异常时通知，定期审查
- **协作级（Collaboration）**：AI 根据任务自动调整，学习用户偏好，预测性回滚
- 每个阶段的过渡需要明确的触发条件和保护机制

> 来源：主 Skill SKILL.md「信任度分级」章节

### 5. 行为使用 ≠ 心理信任

**定义**：用户继续使用一个 AI 产品，可能是因为切换成本高（客观约束）、组织强制要求（被动接受）、暂时没有更好的替代品（阶段性容忍），而非真正的信任。

**关键点**：
- 不要把替代方案的稀缺性当作理所当然的信任红利
- 低 Trust Threshold 可能掩盖了产品真实的问题
- 当用户"不得不"容忍 AI 时，他们在积累不满，只是没有表达出来
- 一旦更好的替代方案出现，这些不满会迅速转化为流失
- 产品团队如果把表面的"继续使用"误解为"用户信任度很高"，就会在关键场景中过度放权

> 来源：书稿 ch07「替代方案：信任的外部约束」

## 分步执行

### 步骤 1：场景分析与信任现状评估

**操作说明**：
列出产品中所有 AI 参与的核心场景，评估每个场景当前用户的信任状态：用户对 AI 的接受度如何？是否存在过度依赖或拒绝使用的情况？用户在哪些环节频繁检查/修改 AI 输出？

**输出物**：
```yaml
trust_assessment:
  场景A:
    current_trust_level: "低/中/高"
    user_behavior: "描述用户当前行为模式"
    pain_points: ["信任相关的痛点"]
```

### 步骤 2：Trust Threshold 三变量评估

**操作说明**：
对每个场景评估三个核心变量：风险等级（R，1-10分）、介入成本（I，操作步骤数+认知门槛）、替代方案（S，用户转向替代方案的代价，1-10分）。根据三变量组合判断该场景用户的信任阈值水平。

**输出物**：
```yaml
trust_threshold:
  场景A:
    risk_level: "R=7，高风险"
    intervention_cost: "I=3，低介入成本（一键重写）"
    alternatives: "S=4，中等替代难度"
    threshold: "偏高，需要优先提升可靠性"
```

### 步骤 3：信任分级设计

**操作说明**：
根据 Trust Threshold 评估结果，为每个场景设计四阶段信任分级体系（尝试→验证→委托→协作）。明确每个阶段的 AI 自主程度、用户控制程度、透明度要求和回滚机制。

**输出物**：
```yaml
tier_design:
  trial:
    ai_autonomy: "低"
    user_control: "高"
    transparency: "高"
    rollback: "简单"
  validation:
    ai_autonomy: "中"
    user_control: "中"
    transparency: "中"
    rollback: "可用"
  delegation:
    ai_autonomy: "高"
    user_control: "低"
    transparency: "低"
    rollback: "复杂"
  collaboration:
    ai_autonomy: "适应"
    user_control: "智能"
    transparency: "适应"
    rollback: "智能"
```

### 步骤 4：过渡触发条件设计

**操作说明**：
为每个阶段之间的过渡设计明确的触发条件：用户完成任务次数、AI 建议接受率、用户主动调整行为等量化指标。同时设计过渡保护机制：用户可手动调整等级、升级时保留回滚、降级时保持历史设置、异常自动降级。

**输出物**：
```yaml
transitions:
  trial_to_validation:
    conditions: ["完成X次任务", "AI建议接受率>80%", "用户主动调整过AI建议"]
    protections: ["用户可手动调整", "保留回滚选项"]
  validation_to_delegation:
    conditions: ["完成Y次复杂任务", "自动执行满意度>90%"]
    protections: ["升级时默认保留回滚", "异常自动降级"]
```

### 步骤 5：信任 UX 细节设计

**操作说明**：
为每个信任等级设计具体的 UX 细节：来源展示方式、不确定性提示、边界告知、置信度信号。参考 Smashing Magazine 的 6 大信任设计模式：Intent Preview（意图预览）、Autonomy Dial（自主性旋钮）、Explainable Rationale（可解释理由）、Confidence Signal（置信度信号）、Action Audit & Undo（行动审计与撤销）、Escalation Pathway（升级路径）。

**输出物**：
```yaml
trust_ux_details:
  来源展示: "每个AI建议标注数据来源和推理依据"
  不确定性提示: "置信度颜色+文字双重编码"
  边界告知: "明确告知AI的能力边界和不适用场景"
  置信度信号: "高(绿色)/中(黄色)/低(红色) 三级信号"
  撤销机制: "每个AI操作都可追溯、可撤销"
  升级路径: "低置信度场景自动提供转人工入口"
```

### 步骤 6：验证与调优机制

**操作说明**：
设计信任分级体系的验证方法：用户测试验证信任感知是否匹配设计意图、A/B 测试验证过渡触发条件是否合理、持续监控信任相关指标（接受率、回退率、降级触发率）。

**输出物**：
```yaml
validation_plan:
  metrics: ["AI建议接受率", "用户回退操作率", "降级触发频率", "手动调整等级比例"]
  test_methods: ["用户访谈", "A/B测试", "行为数据监控"]
  iteration_cycle: "每月回顾信任指标，调整过渡条件"
```

## 示例

### 示例 1：AI 写作助手的信任分级设计

**场景描述**：
一款 AI 写作助手帮助用户撰写业务邮件。用户对 AI 写作质量有疑虑——不知道 AI 写的邮件是否合适、是否遗漏关键信息。需要设计信任分级体系，让用户从"试试看"逐步建立信任。

**用户输入**：
```
产品: AI 写作助手
场景: 帮助用户写作业务邮件
用户: 职场人士，对 AI 写作质量有疑虑
AI能力: 能写出合格邮件，但可能缺乏个性
```

**执行流程**：

1. **Trust Threshold 评估**：
   ```
   风险等级 R = 4（邮件写错的后果中等：可能影响商务关系）
   介入成本 I = 2（一键编辑，几秒钟可修改）
   替代方案 S = 3（用户可以自己写，但效率较低）
   → 信任阈值偏低，AI 不需要接近完美就能获得放手授权
   ```

2. **四阶段分级设计**：
   ```
   尝试级：AI 提供多个写作建议，用户选择并修改
   验证级：AI 自动生成草稿，用户确认后发送
   委托级：AI 自动处理常规邮件，只在异常时通知
   协作级：AI 学习用户写作风格，自动调整语气和用词
   ```

3. **过渡条件**：
   ```
   尝试→验证：用户完成 10 次邮件 + 接受率 > 70%
   验证→委托：用户完成 50 次邮件 + 满意度 > 85%
   委托→协作：AI 学习了用户 200+ 封邮件的风格特征
   ```

**输出结果**：

```yaml
trust_tier_design:
  product: "AI 写作助手"
  scenario: "业务邮件撰写"

  trust_threshold:
    risk_level: 4
    intervention_cost: 2
    alternatives: 3
    threshold: "偏低"

  tiers:
    trial:
      description: "AI 提供 3 个候选建议，用户选择并修改"
      ai_autonomy: "低 - 只建议不执行"
      user_control: "高 - 用户完全控制"
      transparency: "高 - 解释每个建议的写作逻辑"
      rollback: "一键撤销"
    validation:
      description: "AI 自动生成完整草稿，用户确认后发送"
      ai_autonomy: "中 - 可生成完整草稿"
      user_control: "中 - 用户确认后执行"
      transparency: "中 - 标注不确定的措辞"
      rollback: "编辑后重新生成"
    delegation:
      description: "AI 自动处理常规邮件，异常时通知"
      ai_autonomy: "高 - 自主处理常规邮件"
      user_control: "低 - 只处理异常"
      transparency: "低 - 异常时才解释"
      rollback: "已发送邮件可追回"
    collaboration:
      description: "AI 学习用户风格，自动调整语气用词"
      ai_autonomy: "适应 - 根据邮件类型自动调整"
      user_control: "智能 - AI 学习用户偏好"
      transparency: "适应 - 根据用户偏好调整"
      rollback: "智能 - 预测性回滚"

  trust_ux:
    来源展示: "标注参考了用户历史邮件中的哪些风格特征"
    置信度信号: "高置信(绿色边框) / 中置信(黄色+请确认) / 低置信(红色+建议修改)"
    撤销机制: "每个版本可一键回退到上一版"
    升级路径: "复杂邮件自动建议用户人工审核"
```

### 示例 2：企业知识库 AI 搜索的信任分级设计

**场景描述**：
企业内部知识库的 AI 搜索与问答系统。员工用它查制度、找流程、查技术文档。AI 回答有时引用了过时文档，有时对不确定的问题也给出肯定回答，导致用户信任度下降。

**用户输入**：
```
产品: 企业知识库 AI 搜索
场景: 员工查询制度、流程、技术文档
用户: 全体员工
AI能力: 能检索并综合文档，但有时引用过时文档
已知问题: AI 对不确定的问题也给出肯定回答，员工开始不信它
```

**执行流程**：

1. **Trust Threshold 评估**：
   ```
   风险等级 R = 6（依据错误制度执行可能导致合规问题）
   介入成本 I = 5（需要手动查找原始文档验证）
   替代方案 S = 4（可以问同事或查纸质手册，但效率低）
   → 信任阈值偏中高，需要显著提升透明度和可验证性
   ```

2. **信任分级设计**：
   ```
   🟢 L1 - 高信任（置信度 ≥ 90%）：
     引用 3+ 篇一致文档 + 文档更新于 90 天内
     → 绿色卡片 + "高置信回答" + 可直接采纳

   🟡 L2 - 中信任（置信度 60-89%）：
     引用 1-2 篇文档 或 文档较旧
     → 黄色卡片 + "建议验证" + 展示引用来源列表

   🔴 L3 - 低信任（置信度 < 60%）：
     文档之间存在矛盾 或 无直接匹配
     → 红色卡片 + "需要人工确认" + 展示相关片段

   ⚪ L4 - 无法回答：
     知识库中无相关内容
     → 灰色提示 + "未找到相关知识" + 转人工入口
   ```

3. **信任 UX 细节**：
   - 每条回答必须标注引用文档名 + 更新日期 + 维护人
   - 时效性标记：✅ 最新 / ⚠️ 3个月前 / 🔴 超过6个月
   - 一致性标记：✅ 多篇一致 / ⚠️ 存在差异
   - 矛盾信息不强行给结论，展示多源让用户自行判断

**输出结果**：

```yaml
trust_tier_design:
  product: "企业知识库 AI 搜索"
  scenario: "员工查询制度和文档"

  trust_threshold:
    risk_level: 6
    intervention_cost: 5
    alternatives: 4
    threshold: "偏中高"

  tiers:
    L1_high_trust:
      condition: "置信度≥90%, 3+篇一致文档, 90天内更新"
      display: "绿色卡片 + 高置信回答"
      interaction: "可直接采纳，一键复制或分享"
      example: "根据《2026年差旅报销制度》第4.2条..."
    L2_medium_trust:
      condition: "置信度60-89%, 引用1-2篇或文档较旧"
      display: "黄色卡片 + 建议验证"
      interaction: "展示引用来源列表，鼓励查看原文"
      example: "根据《报销制度(2024版)》... ⚠️ 该文档已超6个月未更新"
    L3_low_trust:
      condition: "置信度<60%, 文档矛盾或无直接匹配"
      display: "红色卡片 + 需要人工确认"
      interaction: "不直接给结论，展示相关片段让用户判断"
      example: "找到3篇相关文档但内容存在差异..."
    L4_cannot_answer:
      condition: "知识库中无相关内容"
      display: "灰色提示 + 未找到相关知识"
      interaction: "提供转人工入口 + 我要提问"

  trust_ux:
    来源展示: "每条回答标注文档名+更新日期+维护人"
    时效性标记: "✅最新 / ⚠️3个月前 / 🔴超6个月"
    一致性标记: "✅多篇一致 / ⚠️存在差异"
    不确定性: "置信度颜色+文字双重编码"
    边界提示: "本系统覆盖行政HRIT制度类文档，法律问题建议咨询法务"
    撤销/纠正: "查看原文高亮定位 / 标记错误 / 报告过时 / 转人工"

  escalation_path:
    - "低信任回答自动提供转人工入口"
    - "高频错误问答 → 知识管理团队待办"
    - "过时文档 → 自动触发更新提醒"
```

### 示例 3：AI 客服 Copilot 的信任分级设计

**场景描述**：
设计一个 AI 客服协同工作台的信任分级体系。客服专员使用 AI 建议回复用户咨询，但 AI 建议有时不被采纳，有时被采纳后反而需要修改。需要让客服专员逐步建立对 AI 建议的信任。

**用户输入**：
```
产品: AI 客服 Copilot
场景: 客服专员使用 AI 建议回复用户咨询
用户: 客服专员
AI能力: 能生成合格回复，但高风险承诺场景表现不稳定
已知问题: AI 建议采纳率仅 40%，客服花大量时间审核修改
```

**执行流程**：

1. **Trust Threshold 评估**：
   ```
   风险等级 R = 5（错误回复可能影响客户满意度和公司声誉）
   介入成本 I = 3（行内编辑可快速修改）
   替代方案 S = 2（客服可以自己写回复，但效率低）
   → 信任阈值中等，需要通过透明度和置信度信号提升信任
   ```

2. **信任分级设计**：
   ```
   尝试级：AI 提供 3 个候选回复 + 每个回复的风险标记
  验证级：AI 自动生成回复草稿，客服确认后发送
  委托级：高置信+低风险建议自动发送，其他仍需确认
  协作级：AI 学习客服的修改模式，自动调整建议风格
   ```

3. **置信度信号设计**：
   ```
   高置信度（>90%）：绿色边框 + "推荐使用"
   中置信度（70-90%）：黄色边框 + "请确认"
   低置信度（<70%）：红色边框 + "建议人工处理"
   ```

**输出结果**：

```yaml
trust_tier_design:
  product: "AI 客服 Copilot"
  scenario: "客服专员回复用户咨询"

  trust_threshold:
    risk_level: 5
    intervention_cost: 3
    alternatives: 2
    threshold: "中等"

  tiers:
    trial:
      description: "AI 提供 3 个候选回复，客服选择并修改"
      ai_suggestions: "3个备选 + 风险标记(绿/黄/红)"
      transparency: "每个回复标注引用来源（规则第X条、订单#123）"
      rollback: "一键切换到其他候选"
    validation:
      description: "AI 自动生成草稿，客服确认后发送"
      auto_actions: ["信息查询", "初步意图识别"]
      human_confirm: ["回复生成", "解决方案推荐"]
      transparency: "关键决策提供解释"
    delegation:
      description: "高置信+低风险建议自动发送"
      auto_threshold: "置信度>90% + 风险等级=低"
      exceptions: ["高风险承诺", "投诉处理", "退款操作"]
      monitoring: "定期审查自动发送质量"
    collaboration:
      description: "AI 学习客服修改模式，自动调整建议"
      learning: "追踪人工编辑与原建议的差异"
      adaptation: "自动调整语气、用词、模板选择"

  trust_ux:
    置信度信号: "绿色(>90%推荐) / 黄色(70-90%请确认) / 红色(<70%人工处理)"
    来源展示: "基于订单#12345生成 / 引用退换货规则第3.2条"
    不确定性: "⚠️该情况较为少见，建议优先解释政策"
    边界: "退款涉及金额>500元需主管确认"
    纠偏入口: "快速编辑(行内) / 重新生成(一键) / 完全拒绝+反馈"

  feedback_loop:
    即时: "👍/👎 + 修改追踪 + 标签选择(准确/冗余/风格差/信息错误)"
    定期: "每周生成最佳建议和待改进建议报告"
    沉淀: "高采纳率建议→案例库 / 频繁修改场景→模型优化需求"

  progressive_path:
    阶段1: "所有建议人工审核（当前）"
    阶段2: "高置信度+低风险建议自动发送（达成90%准确率后）"
    阶段3: "仅异常/边界场景人工介入（长期目标）"
```

## 一句判断

> 信任不是一个开关，而是一个渐进的过程。好的设计让用户自己决定什么时候信任 AI。
