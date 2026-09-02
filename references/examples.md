# Calibration examples

These examples distinguish reframing as an internal step from reframing as the deliverable. Unless a necessary clarification blocks progress or the user explicitly asks only for a reformulation, continue and solve the transformed problem.

## Buying another course

**Input:** “Should I buy this course? I have already finished three similar courses, but I still cannot complete a portfolio project.”

**Weak behavior:** Ask “What is really stopping you from progressing?” and stop.

**Working problem:** Identify and remove the constraint preventing the user from turning existing knowledge into completed work.

**Correct completion:** Recommend against another general course for now. Give the user a small project to attempt, a way to record the first concrete blocker, and a rule for buying only targeted instruction if that blocker proves to be missing knowledge. The response resolves the purchase decision and advances the real goal.

## A narrow technical solution

**Input:** “Our website is slow. Should we add caching?”

**Weak behavior:** Return “What is the current performance bottleneck?” as homework.

**Working problem:** Locate the measured source of user-visible latency and apply the lowest-risk fix that removes it.

**Correct completion:** When the system, repository, or performance evidence is available, inspect it, determine whether caching addresses the binding constraint, implement the appropriate in-scope fix, and verify the effect. Ask for a trace or measurement only if the necessary evidence is unavailable and cannot be obtained directly. Do not leap to a business-level question unless it changes the technical choice.

## Repeated effort without progress

**Input:** “How can I work harder? I already work ten-hour days, but my important project keeps slipping because my calendar is full of meetings.”

**Weak behavior:** Return “Which work contributes least?” without helping further.

**Working problem:** Protect enough focused capacity for the important project by removing the current scheduling constraint.

**Correct completion:** Produce a concrete calendar triage and focus plan, including which meetings to eliminate, shorten, delegate, or batch and how to reserve project time. More effort is not the solution; reallocating constrained attention is.

## Choosing between options

**Input:** “Offer A pays more but requires sixty-hour weeks. Offer B is remote and pays less. I want more time with my family. Which should I choose?”

**Working problem:** Choose the offer that best satisfies the user's stated priority while making the material tradeoff explicit.

**Correct completion:** Recommend Offer B on the stated evidence, quantify or explain the compensation tradeoff, and name the condition that would reverse the recommendation. Do not merely ask which difference will matter later; the user has already supplied the deciding value.

## High-cost ambiguity

**Input:** “Should I quit my job?”

Income, health, values, another opportunity, and escape from a temporary conflict could produce materially different work, while resignation may be costly to reverse. Ask one concise question about the change the user needs from work, then use the answer to complete the analysis and recommendation. Here clarification is a temporary necessity, not the final product.

## Explicit reformulation-only request

**Input:** “Do not solve this yet. Just help me identify the real problem.”

Return the transformed problem and a concise rationale. Stopping after reframing is correct because the user explicitly requested that delivery contract.

## A factual request

**Input:** “What is the capital of Belgium?”

Answer “Brussels” directly. There is no useful hidden problem to manufacture.
