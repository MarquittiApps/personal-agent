---
name: no-vibe-coding
description: "Strict enforcement against unplanned, ad-hoc, or intuition-only coding. Mandates spec-first, evidence-based construction per SWEBOK KA03."
---

# Rule: No Vibe Coding (Strict Mode)

## Objective

Eliminate "vibe coding" — the practice of writing code based on intuition, guesswork, or momentum without a clear plan, traceable requirement, or documented rationale. This rule enforces SWEBOK KA03 (Software Construction) discipline: every line of code must be **intentional, justified, and traceable**.

## Definition of Vibe Coding

Vibe coding is any development activity where the agent or developer:
1. Writes code **without reading** the relevant spec, plan, or requirement first.
2. Makes architectural decisions **without documenting** the rationale.
3. Adds features **nobody asked for** ("wouldn't it be cool if...").
4. Copies patterns **without understanding** them ("it worked over there").
5. Skips tests because the code "looks right."
6. Uses a library, framework, or pattern **without verifying** it's in the tech stack.

## Triggers (When to Activate)

- **Always** — this rule has no exceptions.
- Before writing any production code.
- Before proposing any architectural change.
- During code review.

## Essential Rules

### 1. Spec-First Development
No code is written until the following exist and have been reviewed:
1. **Requirement** — A REQ-NNN entry in `SRS.md`.
2. **Design** — The approach is consistent with `ARCHITECTURE_VIEWS.md`.
3. **Plan** — A Track (`spec.md` + `plan.md`) or an approved implementation plan exists.

**Exception:** Emergency hotfixes may skip step 3 ONLY if a retrospective requirement is created within the same session.

### 2. Evidence-Based Decisions
Every technical decision must be supported by at least ONE of:
- A reference to an existing pattern in the codebase.
- A link to official documentation.
- A performance benchmark or measurement.
- An Architecture Decision Record (ADR).

**Forbidden reasoning:**
- ❌ "I think this is better"
- ❌ "This is how it's usually done"
- ❌ "Let's try this and see"

**Required reasoning:**
- ✅ "Per `ARCHITECTURE_VIEWS.md`, the logical view separates X from Y, so..."
- ✅ "The FastAPI docs recommend this pattern for dependency injection..."
- ✅ "REQ-045 specifies sub-200ms response time, so we should use caching..."

### 3. No Gold Plating
The agent must implement **exactly** what is specified — no more, no less.
- Do not add "nice to have" features.
- Do not refactor unrelated code in the same change.
- Do not introduce abstractions "for the future."

If improvements are identified, create a new REQ-NNN and track it separately.

### 4. Mandatory Strategy Declaration
Before writing code, the agent **MUST** declare its strategy in plain English:
```
Strategy: I will modify `app/core/graph.py` to add a new node `validate_input`
that enforces schema validation using Pydantic v2.
Requirement: REQ-023
Test: I will add a unit test in `tests/core/test_graph.py` to verify
validation rejects malformed input.
```

### 5. Comprehension Checkpoint
Before using any existing module, the agent must demonstrate understanding by:
1. Reading the file (not just the function signature).
2. Identifying side effects and dependencies.
3. Stating how the change interacts with existing behavior.

### 6. Test-Evidence Closure
No task is complete until:
- [ ] Tests exist and pass.
- [ ] The agent has **run** the tests (not just written them).
- [ ] Test output is captured as evidence.

## Severity

This rule operates in **STRICT mode** as directed by the project owner.

- **Violation of rules 1-3:** The agent must stop, acknowledge the gap, and remediate before continuing.
- **Violation of rules 4-6:** The agent must retroactively satisfy the requirement before marking the task complete.

## What Not to Do (Don'ts)

- **Never** start coding without reading the relevant spec or track.
- **Never** justify a decision with "I think" or "usually" without evidence.
- **Never** add unrequested features or refactors.
- **Never** claim a task is done without running tests.
- **Never** copy-paste code without understanding its purpose and side effects.
