# Stage Routing Rules

> Version: 2.0 | 8 books, 80 skills, P0-P14

---

## Default Flow (Product Pipeline)

```
P0 → P1 → P2 → P3 → P4 → P5 → P6 → P8 → P9 → P10
```

Note: P7 is knowledge-RAG (part of P4 system building). P5/P6 are stage IDs for business/growth, not sequential positions.

---

## Routing Rules

### 1. P0 → P1 (Needs Discovery → Direction Framing)

Condition: `p0.opportunity_score >= 60`
Action: Auto-enter P1
Exception: `score < 60` → pause, suggest re-examining needs

### 2. P1 → P2 (Direction Framing → Experiment Engine)

Condition: `p1.go_no_go == "go"`
Action: Auto-enter P2
Exception: `"no-go"` → terminate with direction conclusion
Exception: `"conditional"` → enter P2 with constraints attached

### 3. P2 → P3 (Experiment → System Building)

Condition: `p2.convergence_signal == "converge"` AND at least one validated experiment
Action: Auto-enter P3
Exception: `"diverge"` → extend experiments, add P2a-P2e sub-skills
Exception: `"stop"` → terminate, output findings

### 4. P3 → P4 (System → Agent/Skill Design)

Condition: `p3.system_architecture` approved
Action: Auto-enter P4 (agent design, memory, context, RAG as sub-skills)

### 5. P4 → P5 (Agent/Skill → Business Model)

Condition: `p4.system_cost_estimate` available
Action: Auto-enter P5

### 6. P5 → P6 (Business → Growth Strategy)

Condition: `p5.pricing_strategy` confirmed
Action: Auto-enter P6

### 7. P6 → P8 (Growth → UX Design)

Condition: `p6.growth_plan` confirmed
Action: Auto-enter P8 (UX validation before audit)

### 8. P8 → P9 (UX → Audit & Release)

Condition: `p8.ux_design` + trust tiers defined
Action: Auto-enter P9

### 9. P9 → P10 (Audit → Production Ops)

Condition: `p9.release_decision == "go"`
Action: Auto-enter P10
Exception: `"no-go"` → return to failing stage with audit findings

---

## Meta Stage Routing (Available Anytime)

| User Signal | Route To | Skill |
|---|---|---|
| "Team structure question" | P11 | `p11-product-team` |
| "Not sure if I'm asking the right question" | P12 | `p12-contemplation-orchestrator` |
| "How to make better decisions" | P13 | `p13-intuition-orchestrator` |
| "Product feels generic, lacks taste" | P14 | `p14-beauty-orchestrator` |

Meta stages do NOT replace pipeline stages. They supplement decision-making at any point.

---

## Cross-Stage Combos

| Combo | Trigger | Flow |
|---|---|---|
| Needs → Direction | "Take me from pain point to direction" | P0 → P1 (skip intermediate pauses) |
| Business → Growth | "Align pricing with growth" | P5 → P6 (joint optimization) |
| UX → Audit | "Is this UX safe to release?" | P8 → P9 (streamlined audit) |

---

## Rollback Protocol

User can say: "go back to P{N}"

1. Current stage output saved as v1
2. Re-execute target stage → generates v2
3. Downstream stages marked "pending update"
4. User confirms whether to propagate changes downstream
