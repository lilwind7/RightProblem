<h1 align="center">RightQuestion</h1>

<p align="center"><strong>Do not just answer the request literally. Solve the problem the user actually means.</strong></p>

<p align="center"><a href="README.zh-CN.md">简体中文</a></p>

RightQuestion changes how an AI agent interprets work. It looks past the first wording, identifies the problem most likely to produce the result you want, and then keeps working—answering, deciding, diagnosing, planning, creating, or executing as the task requires.

It does not hand you a different question and stop.

You do not need to understand prompts, agents, or programming.

## See the difference

> **You ask:** I have already taken three courses but still cannot finish a portfolio project. Should I buy another course?

A literal answer compares prices, lessons, and reviews. RightQuestion recognizes that the real job is to turn what you already know into completed work. The agent then gives you a practical way to find the actual blocker and decides whether any additional course is justified.

Reframing is the agent's internal step. The useful answer or completed work is what you receive.

## What it does

1. Understands the result you are trying to achieve, not only the words you used.
2. Tests whether your assumed cause, proposed solution, or limited set of options is pointing at the wrong work.
3. Reframes the task internally and continues until it has answered or completed the problem that matters.

If a crucial piece of information can only come from you, the agent asks one focused question and continues after you answer. It does not make you do analysis it can perform itself.

## Install it in your AI assistant

If your AI assistant supports Agent Skills, send it this message and let it handle the installation:

```text
Install the right-question Agent Skill from https://github.com/lilwind7/RightQuestion for my user account. Verify that it is available, then tell me the simplest way to use it. Do not ask me to run terminal commands unless you cannot complete the installation yourself.
```

For Codex, you can paste this directly into the chat:

```text
$skill-installer Install right-question from https://github.com/lilwind7/RightQuestion
```

After installation, describe your question or task naturally, or start with `$right-question` in Codex and `/right-question` in Claude Code or Cursor. The agent will reframe when useful and continue with the work.

Need host-specific or manual instructions? See [Installation guide](INSTALL.md).

## When it helps

- “Should I quit my job?”
- “Which offer should I choose?”
- “Should I buy another course?”
- “Why am I working so hard without getting anywhere?”
- “Should we use the solution I already have in mind?”
- “Am I solving the wrong problem?”

RightQuestion can help with work, study, money and time choices, habits, relationships, creative projects, business decisions, and technical problems. It is most useful when a fast literal answer could send the work in the wrong direction.

## What you get

You get the result the task calls for: an answer, recommendation, diagnosis, plan, artifact, code change, or completed action within the agent's capabilities and your authorization.

There is no fixed three-heading response. When a major reframing matters, the agent may briefly explain what changed, then proceeds with the solution. The deeper reasoning and model comparison stay internal unless you ask for them.

## What is an Agent Skill?

An Agent Skill is a reusable set of instructions an AI assistant can load when it is useful. RightQuestion follows the open [Agent Skills](https://agentskills.io/) format and works with Codex, Claude Code, Cursor, and Gemini CLI. It does not itself require access to your files, accounts, or the internet; any tools needed for the task remain subject to the agent's normal permissions.

## Contributing

Everyday examples, clearer language, accessibility improvements, translations, and compatibility fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

RightQuestion is available under the [MIT License](LICENSE).
