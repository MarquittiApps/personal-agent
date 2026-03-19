# SPEC: SWEBOK v4 Governance Integration

> **Module:** SWEBOK Governance Engine  
> **Epic:** EP-09 — SWEBOK v4 Systemic Integration  
> **Status:** Draft — Pending User Approval  
> **Date:** 2026-03-19  
> **Author:** Agile Spec Factory (PM, PO, Architect, Tech Lead, QA, Scrum Master)

---

## 1. Vision & Strategic Alignment

### 1.1 Why This Matters

The Personal AI Core currently operates with iterative but **unsystematic** development governance. While `.agents/rules/` and `.agents/workflows/` provide basic guardrails (atomic commits, conventional commits, tech-stack enforcement), there is no **unified engineering framework** anchoring agent behavior to established software engineering knowledge.

The SWEBOK v4 (IEEE Computer Society, 2024) provides exactly this: **18 Knowledge Areas (KAs)** covering the complete software engineering lifecycle — from requirements to architecture, security, quality, and operations. Integrating it transforms the project from "ad-hoc AI-assisted development" into **SE 3.0 (AI-Native Software Engineering)**, where the SWEBOK acts as the "operating system" for agent orchestration.

### 1.2 Strategic Goals

| # | Goal | Metric |
|---|------|--------|
| G1 | Eliminate "vibe coding" — every code change traces to a specification | 100% traceability: commit → requirement ID |
| G2 | Establish architectural memory via ADRs | Every significant decision has an ADR |
| G3 | Living documentation as the **driver** (not sub-product) of development | `DEVELOPMENT_PLAN.md` always reflects real state |
| G4 | Agent specialization via SWEBOK KA mapping | Each agent role maps to specific KAs |
| G5 | Quality gates enforced by agents before merge | Pre-merge checklist derived from SWEBOK KA 12 |

### 1.3 Alignment with PRD

This module directly supports **PRD Section 5.1 (Meta-Agent / Self-Evolution)** by providing the constitutional framework that governs how agents create, validate, and evolve code. It also reinforces **Phase 4: Auto-Expansion**, ensuring self-generated code meets engineering standards.

---

## 2. SWEBOK Knowledge Area Mapping & Agent Roles

### 2.1 KA → Agent Role Matrix

The 18 KAs of SWEBOK v4 are mapped to specialized agent roles. Each role can be embodied by an AI agent (skill) or enforced via a rule/workflow.

| KA # | Knowledge Area | Agent Role | Implementation Artifact |
|------|---------------|------------|------------------------|
| KA 01 | Software Requirements | **Requirements Analyst** | Skill: `swebok-requirements-analyst` |
| KA 02 | Software Architecture | **Systems Architect** | Skill: `swebok-architect` |
| KA 03 | Software Design | **Systems Architect** (shared) | Merged with KA 02 skill |
| KA 04 | Software Construction | **Lead Developer** | Rule: `no-vibe-coding.md` |
| KA 05 | Software Testing | **Quality Engineer** | Existing rule: `ai-collaboration.md` (enhanced) |
| KA 06 | Software Operations | **Ops & Config Agent** | Workflow: `swebok-ops-review.workflow.md` |
| KA 07 | Software Maintenance | **Lead Developer** (shared) | Covered by existing workflows |
| KA 08 | Software Configuration Mgmt | **Ops & Config Agent** (shared) | Existing: `commits.md` (enhanced) |
| KA 09 | SE Management & Process | **Supervisor / Scrum Master** | Workflow: `swebok-governance.workflow.md` |
| KA 10 | SE Management | **Supervisor** (shared) | Artifact: `DEVELOPMENT_PLAN.md` |
| KA 11 | SE Models & Methods | **Lead Developer** (shared) | Integrated in construction rule |
| KA 12 | Software Quality | **Quality Engineer** | Rule: `swebok-quality-gates.md` |
| KA 13 | Software Security | **Security Specialist** | Rule: `swebok-security-checklist.md` |
| KA 14 | SE Professional Practice | **All Agents** | Rule: `swebok-compliance-master.md` |
| KA 15 | SE Economics | **PM / PO** | Documented in DEVELOPMENT_PLAN |
| KA 16 | Computing Foundations | Implicit (tech stack) | Existing: `tech-stack.md` |
| KA 17 | Mathematical Foundations | Implicit (metrics) | Quality gate metrics |
| KA 18 | Engineering Foundations | Implicit (practices) | Covered by existing rules |

