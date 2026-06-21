# Video Prompt Method

Use this method for video-generation prompts. It is adapted from the Seedance2 prompt-writing approach supplied by the user: material references, precise camera language, time-segmented motion, sound/music cues, and product continuity.

## Core Formula

```text
@Reference assets + Duration/ratio + Scene setup + Time-segmented action + Camera movement + Subject/product movement + Lighting/color continuity + Sound/music cues + Ending frame + Negative constraints
```

For high-complexity one-take action shots, use the expanded formula:

```text
基础设定 + 场景 + 声音 + 氛围与画质 + 视觉基调 + 色彩与影调 + 画面内容(分镜/景别/构图/运镜/动作链) + 结尾事件 + 负面约束
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

If the target platform uses native asset tags, keep them verbatim:

```markdown
机器人清道夫：<node-asset>...</node-asset>  controls body shape, costume, LED face display, expression state, and prop interaction.
场景：<node-asset>...</node-asset> controls architecture, street layout, background props, and environmental continuity.
```

For every asset, define:

- Identity and visible design.
- Material/costume/surface.
- Behavior range.
- Expression or state changes.
- What must never drift.

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

When the user requests production sound only, state it directly:

```markdown
声音：不需要配乐，不要氛围音，仅保留同期声。保留脚步、衣料摩擦、机械声、道具声、爆炸声、呼吸声或环境内真实声源。
```

## Product Continuity

For commercial shots:

- Keep product package identical to reference.
- Do not invent text or slogans.
- Keep logo readable when the shot's job is product recognition.
- Use post-composited real package when model text fidelity is risky.

## Cinematic Long-Take Prompt Pattern

Use this pattern when a video prompt contains many assets, a single continuous shot, precise cinematography, and a chain of actions. This structure is useful for TVC action scenes, character-driven product shots, and AI video models that respond well to long-form scene prompts.

### 1. 基础设定

Lock every reusable asset before describing the shot:

```markdown
【基础设定】

角色A：<node-asset>...</node-asset> 外形、时代风格、材质、服装、表情规则、可做动作、不可变化项。
角色B：<node-asset>...</node-asset> 外形、性格化特征、动作特征、不可变化项。
关键道具：<node-asset>...</node-asset> 尺寸、材质、启动方式、发光/变形/爆炸等状态变化。
群体角色：<node-asset>...</node-asset> 数量感、外观、运动方式、危险感、不可变化项。
```

Rules:

- Use concrete visible facts, not abstract labels only.
- If a face is a screen, define whether expressions are static or animated.
- If a prop changes state, write the state chain in order.
- If a character has a comic or ugly trait, describe visible features precisely.

### 2. 场景

Define world, period, location, weather, background activity, and set dressing:

```markdown
场景：<node-asset>...</node-asset> 时代、城市/室内/荒野、危机状态、建筑语言、地面材质、道具散落、尸体/车辆/报纸/烟尘等环境细节。
```

Rules:

- Treat the environment as a story engine, not wallpaper.
- Include foreground, midground, background responsibilities when the shot needs depth.
- Put continuity objects here if they must remain across shots.

### 3. 声音

Define music, ambience, and sync sound separately:

```markdown
声音：不需要配乐；不要氛围音；仅保留同期声：脚步、机械关节、道具按钮、风声、爆炸、角色叫声。
```

Rules:

- If no music is wanted, say so explicitly.
- Do not add mood music if the user asks for production sound only.
- Use sound to support the action chain.

### 4. 氛围与画质

Define genre, realism, texture, and blocked aesthetics:

```markdown
【氛围与画质】
风格核心：原子朋克、末日危机、电影级质感、超写实、真人实景拍摄感。
画质要求：Photorealism, ultra realistic, no game CGI look, no stiff slow motion unless requested.
情绪目标：逃亡、追逐、危机感、紧迫感。
```

Rules:

- Put negative style constraints here when they affect the whole shot.
- Translate broad style words into texture, realism, camera, or motion rules.

### 5. 视觉基调

Define camera system, lens family, format, and motion rendering:

```markdown
视觉基调：anamorphic widescreen cinematic look, IMAX film camera feel, Panavision C-series lens character, shallow depth of field, telephoto compression, natural motion blur.
```

Rules:

- Use camera and lens grammar only when it changes the image.
- Do not stack incompatible camera formats.
- State motion blur when high-speed action is essential.

### 6. 色彩与影调

Separate color from lighting:

```markdown
色彩与影调：1960s retro-futurist atom-punk palette, warm orange and sea-salt blue contrast, low-saturation vintage film filter, film grain, strong direct sunlight, natural sun flare, preserved highlight detail, readable shadow detail.
```

Rules:

- Lighting = source and behavior of light.
- Color = palette, saturation, film stock feel, contrast.
- Avoid overexposure if product or character identity matters.

### 7. 画面内容

Break the shot into production grammar before writing the action:

```markdown
【画面内容】

分镜：单镜头一镜到底。
景别：近景，浅景深，长焦压缩空间。
构图：前景主体位于画面右侧，占画面二分之一；背景追击群体位于左侧远处；主体与街道形成动态对角线。
运镜手法：固定机位，跟随拍摄主体。
画面内容：按时间顺序写动作链、道具状态变化、追击关系、爆炸/冲击/失焦等结尾事件。
```

Rules:

- Keep `分镜`, `景别`, `构图`, `运镜手法`, and `画面内容` as separate fields.
- For single-shot prompts, action order must be unambiguous.
- Every prop interaction should include hand, object, trigger, state change, and consequence.
- Ending event should specify what happens to the camera image: shake, blur, focus loss, hard cut, object exits frame.

### 8. 负面约束

End with global and shot-specific negative constraints:

```markdown
负面约束：不要游戏CG感，不要动作迟钝僵硬，不要角色身份漂移，不要错误服装，不要错误道具形状，不要随机字幕，不要过曝，不要镜头无意义乱晃，不要额外角色抢主体。
```

## Long-Take Template

```markdown
【基础设定】
角色/主体1：<node-asset>...</node-asset> ...
角色/主体2：<node-asset>...</node-asset> ...
关键道具：<node-asset>...</node-asset> ...
群体/背景角色：<node-asset>...</node-asset> ...

场景：<node-asset>...</node-asset> ...
声音：...

【氛围与画质】
风格核心：
视觉基调：
色彩与影调：

【画面内容】
分镜：
景别：
构图：
运镜手法：
画面内容：

负面约束：
```

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
