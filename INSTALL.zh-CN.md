# 安装指南

## 最简单：让 AI 自己安装

把下面这句话发给能够管理 Agent Skills 和本地文件的 AI 助手：

```text
请把 https://github.com/lilwind7/RightProblem 里的 right-problem Agent Skill 安装到我的个人技能中。安装后请验证它可以使用，并告诉我最简单的用法。除非你确实无法完成，否则不要让我自己运行终端命令。
```

安装过程中如果出现权限申请，请确认内容后再同意。RightProblem 本身只包含方法说明和示例，不会运行工具，也不会访问外部服务。

## Codex

把下面这句话粘贴到 Codex 对话框：

```text
$skill-installer 请从 https://github.com/lilwind7/RightProblem 安装 right-problem
```

如果没有立即出现，重启一次 Codex。之后可以使用 `$right-problem`，也可以直接自然地描述任务；AI 助手会判断现在最值得处理什么，并产生实际进展。

## Claude Code 和 Cursor

把上面的通用安装请求发给 Agent 即可。两者都支持 `SKILL.md`，并能把文件放入正确的个人技能目录。安装后使用 `/right-problem`，或者直接自然地描述任务；AI 助手会在这套方法能明显改善结果时使用它。

## Gemini CLI

Gemini CLI 支持直接从 GitHub 安装：

```text
gemini skills install https://github.com/lilwind7/RightProblem
```

安装后新建会话，或运行 `/skills reload`。

## 手动安装与开发者选项

如果你希望自己管理本地文件，下载或克隆仓库后运行：

```bash
python3 scripts/install.py
```

Windows：

```powershell
py scripts/install.py
```

默认会安装一份供 Codex、Cursor 和 Gemini CLI 共用的个人版本，再安装一份 Claude Code 版本。这样可以覆盖四种 Agent，同时避免同名 Skill 冲突。已有文件不会被静默覆盖。

常用高级选项：

```bash
python3 scripts/install.py --agent claude
python3 scripts/install.py --agent universal
python3 scripts/install.py --scope project --agent all
python3 scripts/install.py --agent codex --method link
python3 scripts/install.py --dry-run
python3 scripts/install.py --force
python3 scripts/install.py --uninstall
```

`--force` 会先备份不同的旧版本再替换。运行 `python3 scripts/install.py --help` 可以查看全部选项。

## 各 Agent 的目录

| Agent | 个人目录 | 项目目录 | 官方文档 |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/right-problem` | `.agents/skills/right-problem` | [Build skills](https://developers.openai.com/codex/skills/) |
| Claude Code | `~/.claude/skills/right-problem` | `.claude/skills/right-problem` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) |
| Cursor | `~/.cursor/skills/right-problem` | `.cursor/skills/right-problem` | [Agent Skills](https://cursor.com/docs/skills) |
| Gemini CLI | `~/.gemini/skills/right-problem` | `.gemini/skills/right-problem` | [Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| 通用目录 | `~/.agents/skills/right-problem` | `.agents/skills/right-problem` | Codex、Cursor、Gemini CLI 均支持 |

如果正在运行的 Agent 没有发现新 Skill，请重新加载 Skills 或重启 Agent。
