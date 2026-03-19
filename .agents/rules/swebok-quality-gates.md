---
name: swebok-quality-gates
description: "Mandatory quality checkpoints at each development phase, enforcing SWEBOK KA12 (Software Quality) standards."
---

# Rule: SWEBOK Quality Gates

## Objective

Define and enforce mandatory quality checkpoints (gates) that every development artifact must pass before progressing to the next phase. Derived from SWEBOK KA12 (Software Quality) and aligned with the project's `QUALITY_PLAN.md`.

## Triggers (When to Activate)

- When completing any development phase (requirements → design → construction → testing → deployment).
- Before creating a Pull Request.
- Before marking a Track task as complete.
- During sprint review or retrospective.

## Quality Gates

### Gate 1: Requirements Quality (KA01)

Before moving from requirements to design:
- [ ] REQ-NNN is registered in `SRS.md`.
- [ ] Requirement is **unambiguous** — a single interpretation is possible.
- [ ] Requirement is **testable** — a pass/fail criterion can be defined.
- [ ] Requirement is **traceable** — linked to an Epic (EP-NN) and user need.
- [ ] No conflicting requirements exist.

**Gate owner:** Requirements Analyst (agent or human).

### Gate 2: Design Quality (KA02)

Before moving from design to construction:
- [ ] Design is consistent with `ARCHITECTURE_VIEWS.md`.
- [ ] No new external dependencies without ADR justification.
- [ ] API contracts are defined (input/output schemas, error codes).
- [ ] Data model changes are documented.
- [ ] Design adheres to separation of concerns.

**Gate owner:** Architect (agent or human).

### Gate 3: Construction Quality (KA03)

Before moving from construction to testing:
- [ ] Code follows `CONSTITUTION.md` coding standards.
- [ ] `no-vibe-coding.md` rules are satisfied (strategy declared, evidence-based).
- [ ] No TODOs or hacks without a linked issue.
- [ ] Type safety is enforced (Pydantic v2 backend, TypeScript frontend).
- [ ] No hardcoded secrets, credentials, or environment-specific values.

**Gate owner:** Developer (agent or human).

### Gate 4: Testing Quality (KA04)

Before moving from testing to deployment:
- [ ] Unit tests exist for all new/modified functions.
- [ ] Integration tests cover API endpoint contracts.
- [ ] All tests pass locally (`pytest` backend, `vitest`/`playwright` frontend).
- [ ] Edge cases are covered (empty input, null, boundary values).
- [ ] No flaky tests — all tests are deterministic.

**Gate owner:** QA / Test Engineer (agent or human).

### Gate 5: Deployment Quality (KA09)

Before merging to `main`:
- [ ] All previous gates (1-4) are satisfied.
- [ ] Commit messages follow `commits.md` conventions.
- [ ] `doc/swebok/` documents are updated if impacted.
- [ ] `TRACEABILITY_MATRIX.md` is updated with new REQ → code mappings.
- [ ] No regressions — existing tests still pass.

**Gate owner:** Tech Lead / Reviewer (agent or human).

## Gate Failure Protocol

When a gate check fails:
1. **Stop** — do not proceed to the next phase.
2. **Identify** — state which checks failed and why.
3. **Remediate** — fix the gap before re-attempting the gate.
4. **Log** — document the failure and fix for process improvement.

## Metrics (Tracked in `QUALITY_PLAN.md`)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Gate pass rate | ≥ 90% first-attempt | Gates passed / gates attempted |
| Defect escape rate | ≤ 5% | Post-deployment bugs / total bugs |
| Test coverage (backend) | ≥ 80% | `pytest --cov` |
| Test coverage (frontend) | ≥ 70% | `vitest --coverage` |

## What Not to Do (Don'ts)

- **Never** skip a gate for expediency — there are no "fast track" exceptions.
- **Never** self-approve all gates — at least one gate should involve a different reviewer than the author.
- **Never** treat gate failures as bureaucracy — they are defect prevention.
