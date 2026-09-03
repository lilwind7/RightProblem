# Contributing to RightProblem

RightProblem should remain small, portable, and behaviorally sharp. Contributions are most useful when they improve how the skill identifies what matters most now and creates meaningful progress without overstating certainty or completion.

## Good contributions

- A realistic input where the skill follows the wording but solves the wrong problem
- A case that improves the transition from reframing to an answer, action, experiment, or useful checkpoint
- An open-ended goal where the skill claims more certainty or completion than the evidence supports
- A false-positive trigger where a factual or well-framed execution request should stay untouched
- A clearer distinction between evidence, constraints, assumptions, proposed solutions, and authorized actions
- A clearer, shorter default response that preserves the quality of the internal reasoning
- A compatibility fix backed by current host documentation
- A translation that preserves meaning rather than translating word for word

## Change process

1. Describe the input, the observed failure, and the desired behavior.
2. Make the narrowest change that addresses that failure without attracting unrelated requests.
3. Put essential behavior in `SKILL.md`; put conditional detail in `references/`.
4. Keep platform-specific metadata outside the portable instructions.
5. Exercise the relevant cases in [tests/behavior_cases.md](tests/behavior_cases.md) on the target agent and assess the behavioral invariants rather than exact wording.
6. Run the checks below.

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
- For bounded work, does the agent complete and verify the requested result after reframing?
- For open work, does it create useful progress and stop at a justified checkpoint without claiming the long-term goal is complete?
- Does it continue within the same invocation when the next step is clear, executable, and in scope?
- Does it ask the user only for information the agent cannot obtain or safely infer?
- Does a straightforward fact or well-framed task remain straightforward?
- Is the default output led by the result or action, with only decision-relevant reasoning and uncertainty exposed?
- Are internal candidates, scores, and framework names hidden from the default output?
- Do referenced files have a clear reason to be loaded?

Avoid adding a universal rule for a single anecdote. A focused example in `references/examples.md` is often the better first change.
