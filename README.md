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

---

## See What It Does in 30 Seconds

<p align="center">
  <img src="assets/pipeline-flow.png" alt="P0→P7 Pipeline Flow" width="100%">
</p>

**Core Capabilities**: 38 executable Skills + Stage auto-routing + Conflict detection + Evidence chain tracking

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

### Business Model (P5)
The Agent prices using the Certainty Premium formula:
- **Fear Level**: Lawyers' biggest fear is missing a risky clause → High
- **Error Cost**: Missing one clause could mean millions in liability → Extremely high
- **Substitution Cost**: Manual review at $200/hour → Medium
- **Recommended Model**: Insurance Mode (charge per successful review, compensate for misses)

**Output**: Pricing strategy — $5/review, 10x compensation for missed clauses

### Audit & Release (P7)
The Agent checks:
- Reliability: Identification accuracy, hallucination rate
- Safety: Sensitive information handling
- Boundaries: Which clause types require human review
- Cost: Token cost per review vs. pricing

**Output**: Release boundary document — Auto-execute zone / Human handoff zone / Disabled zone

---

## Quick Start

### Option 1: With Hermes Agent (Recommended)

```bash
# 1. Install Hermes
pip install hermes-agent

# 2. Load the Skill
hermes skill add ai-native-pm-agent

# 3. Start a product project
hermes run "I want to build an AI customer service product, help me start from direction framing"
```

### Option 2: Use Skills Directly

```bash
# Clone the repo
git clone https://github.com/gmaxxxie/ai-native-product-agent-.git
cd ai-native-product-agent-

# Initialize product context
python scripts/init_product_context.py --name "My AI Product"

# Run orchestrator tests
python scripts/test_orchestrator.py
```

### Option 3: Manual Per-Stage Usage

Each stage is an independent Skill you can call individually:

| Stage | Trigger Phrase | Output |
|-------|---------------|--------|
| P0 Needs Discovery | "I have a pain point…" | Needs validation report |
| P0a Micro-Needs | "Is this problem too small to matter?" | Micro-needs list |
| P0b Real Needs | "Is this need real or fake?" | Real/fake verdict |
| P0c Decomposition | "Help me decompose this need" | Four-layer breakdown |
| P0d Archaeology | "What's the deep need?" | Deep needs report |
| P1 Direction Framing | "I have an idea…" | Direction Brief |
| P2 Experiment Engine | "Help me design experiments…" | Experiment plan + Rubric |
| P3 System Building | "How to go from experiment to product…" | System architecture |
| P5 Business Model | "How to price this…" | Pricing strategy |
| P5a Certainty Premium | "What's my product worth?" | Premium calculation |
| P6 Growth Strategy | "How to get cold start…" | Growth plan |
| P6a Data Flywheel | "Can my flywheel spin?" | Flywheel assessment + plan |
| P7 Audit & Release | "Ready to launch, check it…" | Release boundary document |

### Option 4: Cross-Book Combos (One-Stop)

| Combo | Trigger Phrase | Output |
|-------|---------------|--------|
| Needs → Direction | "Take me from pain point to direction framing" | Direction Brief |
| Business → Growth | "How should pricing and growth align?" | Pricing-growth alignment |
| UX → Audit | "Is this UX design safe to release?" | UX audit report + release recommendation |

---

## Complete Skill List (38)

### Needs Discovery Layer (P0) — From: *Micro-Needs for AI Products*

| ID | Name | What It Does |
|----|------|-------------|
| p0-needs-orchestrator | Needs Discovery Orchestrator | Coordinates six tool cards for systematic needs discovery |
| p0a-micro-needs-detector | Micro-Needs Five Questions | Detects overlooked micro-needs |
| p0b-real-needs-validator | Real-Needs Five Questions | Distinguishes real needs from fake ones |
| p0c-needs-decomposer | Needs Four-Layer Decomposition | Expression / Scenario / Situation / Cost layers |
| p0d-needs-archaeologist | Needs Archaeology Five Steps | Uncovers deep needs and historical constraints |
| p0e-good-question-generator | Good Questions Six Dimensions | Discovers good questions from six perspectives |
| p0f-agent-boundary-designer | Agent Boundary Checklist | Defines AI permission boundaries |
| p0g-diverse-recommendation-rewriter | Diverse Recommendation Rewrite | From "guess what you like" to "help you discover" |
| p0h-ai-product-triple-balance | AI Product Triple Balance | Business / Humanity / Technology balance |

