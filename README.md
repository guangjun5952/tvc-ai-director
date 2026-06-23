# TVC AI Director Skill Suite

一个面向 TVC 导演、广告创意、AI 影像制作团队的 Codex Skill Suite。

它不是一个单点 prompt，而是一套“广告片工作室工作台”：用一个主路由 skill 判断项目阶段、补齐关键 brief、选择合适的专业子 skill，再把创意提报、导演阐述、PPM、分镜、AI prompt、AI 制作、剪辑和审片修改串成一条可执行的生产链路。

## 它解决什么问题

TVC 工作里最常见的问题不是“不会写一个脚本”，而是信息、判断和交接断在不同阶段：

- 甲方只给一张产品图或一句需求，就希望马上看到创意。
- AI 可以生成画面，但缺少广告导演的 brief 诊断、画幅判断、产品露出、审片逻辑和连续性控制。
- 创意提案常常只讲“拍什么”，没有讲清楚“为什么这样拍”。
- 导演阐述、PPM、分镜、prompt、剪辑、审片反馈之间缺少统一交接格式。
- 多个模型、多个子任务一起工作时，容易跳过前置问题，导致后面的产物看起来完整但方向错误。
- 客户反馈经常是“高级一点”“不够冲击”“不像我们品牌”，需要被翻译成具体的剪辑、镜头、prompt 或制作动作。

这个 Skill Suite 的核心目标是：让 AI 不只是产出内容，而是按真实 TVC 工作流思考、追问、路由和交付。

## 适合谁使用

- TVC 导演
- 广告创意总监
- 制片与 PPM 负责人
- AI 视频导演
- 品牌片、产品片、社媒广告团队
- 需要把传统广告流程迁移到 AI 生产链路的人

默认输出语言为中文；AI 图像和视频 prompt 中会保留必要的英文摄影、镜头、灯光术语。

## 核心能力

### 1. Brief 诊断与前置确认

当客户信息不足时，主路由不会直接开始写创意，而是先进入 brief gate。

默认必须先确认：

1. 画幅方向：横屏、竖屏，还是横竖都要？
2. 投放渠道偏好
3. 成片时长
4. 参考风格
5. 已想好的表达内容
6. 品牌 slogan
7. 禁用词
8. 目标人群
9. 是否可以使用真人演员
10. 是否承担电商转化目标

其中“横屏 / 竖屏 / 横竖都要”被放在最前端，避免系统根据抖音、小红书、B 站等渠道自行猜测画幅。

### 2. 创意提报

`tvc-concept-developer` 重点解决“为什么这样拍”，而不是提前进入分镜。

默认提案结构：

- Project Understanding
- Insight
- Creative Idea
- Creative Concept
- Story Outline
- Key Visual
- Communication Mapping
- Deliverables

它会把产品卖点翻译成用户心理、情绪价值和视频语言，并在需要参考图、参考片、视觉案例时主动进行资料搜索，把可检查的参考链接放进提案。

### 3. 导演阐述与视觉开发

`tvc-director-treatment` 将已通过的创意路线展开成导演阐述：

- 影像风格
- 镜头语言
- 节奏与情绪曲线
- 表演与人物形象设计
- 场景设定
- 产品呈现
- 美术、光影与色彩
- 音乐与声音

它还会为每个关键视觉部分生成 GPT Image 2-ready prompt，并在环境支持时直接生成对应参考图。

### 4. PPM 制作

`tvc-ppm-producer` 负责将创意和导演阐述整理成真实广告制作可以开会确认的 PPM 包：

- 演员、服装、化妆、发型
- 美术、道具、场景
- 产品准备、hero product、packshot
- 摄影、灯光、音乐、声音
- 日程、风险、客户确认项

### 5. 分镜头脚本

`tvc-storyboard-writer` 使用导演级分镜拆解方法：

- 先提炼创意核心
- 再拆解情绪曲线
- 再搭建叙事结构
- 再定义具体视觉语言
- 最后输出可执行分镜表

