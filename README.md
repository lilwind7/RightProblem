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

## Try it now — no installation

Copy the text below into ChatGPT, Claude, Gemini, or almost any other AI assistant. Replace the last line with your own question.

```text
Before answering my question, help me find the question I most need to answer.

Look past the way I first described the problem. Work out what result I actually want, which assumptions I may be making, and whether the solution I mentioned is really necessary. Consider several genuinely different questions, then give me only:

1. What I’m really trying to achieve
2. The one question I should answer first
3. Why starting with that question would help more

Use plain language. If my request is simply factual, answer it normally.

My question: [write your question here]
```

That is enough to experience RightQuestion. Nothing needs to be downloaded.

## Keep it in your AI assistant

If your AI assistant supports Agent Skills, send it this message and let it handle the installation:

```text
Install the right-question Agent Skill from https://github.com/lilwind7/RightQuestion for my user account. Verify that it is available, then tell me the simplest way to use it. Do not ask me to run terminal commands unless you cannot complete the installation yourself.
```

For Codex, you can paste this directly into the chat:

```text
$skill-installer Install right-question from https://github.com/lilwind7/RightQuestion
```

After installation, ask naturally or start with `$right-question` in Codex and `/right-question` in Claude Code or Cursor.

ChatGPT web and mobile users can use the no-install text above. [OpenAI's skill documentation](https://developers.openai.com/codex/skills/) currently describes standalone skills for the ChatGPT desktop app and Codex; broadly installable workflows on web and mobile are distributed as plugins.

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
