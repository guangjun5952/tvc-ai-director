# Prompt Style Guide

Use for AI-generated TVC images and videos.

## Global Continuity Block

Write this before per-shot prompts:

- Brand/product: name, package, color, logo visibility, surface, scale.
- Actor: age range, face features, hair, makeup, wardrobe, expression range.
- World: location, time, art direction, props, weather, atmosphere.
- Camera: lens family, shot grammar, movement limits.
- Light/color: key light, contrast, color palette, texture.
- Forbidden drift: face changes, product deformation, extra text, random logos.

## Image Prompt Pattern

```markdown
生成一张 16:9 TVC 分镜关键帧：
主体：
产品：
场景：
动作瞬间：
构图：
镜头/焦段：
光影：
影调：
质感：
画面不出现：
```

## Video Prompt Pattern

```markdown
生成 4 秒 16:9 TVC 视频镜头：
起始画面：
主体动作：
产品动作：
镜头运动：
光影变化：
节奏：
结束画面：
声音提示：
风格锁定：
负面约束：
```

## Complex One-Take Video Pattern

For complex action shots with multiple referenced assets, native asset IDs, a single continuous take, and detailed physical events, structure the prompt as:

```markdown
【基础设定】
角色/主体1：<node-asset>...</node-asset> 外形、材质、服装、表情/状态规则、不可变化项。
角色/主体2：<node-asset>...</node-asset> 外形、动作特征、不可变化项。
关键道具：<node-asset>...</node-asset> 尺寸、材质、启动方式、发光/变形/爆炸等状态变化。
群体/背景角色：<node-asset>...</node-asset> 数量感、外观、运动方式、危险感。

场景：<node-asset>...</node-asset> 时代、地点、天气、建筑、地面、前中后景、环境道具。
声音：是否配乐、是否氛围音、同期声保留项。

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

Keep `分镜`, `景别`, `构图`, `运镜手法`, and `画面内容` separate. Write the action chain in physical order: hand/object interaction, prop state change, subject movement, background reaction, ending frame/camera consequence.

## Negative Prompt Defaults

Block:

- face drift, identity change, extra fingers, broken hands, warped body, plastic skin
- deformed product, wrong logo, unreadable package text, random brand marks
- random subtitles, extra captions, watermarks, UI artifacts
- flicker, camera jitter, frame jump, object melting, inconsistent lighting
- stock footage look, over-saturated color, unrelated props, crowded background

## Regeneration Notes

Use this structure:

```markdown
保留：
必须修改：
可接受变化：
不可接受：
下一轮提示词补强：
```

## Platform Notes

- If the user names a platform, adapt prompt length and terminology to that platform.
- If no platform is named, keep prompts platform-neutral and production-readable.
- For logo/package shots, prefer controlled keyframes or image-to-video references over pure text prompts.