### 2.2 Priority KAs for Phase 1

Based on immediate project needs and the content in the swebok folder, the first implementation phase focuses on **5 critical KAs**:

1. **KA 01 (Requirements)** — Structured SRS with traceability
2. **KA 02 (Architecture)** — ADR system
3. **KA 04 (Construction)** — Spec-driven coding rules
4. **KA 12 (Quality)** — Quality gates
5. **KA 13 (Security)** — Security review checklist

---

## 3. Directory Structure & Living Documentation

### 3.1 New Directory: `doc/swebok/`

```
doc/swebok/
├── KA01-Requirements/
│   ├── SRS.md                    # Software Requirements Specification (ISO 29148)
│   └── TRACEABILITY_MATRIX.md    # REQ-ID → Code mapping
├── KA02-Architecture/
│   ├── ADR-001-*.md              # Architecture Decision Records
│   └── ARCHITECTURE_VIEWS.md     # 4+1 View Model (Logical, Process, Dev, Physical)
├── KA09-Process/
│   ├── CONSTITUTION.md           # Project "Constitution" — DoD, coding standards, governance
│   └── PROCESS_MODEL.md          # SDLC model and phase definitions
├── KA10-Management/
│   └── DEVELOPMENT_PLAN.md       # Dynamic backlog, risk registry, milestones
├── KA12-Quality/
│   └── QUALITY_PLAN.md           # Quality objectives, metrics, review schedule
└── KA13-Security/
    └── THREAT_MODEL.md           # Attack vectors, mitigations, security posture
```

### 3.2 Bootstrap Documents

Each directory starts with a **seed document** containing the SWEBOK-aligned template. Documents are meant to be **living** — continuously updated by agents as development progresses.

---

## 4. New Agent Artifacts

### 4.1 New Rules (`.agents/rules/`)

#### 4.1.1 `swebok-compliance-master.md`
**Purpose:** Master governance rule requiring all agent actions to cite relevant SWEBOK KAs.

**Key provisions:**
- Every SPEC must reference the KAs it addresses
- Every ADR must cite the architectural rationale per KA 02
- Activity logs must tag the KA domain of the work performed

#### 4.1.2 `no-vibe-coding.md`
**Purpose:** Blocks creation of functions, files, or modules without a prior specification in `doc/swebok/` or `doc/specs/`.

**Key provisions:**
- Before writing implementation code, verify that a SPEC or SRS entry exists
- Exception: hotfixes tagged as `fix(hotfix):` may bypass with post-hoc documentation
- Agents must refuse to implement features lacking a specification anchor

#### 4.1.3 `swebok-quality-gates.md`
**Purpose:** Defines pre-merge quality checkpoints derived from KA 12.

**Key provisions:**
- Unit test coverage ≥ 80% for new code
- No critical linter warnings
- ADR exists for any new architectural pattern introduced
- Security checklist completed for endpoints handling user data

#### 4.1.4 `swebok-security-checklist.md`
**Purpose:** Security review checklist derived from KA 13 and the Secure SDLC.

**Key provisions:**
- Input validation on all API endpoints
- Prompt injection resistance for LLM-facing interfaces
- Credential handling audit (no hardcoded secrets)
- Threat model updated for new attack surfaces

### 4.2 New Skills (`.agents/skills/`)

#### 4.2.1 `swebok-requirements-analyst/`
**Purpose:** Agent skill for structured requirements elicitation following ISO 29148.

