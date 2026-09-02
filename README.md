<h1 align="center">RightQuestion</h1>

<p align="center"><strong>See what matters most now. Move it forward.</strong></p>

<p align="center"><a href="README.zh-CN.md">简体中文</a></p>

RightQuestion helps an AI assistant look past the first wording of a request, work out what matters most in the current situation, and make useful progress. Depending on the task, that may mean giving an answer, making a recommendation, finding a cause, creating a plan, changing a file, or taking an authorized action.

You do not need to understand prompts, agents, or programming.

## See the difference

> **You ask:** I have already taken three courses but still cannot finish a portfolio project. Should I buy another course?

RightQuestion checks what is actually blocking progress now. The assistant may recommend a small project that exposes the first concrete blocker, then use that evidence to decide whether any additional course is worthwhile.

The deeper comparison happens internally. You receive the decision and a practical next step.

## How it works

1. Understands the result you want.
2. Checks whether an assumed cause, proposed solution, or limited set of options is sending the work in the wrong direction.
3. Chooses the most useful problem to work on with the information available now.
4. Answers or acts, checks the result where possible, and continues while the next step is clear and within scope.

For a task with a verifiable finish, the assistant completes it and checks the result. For a long-term or uncertain goal, it makes the most useful progress available now and leaves a clear point for reassessment when new evidence, real-world feedback, or a user decision is needed.

## Install it in your AI assistant

If your AI assistant supports Agent Skills, send it this message and let it handle the installation:

```text
Install the right-question Agent Skill from https://github.com/lilwind7/RightQuestion for my user account. Verify that it is available, then tell me the simplest way to use it. Do not ask me to run terminal commands unless you cannot complete the installation yourself.
```

For Codex, paste this directly into the chat:

```text
$skill-installer Install right-question from https://github.com/lilwind7/RightQuestion
```

After installation, describe your question or task naturally, or start with `$right-question` in Codex and `/right-question` in Claude Code or Cursor. The assistant will apply the method when it can materially improve the work.

Need host-specific or manual instructions? See the [installation guide](INSTALL.md).

## When it helps

- “Should I quit my job?”
- “Which offer should I choose?”
- “Should I buy another course?”
- “Why am I working so hard without getting anywhere?”
- “Should we use the solution I already have in mind?”
- “What should I focus on first if I want this business to succeed?”

RightQuestion can help with work, study, money and time choices, habits, relationships, creative projects, business decisions, and technical problems. It is most useful when answering the words literally could send the work in the wrong direction.

## What you get

You get something useful for the situation now: an answer, recommendation, diagnosis, plan, experiment, artifact, code change, or authorized action.

The response follows your task and requested format. It leads with the result and only includes the reasoning and uncertainty needed to use it. Deeper model comparisons stay internal unless you ask for them.

## What is an Agent Skill?

An Agent Skill is a reusable way of working that an AI assistant can load when useful. RightQuestion follows the open [Agent Skills](https://agentskills.io/) format and works with Codex, Claude Code, Cursor, and Gemini CLI. RightQuestion itself contains portable instructions; tools used for a task remain subject to the assistant's normal permissions.

## Contributing

Everyday examples, clearer language, behavioral evaluations, translations, and compatibility fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

RightQuestion is available under the [MIT License](LICENSE).
