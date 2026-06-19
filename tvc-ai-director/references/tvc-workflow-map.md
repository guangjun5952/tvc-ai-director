# TVC Workflow Map

Use this map to decide stage, specialist skill, and handoff.

## Stage Routing

| Stage | User signals | Specialist | Output |
| --- | --- | --- | --- |
| Brief | brief, 需求, 产品, 人群, 渠道, 预算, 片长 | `$tvc-brief-strategist` | Brief 诊断, 策略任务, 创意方向 |
| Concept | 提案, 创意, 方向, 概念, slogan, 故事 | `$tvc-concept-developer` | 创意路线, 脚本结构, 汇报话术 |
| Treatment | 导演阐述, 影调, 节奏, 镜头语言, 参考片 | `$tvc-director-treatment` | 导演阐述, 影像风格, 执行方法 |
| PPM | PPM, 演员, 服装, 化妆, 美术, 音乐参考, 道具 | `$tvc-ppm-producer` | PPM pack, 确认项, 物料清单 |
| Storyboard | 分镜, 镜头脚本, shot list, 景别, 时长 | `$tvc-storyboard-writer` | 分镜表, 节奏表, 连续性提醒 |
| AI prompt | prompt, 生图, 生视频, Midjourney, Runway, 可灵, 即梦 | `$tvc-ai-shot-prompter` | 图像 prompt, 视频 prompt, 负面约束 |
| AI production | 执行, 批次, 版本, 生成失败, 一致性 | `$tvc-ai-production-coordinator` | 批次表, 物料表, 返工规则 |
| Editing | 剪辑, 节奏, 音乐, 声音, 包装, 交付 | `$tvc-editing-director` | 剪辑时间线, 声音设计, 交付清单 |
| Review | 审片, 客户意见, 修改, 反馈, 不够高级 | `$tvc-client-review-interpreter` | 意图解析, 修改动作, 回复建议 |

## Common Execution Chains

- New vague request: `brief -> concept`.
- Pitch deck request: `brief -> concept -> treatment`.
- PPM request after concept approval: `treatment -> ppm`.
- AI execution request: `storyboard -> ai prompt -> ai production`.
- Full AI TVC: `brief -> concept -> treatment -> storyboard -> ai prompt -> ai production -> editing -> review`.
- Client revision: `review -> editing` or `review -> ai prompt -> ai production -> editing`.

## Sparse Brief Gate

If the user only provides a product image, product name, rough category, or one-line request, do not route to concept yet. Stop at `$tvc-brief-strategist` and ask:

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

After answers arrive, route to `$tvc-concept-developer`, then continue into treatment, storyboard, AI prompt, production, editing, or review as needed.

## Universal Handoff

Every specialist should preserve:

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

## Must-Ask Threshold

Ask before proceeding when missing information affects:

- Product truth, claim legality, logo/package accuracy.
- Aspect ratio direction, target audience, or channel.
- Duration, ratio, or delivery deadline.
- Talent identity, product reference, or required visual asset.
- Client-mandated reference, taboo, or approval condition.

For sparse briefs, the required brief gate questions always count as must-ask.
