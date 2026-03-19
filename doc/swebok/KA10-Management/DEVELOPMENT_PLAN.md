# Development Plan — Personal AI Core

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 10 (SE Management)

---

## 1. Project Overview

The Personal AI Core is a modular AI ecosystem designed to act as a professional co-pilot in engineering, IT, and personal management. See [PRD.md](file:///c:/devWorkspace/personal-agent/PRD.md) for complete product vision.

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

## 3. Current Sprint: Sprint 0 — SWEBOK Foundation

**Goal:** Establish the SWEBOK governance directory structure and bootstrap documents.

| Task | Status | Assignee | Deliverable |
|------|--------|----------|-------------|
| T0.1 Create `doc/swebok/` directory structure | 🔄 In Progress | Agent | Directory scaffold |
| T0.2 Write `CONSTITUTION.md` | 🔄 In Progress | Agent | `KA09-Process/CONSTITUTION.md` |
| T0.3 Write `DEVELOPMENT_PLAN.md` | 🔄 In Progress | Agent | `KA10-Management/DEVELOPMENT_PLAN.md` |
| T0.4 Create `SRS.md` template | ⬜ Pending | Agent | `KA01-Requirements/SRS.md` |
| T0.5 Register EP-09 in EPICOS.md & BACKLOG.md | ⬜ Pending | Agent | Updated planning docs |

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

---

> **Governance:** This document is updated by agents after each merge via the `swebok-governance.workflow.md` Doc-Sync step. Manual updates are allowed for milestone adjustments.
