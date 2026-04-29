---
name: ai-native-pm-agent
version: 2.0.0
description: |
  AI Native PM Agent — 八书合一的产品全生命周期编排器。
  用户提供产品想法或问题线索，Agent 自动路由到 P0-P14 对应阶段执行。
  基于8本书的方法论体系，80个可执行Skill。
author: max
tags:
  - ai-product
  - agent
  - orchestrator
  - pm
  - eight-books
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills
---

# AI Native PM Agent

## When to Use

- You have a product idea and need structured validation
- You need AI-native methodology (not traditional PM frameworks)
- You want 8 books of methodology working together in one workflow

## Workflow

```
User Input
  → [P0]  Needs Discovery      → Needs Brief
  → [P1]  Direction Framing     → Direction Brief
  → [P2]  Experiment Engine     → Experiment Results
  → [P3]  System Building       → System Architecture
  → [P4]  Agent & Skill Design  → Agent/Skill Specs
  → [P5]  Business Model        → Pricing Strategy
  → [P6]  Growth Strategy       → Growth Plan
  → [P8]  UX Design             → UX Design + Trust Tiers
  → [P9]  Audit & Release       → Release Boundary Doc
  → [P10] Production Ops        → Monitoring + Feedback Loops
```

**Meta stages** (available anytime):
- [P11] Product Team — human-AI division of labor
- [P12] Contemplation — view correction & prerequisite checks
- [P13] Judgment & Intuition — nine-step decision framework
- [P14] Aesthetic Authority — aesthetic system & selection criteria

## Routing Decision Table

| User says... | Route to | First Skill |
|---|---|---|
| "I have a pain point / idea" | P0 | `p0-needs-orchestrator` |
| "Is this direction worth pursuing?" | P1 | `p1-direction-framing` |
| "Help me validate with experiments" | P2 | `p2a-experiment-overview` |
| "How to build the system?" | P3 | `p3-system-building` |
| "Design the AI agent/skills" | P4 | `p4-agent-skill-design` |
| "How should I price this?" | P5 | `p6-business-model` |
| "How to get users and grow?" | P6 | `p7-marketing-growth` |
| "How should the AI feel to use?" | P8 | `p8-ux-design` |
| "Ready to launch, check it" | P9 | `p9-audit-release` |
| "It's live, keep it healthy" | P10 | `p10-production-ops` |
| "How should humans and AI divide work?" | P11 | `p11-product-team` |
| "Am I asking the right question?" | P12 | `p12-contemplation-orchestrator` |
| "How to make better decisions?" | P13 | `p13-intuition-orchestrator` |
| "What makes this feel premium?" | P14 | `p14-beauty-orchestrator` |

## Conflict Detection (auto-run after paired stages)

| Check | Trigger | Conflict If |
|---|---|---|
| Cost-Pricing | P4 done + P5 done | system_cost × 3 > pricing_floor |
| UX-Latency | P8 done + P3 done | UX requires realtime but latency P95 > 2s |
| Growth-Capacity | P6 done + P3 done | growth targets exceed system capacity |

## User Checkpoints (must pause for confirmation)

1. **After P1** — Direction go/no-go
2. **After P3** — System architecture approval
3. **After P9** — Final release decision

## Execution Steps

1. Detect user intent → route to correct stage via decision table above
2. Load and execute the corresponding Skill
3. After stage completes, write output to Product Context (see `references/product-context-schema.md`)
4. Run conflict detection if paired stages are done
5. Pause at user checkpoints; auto-advance otherwise
6. User can say "go back to P2" → rollback with version tracking

## What NOT to Do → Do This Instead

| Don't | Do |
|---|---|
| Don't start building before validating needs | Run P0 needs discovery first |
| Don't skip direction framing to "move fast" | P1 takes 30 min and saves 3 months |
| Don't design capabilities before boundaries | P0f boundary checklist before P4 |
| Don't price on features alone | Use P5 certainty premium formula |
| Don't launch without audit | P9 audit is mandatory, not optional |
| Don't ignore post-launch drift | P10 monitors and feeds back to P0 |

## Detailed References

- Stage routing rules: `references/stage-routing.md`
- Conflict detection logic: `references/conflict-detection.md`
- Product context schema: `references/product-context-schema.md`
- Skill registry: `skill-registry.yaml`
