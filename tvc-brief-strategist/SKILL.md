---
name: tvc-brief-strategist
description: TVC brief strategist for diagnosing advertising film briefs and shaping strategy. Use when Codex needs to parse a client brief, identify missing brand/product/audience/channel/budget/timeline constraints, define the communication task, find proposal angles, or prepare strategic inputs before TVC creative development.
---

# TVC Brief Strategist

Use this skill to turn an incomplete TVC request into a strategic brief that creative, treatment, storyboard, and AI production work can use.

## Workflow

1. Extract known facts:
   - Brand, product, category, target audience, business goal, communication task.
   - Required duration, ratio, channels, deadline, budget level, mandatories, forbidden elements.
   - Product claims, proof points, competitors, brand tone, existing assets, reference films.

2. Diagnose gaps:
   - Mark each gap as `must ask`, `can assume`, or `not needed yet`.
   - If the client only provides a product image, product name, rough category, or one-line request, treat the brief as sparse.
   - For sparse briefs, ask the required brief gate questions before proposing creative directions.
   - Confirm aspect ratio direction first: horizontal, vertical, or both.
   - Do not route to `$tvc-concept-developer` until the required brief gate is answered or the user explicitly approves defaults.

3. Define the strategic frame:
   - One-sentence task: "这支片要让谁在什么场景下相信什么，并采取什么行动。"
   - Core tension: user pain, desire, category convention, social mood, or brand opportunity.
   - Creative territory: 2-4 proposal directions, each with audience insight, product role, tone, and risk.

4. Output in this format:

```markdown
Brief 诊断：
关键信息：
待补信息：
策略判断：
创意方向：
下游交接：
```

## Required Brief Gate

For sparse briefs, ask these questions exactly before creative work:

1. 画幅方向先确认：横屏、竖屏，还是横竖都要？
2. 投放渠道偏好是什么？
3. 希望成片时长是多长？
4. 有没有想要参考的风格？
5. 有没有已经想好的、想要表达的内容？
6. 品牌 slogan 是什么？
7. 禁用词有哪些？
8. 目标人群是谁？
9. 是否可以使用真人演员？
10. 是否要承担电商转化目标？

Use this output format:

```markdown
Brief 信息不足：
目前只知道：
暂时不能进入创意的原因：
请先确认以下问题：
1. 画幅方向先确认：横屏、竖屏，还是横竖都要？
2. 投放渠道偏好是什么？
3. 希望成片时长是多长？
4. 有没有想要参考的风格？
5. 有没有已经想好的、想要表达的内容？
6. 品牌 slogan 是什么？
7. 禁用词有哪些？
8. 目标人群是谁？
9. 是否可以使用真人演员？
10. 是否要承担电商转化目标？
```

## Quality Bar

- Do not write final scripts before the communication task is clear.
- Do not generate creative routes from sparse briefs before the required brief gate is answered.
- Separate product truth from emotional promise.
- Keep proposal directions meaningfully different, not cosmetic variations.
- Name legal, claim, talent, product, or channel risks early.
