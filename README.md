<p align="center">
  <img src="assets/hero-banner.png" alt="AI Native PM Agent — From Idea to Production" width="100%">
</p>

# AI Native PM Agent

> An AI product coach that asks "Is this direction really worth pursuing?" — with structured methodology backing every decision, from spark of inspiration to production deployment.

[📖 中文版 README](./README_CN.md)

---

## Why Do You Need This?

90% of AI product teams die in the same traps:

- **Direction Trap**: Spend 3 months building an AI feature, only to find users won't pay for it
- **Needs Trap**: Fake needs look too much like real ones — AI makes prototyping near-free, but also lets you build the wrong thing faster
- **Boundary Trap**: AI crosses the line and does things it shouldn't, triggering compliance risks
- **Hallucination Trap**: Pre-launch accuracy looks like 95%, post-launch reality says otherwise
- **Cost Trap**: Token bills explode, business model falls apart

This Agent doesn't write code for you — it **makes you pause at every critical decision point and verify with structured methods**.

### Why Not Just Use Traditional Product Methodology?

Traditional product frameworks (Lean Startup, Jobs-to-be-Done, Design Thinking) were built for a world where **prototyping was expensive and AI didn't exist**. They break down in the AI era because:

| Traditional Assumption | AI Era Reality |
|----------------------|----------------|
| Build-Measure-Learn takes weeks | AI prototypes are near-free — you can build the wrong thing *faster* |
| User needs are relatively stable | AI creates new needs and makes old ones obsolete overnight |
| Product boundaries are clear | AI crosses lines you didn't draw — compliance, ethics, autonomy |
| Cost scales with features | Token costs scale with usage — business model can invert |
| Launch is a milestone | AI products degrade post-launch (hallucinations, drift, adversarial inputs) |

**This methodology is AI Native from the ground up**: it starts with boundary design before capability design, validates with certainty rather than confidence, and prices on risk reduction rather than feature count. Every stage assumes AI is in the loop — and designs for what happens when it goes wrong.

---

## See What It Does in 30 Seconds

<p align="center">
  <img src="assets/pipeline-flow.png" alt="P0→P14 Pipeline Flow" width="100%">
</p>

**Core Capabilities**: **80 executable Skills** across 8 stages + Stage auto-routing + Conflict detection + Evidence chain tracking

---

## A Concrete Example

**Scenario**: You want to build an "AI Contract Review Assistant"

### Needs Discovery (P0)
The Agent validates the need with tool cards:
- **Micro-Needs Five Questions**: Lawyers review contract clauses daily — the pain is small but constant
- **Real-Needs Validation**: Long-standing problem + compensation behaviors (manual annotation) + structural root cause (liability risk)
- **Four-Layer Decomposition**: Surface: "automate review" → Situation: "lawyers bear liability risk" → Cost: "$200/hour per review"
- **Agent Boundary Checklist**: AI can flag risky clauses, but cannot determine contract validity

**Output**: Needs validated + Agent boundary design

### Direction Framing (P1)
The Agent asks you:
- Where does contract data come from? (Availability)
- Does it involve client confidentiality? (Desensitization)
- Who is responsible for review results? (Authorization)
- Is the output format standardized? (Structured)
- What happens when new regulations emerge? (Sustained supply)

**Output**: Direction Brief — clear go/no-go with conditions

### Business Model (P6)
The Agent prices using the Certainty Premium formula:
- **Fear Level**: Lawyers' biggest fear is missing a risky clause → High
- **Error Cost**: Missing one clause could mean millions in liability → Extremely high
- **Substitution Cost**: Manual review at $200/hour → Medium
- **Recommended Model**: Insurance Mode (charge per successful review, compensate for misses)

**Output**: Pricing strategy — $5/review, 10x compensation for missed clauses

### Audit & Release (P9)
The Agent checks:
- Reliability: Identification accuracy, hallucination rate
- Safety: Sensitive information handling
- Boundaries: Which clause types require human review
- Cost: Token cost per review vs. pricing

**Output**: Release boundary document — Auto-execute zone / Human handoff zone / Disabled zone

---

## Quick Start

### Option 1: One-Click Install (Recommended)

