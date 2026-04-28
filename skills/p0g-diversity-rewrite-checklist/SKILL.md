---
name: p0g-diversity-rewrite-checklist
version: 1.0.0
description: 多元推荐改写清单。当团队想重写推荐系统时，最容易只在原目标函数上加一点随机。 这个 Skill 帮你避免"看起来更多元，底层仍然单一"。
  基于《AI rebuild product needs》工具卡。
author: Max
tags: p0, 需求发现, 多元推荐检查
- book-skill
- recommendation
- diversity
- algorithm
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p0g-diversity-rewrite-checklist
stage: p0g
source_book: AI rebuild product needs
source_chapter: 第7章 多元推荐改写-检查清单

---


# 多元推荐改写清单

## 一句话定位

检查推荐系统是真正多元，还是只是"加了点随机"。六项检查避免假多元。

## 何时触发

- 计划改写推荐系统
- 觉得当前推荐越来越窄
- 用户反馈"总是看到类似内容"
- 需要评估推荐系统的多元性

## 输入

当前推荐系统的目标和方案描述。

**示例输入**：
```
产品: 知识内容平台
目标: "把停留时长再做高一点"
当前方案: 增加相似内容推荐，加一点随机探索
```

## 输出

六项检查结果 + 改写建议 + 目标函数评估。

## 六项检查

### Check 1: 目标函数是否包含多样性或探索目标？

**检测方法**：
- 打开推荐系统的目标函数，看看除了停留时长/点击率/转化率，还有什么
- 是否有明确的多样性指标（如内容覆盖度、主题分散度、新内容曝光率）？
- 这些指标在优化目标中的权重是多少？

**输出格式**：
```
目标函数多样性: [yes/no/partial]
多样性指标: ["列表"]
权重: "多样性指标在总目标中的权重"
风险: "如果没有，会发生什么"
```

### Check 2: 用户能不能主动切换"更开阔"而不是"更精准"？

**检测方法**：
- 产品中是否有明确的"探索模式"或"开阔模式"？
- 用户是否能主动选择"我想看不一样的东西"？
- 还是只能被动接受系统给的推荐？

**输出格式**：
```
主动切换入口: [yes/no]
入口位置: "在哪里"
默认模式: "精准/开阔/混合"
用户控制感: [high/medium/low]
```

### Check 3: 系统有没有低冲突的异质内容入口？

**检测方法**：
- 推荐的"异质内容"是低冲突的（相关但不同视角），还是高冲突的（对立、争议）？
- 是否有"软过渡"设计，让用户自然接触新主题？
- 还是只是在熔炉里塞对立内容？

**输出格式**：
```
异质内容类型: [low_conflict/high_conflict/mixed]
过渡设计: [yes/no]
接触方式: "用户如何接触到异质内容"
```

### Check 4: 推荐有没有连接现实世界？

**检测方法**：
- 推荐内容是否能引导用户做出现实行动？
- 还是只是让用户在屏幕里花更多时间？
- 是否有"线上到线下"的连接设计？

**输出格式**：
```
现实连接: [yes/no/partial]
行动引导: "推荐是否能引导现实行动"
线下连接: [yes/no]
```

### Check 5: 团队有没有衡量"新的可能性被打开"？

**检测方法**：
- 团队的评估指标是不是只有点击率、停留时长？
- 是否有指标衡量用户是否接触了新主题、新领域？
- 是否有指标衡量用户的"视野是否变宽"？

**输出格式**：
```
多元性指标: [yes/no]
指标列表: ["具体指标"]
评估频率: "多久评估一次"
```

### Check 6: 用户能不能把自己从默认推荐轨迹里拉出来？

**检测方法**：
- 用户是否能够"重置"或"跳出"当前推荐轨迹？
- 是否有机制让用户主动表达"我不想看这个"？
- 系统是否会记住用户的"探索"偏好？

**输出格式**：
```
跳出机制: [yes/no]
跳出方式: "如何跳出"
用户主动权: [high/medium/low]
系统记忆: "是否记住探索偏好"
```

## 综合输出格式

```yaml
diversity_rewrite_assessment:
  input:
    product: "产品名称"
    current_goal: "当前目标"
    current_approach: "当前方案"
  
  checks:
    check1_objective:
      has_diversity_goal: "yes/no"
      diversity_metrics: ["指标"]
      weight: "权重"
      risk: "风险"
    
    check2_user_control:
      has_exploration_mode: "yes/no"
      entry_point: "入口"
      default_mode: "默认模式"
      user_control: "high/medium/low"
    
    check3_heterogeneous_content:
      conflict_level: "low_conflict/high_conflict/mixed"
      has_transition: "yes/no"
      exposure_method: "接触方式"
    
    check4_real_world:
      has_connection: "yes/no"
      action_guidance: "行动引导"
      offline_link: "yes/no"
    
    check5_measurement:
      has_diversity_metrics: "yes/no"
      metrics: ["指标"]
      review_frequency: "评估频率"
    
    check6_user_escape:
      has_escape: "yes/no"
      escape_method: "跳出方式"
      user_agency: "high/medium/low"
      system_memory: "yes/no"
  
  overall_assessment:
    is_truly_diverse: "yes/no/partial"
    fake_diversity_risk: "high/medium/low"
    key_gaps: ["关键缺口"]
  
  rewrite_recommendation:
    objective_changes: "目标函数改写建议"
    ui_changes: "界面改进建议"
    metric_changes: "评估指标改进建议"
    priority: "P0/P1/P2"
```

## 快速使用法

1. 填写产品、目标、当前方案
2. 逐项过六个检查
3. 如果超过 3 项不通过，推荐系统需要重写而不是优化

## 常见误判

- **加一点随机 = 多元**：随机探索不等于系统性多样性
- **内容更杂 = 更自由**：用户可能只是被塞了更多不相关的东西
- **点击更多 = 更好**：可能只是用户在翻找自己真正想看的

## 一句判断

> 多元推荐不是精度的对立面，而是对单一目标精度的修正。
