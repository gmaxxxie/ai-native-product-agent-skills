#!/usr/bin/env python3
"""
初始化 AI Native PM Agent 的 Product Context
Usage: python3 init_product_context.py "用户输入的产品想法"
"""

import json
import uuid
from datetime import datetime


def init_product_context(user_input: str) -> dict:
    """初始化产品上下文"""
    
    context = {
        "meta": {
            "product_id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "agent_version": "1.0"
        },
        "state": {
            "current_stage": "p1",
            "completed_stages": [],
            "status": "active"
        },
        "artifacts": {
            "p1_needs": {
                "user_input": user_input,
                "user_problem": None,
                "target_users": [],
                "pain_points": [],
                "opportunity_score": None
            },
            "p2_direction": {},
            "p3_ux": {},
            "p4_system": {},
            "p5_business": {},
            "p6_growth": {},
            "p7_audit": {}
        },
        "decisions": [],
        "flags": {
            "needs_revisit": [],
            "blockers": [],
            "user_approvals": []
        }
    }
    
    return context


if __name__ == "__main__":
    import sys
    
    user_input = sys.argv[1] if len(sys.argv) > 1 else "未提供输入"
    context = init_product_context(user_input)
    print(json.dumps(context, indent=2, ensure_ascii=False))
