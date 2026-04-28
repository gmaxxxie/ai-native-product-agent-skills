#!/usr/bin/env python3
"""
AI Native PM Agent — 最终验证脚本
验证所有组件、Skill、脚本和配置是否完整
"""

import os
import sys
import json
from pathlib import Path

SKILL_DIR = Path.home() / ".hermes" / "skills"
AGENT_DIR = SKILL_DIR / "ai-native-pm-agent"


def check_file(path: Path, desc: str) -> bool:
    """检查文件是否存在"""
    exists = path.exists()
    status = "✅" if exists else "❌"
    print(f"  {status} {desc}: {path}")
    return exists


def validate_skill(skill_name: str) -> bool:
    """验证单个 Skill 是否完整"""
    # 先检查直接路径
    skill_dir = SKILL_DIR / skill_name
    # 再检查 book-writing 子目录
    if not skill_dir.exists():
        skill_dir = SKILL_DIR / "book-writing" / skill_name
    
    skill_md = skill_dir / "SKILL.md"
    
    if not skill_md.exists():
        print(f"  ❌ Skill '{skill_name}' 缺少 SKILL.md")
        return False
    
    content = skill_md.read_text()
    checks = [
        ("name:" in content, "YAML frontmatter：name"),
        ("description:" in content, "YAML frontmatter：description"),
        ("tags:" in content, "YAML frontmatter：tags"),
        ("## " in content, "Markdown 标题"),
    ]
    
    all_pass = True
    for check, desc in checks:
        status = "✅" if check else "❌"
        if not check:
            all_pass = False
        print(f"    {status} {desc}")
    
    return all_pass


def validate_agent_components() -> bool:
    """验证 Agent 核心组件"""
    print("\n📦 验证 Agent 核心组件...")
    
    components = [
        (AGENT_DIR / "SKILL.md", "主入口 SKILL.md"),
        (AGENT_DIR / "ARCHITECTURE.md", "架构设计文档"),
        (AGENT_DIR / "references" / "product-context-schema.md", "上下文 Schema"),
        (AGENT_DIR / "references" / "stage-routing.md", "阶段路由规则"),
        (AGENT_DIR / "references" / "conflict-detection.md", "冲突检测规则"),
        (AGENT_DIR / "scripts" / "init_product_context.py", "初始化脚本"),
        (AGENT_DIR / "scripts" / "test_orchestrator.py", "编排测试脚本"),
        (AGENT_DIR / "templates" / "report-template.md", "报告模板"),
    ]
    
    results = [check_file(path, desc) for path, desc in components]
    return all(results)


def validate_all_skills() -> bool:
    """验证所有 Skill"""
    print("\n🔧 验证所有 Skill...")
    
    skills = [
        "ai-native-pm-agent",
        "ai-native-product-needs",
        "ai-native-direction-framing",
        "ai-native-experiment-engine",
        "ai-native-system-building",
        "ai-native-agent-skill-design",
        "ai-native-memory-system",
        "ai-native-context-engineering",
        "ai-native-knowledge-rag",
        "ai-native-ux-design",
        "ai-native-user-experience",
        "ai-native-business-model",
        "ai-native-marketing-growth",
        "ai-native-audit-release",
        "ai-native-production-ops",
    ]
    
    results = []
    for skill in skills:
        print(f"\n  📚 {skill}")
        results.append(validate_skill(skill))
    
    return all(results)


def run_unit_tests() -> bool:
    """运行单元测试"""
    print("\n🧪 运行单元测试...")
    
    # 运行现有的编排器测试
    scripts_dir = AGENT_DIR / "scripts"
    sys.path.insert(0, str(scripts_dir))
    
    try:
        import test_orchestrator as test_mod
        test_mod.test_stage_routing()
        test_mod.test_conflict_detection()
        test_mod.test_product_context_init()
        print("  ✅ 所有单元测试通过")
        return True
    except Exception as e:
        print(f"  ❌ 测试失败: {e}")
        return False


def validate_context_schema() -> bool:
    """验证上下文 Schema 可用"""
    print("\n📝 验证 Product Context Schema...")
    
    from init_product_context import init_product_context
    
    ctx = init_product_context("我想做一个AI客服协同系统")
    
    checks = [
        ("meta" in ctx, "meta 字段"),
        ("state" in ctx, "state 字段"),
        ("artifacts" in ctx, "artifacts 字段"),
        ("decisions" in ctx, "decisions 字段"),
        ("flags" in ctx, "flags 字段"),
        (ctx["state"]["current_stage"] == "p1", "初始阶段为 p1"),
        (len(ctx["artifacts"]) == 7, "7个阶段 artifacts"),
    ]
    
    all_pass = True
    for check, desc in checks:
        status = "✅" if check else "❌"
        if not check:
            all_pass = False
        print(f"  {status} {desc}")
    
    return all_pass


def validate_workflow_connectivity() -> bool:
    """验证工作流连通性"""
    print("\n🔗 验证工作流连通性...")
    
    # 验证阶段路由
    from test_orchestrator import should_advance
    
    # 模拟完整流程
    stages = [
        ("p1", {"opportunity_score": 80}, True, "P1→P2"),
        ("p2", {"go_no_go": "go"}, True, "P2→P3"),
        ("p3", {"ux_design": {}}, True, "P3→P4"),
        ("p4", {"system_design": {}}, True, "P4→P5"),
        ("p5", {"pricing_model": "subscription"}, True, "P5→P6"),
        ("p6", {"growth_strategy": {}}, True, "P6→P7"),
        ("p7", {"audit": "go"}, True, "P7 完成"),
    ]
    
    all_pass = True
    for stage, artifact, expected, desc in stages:
        result = should_advance(stage, artifact)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_pass = False
        print(f"  {status} {desc}: 可通过={result}")
    
    return all_pass


def print_summary(results: dict) -> None:
    """打印验证摘要"""
    print("\n" + "=" * 60)
    print("📊 验证摘要")
    print("=" * 60)
    
    total = len(results)
    passed = sum(results.values())
    
    for name, result in results.items():
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {status} {name}")
    
    print("-" * 60)
    print(f"  总计: {passed}/{total} 项通过")
    
    if passed == total:
        print("\n🎉 所有验证通过！Agent 已就绪。")
    else:
        print(f"\n⚠️ {total - passed} 项验证失败，请修复后重试。")
    
    print("=" * 60)


if __name__ == "__main__":
    print("=" * 60)
    print("🚀 AI Native PM Agent — 最终验证")
    print("=" * 60)
    
    results = {
        "Agent 组件完整性": validate_agent_components(),
        "Skill 完整性": validate_all_skills(),
        "单元测试": run_unit_tests(),
        "上下文 Schema": validate_context_schema(),
        "工作流连通性": validate_workflow_connectivity(),
    }
    
    print_summary(results)
    
    sys.exit(0 if all(results.values()) else 1)
