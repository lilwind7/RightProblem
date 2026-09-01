---
name: right-question
description: Help people find the one question that matters most before they decide or act. Use when someone feels stuck, is choosing between options, keeps trying without progress, asks “Should I do X?”, or may be solving the wrong problem—in work, life, learning, relationships, creative projects, business, or technical decisions. Skip simple factual questions and clear execution requests.
license: MIT
metadata:
  version: "1.1.0"
---

# RightQuestion

Help the user find the question they most need to answer, not merely a cleaner version of the question they happened to ask.

The user's first question is a clue. It may mix together what they want, what they know, what they assume, and a solution they already have in mind. Keep the result they care about and any real constraints, but let the question itself change completely when that would help more.

## When to use

Use this skill when the user:

- asks “Should I do X?” or “Which option should I choose?”
- feels stuck, conflicted, overwhelmed, or unsure where to start
- keeps working on something without getting the result they want
- asks for tactics before the real obstacle is clear
- may be treating one possible solution as the only solution

Do not force this process onto a simple request for a fact or a clearly defined task. Answer those normally.

## Method

### 1. Find the result behind the question

Separate the input into:

- what the user ultimately wants to be different
- what is known about the current situation
- real constraints that cannot be ignored
- guesses about why the problem exists
- solutions already being considered
- the question the user explicitly asked

Ask internally:

> If the user got a perfect answer to their original question, what would they hope becomes better afterward?

Treat an inferred goal as uncertain. Ask one short clarifying question only when different plausible goals would lead to very different questions and a wrong guess would matter. Otherwise continue and make the uncertainty visible.

### 2. Loosen the original framing

Temporarily set aside the explicit question. Do not assume that the named solution is necessary, that the suspected cause is correct, or that the problem exists at the level where the user described it.

Keep the desired result, relevant evidence, and real constraints. Reopen everything else.

### 3. Consider different questions

Internally generate genuinely different candidates. Look across possible root causes, current obstacles, behavior, incentives, risks, value, capabilities, and next steps when relevant. Do not generate a list of paraphrases.

For a broad or difficult situation where the candidates are too similar, read [references/lenses.md](references/lenses.md) and use only the perspectives that open a meaningfully different path.

### 4. Choose the question that changes the most

Prefer the question whose reliable answer would most improve the user's chance of getting the result they want. Consider:

- how strongly the answer affects the outcome
- how uncertain and important the answer currently is
- whether it would change what the user does next
- whether it gets closer to the reason the problem exists
- whether answering it is worth the effort

Apply this final test:

> If the user could get a trustworthy answer to only one question before acting, which answer would help them most?

### 5. Respond simply

Use the user's language and everyday words. Translate the output labels naturally when needed. Do not mention frameworks or internal scoring unless asked.

By default, return:

**What you’re really trying to achieve**

[One short sentence. Mark uncertainty when inferred.]

**The question to answer first**

[One question.]

**Why start here**

[A brief explanation of how the answer would help more than the original question.]

Follow an explicit request for a shorter format. Include at most two alternatives, and only when they point to genuinely different, valuable paths. Do not show the full candidate set.

## Guardrails

- Do not merely polish, broaden, or make the original question sound smarter.
- Do not keep a proposed solution just because the user mentioned it first.
- Do not ignore goals or constraints the user clearly stated.
- Do not turn the response into a lecture or a display of reasoning frameworks.
- Ask for clarification only when the ambiguity is both important and costly.
- Return the question rather than solving the whole problem unless the user also asks to continue.

When the difference between a paraphrase and a useful new question is unclear, read [references/examples.md](references/examples.md).

## Success criterion

The user should feel:

> I came looking for an answer, but this is the question I actually needed.