### Direction & Experiment Layer (P1–P2) — From: *AI Native Product Methodology*

| ID | Name | What It Does |
|----|------|-------------|
| p1-direction-framing | Direction Framing | Five-dimension judgment, Direction Brief |
| p2-experiment-engine | Experiment Engine | Capability / Product / Business three-layer experiments |

### System Building Layer (P3–P4) — From: *AI Native Product Methodology*

| ID | Name | What It Does |
|----|------|-------------|
| p3-system-building | System Building | From experiments to product |
| p4-agent-skill-design | Agent & Skill Unit Design | Agent/Skill unit design |
| p5-memory-system | Memory System Design | AI product memory architecture |
| p6-context-engineering | Context Engineering | Context management system |
| p7-knowledge-rag | RAG & Knowledge System | Knowledge management + RAG design |

### Business Model Layer (P5) — From: *JUDGMENT*

| ID | Name | What It Does |
|----|------|-------------|
| p6-business-model | AI Native Business Model (Overview) | Certainty Premium business model design |
| p6a-certainty-premium-calculator | Certainty Premium Calculator | Calculates certainty premium |
| p6b-arbiter-mode-designer | Arbiter Mode Designer | "Truth-as-a-Service" business model |
| p6c-insurance-mode-designer | Insurance Mode Designer | "Result Guarantee" business model |
| p6d-prediction-arbitrage-designer | Prediction Arbitrage Designer | "Time Arbitrage" business model |

### Growth Strategy Layer (P6) — From: *Aesthetic Authority*

| ID | Name | What It Does |
|----|------|-------------|
| p7-marketing-growth | AI Native Marketing & Growth (Overview) | Growth flywheel & marketing strategy |
| p7a-data-flywheel-builder | Data Flywheel Builder | Assesses and builds self-reinforcing data flywheels |
| p7b-intent-prediction-designer | Intent Prediction Designer | From audience targeting to individual foresight |
| p7c-predictive-retention-designer | Predictive Retention Designer | From post-churn recovery to pre-churn prevention |
| p7d-marketing-productizer | Marketing-as-Product Designer | Turns marketing activities into product features |

### User Experience Layer (P4) — From: *Contemplation*

| ID | Name | What It Does |
|----|------|-------------|
| p8-ux-design | AI Native UX Design (Overview) | UX design methodology |
| p8a-rax-risk-assessor | RAX Risk Assessor | Risk / Ambiguity / eXposure assessment |
| p8b-trust-tier-designer | Trust Tier Designer | Progressive trust system design |
| p8c-progressive-disclosure | Progressive Disclosure Checklist | Feature reveal pacing design |

### Audit & Operations Layer (P7) — From: *AI Native Product Methodology*

| ID | Name | What It Does |
|----|------|-------------|
| p9-audit-release | Audit & Release | Go/no-go decision |
| p10-production-ops | Production Operations | Monitoring & feedback loops |

### Cross-Book Combo Skills

| ID | Name | What It Does |
|----|------|-------------|
| combo-needs-to-direction | Needs → Direction | Pain point to Direction Brief in one pass |
| combo-business-to-growth | Business → Growth | Pricing-flywheel alignment design |
| combo-ux-to-audit | UX → Audit | RAX assessment + trust tiers + release recommendation |

---

## Project Structure

