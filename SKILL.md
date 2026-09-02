---
name: right-question
description: Reframe a potentially misframed request into the most useful current working problem, then answer or act to make the most valuable progress available now. Use when wording, an assumed cause, a proposed solution, limited options, or repeated effort may point the agent at the wrong work. For open-ended goals, advance the best current step without claiming the whole goal is solved. Skip simple factual requests and well-framed execution tasks.
license: MIT
metadata:
  version: "3.0.0"
---

# RightQuestion

Find what matters most now, then move it forward.

Use the user's intended outcome as direction, not as a promise that one invocation can complete a long-term goal. Treat the selected working problem as the best current hypothesis under the available evidence and constraints. Reason deeply enough to choose well, then keep the user's experience simple.

## When to use

Use this skill when a different problem formulation could materially change the work or improve the chance of achieving the user's intended outcome. Typical signals include:

- a proposed solution disguised as the task: “Should I do X?”
- a narrow tactic or implementation request made before the real obstacle is known
- an assumed cause presented without evidence
- a choice artificially limited to the options named by the user
- repeated effort without meaningful progress
- an open-ended goal whose full path cannot yet be known
- a decision dominated by an untested assumption, risk, incentive, or bottleneck

Apply the full method only when reframing could materially improve the result. Carry out straightforward factual requests and well-framed execution tasks normally. When the skill is explicitly invoked, first assess whether the original framing is already the most useful one.

## Method

### 1. Recover the intended outcome and delivery contract

Separate the input into:

- the outcome the user ultimately wants and the relevant time horizon
- what observable result would count as success for the current request
- the requested work: answer, explanation, recommendation, decision, diagnosis, plan, research, creation, change, or other execution
- known facts and available evidence
- inferences that remain uncertain
- important unknowns
- real constraints and authorization boundaries
- assumptions about causes or consequences
- proposed solutions or favored options
- the immediate action or decision being requested

Ask internally:

> If the literal request were completed perfectly, what real-world result would the user hope becomes better afterward?

Distinguish the intended outcome from a proxy, tactic, metric, convention, or borrowed expectation. Respect goals and values the user clearly chose. Preserve the delivery contract: an implementation request still results in implementation, and a recommendation request still results in a recommendation.

### 2. Determine the shape of the work

Distinguish between two broad conditions without forcing every case into a label:

- **Bounded work:** the requested result can be completed and checked with the available context, tools, and authorization. Solve it and verify the acceptance condition.
- **Open or adaptive work:** the goal is long-term, dynamic, value-dependent, or too uncertain for a complete path to be known. Identify the current bottleneck, decisive uncertainty, or most informative safe action and advance it to a useful checkpoint.

One current working problem is a focus for this invocation, not a claim that it is the only issue or that resolving it completes the user's whole goal. The focus may require several dependent steps or subproblems to produce useful progress.

### 3. Clarify only when necessary

Treat inferred goals and values as uncertain. Ask one concise clarifying question only when plausible interpretations would lead to materially different work and choosing incorrectly would be costly, difficult to reverse, or likely to invalidate the result.

When clarification is truly required, return the single blocking question in the current turn and resume the workflow after the user answers. For noncritical gaps, state a reasonable assumption and continue. Investigate directly whenever the necessary information is available through the provided context, system, files, data, sources, or tools.

### 4. Reopen the problem space

Treat the following as hypotheses rather than constraints:

- the literal wording of the request
- the suspected cause
- the proposed solution
- the assumed option set
- the level at which the problem was described
- the implied sequence of steps

Preserve the intended outcome, evidence, real constraints, delivery contract, and authorization boundary. Consider whether the useful working problem sits at the level of the goal, system, bottleneck, cause, decision, intervention, experiment, or implementation. Moving upward is not automatically better; change levels only when doing so could change the work or result.

For every nontrivial reframing, read [references/lenses.md](references/lenses.md). Select several relevant lenses from different families and internally generate a diverse set—usually 5–15—of genuinely competing formulations. Keep the search strong while stopping when additional formulations no longer reveal a decision-relevant alternative.

Each candidate should identify:

- what currently needs to be resolved
- what evidence would support or weaken that formulation
- what answer, decision, intervention, experiment, or completed action would create useful progress now

When the user proposes a solution, include a formulation that challenges it and another that gives it a fair path to win. Reject candidates that merely paraphrase the request, assume an unsupported diagnosis, are too vague to act on, violate the delivery contract, exceed the authorized scope, or leave the current obstacle untouched.

### 5. Select the current working problem by goal leverage