```bash
# Install all 80 skills + orchestrator
curl -fsSL https://raw.githubusercontent.com/gmaxxxie/ai-native-product-agent-skills/main/install.sh | bash

# Start a product project
hermes run "I want to build an AI customer service product, help me start from direction framing"
```

### Option 2: Install from GitHub URL

Install individual skills on demand:

```bash
# Orchestrator (entry point)
hermes skills install \
  https://raw.githubusercontent.com/gmaxxxie/ai-native-product-agent-skills/main/orchestrator/SKILL.md \
  --name ai-native-pm-agent

# Any individual skill
hermes skills install \
  https://raw.githubusercontent.com/gmaxxxie/ai-native-product-agent-skills/main/skills/p1-direction-framing/SKILL.md \
  --name p1-direction-framing
```

### Option 3: Clone & Local Install

```bash
git clone https://github.com/gmaxxxie/ai-native-product-agent-skills.git
cd ai-native-product-agent-skills
bash install.sh   # copies all skills to ~/.hermes/skills/ai-native-pm/
```

### Option 4: Use with Other AI Agents

These skills work as structured prompts — they're not tied to any specific agent framework.

**The simplest way**: just tell your AI agent to install from this repo.

| Agent | Install Command |
|-------|----------------|
| **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** | `hermes skills install https://github.com/gmaxxxie/ai-native-product-agent-skills` |
| **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** | `claude "Install all skills from https://github.com/gmaxxxie/ai-native-product-agent-skills into this project"` |
| **[OpenAI Codex](https://github.com/openai/codex)** | `codex "Clone and set up https://github.com/gmaxxxie/ai-native-product-agent-skills — read all SKILL.md files and make them available as product methodology tools"` |
| **[OpenCode](https://github.com/nicepkg/opencdoe)** | `opencdoe run "Install AI Native PM Agent from https://github.com/gmaxxxie/ai-native-product-agent-skills"` |
| **Any LLM** | Just paste: *"Read the skills from https://github.com/gmaxxxie/ai-native-product-agent-skills and apply the methodology to my product idea"* |

> 💡 **Tip**: Claude Code, Codex, and OpenCode can all `git clone` the repo and read SKILL.md files directly. Just give them the repo URL and tell them to install — they'll figure out the rest.

### Per-Stage Usage

Each stage is an independent Skill you can call individually:

| Stage | Trigger Phrase | Output |
|-------|---------------|--------|
| **P0** Needs Discovery | "I have a pain point…" | Needs validation report |
| **P0a** Micro-Needs | "Is this problem too small to matter?" | Micro-needs list |
| **P0b** Real Needs | "Is this need real or fake?" | Real/fake verdict |
| **P0c** Decomposition | "Help me decompose this need" | Four-layer breakdown |
| **P0d** Archaeology | "What's the deep need?" | Deep needs report |
| **P1** Direction Framing | "I have an idea…" | Direction Brief |
| **P2** Experiment Engine | "Help me design experiments…" | Experiment plan + Rubric |
| **P3** System Building | "How to go from experiment to product…" | System architecture |
| **P5** Business Model | "How to price this…" | Pricing strategy |
| **P6** Growth Strategy | "How to get cold start…" | Growth plan |
| **P8** UX Design | "How should this AI feel to use?" | UX design + trust tiers |
| **P9** Audit & Release | "Ready to launch, check it…" | Release boundary document |
| **P10** Production Ops | "It's live, how do I keep it healthy?" | Monitoring + feedback loops |
| **P11** Product Team | "How should humans and AI collaborate?" | Team structure + roles |
| **P12** Contemplation | "Am I even asking the right question?" | View correction + prerequisite check |
| **P13** Judgment & Intuition | "How do I make better decisions?" | Nine-step decision framework |
| **P14** Aesthetic Authority | "What makes this feel premium?" | Aesthetic system + selection criteria |

### Cross-Stage Combos (One-Stop)

| Combo | Trigger Phrase | Output |
|-------|---------------|--------|
| Needs → Direction | "Take me from pain point to direction framing" | Direction Brief |
| Business → Growth | "How should pricing and growth align?" | Pricing-growth alignment |
| UX → Audit | "Is this UX design safe to release?" | UX audit report + release recommendation |

---

## Complete Skill List (80 Skills)

### P0 — Needs Discovery Layer (17 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| p0-needs-orchestrator | Needs Discovery Orchestrator | Coordinates six tool cards for systematic needs discovery |
| p0-product-needs | AI Native Product Needs | Unified needs discovery + fake needs detection |
| p0a-micro-needs-detector | Micro-Needs Five Questions | Detects overlooked micro-needs |
| p0b-real-needs-validator | Real-Needs Five Questions | Distinguishes real needs from fake ones |
| p0c-needs-decomposer | Needs Four-Layer Decomposition | Expression / Scenario / Situation / Cost layers |
| p0d-needs-archaeologist | Needs Archaeology Five Steps | Uncovers deep needs and historical constraints |
| p0e-good-question-generator | Good Questions Six Dimensions | Discovers good questions from six perspectives |
| p0f-agent-boundary-designer | Agent Boundary Checklist | Defines AI permission boundaries |
| p0g-diverse-recommendation-rewriter | Diverse Recommendation Rewrite | From "guess what you like" to "help you discover" |
| p0g-diversity-rewrite-checklist | Diversity Rewrite Checklist | Validates diversity rewrite quality |
| p0h-ai-product-triple-balance | AI Product Triple Balance | Business / Humanity / Technology balance |
| p0h-triple-balance-assessor | Triple Balance Assessor | Evaluates product triple balance state |

### P1–P2 — Direction & Experiment Layer (8 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| p1-direction-framing | Direction Framing | Five-dimension judgment, Direction Brief |
| p2-experiment-engine | Experiment Engine (Overview) | Capability / Product / Business three-layer experiments |
| p2a-experiment-overview | Experiment Overview | Materials prep, three-layer design, evaluation Rubric |
| p2b-product-form-exploration | Product Form Exploration | Capability boundary, interaction prototype, form judgment |
| p2c-process-redesign | Process Redesign | Task decomposition, human-AI collaboration mode |
| p2d-convergence-decision | Convergence Decision | Experiment records, convergence signals, continue/pause/stop |
| p2e-shadow-validation | Shadow Validation | Shadow system, parallel run, human comparison, audit evidence |

### P3–P4 — System Building Layer (5 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| p3-system-building | System Building | From experiments to product |
| p4-agent-skill-design | Agent & Skill Unit Design | Agent/Skill unit design |
| p5-memory-system | Memory System Design | AI product memory architecture |
| p6-context-engineering | Context Engineering | Context management system |
| p7-knowledge-rag | RAG & Knowledge System | Knowledge management + RAG design |

### P5–P6 — Business Model Layer (5 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| p6-business-model | AI Native Business Model (Overview) | Certainty Premium business model design |
| p6a-certainty-premium-calculator | Certainty Premium Calculator | Calculates certainty premium |
| p6b-arbiter-mode-designer | Arbiter Mode Designer | "Truth-as-a-Service" business model |
| p6c-insurance-mode-designer | Insurance Mode Designer | "Result Guarantee" business model |
| p6d-prediction-arbitrage-designer | Prediction Arbitrage Designer | "Time Arbitrage" business model |

### P7 — Growth Strategy Layer (6 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| p7-marketing-growth | AI Native Marketing & Growth (Overview) | Growth flywheel & marketing strategy |
| p7a-data-flywheel-builder | Data Flywheel Builder | Assesses and builds self-reinforcing data flywheels |
| p7b-intent-prediction-designer | Intent Prediction Designer | From audience targeting to individual foresight |
| p7c-predictive-retention-designer | Predictive Retention Designer | From post-churn recovery to pre-churn prevention |
| p7d-marketing-productizer | Marketing-as-Product Designer | Turns marketing activities into product features |
| p7e-customer-loop | Customer Loop | Early customer filtering, co-creation boundaries, feedback loops |

### P8 — User Experience Layer (4 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| p8-ux-design | AI Native UX Design (Overview) | UX design methodology |
| p8a-rax-risk-assessor | RAX Risk Assessor | Risk / Ambiguity / eXposure assessment |
| p8b-trust-tier-designer | Trust Tier Designer | Progressive trust system design |
| p8c-progressive-disclosure | Progressive Disclosure Checklist | Feature reveal pacing design |

### P9–P11 — Audit, Operations & Team Layer (9 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| p9-audit-release | Audit & Release | Go/no-go decision |
| p10-production-ops | Production Operations | Monitoring & feedback loops |
| p10a-value-discovery-loop | Value Discovery Loop | From value signal to direction correction闭环 |
| p10b-aiops-case | AIOps Case Template | Complete methodology path for high-risk scenarios |
| p10c-customer-service-case | AI Customer Service Case | Service collaboration, Copilot, experience leverage |
| p10d-saas-case | AI Native SaaS Case | Semantic layer, capability moats, data flywheels |
| p11-product-team | AI Native Product Team | Human-AI division, capability gaps, team roles |

### P12 — Contemplation Layer (10 Skills)

*From: Contemplation — Product Judgment, User Understanding, and Decision Correction in the AI Era*

| ID | Name | What It Does |
|----|------|-------------|
| p12-contemplation-orchestrator | Contemplation Orchestrator | Routes to correct chapter skill, chains full decision-correction flow |
| p12a-contemplation-right-view | Right View | Three-layer problem framing: phenomenon / situation / relationship |
| p12a-contemplation-view-correction | View Correction | Default checks, evidence validation, consequence inquiry, eight correction angles |
| p12a-contemplation-prerequisite-check | Prerequisite Check | Identifies situational changes, validates assumptions, reassigns methods |
| p12a-contemplation-right-thinking | Right Thinking | Dissect judgment chain, distinguish premise/evidence/reasoning/emotion |
| p12a-contemplation-right-speech | Right Speech | Language cleaning, meeting health check, honest expression practice |
| p12a-contemplation-right-action | Right Action | Value/cost/emotion/exit-right quadruple check before execution |
| p12a-contemplation-right-livelihood | Right Livelihood | Revenue source review and incentive bias check |
| p12a-contemplation-right-effort | Right Effort | Zero-based analysis, pause strategy, stop-loss decision |
| p12a-contemplation-right-mindfulness | Right Mindfulness | Establish personal and team decision awareness |

### P13 — Judgment & Intuition Layer (12 Skills)

*From: Intuition — Judgment and Intuition in the AI Era*

| ID | Name | What It Does |
|----|------|-------------|
| p13-intuition-orchestrator | Intuition Orchestrator | Nine-step closed-loop decision roadmap router |
| p13a-judgment-metacognition | Judgment Metacognition | Understanding judgment, identifying judgment scenarios |
| p13b-systemic-thinker | Systemic Thinking | Structural analysis, relationship mapping, feedback loop identification |
| p13c-product-psychology | Product Psychology | User mental models, behavior design, motivation analysis |
| p13d-intuition-training | Intuition Training | Compress intuition into cognitive models and pattern recognition |
| p13e-nine-step-framework | Nine-Step Framework Overview | Complete framework from "what to do" to feedback loop |
| p13f-first-half-judgment | First Half — What & Worth | "What to do, is it worth it, should we use AI" judgment |
| p13g-mid-judgment | Mid — Form & Trust | "What form, how much trust, how to do it" judgment |
| p13h-validation-market | Second Half — Validation | "How to validate, how to enter market, feedback loop" |
| p13i-judgment-traps | Judgment Traps | Common judgment errors and cognitive bias defenses |
| p13j-organizational-judgment | Organizational Judgment | Translating personal judgment into team judgment capability |
| p13k-intuition-evolution | Intuition Evolution | Continuous judgment training, standard improvement mechanism |

### P14 — Aesthetic Authority Layer (9 Skills)

*From: AI Beaty — Aesthetic Authority in the Age of AI*

| ID | Name | What It Does |
|----|------|-------------|
| p14-beauty-orchestrator | Beauty Orchestrator | Routes to aesthetic training and aesthetic authority system |
| p14a-beauty-redefinition | Aesthetic Redefinition | Generation anxiety, six aesthetic dimensions, dual-axis model |
| p14b-beauty-ai-roles | AI's Role in Aesthetics | Amplifier / sparring partner / collaborator, not aesthetic itself |
| p14c-beauty-selection | Selection Over Generation | Selection is the new core skill — Context determines output ceiling |
| p14d-beauty-narrative | Narrative as Aesthetic | Story structure, emotional rhythm, information architecture aesthetics |
| p14e-beauty-human-edge | Human Indispensability | Aesthetic as moat, standard evolution, human core advantage |
| p14f-beauty-commercial | Commercial Value of Aesthetics | Market acceptance, aesthetic premium, experiential aesthetics |
| p14g-beauty-system | Aesthetic Training System | Systematic aesthetic standard accumulation and calibration |
| p14h-beauty-preface | Preface & Core Proposition | Aesthetic authority as core competitive advantage when everything can be generated |

### Cross-Book Combo Skills (3 Skills)

| ID | Name | What It Does |
|----|------|-------------|
| combo-needs-to-direction | Needs → Direction | Pain point to Direction Brief in one pass |
| combo-business-to-growth | Business → Growth | Pricing-flywheel alignment design |
| combo-ux-to-audit | UX → Audit | RAX assessment + trust tiers + release recommendation |

---

## Project Structure

```
ai-native-pm-agent-skills/
├── README.md / README_CN.md         # This document (EN / 中文)
├── ARCHITECTURE.md                  # System architecture design
├── skill-registry.yaml              # Skill registry (80 skills registered)
├── orchestrator/SKILL.md            # Main orchestrator: stage routing + conflict detection
├── install.sh                       # One-click install script
├── assets/                          # Hero banner, pipeline flow, industry matrix, methodology books
├── skills/
│   ├── p0-needs-orchestrator/        # P0 Needs Discovery orchestrator
│   ├── p0-product-needs/             # P0 unified needs discovery
│   ├── p0a-micro-needs-detector/     # P0a micro-needs detection
│   ├── p0b-real-needs-validator/     # P0b real vs fake needs
│   ├── p0c-needs-decomposer/        # P0c four-layer decomposition
│   ├── p0d-needs-archaeologist/     # P0d deep needs archaeology
│   ├── p0e-good-question-generator/ # P0e good questions six dimensions
│   ├── p0f-agent-boundary-designer/ # P0f AI boundary design
│   ├── p0g-diverse-recommendation-rewriter/    # P0g diversity rewrite
│   ├── p0g-diversity-rewrite-checklist/       # P0g diversity checklist
│   ├── p0h-ai-product-triple-balance/         # P0h triple balance
│   ├── p0h-triple-balance-assessor/           # P0h balance assessor
│   ├── p1-direction-framing/        # P1 direction framing
│   ├── p2-experiment-engine/        # P2 experiment overview
│   ├── p2a-experiment-overview/     # P2a experiment setup
│   ├── p2b-product-form-exploration/ # P2b product form
│   ├── p2c-process-redesign/       # P2c process redesign
│   ├── p2d-convergence-decision/    # P2d convergence decision
│   ├── p2e-shadow-validation/       # P2e shadow validation
│   ├── p3-system-building/          # P3 system building
│   ├── p4-agent-skill-design/       # P4 agent & skill design
│   ├── p5-memory-system/           # P5 memory system
│   ├── p6-context-engineering/      # P6 context engineering
│   ├── p7-knowledge-rag/            # P7 RAG & knowledge
│   ├── p6-business-model/           # P6 business model overview
│   ├── p6a-certainty-premium-calculator/    # P6a certainty premium
│   ├── p6b-arbiter-mode-designer/  # P6b arbiter mode
│   ├── p6c-insurance-mode-designer/ # P6c insurance mode
│   ├── p6d-prediction-arbitrage-designer/   # P6d prediction arbitrage
│   ├── p7-marketing-growth/         # P7 marketing overview
│   ├── p7a-data-flywheel-builder/   # P7a data flywheel
│   ├── p7b-intent-prediction-designer/      # P7b intent prediction
│   ├── p7c-predictive-retention-designer/   # P7c predictive retention
│   ├── p7d-marketing-productizer/   # P7d marketing productizer
│   ├── p7e-customer-loop/           # P7e customer loop
│   ├── p8-ux-design/               # P8 UX design overview
│   ├── p8a-rax-risk-assessor/       # P8a RAX risk assessment
│   ├── p8b-trust-tier-designer/     # P8b trust tier design
│   ├── p8c-progressive-disclosure/  # P8c progressive disclosure
│   ├── p9-audit-release/           # P9 audit & release
│   ├── p10-production-ops/          # P10 production operations
│   ├── p10a-value-discovery-loop/  # P10a value discovery loop
│   ├── p10b-aiops-case/            # P10b AIOps case
│   ├── p10c-customer-service-case/  # P10c AI customer service case
│   ├── p10d-saas-case/              # P10d SaaS case
│   ├── p11-product-team/           # P11 product team design
│   ├── p12-contemplation-orchestrator/     # P12 Contemplation orchestrator
│   ├── p12a-contemplation-right-view/      # P12 right view
│   ├── p12a-contemplation-view-correction/ # P12 view correction
│   ├── p12a-contemplation-prerequisite-check/   # P12 prerequisite
│   ├── p12a-contemplation-right-thinking/    # P12 right thinking
│   ├── p12a-contemplation-right-speech/      # P12 right speech
│   ├── p12a-contemplation-right-action/      # P12 right action
│   ├── p12a-contemplation-right-livelihood/   # P12 right livelihood
│   ├── p12a-contemplation-right-effort/       # P12 right effort
│   ├── p12a-contemplation-right-mindfulness/  # P12 right mindfulness
│   ├── p13-intuition-orchestrator/    # P13 Intuition orchestrator
│   ├── p13a-judgment-metacognition/   # P13a judgment metacognition
│   ├── p13b-systemic-thinker/        # P13b systemic thinking
│   ├── p13c-product-psychology/       # P13c product psychology
│   ├── p13d-intuition-training/      # P13d intuition training
│   ├── p13e-nine-step-framework/     # P13e nine-step overview
│   ├── p13f-first-half-judgment/     # P13f first half
│   ├── p13g-mid-judgment/            # P13g mid judgment
│   ├── p13h-validation-market/       # P13h validation & market
│   ├── p13i-judgment-traps/          # P13i judgment traps
│   ├── p13j-organizational-judgment/  # P13j organizational judgment
│   ├── p13k-intuition-evolution/      # P13k intuition evolution
│   ├── p14-beauty-orchestrator/       # P14 Beauty orchestrator
│   ├── p14a-beauty-redefinition/     # P14a aesthetic redefinition
│   ├── p14b-beauty-ai-roles/         # P14b AI's role in aesthetics
│   ├── p14c-beauty-selection/         # P14c selection over generation
│   ├── p14d-beauty-narrative/        # P14d narrative aesthetics
│   ├── p14e-beauty-human-edge/        # P14e human edge
│   ├── p14f-beauty-commercial/        # P14f commercial value
│   ├── p14g-beauty-system/            # P14g training system
│   ├── p14h-beauty-preface/          # P14h core proposition
│   ├── combo-needs-to-direction/     # Combo: pain point → direction
│   ├── combo-business-to-growth/     # Combo: pricing → growth
│   └── combo-ux-to-audit/            # Combo: UX → audit
└── scripts/
    ├── init_product_context.py       # Product context initialization
    ├── test_orchestrator.py         # Orchestrator tests
    └── final_validation.py          # Final validation
```

---

## Eight Books Behind the Methodology

<p align="center">
  <img src="assets/methodology-books.png" alt="Eight Books Methodology Synthesis" width="100%">
</p>

All **80 Skills** are derived from eight methodology books. Each book's tool cards and concept cards have been converted into executable Skills:

| # | Book | Status | Stages Covered | Skills |
|---|------|--------|---------------|--------|
| 1 | [Micro-Needs for AI Products](https://www.amazon.com/dp/B0GT48SZ5R) | ✅ Published | P0 Needs Discovery | 12 |
| 2 | [AI Native Product Methodology](https://www.amazon.com/dp/B0GSMXD24H) | ✅ Published | P1–P2 Direction / Experiment | 7 |
| 3 | [AI Native UX Design](https://www.amazon.com/dp/B0GX2H4D33) | 📖 Coming Soon | P8 UX Design | 4 |
| 4 | [JUDGMENT: AI Native Business Model](https://www.amazon.com/dp/B0GRQVR2J4) | ✅ Published | P5–P6 Business Model | 5 |
| 5 | [AI Native Marketing & Growth](https://www.amazon.com/dp/B0GCHHZBV3) | 📖 Coming Soon | P7 Growth Strategy | 6 |
| 6 | [Contemplation](https://www.amazon.com/dp/B0GX2H4D33) | ✅ Published | P12 Contemplation & Decision Correction | 10 |
| 7 | [Intuition: Judgment & Decision](https://www.amazon.com/dp/B0GCHHZBV3) | 📖 Coming Soon | P13 Judgment & Intuition | 12 |
| 8 | [Aesthetic Authority](https://www.amazon.com/dp/B0GCHHZBV3) | ✅ Published | P14 Aesthetic Authority | 9 |

📖 **Available on Amazon** (5 published):
- **[Micro-Needs for AI Products](https://www.amazon.com/dp/B0GT48SZ5R)** — Needs discovery, micro-needs detection, real-needs validation, needs decomposition, agent boundary design
- **[AI Native Product Methodology](https://www.amazon.com/dp/B0GSMXD24H)** — Direction framing, experiment engine, system building, audit & release, production operations
- **[JUDGMENT: How to Make Better AI Product Decisions](https://www.amazon.com/dp/B0GRQVR2J4)** — Certainty Premium, business model design, pricing strategy
- **[Contemplation: Product Judgment, User Understanding, and Decision Correction in the AI Era](https://www.amazon.com/dp/B0GX2H4D33)** — Right view, prerequisite checks, judgment correction, decision mindfulness
- **[Aesthetic Authority: Why Human Judgment and Taste Matter in the Age of AI](https://www.amazon.com/dp/B0GCHHZBV3)** — Data flywheel, intent prediction, predictive retention, marketing-as-product

📖 **Coming Soon** (3 in progress):
- **AI Native UX Design** — RAX risk assessment, trust tier design, progressive disclosure
- **AI Native Marketing & Growth** — Data flywheel, intent prediction, predictive retention, marketing-as-product
- **Intuition: Judgment & Decision** — Nine-step decision framework, judgment traps, organizational judgment

---

## Industry Scenarios

<p align="center">
  <img src="assets/industry-matrix.png" alt="AI Across Industries" width="100%">
</p>

| Industry | Typical Scenario | Key Boundary Design |
|----------|-----------------|-------------------|
| Legal | Contract review assistant | Copilot only — no replacing lawyer decisions |
| Healthcare | Diagnostic support system | "Second opinion" only |
| Finance | Anti-fraud scoring | 100% human review for high-risk |
| E-commerce | AI customer service | Refund promises require human confirmation |
| DevOps | AIOps triage | Suggestions only — no auto-remediation |
| HR | Resume screening | Bias detection + blind screening mode |
| Education | Personalized learning | Hints only — no direct answers |
| Content | Marketing copywriting | Human refinement + compliance check |

---

## Design Principles (Why We Designed It This Way)

1. **Problem before solution** — Validate that the problem is real before building features
2. **Boundaries before capabilities** — Define what AI shouldn't do before designing what it can
3. **Evidence before decisions** — Replace "I think it works" with Shadow validation
4. **Orchestration before automation** — Keep human confirmation at critical decision points
5. **Iteration before perfection** — Optimize through failure analysis, not first-time perfection
6. **View correction before action** — Check if you're asking the right question before answering
7. **Judgment before intuition** — Make the reasoning explicit before trusting gut feel
8. **Aesthetic authority over feature completeness** — What you choose not to build defines the product

---

## Contributing

Issues and PRs are welcome! Priority areas:
- **New scenarios**: Add industry cases with complete input-output examples
- **Boundary designs**: How to draw AI boundaries in high-risk scenarios
- **Failure cases**: Failed experiment analyses are more valuable than success stories
- **New tool cards**: Convert book concept cards into executable Skills

---

## License

MIT License

---

> "Problem before solution. Boundaries before capabilities. Evidence before decisions. Orchestration before automation."
