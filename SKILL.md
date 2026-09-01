---
name: right-question
description: Reframe solution-first, narrow, or possibly misframed requests into the single question whose answer would most improve the user's chance of reaching the real goal. Use for “Should I use X?”, “How do I implement Y?”, stuck decisions, plans, diagnoses, and broad goals where the stated question may not target the real bottleneck. Skip straightforward factual or execution requests whose framing is not materially limiting progress.
license: MIT
metadata:
  version: "1.0.0"
---

# RightQuestion

Find the question the user should answer next, not a polished version of the question they happened to ask.

Treat the input as evidence about the goal, context, assumptions, and current theory of the problem. Preserve the actual outcome and real constraints; everything else—including the named solution and vocabulary—is provisional.

## Decide whether reframing helps

Apply this method when a different question could materially change the next decision or improve the chance of success. Typical signals include:

- a proposed solution disguised as a question: “Should I use X?”
- a narrow implementation question with an unstated business or engineering consequence
- repeated effort without progress
- a broad goal with no identified bottleneck
- a decision dominated by an untested assumption, risk, or incentive

Do not force reframing onto a straightforward request for facts or execution when there is no meaningful external goal to optimize. Answer that request normally.

## Method

### 1. Reconstruct the real goal

Separate the input into:

- desired outcome
- current evidence and real constraints
- assumptions about causes
- proposed solution
- explicit question

Ask internally:

> If the original question were answered perfectly, what result would the user hope to achieve?

Treat inferred goals as uncertain. If multiple plausible goals would produce materially different questions and choosing incorrectly would be costly, ask one concise clarifying question. Otherwise continue and label the inference.

### 2. Reopen the problem space

Temporarily discard the explicit question. Treat the framing, proposed solution, named concepts, and stated problem level as hypotheses rather than constraints.

Keep only evidence, the desired outcome, and real-world constraints. The final question may use completely different concepts and vocabulary.

### 3. Generate genuinely competing questions

Internally consider several distinct explanations for what most limits progress—for example root cause, bottleneck, behavior, incentives, risk, value, capability, or implementation. Generate a diverse candidate set when the problem supports it; do not create cosmetic paraphrases.

For broad or difficult problems where the candidates converge too quickly, read [references/lenses.md](references/lenses.md) and use only the lenses that create meaningfully different views.

### 4. Select by goal leverage

Choose the candidate whose reliable answer would most improve the probability of reaching the goal. Consider:

- causal importance
- decision-relevant information gain
- proximity to a root cause
- ability to change the next action
- investigation cost

Goal leverage dominates the other criteria. Apply this final test:

> If the user could get a reliable answer to only one question before acting, which answer would most improve their chance of success?

### 5. Return one question

Use the user's language unless they ask otherwise. By default, return:

**Underlying goal**

[One concise sentence. Mark uncertainty when inferred.]

**Highest-leverage question**

[One question.]

**Why this question**

[A brief explanation of why its answer advances the goal more than the original question.]

Follow an explicit request for a shorter format. Include at most two alternatives, and only when they represent genuinely different high-value paths. Do not expose the full candidate set, model inventory, or scoring process unless asked.

## Guardrails

- Do not merely improve wording or make the original question broader.
- Do not preserve a proposed solution just because the user named it.
- Do not discard explicit constraints or override a goal the user clearly chose.
- Move a narrow technical question upward only when the higher-level consequence changes the technical choice.
- Ask for clarification only when ambiguity is both material and costly; useful uncertainty can remain visible in the output.
- Return the question rather than solving the entire underlying problem, unless the user also asks to continue.

When calibration is useful, or when the boundary between reframing and paraphrasing is unclear, read [references/examples.md](references/examples.md).

## Success criterion

The result should make the user think:

> That's not what I originally asked, but that's actually the question I need to answer.
