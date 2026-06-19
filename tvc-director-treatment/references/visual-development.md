# Director Treatment Visual Development

Use this reference when a director treatment needs generated images, moodboards, key visuals, character designs, or product presentation references.

Default behavior: write the GPT-Image2 prompt and generate the image for each visual deliverable when image tools are available. If image generation cannot run, output the prompt and mark the image as pending generation.

## Visual Asset Map

| Treatment section | Image deliverable | Purpose |
| --- | --- | --- |
| Image style | Style frame / mood frame | Show overall tone, color, texture, and atmosphere |
| Camera language | Cinematic frame reference | Show lens, framing, depth, movement feeling |
| Rhythm/emotion | Beat-board strip or contrast pair | Show before/after emotional transition |
| Performance/persona | Character design + three-view | Align casting, styling, makeup, wardrobe, posture |
| Scene setting | Environment concept image | Align location, time, art direction, props |
| Product presentation | Hero product frame | Align packshot, texture, hand interaction, logo visibility |
| Light/color | Lighting mood frame | Align color contrast, key light, shadow, highlight |
| Key visual | Campaign hero image | Align the single most memorable visual idea |

## GPT Image 2 Prompt Pattern

Use this structure for each visual:

```markdown
用途：
画幅：
主体：
场景：
动作/状态：
构图：
镜头语言：
光影色彩：
美术与材质：
品牌/产品要求：
风格关键词：
负面约束：
```

## Image Style Reference Prompt

```text
Create a high-end TVC director treatment style frame.
The image should communicate the film's overall visual tone, color palette, atmosphere, and emotional texture.
Do not create a final storyboard shot; create a mood-defining reference frame for client approval.
```

## Camera Language Reference Prompt

```text
Create a cinematic frame that demonstrates lens language, framing, depth of field, and camera attitude for a TVC.
Emphasize how the camera makes the product or character feel, not only what is visible.
```

## Character Three-View Prompt

```text
Create one clean character design sheet with front, side, and back views of the same person.
Neutral standing pose, consistent face, hairstyle, makeup, wardrobe, body proportion, and color palette.
Commercial casting reference style, not fashion illustration, not celebrity likeness.
Plain light background, no text unless requested.
```

## Scene Setting Prompt

```text
Create a TVC environment concept image for a director treatment.
Show the location, time of day, art direction, props, atmosphere, and practical shooting/AI-generation feasibility.
The scene should support the creative concept and audience psychology.
```

## Product Presentation Prompt

```text
Create a premium TVC product presentation reference.
The product must match the provided reference image in shape, package color, label layout, logo position, material, and scale.
Show texture, condensation, hand interaction, or hero packshot logic as requested.
Avoid hallucinated text, distorted logos, wrong packaging, extra products, or unreadable labels.
```

## Key Visual Prompt

```text
Create a campaign key visual for the TVC concept.
It should combine the core insight, product role, visual metaphor, and emotional promise in one memorable image.
Composition should be suitable for proposal deck and social campaign adaptation.
```

## Output Discipline

- Label each visual by section.
- Explain why the image is needed.
- By default, generate each image, show it inline, and preserve the prompt used.
- If only preparing prompts because the user requested prompt-only output or tools are unavailable, make prompts detailed enough for direct batch generation.
- Keep references and generated images separate from final storyboard frames.
