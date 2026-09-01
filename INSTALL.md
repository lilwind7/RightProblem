# Installation guide

## The easiest method: ask your assistant

Paste this into an AI assistant that can manage Agent Skills and local files:

```text
Install the right-question Agent Skill from https://github.com/lilwind7/RightQuestion for my user account. Verify that it is available, then tell me the simplest way to use it. Do not ask me to run terminal commands unless you cannot complete the installation yourself.
```

Review any permission request before approving it. RightQuestion itself contains instructions and examples only; it does not run tools or access external services.

## Codex

Paste this into a Codex chat:

```text
$skill-installer Install right-question from https://github.com/lilwind7/RightQuestion
```

If it does not appear immediately, restart Codex. Then use `$right-question` or ask naturally.

## Claude Code and Cursor

Paste the general installation request above into the agent. Both products support `SKILL.md` skills and can place the folder in the correct user-level location. After installation, use `/right-question` or ask naturally.

## Gemini CLI

Gemini CLI can install directly from GitHub:

```text
gemini skills install https://github.com/lilwind7/RightQuestion
```

Then start a new session or run `/skills reload`.

## Manual and developer installation

If you prefer a local checkout, download or clone this repository and run:

```bash
python3 scripts/install.py
```

On Windows:

```powershell
py scripts/install.py
```

The default installs user-level copies for Codex, Claude Code, Cursor, and Gemini CLI. Existing installations are never overwritten silently.

Useful options:

```bash
python3 scripts/install.py --agent claude
python3 scripts/install.py --agent universal
python3 scripts/install.py --scope project --agent all
python3 scripts/install.py --agent codex --method link
python3 scripts/install.py --dry-run
python3 scripts/install.py --force
python3 scripts/install.py --uninstall
```

`--force` backs up a different existing installation before replacing it. Run `python3 scripts/install.py --help` for all options.

## Skill locations

| Host | User-level | Project-level | Official documentation |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/right-question` | `.agents/skills/right-question` | [Build skills](https://developers.openai.com/codex/skills/) |
| Claude Code | `~/.claude/skills/right-question` | `.claude/skills/right-question` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) |
| Cursor | `~/.cursor/skills/right-question` | `.cursor/skills/right-question` | [Agent Skills](https://cursor.com/docs/skills) |
| Gemini CLI | `~/.gemini/skills/right-question` | `.gemini/skills/right-question` | [Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| Portable alias | `~/.agents/skills/right-question` | `.agents/skills/right-question` | Supported by Codex, Cursor, and Gemini CLI |

If a running host does not discover the new skill, reload its skills or restart it.
