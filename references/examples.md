# Calibration examples

These examples show the distance between paraphrasing and useful reframing. Adapt the reasoning, not the wording.

## Solution-first product decision

**Input:** “Should we build a mobile app?”

**Likely goal:** Increase repeat customer engagement.

**Weak paraphrase:** “Would a mobile app improve customer engagement?”

**Higher-leverage question:** “What recurring customer job is currently painful enough that people would repeatedly choose a dedicated experience over the channels they already use?”

The better question tests whether the proposed solution has a durable reason to exist.

## Narrow technical decision

**Input:** “Should every database operation use a transaction?”

**Likely goal:** Prevent harmful data inconsistency.

**Weak paraphrase:** “Which operations need transactions?”

**Higher-leverage question:** “Which multi-step operations on critical business paths can enter a partially completed state that causes unacceptable and non-self-recoverable consequences?”

The answer creates a basis for choosing among transactions, idempotency, compensation, state machines, or temporary inconsistency.

## Broad stalled goal

**Input:** “How can I grow my newsletter faster?”

**Likely goal:** Build a larger audience that continues to engage.

**Weak paraphrase:** “Which growth tactics should I try?”

**Higher-leverage question:** “At which step—discovery, signup, first-value experience, or ongoing retention—are otherwise suitable readers dropping out most, and why?”

The better question locates the current constraint before prescribing acquisition tactics.

## Factual boundary

**Input:** “What is the capital of Belgium?”

Answer the factual question directly. There is no useful external goal to recover and no reason to manufacture one.
