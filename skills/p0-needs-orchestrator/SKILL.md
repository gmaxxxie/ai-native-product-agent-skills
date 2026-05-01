---
name: p0-needs-orchestrator
version: 1.1.0
description: 需求发现编排器。协调微需求检测、真需求验证、需求拆解、需求考古、好问题生成、Agent 边界设计、多元推荐改写、AI 产品三重平衡八个工具卡，
  按顺序执行并输出完整的需求发现报告。自包含——八个工具卡的核心方法已内嵌。
  基于《AI rebuild product needs》读者工具箱。
author: Max
tags:
  - p0
  - 需求发现
  - 编排器
  - book-skill
  - needs-discovery
  - orchestrator
  - ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p0-needs-orchestrator
stage: p0
source_book: AI rebuild product needs
source_chapter: 编排器
absorbed_skills:
  - p0a-micro-needs-detector
  - p0b-real-needs-validator
  - p0c-needs-decomposer
  - p0d-needs-archaeologist
  - p0e-good-question-generator
  - p0f-agent-boundary-designer
  - p0g-diverse-recommendation-rewriter
  - p0h-ai-product-triple-balance

---


# 需求发现编排器

## 一句话定位

从一个模糊的痛点线索出发，系统性地跑完六个工具卡，输出可直接进入方向定界的需求发现报告。

## 何时触发

- 你有一个产品想法或痛点线索，需要系统性验证
- 需要从需求发现到方向定界的完整过程
- 想要确保需求判断有结构化依据

## 输入

一个模糊的产品想法或痛点描述。

**示例输入**：
```
"我想做一个 AI 客服产品，帮企业自动回复客户问题"
```

## 编排流程

```
用户输入
  ↓
【Step 1: 微需求检测】p0a-micro-needs-detector
  → 输出: 是否存在被忽视的微需求
  ↓
【Step 2: 需求四层拆解】p0c-needs-decomposer
  → 输出: 表达层/场景层/处境层/代价层
  ↓
【Step 3: 真需求验证】p0b-real-needs-validator
  → 输出: 真/伪需求判断
  ↓
【Step 4: 需求考古】p0d-needs-archaeologist
  → 输出: 深层需求 + 历史约束
  ↓
【Step 5: 好问题生成】p0e-good-question-generator
  → 输出: 六维度研究问题
  ↓
【Step 6: Agent 边界设计】p0f-agent-boundary-designer
  → 输出: 完整边界文档
  ↓
输出: 需求发现报告
```

## 每个 Step 的输入输出

### Step 1: 微需求检测

**输入**：用户原始想法
**输出**：
```yaml
micro_needs:
  found: true/false
  needs: ["发现的微需求列表"]
  recommendation: "是否需要重新定义问题"
```

### Step 2: 需求四层拆解

**输入**：用户原始想法
**输出**：
```yaml
decomposition:
  layer1: "表达层"
  layer2: "场景层"
  layer3: "处境层"
  layer4: "代价层"
  reframed_problem: "重定义的问题"
```

### Step 3: 真需求验证

**输入**：重定义后的需求
**输出**：
```yaml
validation:
  is_real: true/false
  pass_count: "X/5"
  confidence: "high/medium/low"
  if_fake: "如果是伪需求，真正的问题可能是"
```

### Step 4: 需求考古

**输入**：已验证的需求
**输出**：
```yaml
archaeology:
  deep_need: "深层需求"
  constraints: ["约束条件"]
  historical_attempts: ["历史尝试"]
  productizable: "yes/no"
```

### Step 5: 好问题生成

**输入**：深层需求
**输出**：
```yaml
good_questions:
  dimensions: ["六个维度的问题"]
  best_question: "最佳研究问题"
  research_direction: "研究方向"
```

### Step 6: Agent 边界设计

**输入**：产品场景
**输出**：
```yaml
boundary:
  decision: "决策权边界"
  data: "数据边界"
  action: "行为边界"
  responsibility: "责任边界"
  human_ai: "人机协作边界"
```

## 工具卡方法详解（自包含）

以下八个工具卡已合并到编排器中，不再作为独立 Skill 存在。每个工具卡的核心方法浓缩为 1-2 句话，便于快速参考。

### § p0a: 微需求五问检测器

用五个问题检测那些"太小不值得做"的问题是否是真正的产品起点：(1) 是否每天发生但每次很小？(2) 用户是否已发展出稳定 workaround？(3) 不做的话谁在默默承担代价？(4) 负担是否带着羞耻/疲惫/责任风险而不易表达？(5) 系统一旦接住，用户体感是否明显变轻？微需求靠重复出现的代价成立，不靠声量成立。

### § p0b: 真需求判断五问

