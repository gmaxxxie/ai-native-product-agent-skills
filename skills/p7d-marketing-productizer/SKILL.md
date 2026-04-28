---
name: p7d-marketing-productizer
version: 1.0.0
description: 营销产品化设计器。基于《AI Native 营销与增长》营销产品化概念卡， 帮助产品将营销活动设计为产品功能，让用户在使用中自然完成"被营销"。
author: Max
tags: p7, 营销增长, 营销产品化
- book-skill
- marketing-productization
- plg
- growth
- ai-product
requires: []
homepage: https://github.com/gmaxxxie/ai-native-product-agent-skills/tree/main/skills/p7d-marketing-productizer
stage: p7d
source_book: AI Native 营销与增长
source_chapter: 第05章 营销产品化

---


# 营销产品化设计器

## 一句话定位

把营销活动变成产品功能——让用户在使用中自然完成"被营销"，而不是被打断。

## 何时触发

- 广告投放成本持续上升，ROI 下降
- 想从 PLG 进化到"营销即产品"
- 需要设计自传播、自增长的产品机制
- 传统营销方式与产品体验矛盾

## 输入

产品场景 + 当前营销方式 + 增长瓶颈。

**示例输入**：
```
产品: AI 设计工具
当前营销: 投放广告 + KOL 合作
增长瓶颈: 获客成本 $50，LTV $80，边际利润太薄
```

## 设计流程

### Step 1: 营销动作识别

**任务**：识别当前营销中哪些动作可以产品化。

```
传统营销动作 → 产品化方向:

广告投放 → 产品内推荐位
KOL 合作 → 用户生成内容/模板市场
邮件营销 → 产品内消息/智能提醒
促销活动 → 产品内成就/解锁机制
案例推广 → 产品内社区/展示墙
邀请有礼 → 产品内协作/分享功能
```

### Step 2: 产品化路径设计

**任务**：为每个营销动作设计产品化路径。

```
路径 1: 内容即营销
  - 用户使用产品时产生内容
  - 内容自动带品牌水印/链接
  - 内容被分享后，新用户自然触达
  - 示例: Notion 模板、Figma 社区

路径 2: 协作即传播
  - 产品天然需要多人协作
  - 每次邀请协作就是一次获客
  - 示例: Google Docs 分享、Figma 协作

路径 3: 数据即推荐
  - 用户使用数据自动优化推荐
  - 推荐本身就是增长手段
  - 示例: Spotify 年度回顾、Duolingo 打卡

路径 4: 成就即传播
  - 用户完成里程碑时自动生成分享内容
  - 分享内容带产品入口
  - 示例: 健身 App 完成挑战、游戏通关
```

### Step 3: 飞轮验证

**任务**：验证产品化营销是否形成自增强飞轮。

```
飞轮验证:
  Q1: 用户使用产品是否自然产生可分享内容？ → 是/否
  Q2: 分享内容是否自然引导新用户进入？ → 是/否
  Q3: 新用户使用是否自然产生更多内容？ → 是/否
  Q4: 循环是否可以自运转（不依赖广告预算）？ → 是/否
```

### Step 4: 启动策略

**任务**：设计冷启动策略，让飞轮从静止开始转动。

```
冷启动:
  阶段 1 (0-1000 用户): 
    - 手动引导核心用户生成内容
    - 精心设计首批分享模板
  阶段 2 (1000-10000):
    - 优化分享体验，降低分享门槛
    - 建立内容质量筛选机制
  阶段 3 (10000+):
    - 飞轮自转，减少广告投入
    - 专注提升内容质量和分享率
```

## 综合输出格式

```yaml
marketing_productization:
  input:
    product: "产品名称"
    current_marketing: "当前营销方式"
    bottleneck: "增长瓶颈"
  
  conversion_map:
    - traditional: "传统营销动作"
      productized: "产品化方向"
      effort: "低/中/高"
      impact: "低/中/高"
  
  chosen_path:
    path: "选择的产品化路径"
    why: "为什么选这条路径"
    key_mechanism: "核心机制"
  
  flywheel:
    user_action: "用户行为"
    content_generated: "产生的内容"
    sharing_mechanism: "分享机制"
    new_user_entry: "新用户入口"
    self_sustaining: "是否可自运转"
  
  cold_start:
    phase1: "0-1000 用户策略"
    phase2: "1000-10000 策略"
    phase3: "10000+ 策略"
  
  metrics:
    primary: "有机获客占比"
    secondary: ["分享率", "内容生成率", "新用户转化率"]
```

## 常见误判

- **强行产品化**：不是所有营销都适合产品化，强行做会伤害体验
- **忽视冷启动**：飞轮需要外力启动，不会自己转起来
- **内容质量失控**：UGC 没有筛选机制，低质量内容反而伤害品牌

## 一句判断

> 最好的营销不是让用户看到广告，而是让用户使用产品时自然成为传播节点。