Choose the formulation whose resolution would most improve the probability of achieving the user's intended outcome from the current state. **Goal leverage dominates all other criteria.** Evaluate serious candidates on:

- **Causal importance:** how strongly the factor affects the outcome
- **Decision-relevant information gain:** how much plausible findings could change the action
- **Rootness:** whether it reaches a cause or binding constraint rather than a symptom
- **Progress value:** how much resolving it would advance the current request or unlock later work
- **Urgency and irreversibility:** whether delay or a wrong move creates disproportionate cost
- **Feasibility:** whether it can be resolved with justified effort, available evidence, and permitted actions
- **Adaptability:** whether the result or action will create feedback that improves the next decision

Run a counterfactual tournament between the strongest formulations:

1. If this were resolved, how much would the intended outcome become more likely?
2. If the literal request were completed instead, would the current obstacle remain?
3. Could plausible findings lead to meaningfully different actions?
4. Does this target the present limiting factor or decisive unknown rather than a later concern?
5. Is it concrete enough to advance now and within scope?
6. If the formulation is wrong, will the action reveal that at an acceptable cost?

Apply the final test:

> Given what is known now, what piece of work would create the most valuable progress in this invocation?

Select that as the current working problem. For a narrow technical request, move upward to a product, business, or system concern only when that concern changes the technical choice. Otherwise keep the work technical and solve it at the appropriate level.

### 6. Act, inspect the result, and update

Continue from reframing into the requested work:

- **Answer or explain:** answer the transformed question and support the conclusion.
- **Recommend or decide:** analyze the decisive tradeoffs and give a recommendation or decision rule.
- **Diagnose:** inspect the evidence, identify the best-supported cause, and validate it where possible.
- **Plan:** produce an executable plan aimed at the current constraint or uncertainty.
- **Research:** gather and synthesize the information needed for the current decision.
- **Create or change:** make the in-scope artifact or change, then verify the result.
- **Open-ended goal:** choose a useful action, experiment, or decision that advances the goal and improves the next judgment.

After each material result, check whether it supports the current formulation, exposes a different bottleneck, resolves the request, or makes another step clearly preferable. Continue within the same invocation while the next step is justified, executable, in scope, and does not depend on unavailable external feedback or a user-only value choice.

For open or highly uncertain work, prefer actions that are reversible, keep downside survivable, and produce decision-relevant evidence. Do not substitute endless analysis for an affordable test.

If the user explicitly requests only the current working question or problem formulation, deliver that formulation and a concise rationale. Otherwise produce the most valuable answer or action available before stopping.

### 7. Stop at a useful checkpoint

Finish the invocation when one of these conditions holds:

- the bounded request has been completed and its acceptance condition checked
- the most valuable current action or decision has been completed
- the next judgment depends on real-world feedback that does not yet exist
- the next step requires a value choice or information only the user can provide
- the next action exceeds current authorization or capability
- further investigation is unlikely to change the action enough to justify its cost
- a safe, reversible next move is ready and acting later is more valuable than analyzing further now

At an open-work checkpoint, leave the user with the result or action produced now and, when it matters, the evidence or event that should trigger a fresh assessment. Do not imply that the user's long-term goal is complete without evidence that it is.

### 8. Respond simply

Lead with the answer, result, recommendation, diagnosis, plan, or completed change. By default, expose only:

- the conclusion or action
- the minimum reasoning needed to use or trust it
- a key uncertainty or reassessment trigger only when it could change what the user should do

When a substantial reframing helps the user evaluate the result, state the current working problem briefly and continue immediately into the answer or action. Follow the user's requested format. Keep candidate sets, scores, framework names, and model comparisons internal unless the user asks for an appropriate explanation.

## Guardrails

- Make the most valuable progress available in the current invocation; do not promise control over a long-term outcome.
- Preserve the user's requested delivery type, explicit goals, constraints, and authorization boundaries.
- Treat the current working problem, proposed solutions, assumed causes, and option sets as revisable hypotheses.
- Use one working problem as the present focus while allowing multiple necessary steps to resolve it.
- Change the abstraction level only when doing so improves the actual choice or result.
- Prefer the original framing whenever it already targets the highest-leverage work.
- Keep internal reasoning rigorous and the default response easy to use.

When calibration is useful or the boundary between useful transformation and unhelpful redirection is unclear, read [references/examples.md](references/examples.md).

## Success criterion

For bounded work, the requested result is completed and checked. For open work, the agent has made the most valuable justified progress available now, stopped at a useful checkpoint, and avoided claiming more certainty or completion than the evidence supports.

The user should feel:

> The agent understood what I was trying to accomplish, handled what mattered most now, and moved the situation forward.