五问给团队装刹车——三问答不扎实先不做方案：(1) 是否长期存在？(2) 让谁持续付出了什么代价？(3) 用户有没有为它发展出补偿行为？(4) 背后是不是有结构而不只是偏好？(5) 没人讨论它还会不会继续存在？真需求靠现实反复支付，伪需求靠热度和顺滑感成立。

### § p0c: 需求四层拆解

把用户原话逐层拆到表达层（用户原话是什么）、场景层（问题发生在何时何地与谁有关）、处境层（为什么被困住、谁在补位党底）、代价层（不接住会持续损失什么），最终重定义问题。任何一层说不清，先不进方案讨论。

### § p0d: 需求考古五步法

五步挖掘深层需求：(1) 现状层——描绘当前"正常"是什么；(2) 历史层——追溯"正常"是怎么来的；(3) 约束层——识别让大家不能做更好的约束条件；(4) 失败层——分析之前尝试过什么、为什么没成功、留下了什么遗产；(5) 深层需求层——提取真正要解决的问题。用户说出来的需求是最新的土壤层，真正的需求往往埋得更深。

### § p0e: 好问题六维观察表

从六个维度发现好问题：用户维度（用户在做什么/想什么/痛什么）、任务维度（任务流程哪里卡住）、系统维度（各系统怎么关联哪里是瓶颈）、组织维度（角色分工与权力分布）、时间维度（过去/现在/未来的变化）、对比维度（别人怎么做的有什么可借鉴）。好问题让正确的答案自然浮现。

### § p0f: Agent 边界清单

系统定义 AI 的五类边界：决策权边界（能不能做决定）、数据边界（能不能访问什么数据）、行为边界（能不能做什么行为）、责任边界（出了问题谁负责）、人机协作边界（什么时候停下来等人）。好的 Agent 边界不是限制 AI 能力，而是让 AI 在安全范围内发挥最大价值。

### § p0g: 多元推荐改写清单

从"猜你喜欢"进化到"帮你发现"：五个改写维度——推荐目标重定义（准确性→价值发现）、多元性引入（多算法混合七种推荐类型）、控制权交还用户（可切换/可解释/可关闭）、透明度设计（可解释推荐）、评估指标升级（准确率+多样性+用户成长）。附带审计六项检查：目标函数多样性、用户主动切换探索模式、低冲突异质内容入口、现实世界连接、新可能性衡量、跳出默认轨迹。多元推荐不是精度的对立面，而是对单一目标精度的修正。

### § p0h: AI 产品三重平衡表

评估商业（能不能创造价值）、人性（对人有没有侵害）、技术（能不能做到）三个维度的平衡。权衡规则：人性风险不可逆则人性优先；技术不成熟但商业机会重大可先 MVP 验证；技术能力不决定人性边界，人性边界决定技术能用多少。附带三层评估伴侣——商业层（长期成本 vs. 价值是否靠高成本堆出）、人性层（负担转移 vs. 主体性保留是否让人更依赖）、文化层（训练了什么价值观现实扩大还是缩小）。核心规则：如果只有商业层有答案，先不要推进。

## 综合输出格式

```yaml
needs_discovery_report:
  input: "原始想法"
  
  executive_summary:
    verdict: "需求是否成立"
    confidence: "high/medium/low"
    key_finding: "最重要的发现"
    recommendation: "建议动作"
  
  detailed_findings:
    micro_needs: "Step 1 结果"
    decomposition: "Step 2 结果"
    validation: "Step 3 结果"
    archaeology: "Step 4 结果"
    good_questions: "Step 5 结果"
    boundary: "Step 6 结果"
  
  next_steps:
    if_proceed: "如果继续，进入方向定界的准备"
    if_revisit: "如果需要回顾，重新定义的方向"
    if_stop: "如果停止，为什么"
  
  artifacts:
    direction_brief_input: "可以直接作为 ai-native-direction-framing 输入的内容"
```

## 使用方式

### 方式一：完整流程

```
我有一个想法: [描述]
帮我跑完需求发现流程
```

### 方式二：单独调用某个工具卡

```
帮我用微需求五问检测这个场景: [描述]
帮我做需求四层拆解: [需求]
帮我验证这个需求是不是真需求: [需求]
```

### 方式三：跳过某些步骤

```
需求已经验证过了，直接进入需求考古
边界设计已经有了，跳过 Step 6
```

## 与其他 Skill 的关系

- **上游输入**：用户的灵感、痛点、市场观察
- **下游输出**：ai-native-direction-framing（方向定界）
- **并行使用**：可以在 p1 过程中反复调用验证

## 一句判断

> 需求发现不是一次性活动，而是持续验证的过程。每个工具卡都是一个检查点，而不是最终答案。
