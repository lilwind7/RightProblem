<h1 align="center">RightQuestion</h1>

<p align="center"><strong>Before asking AI for an answer, make sure you are answering the question that actually matters.</strong></p>

<p align="center"><a href="README.zh-CN.md">简体中文</a></p>

RightQuestion helps when you are stuck, torn between options, or working hard without getting the result you want. It gives your AI assistant one job: look past the first question you asked and find the one question that would help you most right now.

You do not need to understand prompts, agents, or programming.

## See the difference

> **You ask:** Should I quit my job?
>
> **RightQuestion asks:** Which important change you want from your working life can only be achieved by leaving this job?

The first question pushes you toward a yes-or-no answer. The second helps you understand what you actually need and whether quitting is the right way to get it.

## Install it in your AI assistant

If your AI assistant supports Agent Skills, send it this message and let it handle the installation:

```text
Install the right-question Agent Skill from https://github.com/lilwind7/RightQuestion for my user account. Verify that it is available, then tell me the simplest way to use it. Do not ask me to run terminal commands unless you cannot complete the installation yourself.
```

For Codex, you can paste this directly into the chat:

```text
$skill-installer Install right-question from https://github.com/lilwind7/RightQuestion
```

After installation, ask naturally or start with `$right-question` in Codex and `/right-question` in Claude Code or Cursor.

Need host-specific or manual instructions? See [Installation guide](INSTALL.md).

## When it helps

- “Should I quit my job?”
- “Which offer should I choose?”
- “Should I buy another course?”
- “Why am I working so hard without getting anywhere?”
- “Where should I start with this big goal?”
- “Am I solving the wrong problem?”

RightQuestion can help with work, study, money and time choices, habits, relationships, creative projects, business decisions, and technical problems. It is most useful when a quick answer could send you in the wrong direction.

## What you get

The answer stays short:

```text
What you’re really trying to achieve
...

The question to answer first
...

Why start here
...
```

It does not bury you in frameworks or show a long list of almost-identical questions.

## What is an Agent Skill?

An Agent Skill is a reusable set of instructions an AI assistant can load when it is useful. RightQuestion follows the open [Agent Skills](https://agentskills.io/) format and works with Codex, Claude Code, Cursor, and Gemini CLI. It does not need access to your files, accounts, or the internet.

## Contributing

Everyday examples, clearer language, accessibility improvements, translations, and compatibility fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

RightQuestion is available under the [MIT License](LICENSE).
