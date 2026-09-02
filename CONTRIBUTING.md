# Contributing to RightQuestion

RightQuestion should remain small, portable, and behaviorally sharp. Contributions are most useful when they improve how the skill identifies and completes the work that actually advances the user's intended outcome.

## Good contributions

- A realistic input where the skill follows the wording but solves the wrong problem
- A case where the skill reframes correctly but stops instead of completing the requested work
- A false-positive trigger where a factual or well-framed execution request should stay untouched
- A clearer distinction between evidence, constraints, assumptions, proposed solutions, and authorized actions
- A compatibility fix backed by current host documentation
- A translation that preserves meaning rather than translating word for word

## Change process

1. Describe the input, the observed failure, and the desired behavior.
2. Make the narrowest change that addresses that failure without attracting unrelated requests.
3. Put essential behavior in `SKILL.md`; put conditional detail in `references/`.
4. Keep platform-specific metadata outside the portable instructions.
5. Run the checks below.

```bash
python3 -m unittest discover -s tests -v
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

The second command is available in Codex's bundled `skill-creator`; its exact installation path varies. If it is unavailable, verify the [Agent Skills specification](https://agentskills.io/specification) manually.

## Behavioral review checklist

- Does the description say what the skill does and when it applies?
- Does the skill preserve explicit goals, constraints, delivery type, and authorization boundaries?
- Can the transformed working problem differ materially from the input?
- Does resolving it advance the user's intended outcome more than literal completion would?
- Does the agent continue to answer, decide, diagnose, plan, create, or execute after reframing?
- Does it ask the user only for information the agent cannot obtain or safely infer?
- Does a straightforward fact or well-framed task remain straightforward?
- Are internal candidates and frameworks hidden from the default output?
- Do referenced files have a clear reason to be loaded?

Avoid adding a universal rule for a single anecdote. A focused example in `references/examples.md` is often the better first change.
