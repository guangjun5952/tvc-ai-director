# Video Prompt Method

Use this method for video-generation prompts. It is adapted from the Seedance2 prompt-writing approach supplied by the user: material references, precise camera language, time-segmented motion, sound/music cues, and product continuity.

## Core Formula

```text
@Reference assets + Duration/ratio + Scene setup + Time-segmented action + Camera movement + Subject/product movement + Lighting/color continuity + Sound/music cues + Ending frame + Negative constraints
```

## Reference Assets

When the video model supports material references, name assets with `@`:

- `@product_reference`: product bottle, package, logo, packshot.
- `@character_reference`: actor/persona consistency.
- `@wardrobe_reference`: outfit consistency.
- `@scene_reference`: location/world.
- `@style_reference`: visual tone.

Explain what each reference controls:

```markdown
@product_reference: only controls bottle shape, package color, label layout, logo position, and material.
@character_reference: controls face, hairstyle, wardrobe, and body proportion.
```

## Time Segments

Use segments when a shot has progression:

```text
0-1s: starting frame/action.
1-3s: main movement.
3-4s: ending frame or transition state.
```

This prevents vague prompts like "the scene becomes energetic".

## Camera Movement

Use precise terms:

- slow push-in
- handheld follow shot
- locked-off macro close-up
- orbit around product
- low-angle dolly-in
- whip pan
- rack focus from product to face
- top-down product reveal

Avoid:

- cinematic movement
- dynamic shot
- cool camera

## Subject and Product Movement

Describe what moves:

- actor turns head, lowers eyes, opens bottle, takes one sip
- condensation rolls down bottle
- tea liquid catches sunlight
- orange heat-wave ribbons spiral into bottle mouth
- product remains centered and readable

## Sound and Music

Include only useful audio cues:

- bottle cap click
- reverse whoosh
- ice crack
- low city rumble
- music beat enters at 2s
- short silence before product reveal

## Product Continuity

For commercial shots:

- Keep product package identical to reference.
- Do not invent text or slogans.
- Keep logo readable when the shot's job is product recognition.
- Use post-composited real package when model text fidelity is risky.

## Video Prompt Template

```markdown
生成 <duration> 秒 <ratio> TVC 视频镜头。
参考素材：
- @product_reference: ...
- @character_reference: ...

画面设定：
0-1s：
1-3s：
3-<duration>s：

镜头运动：
主体动作：
产品动作：
光影与色彩：
声音/音乐：
结束画面：
连续性要求：
负面约束：
```

## Negative Constraints

Always block:

- face drift
- identity change
- extra fingers
- warped hands
- deformed product
- wrong logo
- hallucinated text
- random subtitles
- flicker
- camera jitter
- object melting
- inconsistent lighting
- stock footage look
- unrelated props