它要求每个镜头都有存在理由，每个镜头都推动情绪或叙事，并明确产品 / logo 露出节点、高潮镜头和结尾记忆点。

如果用户要求“Excel 表格 / xlsx / 分镜表 / prompt 表”，分镜会使用带时间码的表格字段，方便后续直接合并 AI prompt 并导出工作簿。

### 6. AI 图像与视频 Prompt

`tvc-ai-shot-prompter` 将分镜转换为可执行的 AI 生成 prompt。

图片 prompt 使用八层结构：

1. Subject
2. Action
3. Environment
4. Composition
5. Camera
6. Lighting
7. Color Palette
8. Style Reference

视频 prompt 使用 Seedance-style 方法：

- 参考素材引用
- 时长与画幅
- 分段动作
- 运镜
- 主体运动
- 产品连续性
- 声音提示
- 结尾帧
- 负面约束

当分镜和 prompt 需要交付给制片、剪辑或 AI 生成同事时，可以输出合并表：

```markdown
| 镜号 | 时间码 | 时长 | 景别 | 画面内容 | 镜头运动 | 产品/logo | 声音/字幕 | 图片 Prompt | 视频 Prompt | 负面约束 | 连续性锁定 | 重生成备注 |
```

这张表可直接保存为 TSV，再用 `tvc-ai-director/scripts/make_tvc_excel.py` 导出 `.xlsx`。

### 7. AI 制作统筹

`tvc-ai-production-coordinator` 负责真实执行中的混乱部分：

- 素材准备
- 镜头批次
- 版本命名
- 人物、产品、服装、场景连续性
- 生成失败排查
- 返工规则
- 镜头状态管理

### 8. 剪辑与交付

`tvc-editing-director` 负责把生成或拍摄素材组织成可审片版本：

- 前 3 秒策略
- 节奏时间线
- 音乐节拍
- 声音设计
- 字幕包装
- packshot / end card
- 横竖屏与 cutdown 版本
- 交付清单

### 9. 客户审片反馈解析

`tvc-client-review-interpreter` 会先解读客户意见，再决定怎么改：

- 表层要求
- 真实意图
- 必改项
- 可协商项
- 需要追问的问题
- 剪辑 / prompt / 文案 / 画面执行动作
- 客户回复建议

它的目标是避免把含混反馈直接机械执行，保护创意、进度和产品准确性。

## 整体结构

```text
.
├── README.md
├── LICENSE
├── tvc-ai-director/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   │   ├── tvc-workflow-map.md
│   │   ├── tvc-quality-bar.md
│   │   ├── category-playbooks.md
│   │   ├── prompt-style-guide.md
│   │   └── client-communication.md
│   ├── assets/templates/
│   │   ├── brief-template.md
│   │   ├── proposal-template.md
│   │   ├── director-treatment-template.md
│   │   ├── ppm-template.md
│   │   ├── storyboard-template.md
│   │   ├── ai-prompt-template.md
│   │   ├── editing-template.md
│   │   └── review-template.md
│   └── scripts/
│       ├── make_tvc_tables.py
│       └── make_tvc_excel.py
├── tvc-brief-strategist/
├── tvc-concept-developer/
├── tvc-director-treatment/
├── tvc-ppm-producer/
├── tvc-storyboard-writer/
├── tvc-ai-shot-prompter/
├── tvc-ai-production-coordinator/
├── tvc-editing-director/
├── tvc-client-review-interpreter/
└── multi-model-router/
```

## Skill 调用关系

主入口是 `tvc-ai-director`。

它负责：

- 判断用户当前处于哪个 TVC 阶段
- 判断是否缺少路由所需条件
- 在信息不足时先追问
- 在信息充分后调用专业子 skill
- 维护统一交接格式
- 对最终输出做质量门槛检查

常见执行链：

```text
brief -> concept -> treatment -> storyboard -> ai prompt -> ai production -> editing -> review
```

对应关系如下：

