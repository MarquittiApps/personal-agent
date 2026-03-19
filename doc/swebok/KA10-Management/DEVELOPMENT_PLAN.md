# Development Plan — Personal AI Core

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 10 (SE Management)

---

## 1. Project Overview

The Personal AI Core is a modular AI ecosystem designed to act as a professional co-pilot in engineering, IT, and personal management. See [PRD.md](../KA01-Requirements/PRD.md) for complete product vision.

## 2. Epic Registry

| ID | Epic | Status | Phase | Description |
|:---|:-----|:-------|:------|:------------|
| EP-01 | Core Foundation & Infrastructure | ✅ Done | Phase 1 | Repository setup, PostgreSQL database, LangGraph agent infrastructure |
| EP-02 | Command Center (Web Dashboard) | 🔄 In Progress | Phase 2 | React interface, authentication, Zustand state, Omnibar chat |
| EP-03 | Smart Home Module (Multimodal Canvas) | 📋 Backlog | Phase 2 | Floor plan viewer + AI for IoT sensor positioning |
| EP-04 | DevOps & ClinicCare Integration | 📋 Backlog | Phase 3 | MCP connectivity with VS Code, PR monitoring |
| EP-05 | Operations Hub (IT Consultancy) | 📋 Backlog | Phase 3 | Budget management, electrical projects, physical infra |
| EP-06 | Meta-Agent (Self-Evolution) | 📋 Backlog | Phase 4 | Self-improvement, autonomous component generation |
| EP-07 | Daily Planning MVP with AI | ✅ Done | Phase 1 | Google Calendar/Tasks integration via chat with real-time planning UI |
| EP-08 | RAG Knowledge Base & Catalogs | 📋 Backlog | Phase 2 | Vector DB for technical standards (NBRs), IoT catalog |
| **EP-09** | **SWEBOK v4 Governance Integration** | **🔄 In Progress** | **Phase 1** | **Engineering governance framework, living documentation, quality gates** |

## 3. Sprint 3 — Integration & Retroactive Documentation ✅

**Goal:** Integrate legacy knowledge and populate all SWEBOK KAs.

| Task | Status | Assignee | Deliverable |
|------|--------|----------|-------------|
| T3.1 Populate SRS with requirements audit | ✅ Done | Agent | `SRS.md` |
| T3.2 Build traceability matrix from code | ✅ Done | Agent | `TRACEABILITY_MATRIX.md` |
| T3.3 Complete threat model with STRIDE | ✅ Done | Agent | `THREAT_MODEL.md` |
| T3.4 Fill quality plan with metrics | ✅ Done | Agent | `QUALITY_PLAN.md` |
| T3.5 Migrate/consolidate legacy docs | ✅ Done | Agent | Skill/Env integrated |
| T3.6 Remove retired duplicates | ✅ Done | Agent | Cleaned `doc/` |

## 4. Milestones

| Milestone | Target Date | Status | Dependencies |
|-----------|-------------|--------|--------------|
| M1: SWEBOK Foundation (Sprint 0) | 2026-03-19 | 🔄 In Progress | — |
| M2: Governance Rules (Sprint 1) | 2026-03-20 | ⬜ Pending | M1 |
| M3: Skills & Workflows (Sprint 2) | 2026-03-22 | ⬜ Pending | M2 |
| M4: Retroactive Documentation (Sprint 3) | 2026-03-24 | ⬜ Pending | M3 |

## 5. Risk Registry

| ID | Risk | Impact | Probability | Mitigation | Status |
|----|------|--------|------------|------------|--------|
| R1 | Over-bureaucratization slows development | High | Medium | Keep rules lightweight; hotfix escape hatch | Open |
| R2 | Agents ignore new rules | Medium | Low | Rules in standard `.agents/rules/` location | Open |
| R3 | SRS becomes stale | Medium | Medium | Doc-Sync step in governance workflow | Open |
| R4 | Too many KAs to address simultaneously | Medium | High | Phased approach: 5 KAs first | Mitigated |

## 6. Technical Debt Tracker

| ID | Description | Priority | Epic | Status |
|----|-------------|----------|------|--------|
| TD-01 | Existing epics lack formal SRS entries | Medium | EP-09 | Open — Sprint 3 |
| TD-02 | No traceability matrix linking REQs to code | Medium | EP-09 | Open — Sprint 3 |
| TD-03 | No formal threat model | High | EP-09 | Open — Sprint 3 |

- **Deployment:** Implement project documentation sharing via GitHub Pages using MkDocs. Refer to [EPICOS.md](planning/EPICOS.md) and [BACKLOG.md](planning/BACKLOG.md).
- **Workflow:** Create an automated GitHub Issue Management workflow to coordinate between Planning and Execution.
