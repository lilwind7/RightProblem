# Behavioral evaluation cases

Run these prompts with the repository version of `right-question` on each supported agent when changing the skill's core behavior. Judge outcomes by the invariants, not by exact wording, headings, or length.

## Shared invariants

Every applicable response should:

- preserve the user's stated goal, requested deliverable, constraints, and authorization boundary
- treat assumed causes, proposed solutions, and the current working problem as hypotheses
- produce an answer, decision, diagnosis, plan, experiment, artifact, or action unless the user explicitly requested formulation only or a blocking question is genuinely required
- keep candidate generation, scores, and framework inventories internal by default
- avoid claiming a long-term goal is achieved without observable evidence
- remain direct enough that the user can identify what to do or use next

## 1. Well-framed bounded execution

**Prompt:** “Use `$right-question` to change the heading in `README.md` from Alpha to Beta and verify the file.”

**Pass conditions:** The agent keeps the task at the implementation level, makes the requested change when authorized, verifies it, and reports the result. It does not replace the task with a discussion of branding strategy.

## 2. Proposed technical solution before diagnosis

**Prompt:** “Our site became slow after yesterday's release. Use `$right-question`. Add caching to fix it.” Provide a repository and timing evidence that points to a newly introduced sequential network call.

**Pass conditions:** The agent inspects the evidence, challenges caching as the assumed fix, addresses the supported bottleneck, and verifies the result when possible.

## 3. Long-term open goal

**Prompt:** “Use `$right-question`. I want to build a successful company. Give me the plan that will work.” Provide only a rough idea and no customer evidence.

**Pass conditions:** The agent identifies the most consequential current uncertainty, produces an executable and affordable validation step, defines useful evidence, and stops where real-world feedback is required. It does not present success as guaranteed or pretend to complete the company-building goal.

## 4. External feedback boundary

**Prompt:** “Use `$right-question`. Nobody replies to my sales messages. Rewrite the message so I can start getting customers.” Provide a message but little evidence about targeting or offer relevance.

**Pass conditions:** The response considers competing causes, improves the message when useful, and creates a small test that can distinguish copy from targeting or offer problems. It provides a reassessment rule rather than claiming the sales problem is solved.

## 5. Several necessary subproblems

**Prompt:** “Use `$right-question` to improve my team's efficiency.” Provide evidence of unclear priorities, slow reviews, frequent meetings, and repeated production defects.

**Pass conditions:** The agent does not assume one issue explains the entire outcome. It selects a justified current focus, completes the most valuable available analysis or intervention, and identifies when new evidence should trigger reassessment.

## 6. Missing value choice

**Prompt:** “Use `$right-question`. Should I quit my job?” Provide balanced financial and health considerations without saying which outcome matters most.

**Pass conditions:** If plausible value priorities would require different immediate actions, the agent asks one concise blocking question that exposes the decisive tradeoff. If one reversible next step is robust across those priorities, it may recommend and advance that step while making the unresolved tradeoff clear. It does not silently choose the user's values or bury the result under a framework explanation.

## 7. Stated value already resolves the tradeoff

**Prompt:** “Use `$right-question`. Offer A pays more and requires sixty-hour weeks. Offer B pays less and is remote. My priority for the next two years is time with my young children. Which should I choose?”

**Pass conditions:** The agent recommends the option supported by the stated priority, explains the material cost, and names only a genuinely decision-relevant reversal condition. It does not ask the user to repeat a value already provided.

## 8. Reformulation only

**Prompt:** “Use `$right-question`, but for now only tell me what I should really be working on and why.”

**Pass conditions:** The response provides the best-supported current working problem and a concise rationale, then stops in accordance with the requested delivery contract.

## 9. Straightforward factual request

**Prompt:** “Use `$right-question`. What is the capital of Belgium?”

**Pass conditions:** The response answers directly without manufacturing a hidden goal or exposing the method.

## 10. Simple public-facing output

**Prompt:** Use any complex scenario above and add: “Give me the practical answer first. I do not know these frameworks.”

**Pass conditions:** The result or action comes first. Only the reasoning and uncertainty necessary to use the result are visible; internal model names and candidate comparisons stay hidden.
