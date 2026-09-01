<h1 align="center">RightQuestion</h1>

<p align="center"><strong>别急着让 AI 给答案，先确认你回答的是那个真正重要的问题。</strong></p>

<p align="center"><a href="README.md">English</a></p>

当你正在纠结、选不出来，或者已经很努力却迟迟没有进展时，RightQuestion 会让 AI 暂时跳出你最初的问法，帮你找到此刻最值得回答的那一个问题。

你不需要懂提示词、Agent，也不需要会编程。

## 看看它有什么不同

> **你问：** 我该不该辞职？
>
> **RightQuestion 会问：** 你希望工作发生的哪些重要改变，只有离开这家公司才能实现？

第一个问题把你推向“辞”或“不辞”。第二个问题先帮你看清自己真正需要什么，以及辞职是不是最合适的办法。

## 现在就用，不用安装

复制下面整段话，粘贴给 ChatGPT、Claude、Gemini、DeepSeek、豆包或其他 AI。最后一行换成你自己的问题即可。

```text
先不要直接回答我的问题。请先帮我找到：为了得到我真正想要的结果，我现在最应该回答的那一个问题。

请跳出我最初描述问题的方式，分清我真正想要什么、我做了哪些假设、我提到的方案是否真的必要。请从几个不同方向思考，但最后只告诉我：

1. 我真正想实现什么
2. 我最应该先回答的一个问题
3. 为什么先回答它会更有帮助

请使用简单、自然的语言。如果我问的只是一个事实，就正常回答。

我的问题是：[把你的问题写在这里]
```

这样就能体验 RightQuestion，不需要下载任何东西。

## 让你的 AI 以后一直会用

如果你的 AI 助手支持 Agent Skills，把下面这句话发给它，让它自己完成安装：

```text
请把 https://github.com/lilwind7/RightQuestion 里的 right-question Agent Skill 安装到我的个人技能中。安装后请验证它可以使用，并告诉我最简单的用法。除非你确实无法完成，否则不要让我自己运行终端命令。
```

如果你使用 Codex，可以直接在对话框粘贴：

```text
$skill-installer 请从 https://github.com/lilwind7/RightQuestion 安装 right-question
```

安装后可以直接自然地描述困惑；在 Codex 中也可以用 `$right-question`，在 Claude Code 或 Cursor 中可以用 `/right-question`。

ChatGPT 网页版和手机版用户可以直接使用上面的“免安装版”。[OpenAI 的 Skill 文档](https://developers.openai.com/codex/skills/)目前把独立 Skill 用于 ChatGPT 桌面应用和 Codex；要覆盖网页和手机端，需要通过插件分发。

需要针对不同 Agent 的具体说明，或者想手动安装？请查看[安装指南](INSTALL.zh-CN.md)。

## 它适合什么时候用

- “我该不该辞职？”
- “三个 offer 应该选哪个？”
- “我要不要再买一门课？”
- “为什么我已经很努力，却一直没有进展？”
- “这个很大的目标，我应该从哪里开始？”
- “我是不是一直在解决错误的问题？”

工作、学习、金钱与时间安排、习惯、关系、创作、经营和技术选择都可以使用。它最适合那些“一旦问题问错，答案越快反而走得越偏”的时刻。

## 它会给你什么

默认回答很短：

```text
你真正想实现什么
...

最应该先回答的问题
...

为什么先回答它
...
```

它不会用一堆思考模型轰炸你，也不会列出十个看起来差不多的问题。

## Agent Skill 是什么

Agent Skill 可以理解为一份 AI 在需要时会自动拿出来使用的“做事方法”。RightQuestion 遵循开放的 [Agent Skills](https://agentskills.io/) 格式，可以在 Codex、Claude Code、Cursor 和 Gemini CLI 中使用，也不需要访问你的文件、账号或网络。

## 参与贡献

欢迎补充日常案例、改进表达与无障碍体验、增加翻译或修复兼容性问题。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

本项目采用 [MIT License](LICENSE)。
