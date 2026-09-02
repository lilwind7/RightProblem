---
name: right-question
description: Reframe a potentially misframed request into the real problem that best serves the user's intended outcome, then continue to answer, decide, diagnose, plan, create, or execute until that problem is handled. Use when wording, a proposed solution, an assumed cause, or a limited option set may point the agent at the wrong work, including stuck decisions and repeated effort without progress. Skip simple factual requests and well-framed execution tasks.
license: MIT
metadata:
  version: "2.0.1"
---

# RightQuestion

Turn the user's request into the right working problem, then solve it.

Use reframing as an internal routing step: select the working problem that best serves the intended outcome, then answer or execute it. Keep the experience simple without simplifying the reasoning, and continue until the task is handled as fully as the available context, capabilities, and authorization allow.

## When to use

Use this skill when a different problem formulation could materially change the work or improve the chance of achieving the user's intended outcome. Typical signals include:

- a proposed solution disguised as the task: “Should I do X?”
- a narrow tactic or implementation request made before the real obstacle is known
- an assumed cause presented without evidence
- a choice artificially limited to the options named by the user
- repeated effort without meaningful progress
- a decision dominated by an untested assumption, risk, incentive, or bottleneck

Apply the full reframing method only when it could materially improve the work. Carry out straightforward fact requests and well-framed execution tasks normally. When the skill is explicitly invoked, first assess whether the original framing is already the right one.

## Method

### 1. Recover the intended outcome and delivery contract

Separate the input into:

- the outcome the user ultimately wants
- what success would look like, including any relevant time horizon
- the type of work requested: answer, explanation, recommendation, decision, diagnosis, plan, research, creation, change, or other execution
- current evidence and known facts
- real constraints that must be respected
- assumptions about causes or consequences
- proposed solutions or favored options
- the immediate action or decision being requested

Ask internally:

> If the literal request were completed perfectly, what real-world result would the user hope becomes better afterward?

Distinguish the intended outcome from a proxy, tactic, metric, convention, or borrowed expectation. Respect any goal the user clearly chose.

Preserve the user's delivery contract. A request to implement something results in implementation; a request for a recommendation results in a recommendation. Reframing may change the route, while the agent remains responsible for completing the requested type of work.

Keep the transformed work within the original scope, side-effect boundaries, explicit constraints, and required approvals.

### 2. Clarify only when necessary

Treat inferred goals as uncertain. Ask one concise clarifying question only when plausible goals would lead to materially different work and choosing incorrectly would be costly, difficult to reverse, or likely to invalidate the result.

When clarification is truly required, return the single blocking question in the current turn and resume the full workflow after the user answers. For noncritical gaps, state a reasonable assumption and continue. Investigate directly whenever the necessary information is available through the provided context, system, files, data, sources, or tools.

### 3. Reopen the problem space

Treat the following as hypotheses rather than constraints:

- the literal wording of the request
- the suspected cause
- the proposed solution
- the assumed option set
- the level at which the problem was described
- the implied sequence of steps

Preserve the intended outcome, evidence, real constraints, delivery contract, and authorization boundary. Consider whether the useful working problem sits at the level of the goal, system, bottleneck, cause, decision, intervention, or implementation. Moving upward is not automatically better; change levels only when doing so could change the work or result.

For every nontrivial reframing, read [references/lenses.md](references/lenses.md). Select several relevant lenses from different families and internally generate a diverse set—usually 5–15—of genuinely competing problem formulations.

Each candidate should express a distinct theory of what actually needs to be resolved and what successful completion would accomplish. Across the set, consider relevant differences such as:

- the real outcome or definition of success
- root cause versus visible symptom
- current bottleneck versus a later concern
- behavior, incentives, capability, or environment
- user value and unmet need
- risk, reversibility, opportunity cost, or second-order effects
- a crucial unknown that could reverse the decision
- the smallest intervention or test that can produce useful evidence

