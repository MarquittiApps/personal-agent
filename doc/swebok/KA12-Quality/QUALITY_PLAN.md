# Quality Plan — Personal AI Core

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 12 (Software Quality)

---

## 1. Quality Objectives

| Objective | Target | Measurement |
|-----------|--------|-------------|
| Code Coverage (new code) | ≥ 80% | `pytest --cov` / `vitest --coverage` |
| Critical Lint Errors | 0 | `ruff check` / `eslint` |
| Security Vulnerabilities (High/Critical) | 0 | `pip-audit` / `npm audit` |
| Documentation Currency | All active epics documented in SRS | Manual review |
| Requirement Traceability | Every commit links to REQ-NNN | Git log audit |

## 2. Quality Activities

| Activity | Frequency | Owner | KA |
|----------|-----------|-------|-----|
| Unit Testing | Every commit | Developer Agent | KA 05 |
| Code Review | Every PR | Review Agent | KA 12 |
| Security Audit | Per sprint | Security Agent | KA 13 |
| Architecture Review | Per epic | Architect Agent | KA 02 |
| DoD Verification | Task completion | QA Agent | KA 09 |

## 3. Quality Gates

Pre-merge checklist (enforced by `swebok-quality-gates.md` rule):
- [ ] All tests pass
- [ ] Coverage threshold met
- [ ] No critical linter warnings
- [ ] ADR exists for new architecture patterns
- [ ] Security checklist completed for data-handling changes
- [ ] Documentation updated

## 4. Metrics Baseline

> **Note:** Baseline metrics will be established during Sprint 3 (Task T3.4).

| Metric | Current Value | Target |
|--------|--------------|--------|
| Backend test coverage | TBD | ≥ 80% |
| Frontend test coverage | TBD | ≥ 80% |
| Open technical debt items | 3 | < 5 |
| SRS completeness | ~40% | 100% |

---

> **Governance:** Updated quarterly or when quality objectives change via ADR process.
