<h1 align="center">RightQuestion</h1>

<p align="center"><strong>理解真正目标，找准问题，然后完成工作。</strong></p>

<p align="center"><a href="README.md">English</a></p>

RightQuestion 会改变 AI Agent 理解任务的方式：它先跳出用户最初的表述，找出最能带来目标结果的问题，再继续完成后续工作——回答、判断、诊断、规划、创作或执行，具体取决于用户原本要它做什么。

你不需要懂提示词、Agent，也不需要会编程。

## 看看它有什么不同

> **你问：** 我已经上过三门课了，却还是做不完一个作品集项目。我要不要再买一门课？

RightQuestion 会把真正需要解决的问题确定为：如何将已经学会的知识转化为完成的作品。Agent 随后会给出找出实际阻力的具体办法，并据此判断是否需要购买新课程。

Agent 在内部完成问题转化，并向你交付有用的答案或完成的工作。

## 它怎么工作

1. 结合你的表述，理解你真正想得到的结果。
2. 检查你假设的原因、已经想到的方案或有限的选项是否把任务带偏了。
3. 在内部重新确定真正要解决的问题，然后继续工作，直到给出答案或完成任务。

如果某个关键信息确实只能由你提供，Agent 会问一个必要的问题，得到回答后继续；其余可以直接检查和推理的部分由 Agent 完成。

## 安装到你的 AI 助手

如果你的 AI 助手支持 Agent Skills，把下面这句话发给它，让它自己完成安装：

```text
请把 https://github.com/lilwind7/RightQuestion 里的 right-question Agent Skill 安装到我的个人技能中。安装后请验证它可以使用，并告诉我最简单的用法。除非你确实无法完成，否则不要让我自己运行终端命令。
```

如果你使用 Codex，可以直接在对话框粘贴：

```text
$skill-installer 请从 https://github.com/lilwind7/RightQuestion 安装 right-question
```

安装后，直接自然地描述问题或任务即可；在 Codex 中也可以使用 `$right-question`，在 Claude Code 或 Cursor 中可以使用 `/right-question`。Agent 会在必要时重新确定问题，然后继续完成工作。

需要针对不同 Agent 的具体说明，或者想手动安装？请查看[安装指南](INSTALL.zh-CN.md)。

## 它适合什么时候用

- “我该不该辞职？”
- “三个 offer 应该选哪个？”
- “我要不要再买一门课？”
- “为什么我已经很努力，却一直没有进展？”
- “是不是应该直接采用我已经想到的方案？”
- “我是不是一直在解决错误的问题？”

工作、学习、金钱与时间安排、习惯、关系、创作、经营和技术问题都可以使用。它最适合那些“一旦问题理解错，Agent 干得越快反而走得越偏”的任务。

## 你会得到什么

你会得到这项任务真正需要的结果：答案、建议、判断、诊断、计划、作品、代码修改，或者 Agent 在能力和授权范围内完成的操作。

输出形式跟随任务本身和你的要求。一次重要的问题转化如果有助于理解结果，Agent 会简单说明改变了什么，然后继续解决。更深层的模型比较默认留在内部，除非你要求查看。

## Agent Skill 是什么

Agent Skill 可以理解为一份 AI 在需要时会自动拿出来使用的“做事方法”。RightQuestion 遵循开放的 [Agent Skills](https://agentskills.io/) 格式，可以在 Codex、Claude Code、Cursor 和 Gemini CLI 中使用。RightQuestion 本身只包含可移植的指令；具体任务需要的工具仍然遵守 Agent 原有的权限规则。

## 参与贡献

欢迎补充日常案例、改进表达与无障碍体验、增加翻译或修复兼容性问题。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

本项目采用 [MIT License](LICENSE)。
