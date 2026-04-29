<p align="center">
  <img src="assets/hero-banner.png" alt="AI Native PM Agent — 从想法到上线" width="100%">
</p>

# AI Native PM Agent

> 一个会问你"这方向真的值得做吗"的 AI 产品教练——从灵感火花到上线投产，每一步都有方法论兜底。

---

## 为什么需要这个？

做 AI 产品的人，90% 死在同一个坑里：

- **方向坑**：花 3 个月做了个 AI 功能，发现用户根本不想付费
- **需求坑**：伪需求太容易长得像真需求，AI 让原型成本趋近于零，也让你更快做错东西
- **边界坑**：AI 越界做了不该做的事，引发合规风险
- **幻觉坑**：上线前觉得准确率 95%，上线后被真实场景打回原形
- **成本坑**：Token 账单暴涨，商业模式跑不通

这个 Agent 不是帮你写代码的，是帮你在**每个关键决策点停下来，用结构化方法验证一遍**。

### 为什么不直接用传统产品方法论？

传统产品框架（精益创业、JTBD、设计思维）诞生在一个**原型成本高、AI 不存在**的世界。它们在 AI 时代会失效，因为：

| 传统假设 | AI 时代现实 |
|---------|-----------|
| 构建-测量-学习需要数周 | AI 原型几乎免费——你可以**更快地做错东西** |
| 用户需求相对稳定 | AI 创造新需求，也让旧需求一夜过时 |
| 产品边界是清晰的 | AI 会越过你没画的线——合规、伦理、自主性 |
| 成本随功能增长 | Token 成本随用量增长——商业模式可能反转 |
| 上线是里程碑 | AI 产品上线后会退化（幻觉、漂移、对抗输入） |

**这套方法论从底层就是 AI Native 的**：先设计边界再设计能力，用确定性而非信心度做验证，按风险降低而非功能数量定价。每个阶段都预设 AI 在环中——并设计好 AI 出错时怎么办。

---

## 30 秒看懂它能做什么

<p align="center">
  <img src="assets/pipeline-flow.png" alt="P0→P14 产品阶段流转" width="100%">
</p>

**核心能力**：**80 个可执行 Skill** + 阶段自动路由 + 冲突检测 + 证据链追踪

---

## 一个具体例子

**场景**：你想做"AI 合同审查助手"

### 需求发现阶段（P0）
Agent 先用工具卡验证需求：
- **微需求五问**：律师每天都要复查合同条款，这个痛点小但每天都发生
- **真需求判断**：长期存在 + 有补偿行为（手动标注）+ 背后有结构（责任风险）
- **需求四层拆解**：表达层"想自动审查" → 处境层"律师在为责任风险党底" → 代价层"每小时审查成本 $200"
- **Agent 边界清单**：AI 可以标注风险条款，但不能判断合同是否有效

**输出**：需求验证通过 + Agent 边界设计

### 方向定界阶段（P1）
Agent 会问你：
- 合同数据从哪来？（可得性）
- 是否涉及客户机密？（脱敏）
- 审查结果谁负责？（授权）
- 输出格式是否统一？（结构化）
- 新法规出来怎么办？（持续供给）

**输出**：Direction Brief —— 明确这方向能不能做、什么条件下能做

### 商业模式阶段（P6）
Agent 用确定性溢价公式定价：
- **恐惧程度**：律师最怕漏掉风险条款 → 高
- **出错代价**：漏掉一个条款可能导致百万损失 → 极高
- **替代成本**：人工审查每小时 $200 → 中
- **推荐模式**：保险模式（按成功审查次数收费，漏检赔偿）

**输出**：定价策略 — 每次审查 $5，漏检条款赔偿审查费 10 倍

### 审计放行阶段（P9）
Agent 检查：
- 可靠性：识别准确率、幻觉率
- 安全：敏感信息处理
- 边界：哪些条款类型必须人工复核
- 成本：每次审查的 Token 成本 vs 收费

**输出**：放行边界文档 —— 自动执行区 / 人工接管区 / 禁用区

---

## 快速开始

### 方式一：一键安装（推荐）

```bash
# 安装全部 80 个 Skill + 编排器
curl -fsSL https://raw.githubusercontent.com/gmaxxxie/ai-native-product-agent-skills/main/install.sh | bash

# 开始一个产品项目
hermes run "我想做一个 AI 客服产品，帮我从方向定界开始"
```

