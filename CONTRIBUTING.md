# Contributing to RightQuestion

RightQuestion should remain small, portable, and behaviorally sharp. Contributions are most useful when they improve a decision the skill makes rather than add general prompting advice.

## Good contributions

- A realistic input where the skill paraphrases instead of reframing
- A false-positive trigger where a factual or execution request should stay untouched
- A clearer distinction between evidence, constraints, assumptions, and proposed solutions
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

- Does the description say both what the skill does and when it applies?
- Does the skill preserve explicit goals and real constraints?
- Can the resulting question be genuinely different from the input?
- Would answering it change a consequential next decision?
- Does a straightforward factual question remain straightforward?
- Are internal candidates and frameworks hidden from the default output?
- Do referenced files have a clear, conditional reason to be loaded?

Avoid adding a universal rule for a single anecdote. A focused example in `references/examples.md` is often the better first change.
