---
name: tvc-client-review-interpreter
description: TVC client review interpreter for decoding feedback and revisions. Use when Codex needs to analyze client审片意见, distinguish surface comments from real intent, classify mandatory vs negotiable changes, translate vague feedback into edit/prompt/PPM actions, prepare response language, or produce revision execution tables for advertising films.
---

# TVC Client Review Interpreter

Use this skill before changing an edit, prompt, script, or treatment based on client feedback.

## Workflow

1. Parse every comment:
   - Literal request.
   - Likely underlying concern.
   - Affected asset: script, shot, AI prompt, edit, music, VO, packshot, claim, legal, brand tone.

2. Classify:
   - Must change.
   - Can negotiate.
   - Need clarification.
   - Risky or contradictory.

3. Translate into actions:
   - Editing action.
   - Prompt regeneration action.
   - Script/super/VO action.
   - Client response wording.

4. Preserve relationship:
   - Acknowledge the concern.
   - Offer a production-safe interpretation.
   - Ask precise questions only where ambiguity blocks execution.

## Output Format

```markdown
反馈原文：
真实意图判断：
修改优先级：
执行动作表：
需追问问题：
客户回复建议：
下游交接：
```

## Quality Bar

- Never treat vague feedback as literal too quickly.
- Identify contradictions between comments.
- Convert emotional words like "高级", "太平", "不够冲击", "不像我们品牌" into concrete craft levers.
- Protect schedule, continuity, product accuracy, and approval traceability.
