---
name: multi-model-router
description: General routing readiness skill for multi-model, multi-agent, multi-skill, or multi-workflow systems. Use when Codex needs to decide which model, agent, specialist skill, tool, workflow stage, or execution path should handle a task, and must first identify required routing conditions, missing inputs, decision gates, user questions, defaults, or handoff criteria before routing.
---

# Multi Model Router

Use this skill before routing a task across multiple models, agents, specialist skills, tools, or workflow stages.

Core rule: do not route just because a downstream option exists. First identify what information is required to choose correctly. If required routing conditions are missing, ask the user before delegating.

## Routing Readiness Workflow

1. Define the routing universe:
   - What downstream options exist?
   - What is each option good at?
   - What inputs does each option require?
   - What are the failure modes if routed too early?

2. Build a routing gate:
   - Required facts: cannot route accurately without them.
   - Useful facts: improve quality but can be assumed.
   - Defaults: safe assumptions only if the user allows proceeding.
   - Stop conditions: cases where no route should be chosen yet.

3. Compare the user's input against the gate:
   - If required facts are present, route and explain why.
   - If required facts are missing, ask concise, numbered questions.
   - If the user explicitly accepts defaults, name the defaults before routing.

4. Route with a handoff:

```markdown
路由判断：
选择的下游：
为什么选择：
已满足条件：
缺失但已假设：
交接信息：
下游验收标准：
```

## Required Question Design

Ask questions that materially affect routing:

- Objective: what result is being optimized?
- Audience/user: who the output serves.
- Input assets: what materials are available.
- Constraints: time, format, channel, compliance, budget, platform, brand, legal.
- Quality bar: what "good" means.
- Execution mode: human, AI, hybrid, automated, manual.
- Risk tolerance: speed vs accuracy, creative freedom vs control.
- Delivery target: file, script, prompt, design, code, analysis, decision.

Do not ask questions that are merely nice to know.

## Routing Gate Template

```markdown
可选下游：
路由所需条件：
当前已知：
当前缺失：
必须先问：
可默认假设：
不能路由的原因：
回答后路由规则：
```

## Anti-Patterns

- Do not route from keywords alone when downstream choices require business context.
- Do not invent defaults for legal, brand, claim, customer, safety, finance, or delivery constraints.
- Do not ask a long questionnaire when one missing decision controls the route.
- Do not send a task to a creative/execution model before strategy-critical gates are answered.
- Do not continue a multi-step chain if an upstream gate is unresolved.

## Examples

Sparse TVC brief:
- Missing aspect ratio direction, channel, film duration, reference style, intended message, slogan, forbidden words, audience, actor permission, conversion goal.
- Stop at brief gate and ask before routing to concept.

Model choice for writing:
- Need audience, format, tone, length, source material, and factual-risk tolerance.
- If missing, ask before choosing short-form copywriter, long-form writer, editor, or fact-checker.

Design/code routing:
- Need target platform, existing code/design system, viewport, user workflow, and implementation vs mockup intent.
- If missing, ask before routing to design, frontend implementation, or review.

Data-analysis routing:
- Need data source, metric definition, time range, output format, and decision purpose.
- If missing, ask before routing to SQL, spreadsheet, charting, or narrative analysis.