```
ai-native-pm-agent/
├── README.md                       # This document (English)
├── README_CN.md                    # 中文版文档
├── ARCHITECTURE.md                 # System architecture design
├── skill-registry.yaml             # Skill registry
├── orchestrator/SKILL.md           # Main orchestrator: stage routing + conflict detection
├── skills/
│   # Needs Discovery (9)
│   ├── p0-needs-orchestrator/
│   ├── p0a-micro-needs-detector/
│   ├── p0b-real-needs-validator/
│   ├── p0c-needs-decomposer/
│   ├── p0d-needs-archaeologist/
│   ├── p0e-good-question-generator/
│   ├── p0f-agent-boundary-designer/
│   ├── p0g-diverse-recommendation-rewriter/
│   ├── p0h-ai-product-triple-balance/
│   # Direction & Experiment (2)
│   ├── p1-direction-framing/
│   ├── p2-experiment-engine/
│   # System Building (5)
│   ├── p3-system-building/
│   ├── p4-agent-skill-design/
│   ├── p5-memory-system/
│   ├── p6-context-engineering/
│   ├── p7-knowledge-rag/
│   # Business Model (5)
│   ├── p6-business-model/
│   ├── p6a-certainty-premium-calculator/
│   ├── p6b-arbiter-mode-designer/
│   ├── p6c-insurance-mode-designer/
│   ├── p6d-prediction-arbitrage-designer/
│   # Growth Strategy (5)
│   ├── p7-marketing-growth/
│   ├── p7a-data-flywheel-builder/
│   ├── p7b-intent-prediction-designer/
│   ├── p7c-predictive-retention-designer/
│   ├── p7d-marketing-productizer/
│   # User Experience (4)
│   ├── p8-ux-design/
│   ├── p8a-rax-risk-assessor/
│   ├── p8b-trust-tier-designer/
│   ├── p8c-progressive-disclosure/
│   # Audit & Operations (2)
│   ├── p9-audit-release/
│   ├── p10-production-ops/
│   # Cross-Book Combos (3)
│   ├── combo-needs-to-direction/
│   ├── combo-business-to-growth/
│   └── combo-ux-to-audit/
└── scripts/
    ├── init_product_context.py     # Initialization
    ├── test_orchestrator.py        # Tests
    └── final_validation.py         # Final validation
```

---

## Five Books Behind the Methodology

<p align="center">
  <img src="assets/methodology-books.png" alt="Five Books Methodology Synthesis" width="100%">
</p>

All 38 Skills are derived from five methodology books. Each book's tool cards and concept cards have been converted into executable Skills:

| Book | Stages Covered | Skills |
|------|---------------|--------|
| [Micro-Needs for AI Products](https://www.amazon.com/dp/B0GT48SZ5R) | P0 Needs Discovery | 9 |
| [AI Native Product Methodology](https://www.amazon.com/dp/B0GSMXD24H) | P1–P4 Direction / Experiment / System / Audit | 10 |
| [JUDGMENT](https://www.amazon.com/dp/B0GRQVR2J4) | P5 Business Model | 5 |
| [Contemplation](https://www.amazon.com/dp/B0GX2H4D33) | P4 UX Design | 4 |
| [Aesthetic Authority](https://www.amazon.com/dp/B0GCHHZBV3) | P6 Growth Strategy | 5 |

📖 **Get the books on Amazon**:
- **[Micro-Needs for AI Products: Finding What Is Truly Worth Building in the Age of AI](https://www.amazon.com/dp/B0GT48SZ5R)** — Needs discovery, micro-needs detection, real-needs validation, needs decomposition, agent boundary design
- **[AI Native Product Methodology: Building AI Products Through Experimentation, System Design, Governance, and Feedback Loops](https://www.amazon.com/dp/B0GSMXD24H)** — Direction framing, experiment engine, system building, audit & release, production operations
- **[JUDGMENT: HOW TO MAKE BETTER AI PRODUCT DECISIONS](https://www.amazon.com/dp/B0GRQVR2J4)** — Certainty Premium, business model design, pricing strategy
- **[Contemplation: Product Judgment, User Understanding, and Decision Correction in the AI Era](https://www.amazon.com/dp/B0GX2H4D33)** — RAX risk assessment, trust tier design, progressive disclosure
- **[Aesthetic Authority: Why Human Judgment and Taste Matter in the Age of AI](https://www.amazon.com/dp/B0GCHHZBV3)** — Data flywheel, intent prediction, predictive retention, marketing-as-product

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
