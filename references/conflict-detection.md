# Conflict Detection Rules

> Version: 2.0 | Cross-stage consistency checks for P0-P14

---

## Check 1: Cost-Pricing Match

Trigger: P4 (system building) done AND P5 (business model) done

```python
if system_monthly_cost * 3 > pricing_floor:
    CONFLICT: "System cost too high, pricing cannot cover"
    Fix: "Reduce system complexity OR raise pricing via certainty premium"
```

---

## Check 2: UX Realtime vs System Latency

Trigger: P8 (UX design) done AND P3 (system building) done

```python
if ux.interaction_model == "realtime_chat" AND system.latency_p95 > 2000:
    CONFLICT: "UX requires realtime but system too slow"
    Fix: "Optimize latency OR switch UX to async mode"
```

---

## Check 3: Growth Target vs System Capacity

Trigger: P6 (growth) done AND P3 (system building) done

```python
if growth.projected_peak_users > system.capacity_90th:
    CONFLICT: "Growth targets exceed system capacity"
    Fix: "Scale system architecture OR reduce growth targets"
```

---

## Check 4: Needs-Direction Alignment

Trigger: P0 (needs) done AND P1 (direction) done

```python
if direction.target_users != needs.primary_user_segment:
    CONFLICT: "Direction targets different users than needs analysis"
    Fix: "Revisit P0 needs or adjust P1 direction"
```

---

## Check 5: Boundary-Business Consistency

Trigger: P0f (boundary design) done AND P5 (business model) done

```python
if boundary.human_confirmation_required AND business.model == "insurance_mode":
    WARNING: "Insurance mode promises outcomes but boundary requires human checks"
    Fix: "Clarify liability allocation between AI and human"
```

---

## Check 6: Aesthetic-UX Coherence

Trigger: P14 (aesthetic) done AND P8 (UX design) done

```python
if aesthetic.standard == "premium_minimal" AND ux.disclosure_level == "full":
    WARNING: "Premium aesthetic conflicts with full disclosure UX"
    Fix: "Use progressive disclosure to maintain aesthetic while revealing depth"
```

---

## When Conflicts Are Found

1. **CONFLICT** (hard) → Block auto-advance, require user decision
2. **WARNING** (soft) → Log and continue, user can address later
3. User can override any conflict with explicit "proceed anyway"
