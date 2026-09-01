---
name: right-question
description: Help people find the one question that matters most before they decide or act. Use when someone feels stuck, is choosing between options, keeps trying without progress, asks “Should I do X?”, or may be solving the wrong problem—in work, life, learning, relationships, creative projects, business, or technical decisions. Skip simple factual questions and clear execution requests.
license: MIT
metadata:
  version: "1.2.0"
---

# RightQuestion

Find the question the user most needs to answer, not merely a cleaner version of the question they happened to ask.

Keep the experience simple without simplifying the reasoning. Work broadly and rigorously internally; expose only the result that helps the user move forward. The user's first question is evidence about their goal, situation, assumptions, and current theory of the problem—not a boundary the final question must stay inside.

## When to use

Use this skill when a different question could materially change the user's decision or improve their chance of reaching the desired outcome. Typical signals include:

- “Should I do X?” or “Which option should I choose?”
- feeling stuck, conflicted, overwhelmed, or unsure where to start
- repeated effort without meaningful progress
- a tactic or implementation request made before the real obstacle is clear
- a proposed solution being treated as the only available solution
- a decision dominated by an untested assumption, risk, incentive, or bottleneck

Do not force reframing onto a straightforward factual request or clearly defined execution task whose framing does not limit progress. Answer those normally.

## Method

### 1. Reconstruct the outcome and decision

Separate the user's input into:

- the outcome they ultimately want
- what success would look like, including any relevant time horizon
- current evidence and known facts
- real constraints that must be respected
- assumptions about causes or consequences
- proposed solutions or favored options
- the immediate decision or action being blocked
- the explicit question they asked

Ask internally:

> If the original question were answered perfectly, what result would the user hope becomes better afterward?

Distinguish the underlying outcome from a proxy, tactic, metric, convention, or borrowed expectation. Do not replace a goal the user clearly chose. Treat inferred goals as uncertain.

Ask one concise clarifying question only when multiple plausible goals would produce materially different winning questions and choosing the wrong goal would be costly. When clarification is necessary, return only that question in the current turn; it is an input to the method, not the final winning question. Resume the full process after the user answers. Otherwise continue and make important uncertainty visible.

### 2. Reopen the problem space

Temporarily remove the explicit question from consideration. Treat the following as hypotheses rather than constraints:

- the user's wording and named concepts
- the suspected cause
- the proposed solution
- the assumed set of options
- the level at which the problem was described

Preserve the desired outcome, evidence, real constraints, and the user's agency. Consider whether the useful question sits at the level of the goal, system, bottleneck, cause, decision, or next experiment. Moving to a more abstract level is not automatically better; change levels only when doing so could change the actual choice.

### 3. Generate competing questions

For every nontrivial case, read [references/lenses.md](references/lenses.md). Select several relevant lenses from different families and internally generate a diverse set—usually 5–15—of genuinely competing candidate questions before choosing one.

Each candidate should represent a distinct hypothesis about what most limits progress or which unknown most affects the decision. Across the set, consider relevant differences such as:

- whether the desired outcome or success criterion is wrong or incomplete
- root cause versus visible symptom
- current bottleneck versus an eventual concern
- behavior, incentives, capability, or environment
- value and unmet need
- risk, reversibility, opportunity cost, or second-order effects
- a crucial unknown that could reverse the decision
- the smallest useful test or next action

Include a candidate that challenges the proposed solution when one is present. Also give the proposed solution a fair path to win if it is genuinely the highest-leverage route.

Reject candidates that are merely paraphrases, embed an unsupported diagnosis, bundle several questions together, are too vague to answer, or would not change any decision under plausible answers.

### 4. Rank by goal leverage

Choose the candidate whose trustworthy answer would most improve the probability of reaching the user's real goal. **Goal leverage dominates all other criteria.** Evaluate each serious candidate on:

- **Causal importance:** how strongly the underlying factor affects the outcome
- **Decision-relevant information gain:** how much plausible answers could change the choice
- **Rootness:** whether it reaches a cause or binding constraint rather than a symptom
- **Actionability:** whether the answer changes what the user can do next
- **Urgency and irreversibility:** whether delay or a wrong move creates disproportionate cost
- **Answerability and investigation cost:** whether the information can be obtained at a justified cost

Do not let an easy, concrete, or immediately actionable question beat a substantially more consequential one merely because it is easier to answer.

Run a counterfactual tournament between the strongest candidates:

1. If the user had a reliable answer to this question, which decision would change?
2. Would meaningfully different plausible answers lead to different actions? If not, information gain is low.
3. If the proposed solution disappeared, would this question still illuminate the goal?
4. Does it target the current limiting factor rather than a later-stage concern?
5. Is it upstream enough to matter but concrete enough to answer and act on?

Apply the final test:

> If the user could get a trustworthy answer to only one question before acting, which answer would most improve their chance of achieving the outcome?

Select one winner. Keep alternatives only when unresolved goal ambiguity or a genuine near-tie makes a single winner misleading.

### 5. Sharpen the winning question

Make the question:

- singular rather than compound
- specific enough to investigate or answer
- neutral about causes and solutions that are not yet established
- connected to a real decision or change in action
- expressed in the user's language

Do not make it sound clever at the expense of usefulness. Preserve any constraint that materially changes the answer.

For a narrow technical question, move upward to a product, business, or system consequence only when that consequence changes the technical choice. Otherwise keep the question technical and improve it at the same level.

### 6. Respond simply

The depth belongs in the internal reasoning, not in the amount of text shown to the user. Use everyday language and translate the labels naturally when needed. Do not mention lenses, candidate counts, scoring, or framework names unless the user asks.

By default, return:

**What you're really trying to achieve**

[One short sentence. Mark uncertainty when inferred.]

**The question to answer first**

[One question.]

**Why start here**

[Briefly explain which decision, assumption, cause, or bottleneck its answer would clarify and why that matters more than the original question.]

Follow an explicit request for a shorter format. Include at most two alternatives, and only when they represent genuinely different, high-leverage paths. Never show the full internal candidate set by default.

## Guardrails

- Never reduce internal reasoning depth merely to make the experience or final wording simpler.
- Do not merely polish, broaden, or make the original question sound smarter.
- Do not preserve a proposed solution just because the user mentioned it first.
- Do not discard explicit goals or real constraints.
- Do not assume that a more strategic, philosophical, or abstract question has more leverage.
- Do not manufacture a hidden problem when the original request is already well framed.
- Do not turn the response into a lecture or a display of reasoning frameworks.
- Return the question rather than solving the entire underlying problem unless the user also asks to continue.

When calibration is useful or the distinction between paraphrasing and reframing is unclear, read [references/examples.md](references/examples.md).

## Success criterion

The user should feel:

> I came looking for an answer, but this is the question I actually needed.
