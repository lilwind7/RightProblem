<h1 align="center">RightQuestion</h1>

<p align="center"><strong>Don't optimize the question you were given. Find the question worth answering.</strong></p>

<p align="center"><a href="README.zh-CN.md">简体中文</a></p>

RightQuestion is a portable [Agent Skill](https://agentskills.io/) for finding the single question that would most advance a user's real goal. It separates the desired outcome from the original framing, assumptions, and proposed solution, then selects the highest-leverage uncertainty to resolve next.

## What changes

> **Original:** Should every database operation use a transaction?
>
> **RightQuestion:** Which multi-step operations on critical business paths can enter a partially completed state that causes unacceptable and non-self-recoverable consequences?

The second question creates the basis for choosing among transactions, idempotency, compensation, state machines, or accepting temporary inconsistency. It targets the consequence that should drive the implementation choice.

## Install in 30 seconds

Download or clone this repository, then run:

```bash
python3 scripts/install.py
```

On Windows:

```powershell
py scripts/install.py
```

The default installs user-level copies for Codex, Claude Code, Cursor, and Gemini CLI. Existing installations are never overwritten silently.

Install only one host or install into the current project:

```bash
python3 scripts/install.py --agent claude
python3 scripts/install.py --agent universal
python3 scripts/install.py --scope project --agent all
```

Use a symlink while developing, preview operations, safely update, or uninstall:

```bash
python3 scripts/install.py --agent codex --method link
python3 scripts/install.py --dry-run
python3 scripts/install.py --force
python3 scripts/install.py --uninstall
```

`--force` moves the previous version to `.right-question-backups` before replacing it. Run `python3 scripts/install.py --help` for every option.

## Use it

Ask naturally when the agent supports automatic skill selection, or invoke it explicitly:

| Host | Example |
| --- | --- |
| Codex | `$right-question Should we build a mobile app?` |
| Claude Code | `/right-question Should we build a mobile app?` |
| Cursor | `/right-question Should we build a mobile app?` |
| Gemini CLI | `Use the right-question skill: should we build a mobile app?` |

Good inputs include:

- `Should I use microservices for this product?`
- `How can I grow my newsletter faster?`
- `We keep missing deadlines—what should we change?`
- `I have three job offers. How should I choose?`
- `Find the question I should answer before committing to this plan.`

The default response is deliberately small:

```text
Underlying goal
...

Highest-leverage question
...

Why this question
...
```

## Compatibility

RightQuestion uses the open Agent Skills format and has no tool or network dependency.

| Host | User-level path | Project-level path | Documentation |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/right-question` | `.agents/skills/right-question` | [Build skills](https://developers.openai.com/codex/skills/) |
| Claude Code | `~/.claude/skills/right-question` | `.claude/skills/right-question` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) |
| Cursor | `~/.cursor/skills/right-question` | `.cursor/skills/right-question` | [Agent Skills](https://cursor.com/docs/skills) |
| Gemini CLI | `~/.gemini/skills/right-question` | `.gemini/skills/right-question` | [Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| Portable alias | `~/.agents/skills/right-question` | `.agents/skills/right-question` | Supported by Codex, Cursor, and Gemini CLI |

If a running host does not discover a new installation immediately, reload its skills or restart it.

## How it works

The skill follows five moves:

1. Recover the desired outcome, evidence, constraints, assumptions, and proposed solution.
2. Reopen the problem without treating the original framing as truth.
3. Generate genuinely different candidate questions.
4. Rank them by causal importance, information gain, actionability, and investigation cost—with goal leverage dominant.
5. Return the one question whose reliable answer would most improve the chance of success.

Detailed thinking lenses and calibration examples live in `references/` and are loaded only when useful, keeping the default agent context compact.

## Project structure

```text
right-question/
├── SKILL.md                 Portable skill instructions
├── agents/openai.yaml       Codex and ChatGPT UI metadata
├── references/              On-demand lenses and examples
├── scripts/install.py       Cross-platform installer
└── tests/test_install.py    Installer behavior tests
```

## Contributing

Behavioral examples, clearer trigger boundaries, host compatibility improvements, and translations are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change.

RightQuestion is available under the [MIT License](LICENSE).