**Capabilities:**
- Parse user intent into formal SRS entries with unique IDs (REQ-NNN)
- Generate BDD acceptance criteria (Given/When/Then)
- Maintain the traceability matrix

#### 4.2.2 `swebok-architect/`
**Purpose:** Agent skill for architectural analysis and ADR generation.

**Capabilities:**
- Propose and document Architecture Decision Records (ADR-NNN)
- Analyze impact of changes across the 4+1 views
- Validate plan consistency against the project constitution

### 4.3 New Workflows (`.agents/workflows/`)

#### 4.3.1 `swebok-governance.workflow.md`
**Purpose:** Master workflow orchestrating the SWEBOK-aligned SDLC.

**Flow:**
1. **KA-Alignment Pre-check** — Verify intent maps to `KA01`
2. **Architectural Validation** — Analyze impact, generate/update ADRs
3. **Spec-Driven Construction** — Code only from detailed specs
4. **Verification Loop** — Run tests before commit
5. **Doc-Sync** — Update `DEVELOPMENT_PLAN.md` after merge

---

## 5. Agile Sprint Plan

### Sprint 0: Foundation & Bootstrap (Estimated: 1 day)

| Task | Description | KA | Deliverable |
|------|------------|-----|-------------|
| T0.1 | Create `doc/swebok/` directory structure | — | Directory scaffold |
| T0.2 | Write `CONSTITUTION.md` with DoD and coding standards | KA 09 | `doc/swebok/KA09-Process/CONSTITUTION.md` |
| T0.3 | Write `DEVELOPMENT_PLAN.md` seed with current epics | KA 10 | `doc/swebok/KA10-Management/DEVELOPMENT_PLAN.md` |
| T0.4 | Create `SRS.md` template (ISO 29148 aligned) | KA 01 | `doc/swebok/KA01-Requirements/SRS.md` |
| T0.5 | Register EP-09 in `EPICOS.md` and `BACKLOG.md` | — | Updated planning docs |

### Sprint 1: Rules & Governance Engine (Estimated: 1-2 days)

| Task | Description | KA | Deliverable |
|------|------------|-----|-------------|
| T1.1 | Write `swebok-compliance-master.md` rule | KA 14 | `.agents/rules/swebok-compliance-master.md` |
| T1.2 | Write `no-vibe-coding.md` rule | KA 04 | `.agents/rules/no-vibe-coding.md` |
| T1.3 | Write `swebok-quality-gates.md` rule | KA 12 | `.agents/rules/swebok-quality-gates.md` |
| T1.4 | Write `swebok-security-checklist.md` rule | KA 13 | `.agents/rules/swebok-security-checklist.md` |
| T1.5 | Enhance existing `ai-collaboration.md` with KA references | KA 05 | Updated rule |

### Sprint 2: Skills & Workflows (Estimated: 2-3 days)

| Task | Description | KA | Deliverable |
|------|------------|-----|-------------|
| T2.1 | Create `swebok-requirements-analyst` skill | KA 01 | `.agents/skills/swebok-requirements-analyst/SKILL.md` |
| T2.2 | Create `swebok-architect` skill | KA 02 | `.agents/skills/swebok-architect/SKILL.md` |
| T2.3 | Create `swebok-governance.workflow.md` workflow | KA 09 | `.agents/workflows/swebok-governance.workflow.md` |
| T2.4 | Write first ADR: `ADR-001-layered-architecture.md` | KA 02 | `doc/swebok/KA02-Architecture/ADR-001-layered-architecture.md` |

### Sprint 3: Integration & Retroactive Documentation (Estimated: 2-3 days)

