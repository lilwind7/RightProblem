<h1 align="center">RightQuestion</h1>

<p align="center"><strong>不要优化眼前的问题，去找到真正值得回答的问题。</strong></p>

<p align="center"><a href="README.md">English</a></p>

RightQuestion 是一个可跨 Agent 使用的 [Agent Skill](https://agentskills.io/)。它不只是改写用户的问题，而是把真实目标与原始表述、假设、方案分开，找到此刻最值得回答、最能推动目标的问题。

## 它带来的变化

> **原问题：** 每个数据库操作都应该使用事务吗？
>
> **RightQuestion：** 哪些关键业务路径中的多步操作，可能进入部分完成状态，并造成不可接受且无法自愈的后果？

后一个问题能真正支撑技术选择：应该使用事务、幂等、补偿、状态机，还是接受短暂不一致。它找到的是决定方案的业务后果，而不是继续围绕某个方案打转。

## 30 秒安装

下载或克隆本仓库后运行：

```bash
python3 scripts/install.py
```

Windows：

```powershell
py scripts/install.py
```

默认会为当前用户安装 Codex、Claude Code、Cursor 和 Gemini CLI 四个版本；已有安装不会被静默覆盖。

只安装某个 Agent，或安装到当前项目：

```bash
python3 scripts/install.py --agent claude
python3 scripts/install.py --agent universal
python3 scripts/install.py --scope project --agent all
```

开发时使用软链接、预览操作、安全更新或卸载：

```bash
python3 scripts/install.py --agent codex --method link
python3 scripts/install.py --dry-run
python3 scripts/install.py --force
python3 scripts/install.py --uninstall
```

`--force` 会先把旧版本移动到 `.right-question-backups`，再安装新版。运行 `python3 scripts/install.py --help` 可查看全部选项。

## 怎么使用

支持自动选择 Skill 的 Agent 可以直接理解自然语言；也可以显式调用：

| Agent | 示例 |
| --- | --- |
| Codex | `$right-question 我们应该做一个 App 吗？` |
| Claude Code | `/right-question 我们应该做一个 App 吗？` |
| Cursor | `/right-question 我们应该做一个 App 吗？` |
| Gemini CLI | `请使用 right-question skill：我们应该做一个 App 吗？` |

适合输入的问题包括：

- `这个产品应该用微服务吗？`
- `怎样更快地增长我的 newsletter？`
- `我们总是延期，应该改变什么？`
- `我拿到了三个 offer，该怎么选？`
- `帮我找到做这个决定前最应该回答的问题。`

默认输出保持克制：

```text
真实目标
...

最高杠杆问题
...

为什么是这个问题
...
```

## 兼容性

RightQuestion 遵循开放的 Agent Skills 格式，不依赖工具或网络。

| Agent | 用户级目录 | 项目级目录 | 官方文档 |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/right-question` | `.agents/skills/right-question` | [Build skills](https://developers.openai.com/codex/skills/) |
| Claude Code | `~/.claude/skills/right-question` | `.claude/skills/right-question` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) |
| Cursor | `~/.cursor/skills/right-question` | `.cursor/skills/right-question` | [Agent Skills](https://cursor.com/docs/skills) |
| Gemini CLI | `~/.gemini/skills/right-question` | `.gemini/skills/right-question` | [Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| 通用目录 | `~/.agents/skills/right-question` | `.agents/skills/right-question` | Codex、Cursor、Gemini CLI 均支持 |

如果正在运行的 Agent 没有立即发现新 Skill，请重新加载 Skills 或重启 Agent。

## 它是怎么工作的

1. 还原结果目标、事实证据、真实约束、原因假设和用户提出的方案。
2. 暂时丢开原问题，不把当前框架当作事实。
3. 从根因、瓶颈、风险、价值、行为等不同层面生成真正竞争的问题。
4. 按因果重要性、信息增益、行动影响和调查成本排序，以目标杠杆为最高标准。
5. 返回一个问题：如果只能可靠回答一个，哪个最能提高实现目标的概率？

详细思考模型和校准示例位于 `references/`，只有需要时才加载，避免占用默认上下文。

## 参与贡献

欢迎补充真实案例、改进触发边界、增加 Agent 兼容性或翻译。提交修改前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

本项目采用 [MIT License](LICENSE)。
