---
name: tvc-ai-director
description: TVC AI director studio router for advertising film workflows. Use when Codex needs to plan, route, or coordinate TVC/commercial/brand film/product film work across brief diagnosis, creative proposal, director treatment, PPM, storyboard, AI image/video prompting, AI production, editing, client review feedback, revisions, delivery, or any Chinese advertising-film production task.
---

# TVC AI Director

Use this skill as the main router for a TVC AI production studio. Determine the project stage, identify missing information, choose the right `tvc-*` specialist skill, and preserve handoff context across stages.

For any broader multi-model or multi-skill routing problem, apply the same readiness-gate logic as `$multi-model-router`: identify the required routing conditions first, ask for missing conditions, then route.

Default stance:

- Output in Chinese unless the user asks otherwise.
- Prioritize AI production execution while keeping real advertising-studio standards for proposal, PPM, review, and delivery.
- Treat every output as something another specialist can continue from.
- Confirm aspect ratio direction at the front of the workflow.
- When client input is sparse, ask the required brief gate questions before routing into creative work.
- Do not route to concept, treatment, storyboard, prompt, production, or editing until aspect ratio and the required brief gate are answered or the user explicitly says to proceed with defaults.

## Routing Workflow

1. Classify the user request into one or more stages:
   - Brief and strategy: use `$tvc-brief-strategist`.
   - Creative concept and proposal: use `$tvc-concept-developer`.
   - Director treatment: use `$tvc-director-treatment`.
   - PPM and production pack: use `$tvc-ppm-producer`.
   - Shot script and storyboard table: use `$tvc-storyboard-writer`.
   - AI image/video prompts: use `$tvc-ai-shot-prompter`.
   - Storyboard/prompt Excel workbook: use `$tvc-storyboard-writer` + `$tvc-ai-shot-prompter`, then export with `scripts/make_tvc_excel.py` or a spreadsheet tool.
   - AI production coordination: use `$tvc-ai-production-coordinator`.
   - Edit rhythm, sound, packaging, delivery: use `$tvc-editing-director`.
   - Client feedback and revision parsing: use `$tvc-client-review-interpreter`.

2. Apply the sparse-brief gate:
   - If the user only provides a product image, product name, rough category, or one-line request, stop at brief diagnosis.
   - Ask the required questions in `Required Brief Gate`.
   - Aspect ratio is the first gate. Do not assume horizontal or vertical from platform alone.
   - Do not generate creative routes, director treatment, storyboard, AI prompts, or edit plans before the gate is answered.
   - If the user explicitly asks to proceed without answers, state that defaults are being used and list those defaults before routing.

3. Apply the general routing gate:
   - Before choosing any specialist, identify what conditions are required to route accurately.
   - If a missing condition changes the downstream specialist, output questions instead of routing.
   - If all required conditions are present, route with a short reason and handoff.

4. If the request spans stages and the brief gate is complete, create an execution chain before working:
   - Example: `brief -> concept -> treatment -> storyboard -> AI prompt -> production -> editing -> review`.
   - Run the current highest-leverage stage first unless the user names a specific deliverable.

5. Load shared references only when needed:
   - `references/tvc-workflow-map.md`: stage map, routing triggers, handoff format.
   - `references/tvc-quality-bar.md`: quality checks for strategy, craft, AI continuity, review, delivery.
   - `references/category-playbooks.md`: category-specific defaults.
   - `references/prompt-style-guide.md`: image/video prompt discipline.
   - `references/client-communication.md`: client-facing language and feedback interpretation.

6. Use this universal handoff format for multi-stage work:

```markdown
项目背景：
当前阶段：
已知信息：
关键假设：
待补信息：
本阶段产物：
下游注意事项：
建议下一步：
```

## Router Decision Rules

- If the brief is vague, do not jump to scripts or creative routes. Diagnose the brief and ask the required brief gate questions.
- If route choice depends on missing context, ask the routing-gate questions before delegating to another `tvc-*` skill.
- If the user asks for "提案", "创意", "方向", "方案", route to concept after brief diagnosis.
- If the user asks for "导演阐述", "影调", "镜头语言", "参考片", route to treatment.
- If the user asks for "PPM", "演员", "服装", "美术", "音乐参考", "拍摄准备", route to PPM.
- If the user asks for "分镜", "镜头脚本", "shot list", route to storyboard.
- If the user asks for "prompt", "AI生成", "生图", "生视频", "可灵", "Runway", "Midjourney", route to AI shot prompter and production coordinator.
- If the user asks for "Excel", "表格", "xlsx", "分镜表", "prompt表", "生成表格", or asks to put storyboard/prompts into a spreadsheet, route through storyboard + AI shot prompter and export a workbook.
- If the user asks for "剪辑", "节奏", "音乐", "声音", "包装", "交付", route to editing.
- If the user pastes client comments, route to review interpreter before editing.

## Required Brief Gate

When client information is sparse, ask these questions before creative routing:

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

Output only:

```markdown
当前信息判断：
为什么需要补充：
请先确认以下问题：
1. ...
```

## Output Rules

- Be production-practical: tables, lists, scripts, prompts, and revision matrices should be directly usable.
- Preserve brand, product, actor, wardrobe, prop, location, light, and color continuity.
- For AI prompts, include duration, ratio, camera, subject, product, motion, lighting, tone, sound cue if relevant, and negative constraints.
- For client-facing text, separate internal diagnosis from external wording.
- End with a concrete next-stage handoff when the task is part of a chain.

## Templates and Tools

- Use `assets/templates/` when the user needs copyable tables for brief, proposal, treatment, PPM, storyboard, prompt, edit, or review.
- Use `scripts/make_tvc_tables.py` when converting structured Markdown-like rows into CSV for Excel or spreadsheet workflows.
- Use `scripts/make_tvc_excel.py` when converting a TSV storyboard/prompt table into a lightweight `.xlsx` workbook without external dependencies.
- For polished multi-sheet `.xlsx` workbooks, prefer the available spreadsheet runtime/tooling; include at minimum:
  - `分镜+Prompt` sheet with shot timing, frame content, camera, product/logo, sound, image prompt, video prompt, negative constraints, continuity lock, and regeneration notes.
  - `全片一致性` sheet with product, actor, location, color, camera, and forbidden-drift anchors.
  - `执行检查清单` sheet for production/AI-generation QA.

## Quality Gate

Before finalizing, check:

- Does the output match the user's current stage?
- Are missing assumptions named instead of hidden?
- Can the next `tvc-*` skill continue from the handoff?
- Does the plan protect actor/product continuity for AI generation?
- Are client review items translated into actionable production changes?
