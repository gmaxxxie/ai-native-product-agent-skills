#!/usr/bin/env bash
# AI Native PM Agent — One-click Skill Installer
# Installs all 38 skills + orchestrator into ~/.hermes/skills/ai-native-pm/
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/gmaxxxie/ai-native-product-agent-skills/main/install.sh | bash
#   — or —
#   git clone https://github.com/gmaxxxie/ai-native-product-agent-skills.git && cd ai-native-product-agent-skills && bash install.sh

set -euo pipefail

REPO="gmaxxxie/ai-native-product-agent-skills"
BASE_URL="https://raw.githubusercontent.com/${REPO}/main"
CATEGORY="ai-native-pm"
HERMES_SKILLS_DIR="${HOME}/.hermes/skills"
TARGET_DIR="${HERMES_SKILLS_DIR}/${CATEGORY}"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo "🧭 AI Native PM Agent — Skill Installer"
echo "========================================"
echo ""

# Check hermes is installed
if ! command -v hermes &> /dev/null; then
    echo -e "${RED}❌ Hermes Agent not found.${NC}"
    echo "   Install it first: curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash"
    exit 1
fi

echo -e "${GREEN}✅ Hermes found: $(hermes --version 2>/dev/null || echo 'installed')${NC}"
echo ""

# Option 1: If running from a cloned repo, use local files
if [ -f "./skills/p1-direction-framing/SKILL.md" ]; then
    echo -e "${YELLOW}📂 Detected local repo — installing from local files${NC}"
    
    mkdir -p "${TARGET_DIR}"
    
    count=0
    # Install orchestrator
    mkdir -p "${TARGET_DIR}/ai-native-pm-agent"
    cp -r ./orchestrator/* "${TARGET_DIR}/ai-native-pm-agent/" 2>/dev/null || true
    echo -e "  ${GREEN}✅${NC} ai-native-pm-agent (orchestrator)"
    count=$((count + 1))
    
    # Install each skill
    for skill_dir in ./skills/*/; do
        if [ -f "${skill_dir}SKILL.md" ]; then
            skill_name=$(basename "${skill_dir}")
            dest="${TARGET_DIR}/${skill_name}"
            mkdir -p "${dest}"
            cp -r "${skill_dir}"* "${dest}/" 2>/dev/null || true
            echo -e "  ${GREEN}✅${NC} ${skill_name}"
            count=$((count + 1))
        fi
    done
    
    echo ""
    echo -e "${GREEN}🎉 Installed ${count} skills to ${TARGET_DIR}/${NC}"

# Option 2: Install from GitHub URLs
else
    echo -e "${YELLOW}🌐 Installing from GitHub...${NC}"
    
    # Define all skills
    SKILLS=(
        "orchestrator:ai-native-pm-agent"
        "skills/p0-product-needs:p0-product-needs"
        "skills/p0-needs-orchestrator:p0-needs-orchestrator"
        "skills/p0a-micro-needs-detector:p0a-micro-needs-detector"
        "skills/p0b-real-needs-validator:p0b-real-needs-validator"
        "skills/p0c-needs-decomposer:p0c-needs-decomposer"
        "skills/p0d-needs-archaeologist:p0d-needs-archaeologist"
        "skills/p0e-good-question-generator:p0e-good-question-generator"
        "skills/p0f-agent-boundary-designer:p0f-agent-boundary-designer"
        "skills/p0g-diverse-recommendation-rewriter:p0g-diverse-recommendation-rewriter"
        "skills/p0g-diversity-rewrite-checklist:p0g-diversity-rewrite-checklist"
        "skills/p0h-ai-product-triple-balance:p0h-ai-product-triple-balance"
        "skills/p0h-triple-balance-assessor:p0h-triple-balance-assessor"
        "skills/p1-direction-framing:p1-direction-framing"
        "skills/p2-experiment-engine:p2-experiment-engine"
        "skills/p3-system-building:p3-system-building"
        "skills/p4-agent-skill-design:p4-agent-skill-design"
        "skills/p5-memory-system:p5-memory-system"
        "skills/p6-context-engineering:p6-context-engineering"
        "skills/p7-knowledge-rag:p7-knowledge-rag"
        "skills/p6-business-model:p6-business-model"
        "skills/p6a-certainty-premium-calculator:p6a-certainty-premium-calculator"
        "skills/p6b-arbiter-mode-designer:p6b-arbiter-mode-designer"
        "skills/p6c-insurance-mode-designer:p6c-insurance-mode-designer"
        "skills/p6d-prediction-arbitrage-designer:p6d-prediction-arbitrage-designer"
        "skills/p7-marketing-growth:p7-marketing-growth"
        "skills/p7a-data-flywheel-builder:p7a-data-flywheel-builder"
        "skills/p7b-intent-prediction-designer:p7b-intent-prediction-designer"
        "skills/p7c-predictive-retention-designer:p7c-predictive-retention-designer"
        "skills/p7d-marketing-productizer:p7d-marketing-productizer"
        "skills/p8-ux-design:p8-ux-design"
        "skills/p8a-rax-risk-assessor:p8a-rax-risk-assessor"
        "skills/p8b-trust-tier-designer:p8b-trust-tier-designer"
        "skills/p8c-progressive-disclosure:p8c-progressive-disclosure"
        "skills/p9-audit-release:p9-audit-release"
        "skills/p10-production-ops:p10-production-ops"
        "skills/combo-needs-to-direction:combo-needs-to-direction"
        "skills/combo-business-to-growth:combo-business-to-growth"
        "skills/combo-ux-to-audit:combo-ux-to-audit"
    )
    
    count=0
    failed=0
    
    for entry in "${SKILLS[@]}"; do
        IFS=':' read -r path name <<< "${entry}"
        url="${BASE_URL}/${path}/SKILL.md"
        
        # Try hermes skills install
        if printf "${CATEGORY}\ny\n" | hermes skills install "${url}" --name "${name}" 2>/dev/null; then
            echo -e "  ${GREEN}✅${NC} ${name}"
            count=$((count + 1))
        else
            # Fallback: direct download
            dest="${TARGET_DIR}/${name}"
            mkdir -p "${dest}"
            if curl -fsSL "${url}" -o "${dest}/SKILL.md" 2>/dev/null; then
                echo -e "  ${GREEN}✅${NC} ${name} (direct download)"
                count=$((count + 1))
            else
                echo -e "  ${RED}❌${NC} ${name}"
                failed=$((failed + 1))
            fi
        fi
    done
    
    echo ""
    echo -e "${GREEN}🎉 Installed ${count} skills${NC}"
    if [ $failed -gt 0 ]; then
        echo -e "${YELLOW}⚠️  ${failed} skills failed — try running again or install manually${NC}"
    fi
fi

echo ""
echo "📋 Verify:  hermes skills list | grep ai-native-pm"
echo "🚀 Start:   hermes run \"I want to build an AI product, start from needs discovery\""
echo ""
