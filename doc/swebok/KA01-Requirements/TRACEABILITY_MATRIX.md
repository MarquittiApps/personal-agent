# Requirements Traceability Matrix

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 01 (Software Requirements)

---

## Purpose

This matrix maps each requirement (REQ-NNN) to its implementation artifacts (code files, tests, specs) ensuring full traceability from intent to code.

## Matrix

| REQ ID | Description | Epic | Implementation File(s) | Test File(s) | Status |
|--------|------------|------|----------------------|--------------|--------|
| REQ-001 | FastAPI backend with WebSocket | EP-01 | `app/main.py` | `tests/` | ✅ Implemented |
| REQ-002 | PostgreSQL with pgvector | EP-01 | `app/core/database.py` | — | ✅ Implemented |
| REQ-003 | LangGraph multi-agent orchestration | EP-01 | `app/core/graph.py` | — | ✅ Implemented |
| REQ-004 | Local LLM via Ollama | EP-01 | `app/core/llm_factory.py` | — | 📋 Backlog |
| REQ-010 | React web app with auth | EP-02 | `web/` | — | 🔄 In Progress |
| REQ-011 | Omnibar for commands | EP-02 | `web/` | — | ✅ Implemented |
| REQ-020 | Google Calendar integration | EP-07 | `app/tools/` | — | ✅ Implemented |
| REQ-021 | Google Tasks integration | EP-07 | `app/tools/` | — | ✅ Implemented |
| REQ-090 | Living CONSTITUTION.md | EP-09 | `doc/swebok/KA09-Process/CONSTITUTION.md` | — | ✅ Implemented |

---

> **Note:** This matrix will be retroactively populated with full file paths and test references in Sprint 3 (T3.2).
