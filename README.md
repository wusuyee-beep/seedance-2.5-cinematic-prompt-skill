# DDOk × Seedance 2.5 写实电影感视频提示词 Skill

一个面向 Seedance 2.5 的 Claude Code / Codex 兼容 Skill，用于把故事、场景、参考图、参考视频或粗略创意转化为可直接生成的写实电影级视频提示词。

它不是提示词词库，而是一套镜头决策方法：先建立空间和连续性，再组织动作因果、运镜、真实物理、微表演、焦点变化与同期声。

## 适用场景

- 写实电影感文生视频
- 图像、视频、音频多模态参考生成
- 30 秒长叙事与多镜头组织
- 一镜到底与遮挡转场
- 群像对白和纪录片式手持
- 视频延长和时间戳编辑提示词

## 安装

### Claude Code

将整个仓库放入个人 Skill 目录：

```bash
git clone <YOUR_REPOSITORY_URL> ~/.claude/skills/ddok-video-prompt
```

或者只复制 `SKILL.md`、`references/` 到：

```text
~/.claude/skills/ddok-video-prompt/
```

### Codex

将仓库复制或链接到 Codex Skills 目录，并保留 `agents/openai.yaml`。

## 使用

```text
使用 $ddok-video-prompt，把这个故事写成 Seedance 2.5 的 30 秒写实电影感提示词。参考 @Image 1 的人物，参考 @Video 1 的运镜，保留真实同期声。
```

也可以直接提出：

```text
写一个 15 秒、一镜到底、手持纪录片质感的 Seedance 2.5 视频提示词。
```

## 项目结构

```text
ddok-video-prompt/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── seedance-2.5.md
    ├── method.md
    ├── templates.md
    ├── acceptance.md
    ├── case-pattern-analysis.md
    ├── official-seedance-patterns.md
    ├── review-rubric.md
    └── cases.md
```

## 案例

`references/cases.md` 收录并拆分了 6 个 DDOk《Candy》镜头案例：微距物理、实验室群戏、发布会、移动遮挡转场、前景拾取和美术馆群像对白。案例用于学习结构，不应机械复制人物、对白或世界观。

Skill 不会在用户未指定时擅自加入秒数或时间码；每条正式提示词都必须明确“无 BGM，无配乐！”，并只设计现场同期声、环境声、动作声和对白。同时使用“严格、必须、始终、全程、绝不”等原案例式强约束语言锁定关键生成要求。

每次生成后会按 100 分量表自审：DiDi_OK 六案保真占 90 分，Seedance 2.5 官方能力适配占 10 分；硬门槛失败或总分低于 90 的结果必须先重写，再交付。

## 生成资料库

本仓库同时维护面向生成创作的方法入口，视频与静态图像分开管理，避免时序、声音和运镜规则污染单帧生图提示词。

- **视频提示词方向**：当前仓库的 `$ddok-video-prompt`，用于 Seedance 2.5 写实电影感生视频。
- **生图提示词方向**：[cinematic-image-prompt-skill](https://github.com/wusuyee-beep/cinematic-image-prompt-skill)，用于真人电影感、纪实摄影、动漫插画、概念场景、建筑室内和电商产品图。

两套方法的边界、共同基础与选用方式见 [`prompt-library/README.md`](prompt-library/README.md)，生图方向的核心结构见 [`prompt-library/image-prompt-direction.md`](prompt-library/image-prompt-direction.md)。

## 资料来源

- [Seedance 2.5 官方页面](https://seed.bytedance.com/en/seedance2_5)
- [Seedance 2.5 官方介绍](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
- [Anthropic Agent Skills](https://github.com/anthropics/skills)
- [Claude Code Skill Development](https://github.com/anthropics/claude-code/blob/main/plugins/plugin-dev/skills/skill-development/SKILL.md)
- [DiDi_OK 解读《Candy》镜头提示词](https://bytedance.larkoffice.com/wiki/L6Pywea3KiBEqAkg3N9cunZdnFg)

## 权利说明

本项目中的案例文本来自用户提供截图和原始页面，仅用于研究提示词结构与镜头方法。公开发布前，请确认相关案例文本的转载与授权边界。