| Task | Description | KA | Deliverable |
|------|------------|-----|-------------|
| T3.1 | Populate SRS with requirements from existing epics (EP-01→EP-08) | KA 01 | Populated `SRS.md` |
| T3.2 | Create `TRACEABILITY_MATRIX.md` linking REQs to code | KA 01 | `doc/swebok/KA01-Requirements/TRACEABILITY_MATRIX.md` |
| T3.3 | Write `THREAT_MODEL.md` for current attack surfaces | KA 13 | `doc/swebok/KA13-Security/THREAT_MODEL.md` |
| T3.4 | Write `QUALITY_PLAN.md` with metrics baseline | KA 12 | `doc/swebok/KA12-Quality/QUALITY_PLAN.md` |
| T3.5 | Update `agile-spec-factory.workflow.md` to reference SWEBOK | — | Updated workflow |

---

## 6. Acceptance Criteria (Definition of Done)

### 6.1 Sprint 0 DoD
- [ ] `doc/swebok/` directory exists with all 6 KA subdirectories
- [ ] `CONSTITUTION.md` defines DoD, coding standards, and agent governance
- [ ] `DEVELOPMENT_PLAN.md` contains all 8+ existing epics with current status
- [ ] `SRS.md` has the ISO 29148 template structure ready for population
- [ ] EP-09 is registered in `EPICOS.md` and `BACKLOG.md`

### 6.2 Sprint 1 DoD
- [ ] All 4 new rules exist in `.agents/rules/` and are syntactically valid
- [ ] `no-vibe-coding.md` can be manually verified: an agent attempting to code without a spec should be blocked by the rule
- [ ] `swebok-quality-gates.md` defines measurable thresholds
- [ ] `ai-collaboration.md` references SWEBOK KAs alongside its existing protocols

### 6.3 Sprint 2 DoD
- [ ] Both new skills have a valid `SKILL.md` following the project skill standard
- [ ] `swebok-governance.workflow.md` follows the 5-step flow defined in Section 4.3.1
- [ ] ADR-001 documents the existing Layered Architecture decision with rationale
- [ ] All new artifacts are cross-referenced in `CONSTITUTION.md`

### 6.4 Sprint 3 DoD
- [ ] SRS contains ≥ 1 formal requirement per existing epic (EP-01→EP-08)
- [ ] Traceability matrix links at least 10 requirements to specific code files
- [ ] Threat model identifies ≥ 5 attack vectors with mitigations
- [ ] Quality plan defines baseline metrics for test coverage and code quality
- [ ] Updated `agile-spec-factory.workflow.md` includes SWEBOK alignment step

---

## 7. Architectural Decisions Summary

| Decision | Rationale | KA |
|----------|-----------|-----|
| `doc/swebok/` as standalone directory (not inside `.agents/`) | SWEBOK artifacts are **project documentation**, not agent configuration. They serve as the single source of truth for all agents. | KA 09 |
| ISO 29148 for SRS format | Industry standard for requirements specification; ensures interoperability and rigor | KA 01 |
| ADR format for architecture decisions | Lightweight, version-controlled, and widely adopted in engineering teams | KA 02 |
| Rules over hard-coding governance | Rules in `.agents/rules/` can be read by any agent tool (Gemini, Copilot, Claude) without code changes | KA 14 |
| Phased rollout (4 sprints) instead of big-bang | Reduces risk, allows validation at each step, follows Agile principles per KA 09 | KA 09 |
| No backend code changes in Phase 1 | This is a governance/documentation integration — code enforcement comes from rules and workflows, not API changes | KA 10 |

---

## 8. Risk Assessment

| Risk | Impact | Probability | Mitigation |
|------|--------|------------|------------|
| Over-bureaucratization slows development | High | Medium | Keep rules lightweight; `no-vibe-coding` has hotfix escape hatch |
| Agents ignore new rules (tool doesn't read them) | Medium | Low | Rules are in `.agents/rules/` — standard location for all AI tools |
| SRS becomes stale (not updated) | Medium | Medium | `swebok-governance.workflow.md` includes Doc-Sync step |
| Too many KAs to address simultaneously | Medium | High | Phased approach: only 5 KAs in Sprint 1-2 |

---

> **Next Steps:** Upon user approval, begin execution with Sprint 0 (directory structure and bootstrap documents).
