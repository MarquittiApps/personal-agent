# Project Constitution — Personal AI Core

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 09 (SE Process), KA 14 (Professional Practice)

---

## 1. Purpose

This Constitution is the supreme governance document for the Personal AI Core project. It codifies the Definition of Done (DoD), coding standards, agent behavior rules, and quality thresholds that all agents and contributors must follow. Every specification, workflow, and rule in this project derives authority from this Constitution.

## 2. Core Principles

| # | Principle | SWEBOK KA |
|---|-----------|-----------|
| P1 | **Spec-Driven Development** — No code without a prior specification | KA 01, KA 04 |
| P2 | **Architectural Intentionality** — Every significant decision is documented via an ADR | KA 02 |
| P3 | **Quality as a Process** — Quality is verified at every stage, not just at the end | KA 12 |
| P4 | **Security by Design** — Security is addressed from requirements, not patched after deployment | KA 13 |
| P5 | **Human-in-the-Loop** — Critical decisions require explicit human approval | KA 14 |
| P6 | **Living Documentation** — Documentation drives development and is always current | KA 09, KA 10 |

## 3. Definition of Done (DoD)

A task, feature, or sprint is considered **Done** only when ALL of the following are satisfied:

### 3.1 Code Quality
- [ ] Code compiles/runs without errors
- [ ] No critical linter warnings (`ruff` for Python, `eslint` for TypeScript)
- [ ] Follows established coding standards (see Section 5)
- [ ] No hardcoded secrets, credentials, or API keys

### 3.2 Testing
- [ ] Unit tests written and passing (≥ 80% coverage for new code)
- [ ] Integration tests written for cross-module interactions
- [ ] Backend tests use `pytest`; frontend tests use `vitest` or `playwright`

### 3.3 Documentation
- [ ] Relevant SWEBOK documentation updated (`SRS.md`, `DEVELOPMENT_PLAN.md`, ADRs)
- [ ] Code includes docstrings/JSDoc for public interfaces
- [ ] `TRACEABILITY_MATRIX.md` updated if new requirements are addressed

### 3.4 Security
- [ ] Security checklist completed (`.agents/rules/swebok-security-checklist.md`)
- [ ] Input validation on all new API endpoints
- [ ] No new vulnerabilities introduced (dependency audit clean)

### 3.5 Version Control
- [ ] Atomic commits following Conventional Commits format
- [ ] Each commit traces to a requirement ID (REQ-NNN) or task ID
- [ ] PR description includes changes summary and KA references

## 4. Agent Governance

### 4.1 Agent Roles & KA Mapping
Agents operating in this repository must specialize according to the SWEBOK KA matrix defined in `doc/specs/swebok-governance/SPEC.md` (Section 2).

### 4.2 Pre-Execution Protocol
Before writing implementation code, every agent MUST:
1. Read the relevant specification (`doc/specs/` or `doc/swebok/KA01-Requirements/SRS.md`)
2. Verify no conflicts with this Constitution
3. Explain the implementation strategy before coding
4. Cite the SWEBOK KA domain of the work being performed

### 4.3 No-Vibe-Coding Rule
Code generation without a prior specification is **strictly prohibited**. The only exception is hotfixes tagged as `fix(hotfix):`, which must be retroactively documented within 24 hours.

## 5. Coding Standards

### 5.1 Backend (Python 3.12+)
- **Framework:** FastAPI
- **Data Validation:** Pydantic v2
- **Formatting:** `ruff format`
- **Linting:** `ruff check`
- **Testing:** `pytest` with `pytest-asyncio` for async code
- **Type Hints:** Required on all function signatures

### 5.2 Frontend (React 19+ / TypeScript)
- **Build Tool:** Vite
- **Styling:** Tailwind CSS (no inline styles, no CSS modules)
- **State Management:** Zustand (`src/store/`)
- **Data Validation:** Zod
- **Testing:** Vitest (unit), Playwright (E2E)
- **Strict TypeScript:** `strict: true` in `tsconfig.json`

### 5.3 AI Orchestration
- **Framework:** LangChain / LangGraph
- **Local LLM:** Ollama (Llama 3, Phi-3)
- **Cloud LLM:** Gemini 2.5 Pro
- **No other AI libraries** without explicit SPEC approval

## 6. Commit Convention

```
<type>(<scope>): <description>

[optional body]

Refs: REQ-NNN | ADR-NNN | EP-NN
```

**Types:** `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`, `perf`

## 7. Amendment Process

This Constitution may be amended through:
1. A proposal documented as an ADR in `doc/swebok/KA02-Architecture/`
2. Explicit approval from the project owner (Human-in-the-Loop)
3. Update to this document with a version increment

---

> **Cross-References:**
> - [SPEC: SWEBOK Governance](file:///c:/devWorkspace/personal-agent/doc/specs/swebok-governance/SPEC.md)
> - [AI Collaboration Protocol](file:///c:/devWorkspace/personal-agent/.agents/rules/ai-collaboration.md)
> - [Tech Stack Rules](file:///c:/devWorkspace/personal-agent/.agents/rules/tech-stack.md)
