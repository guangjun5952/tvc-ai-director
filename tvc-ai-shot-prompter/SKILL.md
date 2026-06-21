---
name: tvc-ai-shot-prompter
description: TVC AI shot prompter for image and video generation. Use when Codex needs to create structured image prompts, Seedance-style video prompts, cinematic long-take video prompts, node-asset reference prompts, negative prompts, visual continuity rules, actor/product consistency, camera movement, lighting, color, duration, ratio, sound cue notes, regeneration instructions, or prompt tables for TVC storyboard shots.
---

# TVC AI Shot Prompter

Use this skill to convert storyboard shots into executable image prompts and video prompts.

The image prompt and video prompt use different methods:

- Image prompt: use the 8-layer still-image structure.
- Video prompt: use the Seedance-style video structure based on referenced materials, segmented timing, camera movement, audio, and product continuity.
- For complex single-shot cinematic action prompts, use the cinematic long-take structure in `references/video-prompt-method.md`: base assets, scene, sound, atmosphere/quality, visual tone, color, shot design, action chain, ending event, and negative constraints.

## Workflow

1. Create continuity anchors:
   - Brand/product identity.
   - Actor identity, wardrobe, makeup, hair.
   - Location, props, art direction.
   - Lighting, color, lens, camera behavior.
   - Reference assets and how to cite them with `@` when a video model supports material references.

2. Load prompt methods when needed:
   - Read `references/image-prompt-method.md` for still image prompts.
   - Read `references/video-prompt-method.md` for video prompts.

3. For each storyboard shot, write:
   - Image prompt using: Subject + Action + Environment + Composition + Camera + Lighting + Color + Style.
   - Video prompt using: reference material + duration/ratio + time-segmented action + camera movement + product/actor continuity + sound/music + negative constraints.
   - For prompts with multiple referenced characters, props, vehicles, creatures, or `node-asset` IDs, first create a `基础设定` block that locks each asset's identity, costume/material, behavior, and allowed expression/state changes.
   - Negative prompt.
   - Continuity lock.
   - Regeneration notes.

4. Keep prompts executable:
   - Use concrete visual facts instead of abstract emotions.
   - Write actions, not feelings.
   - Separate lighting from color palette.
   - Put style reference last.
   - Do not overload one shot with multiple unrelated events.

## Output Format

```markdown
全片一致性设定：
素材引用规则：
镜头 Prompt 表：
重生成策略：
下游交接：
```

Prompt table columns:

```markdown
| 镜号 | 图片 Prompt | 视频 Prompt | 负面约束 | 连续性锁定 | 重生成备注 |
| --- | --- | --- | --- | --- | --- |
```

## Image Prompt Method

Write still-image prompts in this order:

1. Subject.
2. Action.
3. Environment.
4. Composition.
5. Camera.
6. Lighting.
7. Color Palette.
8. Style Reference.

Do not start with style. Do not write abstract identity only. Describe visible traits, visible actions, and concrete cinematic grammar.

## Video Prompt Method

Use Seedance-style video prompt logic:

- State referenced assets with `@` when available, such as `@product_reference`, `@character_reference`, `@scene_reference`.
- Preserve native asset tags such as `<node-asset>...</node-asset>` when the target platform uses them. Describe what each asset controls immediately after the tag.
- Specify duration and aspect ratio.
- Break motion into time segments when the shot has a beginning, middle, and end.
- Describe camera movement, subject movement, product movement, and ending frame.
- Add sound, music, SFX, or silence cues when useful.
- For product shots, protect package shape, logo, label, material, and scale.
- For one-take action shots, separate `分镜`, `景别`, `构图`, `运镜手法`, and `画面内容` so the model gets both cinematography and event order.

## Prompt Quality Bar

- State what must remain identical across shots.
- Put product shape, logo visibility, and hand interaction rules in the prompt when relevant.
- Avoid impossible camera moves, contradictory light, and multiple time jumps in one generated shot.
- Negative prompts must block extra fingers, warped logos, unreadable text, face drift, product deformation, random subtitles, and unwanted style shifts.
- If a prompt says "失落", "高级", "清爽", or "电影感", translate it into visible action, composition, camera, light, color, or sound.
