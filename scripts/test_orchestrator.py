#!/usr/bin/env python3
"""
测试 AI Native PM Agent 的编排器逻辑
Usage: python3 test_orchestrator.py
"""


def should_advance(stage: str, artifact: dict) -> bool:
    """判断是否可以进入下一阶段"""
    
    if stage == "p1":
        score = artifact.get("opportunity_score", 0)
        return score >= 60
    
    if stage == "p2":
        return artifact.get("go_no_go") == "go"
    
    if stage == "p3":
        return artifact.get("ux_design") is not None
    
    if stage == "p4":
        return artifact.get("system_design") is not None
    
    if stage == "p5":
        return artifact.get("pricing_model") is not None
    
    if stage == "p6":
        return artifact.get("growth_strategy") is not None
    
    if stage == "p7":
        return artifact.get("audit") == "go"
    
    return False


def detect_conflict(conflict_type: str, artifact_a: dict, artifact_b: dict) -> str:
    """检测两个阶段产出物之间的冲突"""
    
    if conflict_type == "cost_pricing":
        cost = artifact_a.get("cost_estimate", 0)
        pricing = artifact_b.get("pricing_monthly_lowest", float('inf'))
        if cost * 3 > pricing:
            return f"CONFLICT: 系统成本({cost})过高，定价({pricing})无法覆盖"
        return None
    
    if conflict_type == "ux_latency":
        interaction = artifact_a.get("interaction_model", "")
        latency = artifact_b.get("latency_p95", 0)
        if interaction == "realtime_chat" and latency > 2000:
            return f"CONFLICT: UX要求实时但系统延迟({latency}ms)过高"
        return None
    
    if conflict_type == "growth_capacity":
        target_mau = artifact_a.get("target_mau_month_6", 0)
        capacity = artifact_b.get("max_concurrent_users", float('inf'))
        if target_mau / 30 > capacity:
            return f"CONFLICT: 增长目标({target_mau} MAU)超出承载({capacity} 并发)"
        return None
    
    return None


def test_stage_routing():
    """测试阶段路由"""
    print("→ 测试阶段路由...")
    
    # P1 → P2
    assert should_advance("p1", {"opportunity_score": 70}) == True
    assert should_advance("p1", {"opportunity_score": 50}) == False
    assert should_advance("p1", {}) == False
    
    # P2 → P3
    assert should_advance("p2", {"go_no_go": "go"}) == True
    assert should_advance("p2", {"go_no_go": "no-go"}) == False
    assert should_advance("p2", {"go_no_go": "conditional"}) == False
    
    # P4 → P5
    assert should_advance("p4", {"system_design": {}}) == True
    assert should_advance("p4", {}) == False
    
    # P7
    assert should_advance("p7", {"audit": "go"}) == True
    assert should_advance("p7", {"audit": "no-go"}) == False
    
    print("✅ 阶段路由测试通过")


def test_conflict_detection():
    """测试冲突检测"""
    print("→ 测试冲突检测...")
    
    # 成本-定价匹配
    p4_ok = {"cost_estimate": 1000}
    p5_ok = {"pricing_monthly_lowest": 5000}
    assert detect_conflict("cost_pricing", p4_ok, p5_ok) is None  # 1000*3=3000 < 5000
    
    p5_low = {"pricing_monthly_lowest": 2000}
    conflict = detect_conflict("cost_pricing", p4_ok, p5_low)
    assert conflict is not None
    assert "成本" in conflict
    
    # UX-延迟匹配
    p3_realtime = {"interaction_model": "realtime_chat"}
    p4_slow = {"latency_p95": 3000}
    conflict = detect_conflict("ux_latency", p3_realtime, p4_slow)
    assert conflict is not None
    assert "延迟" in conflict
    
    p4_fast = {"latency_p95": 500}
    assert detect_conflict("ux_latency", p3_realtime, p4_fast) is None
    
    # 增长-承载匹配
    p6_big = {"target_mau_month_6": 300000}  # 10000/day
    p4_small = {"max_concurrent_users": 5000}
    conflict = detect_conflict("growth_capacity", p6_big, p4_small)
    assert conflict is not None
    assert "增长" in conflict
    
    p4_big = {"max_concurrent_users": 20000}
    assert detect_conflict("growth_capacity", p6_big, p4_big) is None
    
    print("✅ 冲突检测测试通过")


def test_product_context_init():
    """测试上下文初始化"""
    print("→ 测试上下文初始化...")
    
    from init_product_context import init_product_context
    
    ctx = init_product_context("我想做一个AI客服产品")
    
    assert ctx["meta"]["product_id"] is not None
    assert ctx["state"]["current_stage"] == "p1"
    assert ctx["state"]["completed_stages"] == []
    assert ctx["artifacts"]["p1_needs"]["user_input"] == "我想做一个AI客服产品"
    assert ctx["artifacts"]["p1_needs"]["opportunity_score"] is None
    assert ctx["flags"]["blockers"] == []
    
    print("✅ 上下文初始化测试通过")


if __name__ == "__main__":
    print("=" * 50)
    print("🧪 AI Native PM Agent 编排器测试")
    print("=" * 50)
    
    test_stage_routing()
    test_conflict_detection()
    test_product_context_init()
    
    print("=" * 50)
    print("🎉 所有测试通过！")
    print("=" * 50)