### 方式二：从 GitHub URL 安装

按需安装单个 Skill：

```bash
# 编排器（入口）
hermes skills install \
  https://raw.githubusercontent.com/gmaxxxie/ai-native-product-agent-skills/main/orchestrator/SKILL.md \
  --name ai-native-pm-agent

# 任意单个 Skill
hermes skills install \
  https://raw.githubusercontent.com/gmaxxxie/ai-native-product-agent-skills/main/skills/p1-direction-framing/SKILL.md \
  --name p1-direction-framing
```

### 方式三：克隆 & 本地安装

```bash
git clone https://github.com/gmaxxxie/ai-native-product-agent-skills.git
cd ai-native-product-agent-skills
bash install.sh   # 复制所有 Skill 到 ~/.hermes/skills/ai-native-pm/
```

### 方式四：配合其他 AI Agent 使用

这些 Skill 本质上是结构化的方法论提示词——不绑定任何特定 Agent 框架。

**最简单的方式**：直接告诉你的 AI Agent 安装这个仓库。

| Agent | 安装命令 |
|-------|---------|
| **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** | `hermes skills install https://github.com/gmaxxxie/ai-native-product-agent-skills` |
| **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** | `claude "Install all skills from https://github.com/gmaxxxie/ai-native-product-agent-skills into this project"` |
| **[OpenAI Codex](https://github.com/openai/codex)** | `codex "Clone and set up https://github.com/gmaxxxie/ai-native-product-agent-skills — read all SKILL.md files and make them available as product methodology tools"` |
| **[OpenCode](https://github.com/nicepkg/opencdoe)** | `opencdoe run "Install AI Native PM Agent from https://github.com/gmaxxxie/ai-native-product-agent-skills"` |
| **任意 LLM** | 直接粘贴：*"Read the skills from https://github.com/gmaxxxie/ai-native-product-agent-skills and apply the methodology to my product idea"* |

> 💡 **提示**：Claude Code、Codex、OpenCode 都能直接 `git clone` 仓库并读取 SKILL.md 文件。只需要给它们仓库地址并说"安装"——它们会自己搞定。

### 按阶段使用

每个阶段都是独立的 Skill，可以单独调用：

| 阶段 | 触发语 | 输出 |
|------|--------|------|
| **P0** 需求发现 | "我有一个痛点…" | 需求验证报告 |
| **P0a** 微需求检测 | "这个问题太小不值得做？" | 微需求清单 |
| **P0b** 真需求验证 | "这个需求是真的吗？" | 真/伪判定 |
| **P0c** 需求拆解 | "帮我拆解这个需求" | 四层拆解 |
| **P0d** 需求考古 | "深层需求是什么？" | 深层需求报告 |
| **P1** 方向定界 | "我有一个想法…" | Direction Brief |
| **P2** 实验展开 | "帮我设计实验验证…" | 实验方案 + Rubric |
| **P3** 系统构建 | "从实验到产品怎么转化…" | 系统架构方案 |
| **P5** 商业模式 | "怎么收费…" | 定价策略 |
| **P6** 增长策略 | "怎么冷启动…" | 增长方案 |
| **P8** UX 设计 | "AI 产品体验应该怎么设计？" | UX 设计方案 + 信任分级 |
| **P9** 审计放行 | "准备上线了，检查一遍…" | 放行边界文档 |
| **P10** 生产运营 | "已经上线了，怎么保持健康？" | 监控方案 + 反馈循环 |
| **P11** 产品团队 | "人和 AI 怎么分工？" | 团队结构 + 角色定义 |
| **P12** 观照 | "我是不是问错了问题？" | 看法修正 + 前提检查 |
| **P13** 判断力与直觉 | "怎么做出更好的决策？" | 九步决策框架 |
| **P14** 美学权威 | "怎样才能让产品有高级感？" | 美学体系 + 选择标准 |

### 跨阶段组合（一站式）

| 组合 | 触发语 | 输出 |
|------|--------|------|
| 需求→方向 | "帮我从痛点直接走到方向定界" | Direction Brief |
| 商业→增长 | "定价和增长怎么联动？" | 定价-增长联动策略 |
| UX→审计 | "UX 设计能不能安全放行？" | UX 审计报告 + 放行建议 |

---

## 完整 Skill 列表（80 个）

### P0 — 需求发现层（17 个 Skill）

| ID | 名称 | 功能 |
|----|------|------|
| p0-needs-orchestrator | 需求发现编排器 | 协调六个工具卡完成系统性需求发现 |
| p0-product-needs | AI Native 产品需求 | 统一需求发现 + 伪需求检测 |
| p0a-micro-needs-detector | 微需求五问检测器 | 发现被忽视的微需求 |
| p0b-real-needs-validator | 真需求判断五问 | 区分真需求与伪需求 |
| p0c-needs-decomposer | 需求四层拆解卡 | 表达层/场景层/处境层/代价层 |
| p0d-needs-archaeologist | 需求考古五步法 | 挖掘深层需求与历史约束 |
| p0e-good-question-generator | 好问题六维观察表 | 从六个维度发现好问题 |
| p0f-agent-boundary-designer | Agent 边界清单 | 定义 AI 应做/不做/停下来等人的边界 |
| p0g-diverse-recommendation-rewriter | 多元推荐改写器 | 从"猜你喜欢"到"帮你发现" |
| p0g-diversity-rewrite-checklist | 多元推荐检查清单 | 验证多元推荐改写质量 |
| p0h-ai-product-triple-balance | AI产品三重平衡卡 | 平衡功能性/体验性/商业性 |
| p0h-triple-balance-assessor | 三重平衡评估器 | 评估产品三重平衡状态 |

### P1–P2 — 方向定界与实验层（8 个 Skill）

| ID | 名称 | 功能 |
|----|------|------|
| p1-direction-framing | 方向定界 | 五维判断、Direction Brief |
| p2-experiment-engine | 实验展开（总览） | 能力/产品/商业三层实验 |
| p2a-experiment-overview | 实验概述 | 资料准备评估、三层实验体系设计、Rubric 建立 |
| p2b-product-form-exploration | 产品形态探索 | 能力边界分析、交互原型设计、产品形态判断 |
| p2c-process-redesign | 流程重构 | 任务拆解、人机协作模式选择、工作流节点标注 |
| p2d-convergence-decision | 目标收敛决策 | 实验记录整理、收敛信号识别、继续/延后/停止决策 |
| p2e-shadow-validation | 影子验证 | 影子系统设计、并行运行、人工对比、审计放行证据 |

### P3–P4 — 系统构建层（5 个 Skill）

| ID | 名称 | 功能 |
|----|------|------|
| p3-system-building | 系统构建 | 从实验到产品转化 |
| p4-agent-skill-design | 智能体与技能单元设计 | Agent/Skill 单元设计 |
| p5-memory-system | 记忆系统设计 | AI 产品记忆架构 |
| p6-context-engineering | 上下文工程设计 | 上下文管理系统 |
| p7-knowledge-rag | RAG 与知识系统设计 | 知识管理 + RAG 设计 |

### P5–P6 — 商业模式层（5 个 Skill）

| ID | 名称 | 功能 |
|----|------|------|
| p6-business-model | AI Native 商业模式（总览） | 确定性溢价商业模式设计 |
| p6a-certainty-premium-calculator | 确定性溢价计算器 | 计算 AI 产品的确定性溢价空间 |
| p6b-arbiter-mode-designer | 仲裁者模式设计器 | 设计 AI 作为决策仲裁者的商业模式 |
| p6c-insurance-mode-designer | 保险模式设计器 | 设计结果保障型商业模式 |
| p6d-prediction-arbitrage-designer | 预测套利设计器 | 设计信息差套利型商业模式 |

### P7 — 增长策略层（6 个 Skill）

| ID | 名称 | 功能 |
|----|------|------|
| p7-marketing-growth | AI Native 增长策略（总览） | 增长飞轮与营销策略 |
| p7a-data-flywheel-builder | 数据飞轮构建器 | 评估和构建自增强数据飞轮 |
| p7b-intent-prediction-designer | 意图预测营销设计器 | 从人群定向到个体预见 |
| p7c-predictive-retention-designer | 预测性留存设计器 | 从流失后挽回到流失前阻止 |
| p7d-marketing-productizer | 营销产品化设计器 | 把营销活动变成产品功能 |
| p7e-customer-loop | 客户循环 | 早期客户筛选、共创边界、反馈回流与扩张策略 |

### P8 — 用户体验层（4 个 Skill）

| ID | 名称 | 功能 |
|----|------|------|
| p8-ux-design | AI Native UX 设计（总览） | UX 设计方法论 |
| p8a-rax-risk-assessor | RAX 风险评估器 | 评估 AI Agent 代理行动的风险等级 |
| p8b-trust-tier-designer | 信任分级设计器 | 设计 AI Agent 的信任梯度 |
| p8c-progressive-disclosure | 渐进式披露设计器 | 设计信息展示的渐进节奏 |

### P9–P11 — 审计、运营与团队层（9 个 Skill）

| ID | 名称 | 功能 |
|----|------|------|
| p9-audit-release | 审计放行 | go/no-go 决策 |
| p10-production-ops | 生产运行与循环回灌 | 监控与反馈循环 |
| p10a-value-discovery-loop | 价值发现循环 | 从价值信号识别到方向修正的完整闭环 |
| p10b-aiops-case | AIOps 行业案例模板 | 高风险、强约束、重责任场景的完整方法论路径 |
| p10c-customer-service-case | AI 客服行业案例模板 | 服务协同、Copilot、经验复利的完整方法论路径 |
| p10d-saas-case | AI Native SaaS 行业案例模板 | 语义层、能力护城河、数据飞轮的完整方法论路径 |
| p11-product-team | AI Native 产品团队设计 | 人机分工、能力缺口、团队协作流程、角色重新定义 |

### P12 — 观照层（10 个 Skill）

来源：《观照：AI时代的产品观、用户观与决策观》

| ID | 名称 | 功能 |
|----|------|------|
| p12-contemplation-orchestrator | 观照编排器 | 根据问题类型路由到对应章节 Skill，串联全链路决策修正流程 |
| p12a-contemplation-right-view | 正见 | 三层看问题法（现象层/情境层/关系层） |
| p12a-contemplation-view-correction | 看法修正 | 默认检查、证据校验、后果追问、八种修正视角 |
| p12a-contemplation-prerequisite-check | 前提检查 | 识别情境变化、验证假设前提、重配适用方法 |
| p12a-contemplation-right-thinking | 正思维 | 拆解判断链，区分前提/证据/推理/情绪 |
| p12a-contemplation-right-speech | 正语 | 语言清洗、纪要体检、诚实表达练习 |
| p12a-contemplation-right-action | 正业 | 先看机制是否有害，再看结果是否有效 |
| p12a-contemplation-right-livelihood | 正命 | 收入来源审视与激励偏差检查 |
| p12a-contemplation-right-effort | 正精进 | 归零分析、暂停策略、止损决策 |
| p12a-contemplation-right-mindfulness | 正念 | 建立个人与团队的决策觉察力 |

### P13 — 判断力与直觉力层（12 个 Skill）

来源：《判断力与直觉力》

| ID | 名称 | 功能 |
|----|------|------|
| p13-intuition-orchestrator | 判断力编排器 | 九步闭环决策路线图的路由器与聚合器 |
| p13a-judgment-metacognition | 判断力元认知 | 理解什么是判断、识别判断的场景与类型 |
| p13b-systemic-thinker | 系统性思维 | 结构化分析、关系映射、反馈回路识别 |
| p13c-product-psychology | 产品心理学 | 用户心理模型、行为设计、动机分析 |
| p13d-intuition-training | 直觉训练 | 将直觉转化为可压缩的认知模型与模式识别 |
| p13e-nine-step-framework | 九步闭环总论 | 覆盖做什么到反馈回路的完整框架 |
| p13f-first-half-judgment | 九步前半段 | 做什么、值不值得、用不用 AI 的判断框架 |
| p13g-mid-judgment | 九步中段 | 做成什么形态、用户托付度、怎么做的决策框架 |
| p13h-validation-market | 九步后段 | 怎么验证、怎么进入市场、反馈回路的决策框架 |
| p13i-judgment-traps | 判断陷阱与认知偏误 | 识别常见判断错误模式及其防范策略 |
| p13j-organizational-judgment | 组织判断力 | 将个人判断转化为团队判断能力的系统方法 |
| p13k-intuition-evolution | 直觉进化 | 持续训练判断力、建立标准提升机制 |

### P14 — 美学权威层（9 个 Skill）

来源：《AI Beaty：美学权威与 AI 时代的选择力》

| ID | 名称 | 功能 |
|----|------|------|
| p14-beauty-orchestrator | 美学权威编排器 | 审美主导权与美感体系化训练的路由器 |
| p14a-beauty-redefinition | 美感的重新定义 | 生成焦虑、美感六维度、美感双轴模型 |
| p14b-beauty-ai-roles | AI 在审美中的角色定位 | 放大器/陪练器/协作者，而非审美本身 |
| p14c-beauty-selection | 从生产美感到选择美感 | 选择力是新核心技能，Context 决定输出上限 |
| p14d-beauty-narrative | 故事力即美感 | 叙事结构、情感节奏、信息架构的审美维度 |
| p14e-beauty-human-edge | 人的不可替代性 | 美感作为护城河、标准进化、人的核心优势 |
| p14f-beauty-commercial | 美感的商业价值 | 市场接受度、美感溢价、体验美感、物理世界平衡 |
| p14g-beauty-system | 审美训练体系 | 系统化积累与校准审美标准、人机协作流程、标准进化 |
| p14h-beauty-preface | 前言与核心命题 | 当一切都能生成之后，审美主导权成为核心竞争力 |

### 跨书组合 Skill（3 个）

| ID | 名称 | 功能 |
|----|------|------|
| combo-needs-to-direction | 需求→方向 | 痛点线索直接输出 Direction Brief |
| combo-business-to-growth | 商业→增长 | 定价与飞轮的联动设计 |
| combo-ux-to-audit | UX→审计 | RAX 评估 + 信任分级 + 放行建议 |

---

## 项目结构

```
ai-native-pm-agent-skills/
├── README.md / README_CN.md         # 本文档（英文 / 中文）
├── ARCHITECTURE.md                  # 系统架构设计
├── skill-registry.yaml              # Skill 注册表（80 个已注册）
├── orchestrator/SKILL.md           # 主编排器：阶段路由 + 冲突检测
├── install.sh                       # 一键安装脚本
├── assets/                          # 封面图、流程图、行业矩阵、方法论书籍
├── skills/
│   ├── p0-needs-orchestrator/        # P0 需求发现编排器
│   ├── p0-product-needs/             # P0 统一需求发现
│   ├── p0a-micro-needs-detector/     # P0a 微需求检测
│   ├── p0b-real-needs-validator/     # P0b 真/伪需求判断
│   ├── p0c-needs-decomposer/        # P0c 四层需求拆解
│   ├── p0d-needs-archaeologist/      # P0d 深层需求考古
│   ├── p0e-good-question-generator/  # P0e 好问题六维度
│   ├── p0f-agent-boundary-designer/  # P0f AI 边界设计
│   ├── p0g-diverse-recommendation-rewriter/    # P0g 多元推荐改写
│   ├── p0g-diversity-rewrite-checklist/        # P0g 多元推荐检查清单
│   ├── p0h-ai-product-triple-balance/          # P0h 三重平衡
│   ├── p0h-triple-balance-assessor/            # P0h 三重平衡评估
│   ├── p1-direction-framing/         # P1 方向定界
│   ├── p2-experiment-engine/         # P2 实验总览
│   ├── p2a-experiment-overview/      # P2a 实验概述
│   ├── p2b-product-form-exploration/ # P2b 产品形态探索
│   ├── p2c-process-redesign/         # P2c 流程重构
│   ├── p2d-convergence-decision/      # P2d 目标收敛
│   ├── p2e-shadow-validation/        # P2e 影子验证
│   ├── p3-system-building/           # P3 系统构建
│   ├── p4-agent-skill-design/        # P4 智能体与技能设计
│   ├── p5-memory-system/             # P5 记忆系统
│   ├── p6-context-engineering/       # P6 上下文工程
│   ├── p7-knowledge-rag/              # P7 RAG 与知识系统
│   ├── p6-business-model/             # P6 商业模式总览
│   ├── p6a-certainty-premium-calculator/    # P6a 确定性溢价
│   ├── p6b-arbiter-mode-designer/    # P6b 仲裁者模式
│   ├── p6c-insurance-mode-designer/  # P6c 保险模式
│   ├── p6d-prediction-arbitrage-designer/   # P6d 预测套利
│   ├── p7-marketing-growth/           # P7 增长总览
│   ├── p7a-data-flywheel-builder/    # P7a 数据飞轮
│   ├── p7b-intent-prediction-designer/      # P7b 意图预测
│   ├── p7c-predictive-retention-designer/  # P7c 预测性留存
│   ├── p7d-marketing-productizer/    # P7d 营销产品化
│   ├── p7e-customer-loop/            # P7e 客户循环
│   ├── p8-ux-design/                 # P8 UX 设计总览
│   ├── p8a-rax-risk-assessor/        # P8a RAX 风险评估
│   ├── p8b-trust-tier-designer/      # P8b 信任分级
│   ├── p8c-progressive-disclosure/   # P8c 渐进式披露
│   ├── p9-audit-release/             # P9 审计放行
│   ├── p10-production-ops/           # P10 生产运营
│   ├── p10a-value-discovery-loop/    # P10a 价值发现循环
│   ├── p10b-aiops-case/             # P10b AIOps 案例
│   ├── p10c-customer-service-case/   # P10c AI 客服案例
│   ├── p10d-saas-case/              # P10d SaaS 案例
│   ├── p11-product-team/            # P11 产品团队
│   ├── p12-contemplation-orchestrator/    # P12 观照编排器
│   ├── p12a-contemplation-right-view/     # P12 正见
│   ├── p12a-contemplation-view-correction/ # P12 看法修正
│   ├── p12a-contemplation-prerequisite-check/  # P12 前提检查
│   ├── p12a-contemplation-right-thinking/  # P12 正思维
│   ├── p12a-contemplation-right-speech/    # P12 正语
│   ├── p12a-contemplation-right-action/    # P12 正业
│   ├── p12a-contemplation-right-livelihood/ # P12 正命
│   ├── p12a-contemplation-right-effort/    # P12 正精进
│   ├── p12a-contemplation-right-mindfulness/ # P12 正念
│   ├── p13-intuition-orchestrator/         # P13 判断力编排器
│   ├── p13a-judgment-metacognition/        # P13a 判断力元认知
│   ├── p13b-systemic-thinker/              # P13b 系统性思维
│   ├── p13c-product-psychology/             # P13c 产品心理学
│   ├── p13d-intuition-training/            # P13d 直觉训练
│   ├── p13e-nine-step-framework/            # P13e 九步框架总览
│   ├── p13f-first-half-judgment/            # P13f 九步前半段
│   ├── p13g-mid-judgment/                   # P13g 九步中段
│   ├── p13h-validation-market/              # P13h 九步后半段
│   ├── p13i-judgment-traps/                 # P13i 判断陷阱
│   ├── p13j-organizational-judgment/        # P13j 组织判断力
│   ├── p13k-intuition-evolution/             # P13k 直觉进化
│   ├── p14-beauty-orchestrator/              # P14 美学编排器
│   ├── p14a-beauty-redefinition/           # P14a 美感重新定义
│   ├── p14b-beauty-ai-roles/               # P14b AI 审美角色
│   ├── p14c-beauty-selection/               # P14c 选择美感到生产美感
│   ├── p14d-beauty-narrative/               # P14d 叙事即美感
│   ├── p14e-beauty-human-edge/              # P14e 人的不可替代
│   ├── p14f-beauty-commercial/               # P14f 美感商业价值
│   ├── p14g-beauty-system/                  # P14g 审美训练体系
│   ├── p14h-beauty-preface/                 # P14h 核心命题
│   ├── combo-needs-to-direction/     # 组合：痛点→方向
│   ├── combo-business-to-growth/      # 组合：商业→增长
│   └── combo-ux-to-audit/            # 组合：UX→审计
└── scripts/
    ├── init_product_context.py        # 产品上下文初始化
    ├── test_orchestrator.py           # 编排器测试
    └── final_validation.py            # 最终验证
```

---

## 八本书的方法论体系

<p align="center">
  <img src="assets/methodology-books.png" alt="八本书方法论合成" width="100%">
</p>

80 个 Skill 全部来自八本方法论著作。每本书的工具卡和概念卡都已转化为可执行的 Skill：

| # | 书籍 | 状态 | 覆盖阶段 | Skill 数 |
|---|------|------|---------|---------|
| 1 | [AI rebuild product needs](https://www.amazon.com/dp/B0GT48SZ5R) | ✅ 已出版 | P0 需求发现 | 12 |
| 2 | [AI Native 产品方法论](https://www.amazon.com/dp/B0GSMXD24H) | ✅ 已出版 | P1–P2 方向定界与实验 | 7 |
| 3 | [AI Native 用户体验](https://www.amazon.com/dp/B0GX2H4D33) | 📖 即将出版 | P8 UX 设计 | 4 |
| 4 | [AI 确定性商业模式](https://www.amazon.com/dp/B0GRQVR2J4) | ✅ 已出版 | P5–P6 商业模式 | 5 |
| 5 | [AI Native 营销与增长](https://www.amazon.com/dp/B0GCHHZBV3) | 📖 即将出版 | P7 增长策略 | 6 |
| 6 | [观照：AI时代的产品观、用户观与决策观](https://www.amazon.com/dp/B0GX2H4D33) | ✅ 已出版 | P12 观照与决策修正 | 10 |
| 7 | [判断力与直觉力](https://www.amazon.com/dp/B0GCHHZBV3) | 📖 即将出版 | P13 判断力与直觉 | 12 |
| 8 | [AI Beaty：美学权威与选择力](https://www.amazon.com/dp/B0GCHHZBV3) | ✅ 已出版 | P14 美学权威 | 9 |

📖 **Amazon 已出版**（5本）：
- **[AI rebuild product needs](https://www.amazon.com/dp/B0GT48SZ5R)** — 需求发现、微需求检测、真需求验证、需求拆解、Agent 边界设计
- **[AI Native 产品方法论](https://www.amazon.com/dp/B0GSMXD24H)** — 方向定界、实验展开、系统构建、审计放行、生产运营
- **[AI 确定性商业模式](https://www.amazon.com/dp/B0GRQVR2J4)** — 确定性溢价、商业模式设计、定价策略
- **[观照：AI时代的产品观、用户观与决策观](https://www.amazon.com/dp/B0GX2H4D33)** — 正见、前提检查、判断修正、决策觉察
- **[AI Beaty：美学权威与选择力](https://www.amazon.com/dp/B0GCHHZBV3)** — 数据飞轮、意图预测、预测性留存、营销产品化

📖 **即将出版**（3本）：
- **AI Native 用户体验** — RAX 风险评估、信任分级、渐进式披露
- **AI Native 营销与增长** — 数据飞轮、意图预测、预测性留存、营销产品化
- **判断力与直觉力** — 九步决策框架、判断陷阱、组织判断力

---

## 行业场景

<p align="center">
  <img src="assets/industry-matrix.png" alt="AI 各行业应用" width="100%">
</p>

| 行业 | 典型场景 | 关键边界设计 |
|------|---------|-----------|
| 法律 | 合同审查助手 | 仅 Copilot 模式——不替代律师决策 |
| 医疗 | 诊断支持系统 | 仅"第二意见"模式 |
| 金融 | 反欺诈评分 | 高风险场景 100% 人工复核 |
| 电商 | AI 客服 | 退款承诺需人工确认 |
| DevOps | AIOps 故障分诊 | 仅建议模式——不自动修复 |
| HR | 简历筛选 | 偏见检测 + 盲筛模式 |
| 教育 | 个性化学习 | 仅提示模式——不直接给答案 |
| 内容 | 营销文案 | 人工审核 + 合规检查 |

---

## 设计原则（为什么这样设计）

1. **问题先于方案** — 在构建功能前先验证问题是否真实存在
2. **边界先于能力** — 先定义 AI 不应该做什么，再设计它能做什么
3. **证据先于决策** — 用影子验证替代"我觉得能跑"
4. **编排先于自动化** — 在关键决策点保留人工确认环节
5. **迭代先于完美** — 通过失败分析优化，而非追求一次做对
6. **看法修正先于行动** — 在行动前先检查是否问对了问题
7. **判断先于直觉** — 在信任直觉前先让推理过程显性化
8. **美学权威优先于功能完整性** — 你选择不做什么定义了产品

---

## 贡献

欢迎提交 Issue 和 PR！优先领域：
- **新行业场景**：添加带完整输入输出示例的行业案例
- **边界设计**：高风险场景下如何划定 AI 边界
- **失败案例分析**：失败实验的分析比成功经验更有价值
- **新工具卡**：将书的概念卡转化为可执行的 Skill

---

## 开源协议

MIT License

---

> "问题先于方案。边界先于能力。证据先于决策。编排先于自动化。"
