# Software Requirements Specification (SRS)

> **Project:** Personal AI Core  
> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Standard:** ISO/IEC/IEEE 29148:2018  
> **Governed by:** SWEBOK v4 — KA 01 (Software Requirements)

---

## 1. Introduction

### 1.1 Purpose
This SRS defines the functional and non-functional requirements for the Personal AI Core system. It serves as the single source of truth for requirements, from which all specifications, tasks, and acceptance criteria are derived.

### 1.2 Scope
The Personal AI Core is a modular AI ecosystem with 6 main modules (see [PRD.md](PRD.md)), a React web interface, and LangGraph-based agent orchestration. This SRS covers all user-facing and system-level requirements.

### 1.3 Definitions & Acronyms

| Term | Definition |
|------|-----------|
| KA | Knowledge Area (SWEBOK v4) |
| SRS | Software Requirements Specification |
| ADR | Architecture Decision Record |
| REQ | Requirement (functional or non-functional) |
| QoS | Quality of Service |
| RBAC | Role-Based Access Control |
| MCP | Model Context Protocol |

---

## 2. Product Requirements

### 2.1 Functional Requirements

#### 2.1.1 Module: Core Infrastructure (EP-01) ✅

| ID | Requirement | Priority | Status |
|----|------------|----------|--------|
| REQ-001 | The system shall provide a FastAPI backend server with WebSocket support for real-time agent communication | P0 | Implemented |
| REQ-002 | The system shall use PostgreSQL with pgvector extension for persistent storage and vector search | P0 | Implemented |
| REQ-003 | The system shall integrate with LangGraph for multi-agent orchestration with Human-in-the-Loop interrupts | P0 | Implemented |
| REQ-004 | The system shall support local LLM inference via Ollama (Llama 3, Phi-3) | P1 | Backlog |

#### 2.1.2 Module: Command Center — Web Dashboard (EP-02) 🔄

| ID | Requirement | Priority | Status |
|----|------------|----------|--------|
| REQ-010 | The system shall provide a React web application with authentication and session management | P0 | In Progress |
| REQ-011 | The system shall provide an Omnibar for global natural language commands | P0 | Implemented |
| REQ-012 | The system shall display a unified intelligence feed (Command Center) with agent notifications | P1 | In Progress |
| REQ-013 | The system shall provide a 3-layer planning dashboard (daily/weekly/monthly views) | P1 | Backlog |

#### 2.1.3 Module: Daily Planning MVP (EP-07) ✅

| ID | Requirement | Priority | Status |
|----|------------|----------|--------|
| REQ-020 | The system shall integrate with Google Calendar API for reading and creating events | P0 | Implemented |
| REQ-021 | The system shall integrate with Google Tasks API for task management | P0 | Implemented |
| REQ-022 | The system shall provide AI-powered daily planning insights via chat | P0 | Implemented |

#### 2.1.4 Module: Smart Home Canvas (EP-03) 📋

| ID | Requirement | Priority | Status |
|----|------------|----------|--------|
| REQ-030 | The system shall accept floor plan uploads (PDF/Image) and render them in a 2D viewer | P1 | Backlog |
| REQ-031 | The system shall use Gemini multimodal capabilities to suggest IoT sensor positions on floor plans | P1 | Backlog |
| REQ-032 | The system shall generate a Bill of Materials (BOM) from sensor placement configurations | P2 | Backlog |

#### 2.1.5 Module: SWEBOK Governance (EP-09) 🔄

| ID | Requirement | Priority | Status |
|----|------------|----------|--------|
| REQ-090 | The system shall maintain a living CONSTITUTION.md defining DoD and governance rules | P0 | In Progress |
| REQ-091 | The system shall enforce spec-driven development via the no-vibe-coding rule | P0 | Backlog |
| REQ-092 | The system shall generate and maintain ADRs for significant architectural decisions | P1 | Backlog |
| REQ-093 | The system shall maintain a traceability matrix linking requirements to code | P1 | Backlog |
| REQ-094 | The system shall enforce quality gates before merges via agent rules | P1 | Backlog |

### 2.2 Non-Functional Requirements (Quality of Service)

| ID | Category | Requirement | Target | Status |
|----|----------|------------|--------|--------|
| QoS-001 | Performance | Backend API response time | ≤ 200ms (p95) for non-LLM endpoints | Implemented |
| QoS-002 | Performance | Local LLM latency per token | ≤ 50ms | Proposed |
| QoS-003 | Reliability | LLM hallucination rate for data retrieval | < 1% across validation test set | Proposed |
| QoS-004 | Security | Local-first data storage for sensitive user data | AES-256 encrypted local volumes | Implemented |
| QoS-005 | Availability | Web dashboard uptime | ≥ 99% during development phase | Implemented |
| QoS-006 | Maintainability | Test coverage for new code | ≥ 80% | In Progress |

### 2.3 Technical Constraints

| ID | Constraint | Justification |
|----|-----------|---------------|
| TC-001 | Backend must use Python 3.12+ with FastAPI | Established tech stack |
| TC-002 | Frontend must use React 19+ with TypeScript and Vite | Established tech stack |
| TC-003 | AI orchestration must use LangChain/LangGraph | Consistency and ecosystem compatibility |
| TC-004 | State management must use Zustand | Lightweight, performant for dashboards |
| TC-005 | Token-cost budget must not exceed $500/month during development | Economic constraint |

## 3. The "5-Whys" of Agent Privacy
1. **Why must the agent use local-first storage?** To ensure the user has total data agency.
2. **Why is data agency a requirement?** To prevent the leakage of the user’s cognitive patterns and private credentials to third-party LLM providers.
3. **Why must we prevent this leakage?** Because the agent manages OAuth tokens for the user's financial and legal accounts.
4. **Why are these tokens handled by the agent?** Because the agent's core function is autonomous task execution across secure platforms.
5. **Why does this matter?** A leak constitutes a total compromise of the user's digital identity, creating professional and legal liability.

## 4. Traceability
Requirements are traced to implementation via the [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) file in this directory. 
