---
name: tvc-ai-production-coordinator
description: TVC AI production coordinator for managing generated-video execution. Use when Codex needs to plan AI production batches, prepare reference assets, manage actor/product continuity, version naming, shot status, regeneration decisions, quality control, tool handoffs, missing material lists, or production schedules for AI-made TVCs.
---

# TVC AI Production Coordinator

Use this skill to manage the practical execution of AI-generated TVC shots.

## Workflow

1. Build the production map:
   - Shot list, priority, dependencies, assets needed, tool target, status.

2. Prepare materials:
   - Product reference, actor reference, wardrobe reference, location/style references, logo/packshot assets, audio references.

3. Control continuity:
   - Assign anchors for actor face, wardrobe, product, props, lighting, color, aspect ratio, camera grammar.
   - Track which shots reuse which references.

4. Manage generations:
   - Batch shots by scene, character, location, or product setup.
   - Define version names, acceptance criteria, reject reasons, regeneration instructions.

## Output Format

```markdown
制作批次：
物料准备：
连续性锁定：
镜头状态表：
返工规则：
下游交接：
```

## Quality Bar

- Generate hero product, face, and hand-interaction shots with the strictest references.
- Do not let a beautiful shot pass if it breaks continuity or product truth.
- Keep version naming simple enough for editing and client review.
