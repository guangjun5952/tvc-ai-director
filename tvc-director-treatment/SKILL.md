---
name: tvc-director-treatment
description: TVC director treatment and visual development skill for advertising films. Use when Codex needs to produce rich director statements, image style, camera language, rhythm, performance/persona design, character turnaround prompts, scene design, art direction, lighting, product presentation, music/sound mood, reference analysis, GPT Image 2 visual-generation prompts, or client-facing treatment decks for a TVC.
---

# TVC Director Treatment

Use this skill to translate an approved creative concept into a rich director treatment and visual development package.

The output should explain both:

- Why this execution expresses the creative idea.
- What visual evidence the client can see before production.

## Core Stance

- Write as a director speaking to a client, not as a production checklist.
- Be richer than a short style note: include emotion, image logic, camera grammar, performance, world, product, rhythm, sound, and visual proof.
- Use image generation as a treatment tool. For every major visual section, write a GPT-Image2-ready prompt and generate the corresponding image by default when image tools are available.
- Only skip image generation when the user explicitly asks for text/prompts only, or when the current environment cannot generate images.
- Keep generated visuals as references for approval, not final production frames unless the user asks.

## Workflow

1. Confirm inputs:
   - Approved creative idea or proposal route.
   - Product truth, audience, channel, duration, visual references, actor policy, and AI/live-action mode.
   - If these are missing and affect treatment direction, route back to `$tvc-brief-strategist` or `$tvc-concept-developer`.

2. Load visual development guidance when images are needed:
   - Read `references/visual-development.md`.
   - Use it to create visual deliverables and image-generation prompts.

3. Build the treatment:
   - Director statement.
   - Film promise and emotional arc.
   - Image style and color system.
   - Camera language and lens/movement grammar.
   - Rhythm and edit feeling.
   - Performance and persona design.
   - Scene/world design.
   - Product presentation.
   - Art direction, lighting, texture.
   - Music and sound.
   - Reference and visual development plan.

4. Generate visual assets for each major section:
   - Image style reference.
   - Camera language reference.
   - Performance/persona design, including character three-view when relevant.
   - Scene setting image.
   - Product presentation image.
   - Lighting/color mood image.
   - Key visual or hero frame.
   - For each asset, output the GPT-Image2 prompt, generate the image, show it inline, and preserve the prompt used.

5. Hand off to:
   - `$tvc-ppm-producer` for PPM expansion.
   - `$tvc-storyboard-writer` for shot-by-shot structure.
   - `$tvc-ai-shot-prompter` if visual prompts need per-shot conversion.

## Output Format

```markdown
## 导演阐述

## 影像风格
- 文字阐述：
- 视觉参考图 / GPT Image 2 Prompt：

## 镜头语言
- 文字阐述：
- 视觉参考图 / GPT Image 2 Prompt：

## 节奏与情绪曲线
- 文字阐述：
- 视觉参考图 / GPT Image 2 Prompt：

## 表演与人物形象设计
- 文字阐述：
- 人物三视图 / GPT Image 2 Prompt：

## 场景设定
- 文字阐述：
- 场景设定图 / GPT Image 2 Prompt：

## 产品呈现
- 文字阐述：
- 产品呈现图 / GPT Image 2 Prompt：

## 美术、光影与色彩
- 文字阐述：
- 光影色彩参考图 / GPT Image 2 Prompt：

## 音乐与声音

## 视觉开发清单

## 下游交接
```

## Image Generation Rules

- Generate images by default for the visual sections when image tools are available.
- If the user asks for prompts only, do not generate images.
- If image tools are unavailable or blocked, provide GPT Image 2-ready prompts and explicitly state that image generation was not executed.
- For OpenAI image API implementation details, use `$openai-docs` when current API syntax matters.
- For normal in-chat image generation, use `$imagegen` behavior when available.
- Do not invent exact brand packaging details not present in the provided product reference.
- For product images, require reference-image fidelity and block logo/text hallucination.
- For character three-view, specify front, side, back views on one clean sheet, consistent wardrobe and face, neutral pose.
- For multiple treatment images, generate one asset per prompt rather than asking for a single collage unless the section specifically needs a beat-board or three-view sheet.

## Quality Bar

- Every visual choice must serve the creative idea and audience psychology.
- Treatment writing must explain "why this visual language", not merely list adjectives.
- Each generated/reference image must answer a client question.
- Preserve continuity for later storyboard and AI prompting.
- Product presentation must protect shape, logo, package color, material, and scale.
- Character/persona design must match audience and avoid celebrity likeness unless explicitly approved.
