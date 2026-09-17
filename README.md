<div align="center">

# 🎥 DiDi_OK × Seedance 2.5 Cinematic Prompt Skill

**把一个故事或参考素材，变成空间连续、动作可信、运镜清楚、同期声完整的电影级视频提示词。**

[简体中文](README.md) · [English](README_EN.md)

[![Agent Skill](https://img.shields.io/badge/Agent_Skill-SKILL.md-111827?style=flat-square)](https://agentskills.io/)
[![Seedance 2.5](https://img.shields.io/badge/Seedance-2.5-2563EB?style=flat-square)](https://seed.bytedance.com/en/seedance2_5)
[![Codex](https://img.shields.io/badge/Codex-compatible-10A37F?style=flat-square)](https://github.com/openai/codex)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-D97757?style=flat-square)](https://docs.anthropic.com/en/docs/claude-code)
[![Qwen Code](https://img.shields.io/badge/Qwen_Code-compatible-615CED?style=flat-square)](https://qwenlm.github.io/qwen-code-docs/zh/users/features/skills/)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

[快速开始](#30-秒开始) · [作品静帧](#didi_ok-作品静帧) · [六个原始 Case](#六个-didi_ok-case) · [六类镜头模板](references/templates.md) · [写实测试 Prompt](prompt-library/test-cases-v2.md) · [方法资料库](#方法资料库) · [参与贡献](CONTRIBUTING.md)

</div>

![DiDi_OK × Seedance 2.5 Cinematic Prompt Skill](assets/seedance-cinematic-hero.png)

---

这不是“电影感词汇堆砌器”。它以 DiDi_OK《Candy》六个镜头 Case 为主要规则来源，先建立写实视觉合同、人物与空间拓扑，再组织摄影机路径、动作因果、真实物理、焦点变化、微表演、完整对白和现场同期声。每条正式 Prompt 都必须明确：**无 BGM，无配乐！**

## 目录

- [为什么需要它](#为什么需要它)
- [30 秒开始](#30-秒开始)
- [工作方式](#工作方式)
- [适用方向](#适用方向)
- [DiDi_OK 作品静帧](#didi_ok-作品静帧)
- [六个 DiDi_OK Case](#六个-didi_ok-case)
- [实测 Case](#实测-case)
- [安装](#安装)
- [方法资料库](#方法资料库)
- [质量审核](#质量审核)
- [项目结构](#项目结构)

## 为什么需要它

| 常见问题 | 这个 Skill 的处理方式 |
| --- | --- |
| 只写“电影感、真实、8K”，画面仍然空泛 | 开头固定画幅、摄影媒介感、写实程度、色彩与整体气质 |
| 多人物站位、视线和遮挡关系混乱 | 明确前中后景、左右、内外、人物站位与摄影机位置 |
| 运镜名称很多，但看不出镜头怎么走 | 写清方向、速度、景别变化、移动动机与操作者反应 |
| 动作像瞬移，物体没有重量 | 按触发、接触、受力、阻力、惯性、反应和结果描述 |
| 人物同时转头、同时惊讶，缺少真实表演 | 设计呼吸、眼神、停顿、潜台词和错开的反应时差 |
| 有对白，却没有镜头与他人反应 | 完整写出台词，并同步语气、动作、焦点和听者反应 |
| 模型自动生成煽情配乐 | 每条正式 Prompt 都单独写明“无 BGM，无配乐！” |
| 内容塞得太满或时长凭空出现 | Prompt 正文不擅加秒数；完成后按内容容量独立推荐时长 |

## 30 秒开始

```text
使用 $didi-ok-video-prompt，把“雨夜，一个外卖员在即将关门的唱片店门口听见熟悉旋律”写成 Seedance 2.5 写实电影感视频提示词。
```

有参考素材时，明确每份素材的职责：

```text
参考 @Image 1 的人物与服装，参考 @Image 2 的空间布局，参考 @Video 1 的手持运镜节奏。写成一镜到底的 Seedance 2.5 视频提示词，保留真实同期声，不要 BGM。
```

```mermaid
flowchart LR
    A[故事或素材] --> B[视觉合同与空间]
    B --> C[动作因果与运镜]
    C --> D[表演、对白与同期声]
    D --> E[禁止项与故障防护]
    E --> F[审核与推荐时长]
```

## 工作方式

1. 锁定用户不可改变的故事、人物、台词、画幅和参考素材职责。
2. 建立主体、摄影机、前中后景、左右内外、视线与遮挡的空间关系。
3. 按起始状态、触发、中间态、人物反应和可见结果组织事件。
4. 选择与叙事动机一致的机位、景别、焦点变化、移动路线和镜头形式。
5. 补足真实物理、微表演、完整对白以及有距离和材质层次的同期声。
6. 加入与当前镜头直接相关的禁止项，并明确“无 BGM，无配乐！”。
7. 按 100 分量表审核；未达 90 分或触发硬门槛时先重写。
8. Prompt 正文完成后，再按动作、对白、运镜、反应和收束容量独立推荐时长。

## 适用方向

| 方向 | 优先控制 |
| --- | --- |
| 写实人物 / 微表演 | 眼神、呼吸、停顿、潜台词、反应时差和皮肤质感 |
| 多主体 / 群像对白 | 人物身份、站位、视线、差异化动作、焦点接力与完整对白 |
| 产品 / 微距物理 | 材质、接触、摩擦、表面张力、结构连续性与真实声音 |
| 建筑 / 连续空间 | 尺度、结构、路线、遮挡、曝光适应、反射和空间混响 |
| 纪录片 / 发布会 | 现场操作者感、手持误差、自动对焦、公共空间与环境声 |
| 参考图 / 视频 / 音频生成 | 每份素材职责单一明确，避免人物、构图、运动与声音互相污染 |

## DiDi_OK 作品静帧

以下为用户提供的 DiDi_OK 作品静帧，用于展示不同题材中的镜头意识与视觉结果。它们是作品画廊，不等同于下方六个《Candy》规则 Case，也不计入已经回填成片的两条真人写实 Seedance 2.5 验证 Case。

<table>
  <tr>
    <td width="50%"><img src="assets/works/candy-eye-closeup.png" alt="糖果作品中的人物眼部极近景"><br><sub>人物眼部极近景：局部光影、压迫距离与视觉注意力</sub></td>
    <td width="50%"><img src="assets/works/candy-foreground-pickup.png" alt="前景糖果拾取镜头"><br><sub>前景糖果拾取：贴地机位、近大远小与手指交互</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="assets/works/office-standoff.png" alt="警局多人物对峙"><br><sub>警局对峙：多主体站位、视线冲突与空间压力</sub></td>
    <td width="50%"><img src="assets/works/battlefield-follow.png" alt="战场后方跟拍"><br><sub>战场跟拍：后方移动视角、烟火层次与群体推进</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="assets/works/battlefield-scope-view.png" alt="战场瞄准镜视角"><br><sub>瞄准镜观察：远距视觉证据、主观视场与目标压缩</sub></td>
    <td width="50%"><img src="assets/works/battlefield-rifle-pov.png" alt="战场第一人称枪械视角"><br><sub>第一人称战场：枪械前景、队员层次与运动方向</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="assets/works/shepherd-earth-moon.png" alt="SHEPHARD THE SHEPHERD 地月概念画面"><br><sub>SHEPHARD THE SHEPHERD：图形化空间关系与叙事信息</sub></td>
    <td width="50%"><img src="assets/works/lab-observation-room.png" alt="实验室玻璃观察空间"><br><sub>实验室观察：玻璃内外、观看关系与压抑制度空间</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="assets/works/cat-ants-candy.png" alt="猫与蚂蚁搬运糖果"><br><sub>猫与蚂蚁糖果：微距尺度冲突、材质与前后层次</sub></td>
    <td width="50%"><img src="assets/works/museum-dance.png" alt="美术馆群像观看画作"><br><sub>美术馆群像：背影层次、共同观看物与焦点接力</sub></td>
  </tr>
</table>

## 六个 DiDi_OK Case

本仓库把 DiDi_OK《Candy》提示词拆成六类独立 Case，而不是混成一个案例：

| Case | 核心能力 |
| --- | --- |
| 微距蚂蚁搬运糖果 | 微观纪录片、群体差异化运动、接触与滚动阻力 |
| 实验室群戏与糖果爆裂 | 多机位群像、压抑空间、物理爆裂与反应时差 |
| 女发言人发布会 | 记者手持、公共发言、品牌空间和克制表演 |
| 人物绕后与遮挡转场 | 一镜到底、实体遮挡、旧空间与新空间连续替换 |
| 前景糖果拾取 | 贴地机位、近大远小、手指交互和焦点变化 |
| 美术馆群像对白 | 人群游走、多人观点接力、长焦证据揭示和同期声 |

[查看六案原文与完整拆解](references/cases.md) · [查看六案模块频率分析](references/case-pattern-analysis.md)

## 实测 Case

旧版五条测试 Prompt 已全部下线，动漫方向已经删除。测试不再继续按产品、建筑等题材扩类，只保留“群像”和“单人物”两个真人写实 Case：

| 类型 | 测试主题 | 状态 |
| --- | --- | --- |
| 群像 | 合租厨房里的焦边煎蛋 | 已回填 30.08 秒原始成片与五张静帧 |
| 单人物 | 浴室剪坏刘海 | 已回填 30.08 秒原始成片与五张静帧 |

[查看合租厨房群像实测 Case](cases/shared-kitchen/README.md) · [查看浴室剪发单人物实测 Case](cases/bathroom-haircut/README.md) · [复制两条完整真人写实测试 Prompt](prompt-library/test-cases-v2.md)

## 安装

最通用的社区安装方式：

```bash
npx skills add wusuyee-beep/seedance-2.5-cinematic-prompt-skill -g
```

也可以手动克隆完整仓库：

```bash
git clone https://github.com/wusuyee-beep/seedance-2.5-cinematic-prompt-skill.git didi-ok-video-prompt
```

把整个 `didi-ok-video-prompt/` 目录放入目标 Agent 的 Skills 目录。不要只复制 `SKILL.md`，因为六案、审核表、Seedance 能力边界和时长规则位于 `references/`。

- Codex：`~/.codex/skills/didi-ok-video-prompt/`
- Claude Code：`~/.claude/skills/didi-ok-video-prompt/`
- CodeBuddy：用户级或项目级 Skills 目录
- Qwen Code：`~/.qwen/skills/didi-ok-video-prompt/`
- Qoder：通过 Skills 上传 ZIP，或放入 `~/.qoder/skills/`

安装后可用以下请求测试：

```text
使用 $didi-ok-video-prompt 写一个写实电影感视频 Prompt：一名女人在凌晨便利店发现收银员与照片里的人长得一模一样。只保留真实同期声，无 BGM、无配乐。
```

## 方法资料库

| 文件 | 解决的问题 |
| --- | --- |
| [`cases.md`](references/cases.md) | 六个 DiDi_OK 原始 Case 的独立文本与边界 |
| [`case-pattern-analysis.md`](references/case-pattern-analysis.md) | 六案共有、高频和差异化模块的占比规律 |
| [`method.md`](references/method.md) | 从粗略创意组织成可执行视频 Prompt 的方法 |
| [`templates.md`](references/templates.md) | 连续镜头、参考生成、对白和输出结构模板 |
| [`audiovisual-language-analysis.md`](references/audiovisual-language-analysis.md) | 六案逐段功能、视听语言原理、复刻公式及超低机位/手持/变焦语法 |
| [`audiovisual-language-sources.md`](references/audiovisual-language-sources.md) | 中传教材、官方公开课与专业摄影/纪录片参考书目 |
| [`seedance-2.5.md`](references/seedance-2.5.md) | 官方能力边界与模型适配规则 |
| [`duration-recommendation.md`](references/duration-recommendation.md) | Prompt 之后如何按内容容量推荐生成时长 |
| [`review-rubric.md`](references/review-rubric.md) | 交付前 100 分审核与硬门槛 |
| [`acceptance.md`](references/acceptance.md) | 最终交付必须满足的验收标准 |

## 质量审核

| 模块 | 分值 |
| --- | ---: |
| 视觉合同与画幅 | 10 |
| 主题细节与连续性 | 15 |
| 空间拓扑 | 15 |
| 摄影机与操作者 | 15 |
| 动作因果与物理 | 10 |
| 焦点、表演与反应 | 10 |
| 同期声与对白 | 10 |
| 强约束与故障防护 | 5 |
| Seedance 2.5 官方适配 | 10 |

任何一项硬门槛失败都会直接退回重写，包括：遗漏“无 BGM，无配乐！”，缺少画幅、空间、摄影机路线、动作因果、现场声音或针对性禁止项，擅自改写用户参考职责，或者把未经要求的秒数和时间码塞进 Prompt 正文。

## 项目结构

```text
didi-ok-video-prompt/
├── SKILL.md
├── agents/openai.yaml
├── assets/seedance-cinematic-hero.png
├── assets/works/
├── cases/shared-kitchen/
├── cases/bathroom-haircut/
├── prompt-library/
│   ├── README.md
│   ├── image-prompt-direction.md
│   └── test-cases-v2.md
├── references/
│   ├── cases.md
│   ├── case-pattern-analysis.md
│   ├── method.md
│   ├── templates.md
│   ├── audiovisual-language-analysis.md
│   ├── audiovisual-language-sources.md
│   ├── seedance-2.5.md
│   ├── duration-recommendation.md
│   ├── review-rubric.md
│   └── acceptance.md
└── scripts/validate_skill.py
```

## 方法依据

主要规则中，DiDi_OK 六个 Case 占 90%，Seedance 2.5 官方能力说明占 10%。案例提供镜头语言、空间组织、物理、表演和声音层面的生成规律；官方资料负责校准参考输入、长叙事、延长编辑和单次最长 30 秒等模型能力边界。

- [Seedance 2.5 官方页面](https://seed.bytedance.com/en/seedance2_5)
- [Seedance 2.5 官方介绍](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
- [DiDi_OK 解读《Candy》镜头提示词](https://bytedance.larkoffice.com/wiki/L6Pywea3KiBEqAkg3N9cunZdnFg)

## 相关项目

- [Cinematic Image Prompt Skill](https://github.com/wusuyee-beep/cinematic-image-prompt-skill)：负责单帧电影感生图提示词，不包含时间、运镜与声音规则。

如果它帮你稳定产出了更好的视频，欢迎 Star、提交真实 Case，或把一次失败生成整理成可复现问题。

## 权利说明

本项目中的 DiDi_OK 案例文本来自用户提供截图和原始页面，仅用于研究提示词结构与镜头方法。公开转载或商业使用前，请确认相关授权边界。

## License

[MIT](LICENSE)
