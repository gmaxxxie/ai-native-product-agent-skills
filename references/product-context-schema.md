# Product Context Schema

> Version: 2.0 | Shared context protocol across P0-P14

---

## Schema

```yaml
version: "2.0"
meta:
  product_id: string          # UUID
  created_at: timestamp
  updated_at: timestamp
  agent_version: "2.0"

state:
  current_stage: string       # p0-p14
  completed_stages: [string]
  status: active|blocked|completed|revisit

# Pipeline outputs
artifacts:
  p0_needs_brief: null           # Needs validation + boundary design
  p1_direction_brief: null       # Direction go/no-go + conditions
  p2_experiment_results: null    # Experiment records + convergence signal
  p3_system_architecture: null   # Architecture + cost estimate
  p4_agent_skill_specs: null     # Agent/Skill/Memory/Context/RAG design
  p5_business_model: null        # Pricing + revenue model
  p6_growth_plan: null           # Acquisition/activation/retention strategy
  p8_ux_design: null             # UX design + trust tiers + RAX assessment
  p9_release_boundary: null      # Auto zone / human zone / disabled zone
  p10_ops_config: null           # Monitoring + feedback loop config

# Meta stage outputs (optional, filled on demand)
meta_artifacts:
  p11_team_design: null          # Human-AI division + roles
  p12_contemplation_notes: null  # View corrections + prerequisite checks
  p13_judgment_record: null      # Decision framework output
  p14_aesthetic_standard: null   # Aesthetic system + selection criteria

# Conflict detection results
conflict_checks:
  p0_p1_needs_direction: null
  p3_p5_cost_pricing: null
  p3_p8_ux_latency: null
  p3_p6_growth_capacity: null
  p0f_p5_boundary_business: null
  p8_p14_aesthetic_ux: null

# Rollback history
history:
  - stage: string
    version: integer
    completed_at: timestamp
    artifacts_key: string
```

---

## Context Passing Rules

1. Each stage reads ONLY its direct predecessor's output + meta_artifacts
2. P0-P10 pipeline stages write to `artifacts`
3. P11-P14 meta stages write to `meta_artifacts`
4. Conflict checks auto-populate `conflict_checks` after paired stages complete
5. Rollback preserves v1, new execution generates v2