| 阶段 | Skill | 作用 |
| --- | --- | --- |
| Brief | `tvc-brief-strategist` | 诊断 brief，补齐关键信息，形成策略任务 |
| Concept | `tvc-concept-developer` | 生成创意提报，解释为什么这样拍 |
| Treatment | `tvc-director-treatment` | 展开导演阐述和视觉开发 |
| PPM | `tvc-ppm-producer` | 生成完整 PPM 包和确认清单 |
| Storyboard | `tvc-storyboard-writer` | 将创意拆成可执行分镜脚本 |
| AI Prompt | `tvc-ai-shot-prompter` | 输出图像 prompt、视频 prompt 和负面约束 |
| Excel Export | `tvc-ai-director/scripts/make_tvc_excel.py` | 将分镜/prompt TSV 表导出为 `.xlsx` |
| AI Production | `tvc-ai-production-coordinator` | 管理 AI 生成批次、连续性和返工 |
| Editing | `tvc-editing-director` | 规划剪辑、声音、字幕、版本和交付 |
| Review | `tvc-client-review-interpreter` | 解析客户意见并生成修改动作表 |
| General Routing | `multi-model-router` | 提供通用多模型 / 多技能路由门槛方法 |

每个子 skill 输出都尽量保留统一交接字段：

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

这样上游产物可以被下游 skill 直接接住，而不需要重新解释背景。

## 使用方式

将这些目录复制到 Codex skills 目录：

```bash
cp -R tvc-* multi-model-router ~/.codex/skills/
```

然后在 Codex 中调用：

```text
[$tvc-ai-director] 我要做一条冰红茶广告，客户只给了一张产品图。
```

信息不足时，主 skill 会先问关键问题；信息完整后，会自动进入合适的子 skill。

也可以直接调用某个子 skill：

```text
[$tvc-storyboard-writer] 根据这个创意路线生成分镜头脚本。
```

生成 Excel 表格：

```text
[$tvc-ai-director] 按这个创意生成分镜头脚本、图片和视频 prompt，并整理成 Excel 表格。
```

脚本用法：

```bash
python3 tvc-ai-director/scripts/make_tvc_excel.py storyboard-prompts.tsv storyboard-prompts.xlsx
```

TSV 第一行是表头，列之间用 tab 分隔。脚本会生成带冻结表头、自动筛选、自动换行和基础列宽的 `.xlsx` 文件，不依赖第三方 Python 包。

## 为什么一个 TVC 导演会需要它

这个 Skill Suite 来自一个很具体的工作困境：TVC 导演今天面对的已经不是单纯的“拍一条片”。

在真实工作中，导演经常同时要处理这些问题：

- 客户 brief 很少，但期望很高。
- 甲方可能只给一张 SKU 图，却希望马上看到创意、风格、分镜和 AI 画面。
- 平台越来越碎片化，同一个创意可能要适配抖音、小红书、B 站、横屏、竖屏和 cutdown。
- 传统广告流程里，创意、导演阐述、PPM、分镜、后期和审片本来就需要大量沟通；到了 AI 制作里，还多了 prompt、参考图、角色一致性、产品准确性和生成返工。
- 客户说“更高级”“更年轻”“更有冲击力”时，导演不能只照字面改，而要判断背后的担心是什么。
- AI 工具可以生成单张漂亮图片，但广告真正需要的是从策略到画面再到交付的连续判断。

所以这个 skill 的目标不是替代导演，而是把导演脑子里那些容易被反复消耗的判断流程沉淀下来：

- 什么时候不能往下做，必须先问 brief？
- 什么时候该出创意，什么时候该出导演阐述？
- 分镜怎么既能拍，又能给 AI 执行？
- prompt 怎么保护人物、产品、包装和画幅？
- 客户反馈怎么变成具体修改动作？

它更像一个 TVC 导演的 AI 工作台：帮导演守住流程、节奏、判断和交接，让创意精力留给真正重要的部分。

## License

MIT