When the user proposes a solution, include a formulation that challenges it and another that gives it a fair path to win. Reject candidates that merely paraphrase the request, assume an unsupported diagnosis, are too vague to complete, violate the delivery contract, exceed the authorized scope, or would leave the central obstacle untouched.

### 4. Select the working problem by goal leverage

Choose the formulation whose successful resolution would most improve the probability of achieving the user's intended outcome. **Goal leverage dominates all other criteria.** Evaluate serious candidates on:

- **Causal importance:** how strongly the underlying factor affects the outcome
- **Decision-relevant information gain:** how much plausible findings could change the action
- **Rootness:** whether it reaches a cause or binding constraint rather than a symptom
- **Completion value:** how much solving it would advance the requested result
- **Urgency and irreversibility:** whether delay or a wrong move creates disproportionate cost
- **Feasibility:** whether it can be resolved with justified effort, available evidence, and permitted actions

Run a counterfactual tournament between the strongest formulations:

1. If this problem were solved, how much would the intended outcome improve?
2. If the literal request were completed instead, would the central obstacle remain?
3. Could plausible findings lead to meaningfully different actions?
4. Does this target the current limiting factor rather than a later-stage concern?
5. Is it concrete enough to resolve and within the user's scope and authorization?

Apply the final test:

> If the agent could complete only one piece of work in this turn, which problem's resolution would most advance the result the user actually wants?

Select one working problem. It may be a question, diagnosis, decision, outcome, or execution target, and it becomes the target for the rest of the workflow.

For a narrow technical request, move upward to a product, business, or system concern only when that concern changes the technical choice. Otherwise keep the working problem technical and solve it at the appropriate level.

### 5. Solve or execute the transformed problem

Immediately continue from reframing to completion. Match the original delivery contract:

- **Answer or explain:** answer the transformed question and support the conclusion.
- **Recommend or decide:** analyze the decisive tradeoffs and give a recommendation or decision rule.
- **Diagnose:** inspect the available evidence, identify the most likely cause, and validate it where possible.
- **Plan:** produce a plan that addresses the actual constraint and leads to the intended outcome.
- **Research:** gather and synthesize the information needed to resolve the working problem.
- **Create or change:** make the artifact or in-scope change, then verify the result.

Use available tools and context to inspect the provided system, files, data, or sources and complete the requested work directly.

If the better route requires a materially different external action or broader authority than the user granted, complete the safe in-scope reasoning and ask for authorization before that action. If progress is genuinely blocked by missing user-only information, ask the smallest question that unlocks the work, then continue after the answer.

If the user explicitly requests only the right question or problem formulation, deliver that formulation and its concise rationale. In every other case, proceed to resolution after any necessary blocking clarification.

### 6. Respond with the completed work

Lead with the answer, result, recommendation, diagnosis, plan, or completed change. Let the task and the user's requested format determine the response structure.

When the transformation is substantial and knowing it helps the user evaluate the result, briefly state the working problem or changed assumption, then immediately continue with the solution. Otherwise keep the reframing internal.

Use the user's language and follow their requested format. Keep the candidate set, scores, model inventory, and chain of reasoning internal unless the user explicitly asks for an appropriate summary.

## Guardrails

- Complete the selected working problem within the same workflow.
- Preserve the user's requested delivery type and take responsibility for the work the agent can perform.
- Treat proposed solutions, assumed causes, option sets, and problem levels as hypotheses.
- Preserve explicit goals, constraints, deliverables, and authorization boundaries.
- Change the abstraction level only when doing so improves the actual choice or result.
- Prefer the original framing whenever it already targets the highest-leverage work.
- Keep frameworks and internal candidate comparisons out of the default response.

When calibration is useful or the difference between useful transformation and unhelpful redirection is unclear, read [references/examples.md](references/examples.md).

## Success criterion

The user should feel:

> The agent understood what I was really trying to accomplish and handled the work that mattered.
