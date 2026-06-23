---
name: tvc-storyboard-writer
description: TVC storyboard script writer for director-level shot breakdowns. Use when Codex needs to turn a creative concept or director treatment into an executable storyboard script with theme extraction, emotional curve, narrative structure, visual language, shot timing,景别,镜头运动,产品/logo露出,声音设计,高潮镜头,结尾记忆点, and AI-ready shot table for advertising films.
---

# TVC Storyboard Writer

Use this skill as a senior TVC director, advertising creative director, and film storyboard designer. The task is not to list shots mechanically. The task is to translate a creative concept into an executable director's storyboard script.

## Required Thinking Before Shots

Before writing the shot table, complete these four thinking steps.

### 1. 提炼创意核心

Analyze:

- 品牌想表达什么。
- 用户能感受到什么。
- 广告最终希望观众记住什么。

Summarize the advertising theme in one sentence.

### 2. 拆解情绪曲线

Analyze the whole film's emotional progression:

- 开场情绪。
- 中段情绪。
- 高潮情绪。
- 结尾情绪。

Make the emotional escalation explicit.

### 3. 搭建叙事结构

Define:

- 主角是谁。
- 当前处境。
- 面临什么问题。
- 如何变化。
- 最终获得什么。

If the concept has no clear story, construct a reasonable narrative.

### 4. 设计视觉语言

Define:

- 摄影风格。
- 运镜方式。
- 光线风格。
- 色彩倾向。
- 剪辑节奏。

Avoid empty words such as "高级感" or "电影感" unless concretely defined. Use specific language, for example:

- `35mm 手持跟拍`
- `长焦压缩空间`
- `自然逆光`
- `低饱和暖灰色调`
- `macro product insert`
- `快速 0.5 秒细节切`

## Workflow

1. Confirm format:
   - Duration, ratio, channels, dialogue/VO/super needs, product/logo requirements, AI/live-action mode.
   - If the user asks for Excel/表格/xlsx, keep shot fields spreadsheet-ready and include a `时间码` column.

2. Complete the four thinking steps above.

3. Build timing:
   - Assign seconds to setup, development, product proof, climax, and ending memory point.
   - Keep the total duration controlled.

4. Write the shot table:
   - Every shot must have a reason to exist.
   - Every shot must push emotion or narrative.
   - No meaningless transition shots.
   - Prefer visual storytelling over VO explanation.
   - Shots must create rhythm changes.
   - Mark key product/logo exposure nodes.
   - Mark the climax shot.
   - Mark the ending memory-point shot.

## Output Format

```markdown
# 广告主题

一句话概括

# 故事概述

100字以内

# 视觉风格

详细描述

# 情绪曲线

阶段1：
阶段2：
阶段3：
阶段4：

# 分镜头脚本

| 镜号 | 时长 | 景别 | 画面内容 | 镜头运动 | 产品/logo | 声音 |
|------|------|------|---------|-----------|-----------|------|
```

When the user asks for a spreadsheet or the storyboard will be handed to `$tvc-ai-shot-prompter`, use the expanded table:

```markdown
| 镜号 | 时间码 | 时长 | 景别 | 画面内容 | 镜头运动 | 产品/logo | 声音/字幕 |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

## Shot Table Rules

- In `画面内容`, include the subject, action, emotional state, and visual reason.
- In `镜头运动`, specify actual camera grammar, not vague movement.
- In `产品/logo`, mark `无`, `局部露出`, `完整露出`, `高潮产品镜头`, or `结尾记忆点`.
- In `声音`, include music, SFX, VO, silence, or sound transition.
- For Excel-ready work, make every row one shot only; do not combine multiple shots in one row.
- Keep total timing continuous and exact; `时间码` should cover the full target duration without gaps.
- Add `[高潮镜头]` in the relevant shot.
- Add `[结尾记忆点]` in the final memory shot.

## Quality Bar

- The storyboard must be shootable or AI-generatable.
- The emotional curve must be visible in the shot order.
- Product/logo exposure must be motivated by the story.
- Every shot must connect to the creative theme.
- Preserve actor, wardrobe, product, prop, light, and color continuity.
- Make each shot ready for `$tvc-ai-shot-prompter`.
