# Threat Model — Personal AI Core

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 13 (Software Security)

---

## 1. System Overview

The Personal AI Core is an agent-based system that handles:
- User credentials (Google OAuth tokens)
- Personal calendar and task data
- Professional project information
- LLM interactions (prompts containing sensitive context)

## 2. Trust Boundaries

```
┌─────────────────────────────────────────┐
│         Trusted Zone (Local)            │
│  ┌──────────┐  ┌──────────┐ ┌────────┐ │
│  │ FastAPI   │  │PostgreSQL│ │ Ollama │ │
│  │ Backend   │  │ (Docker) │ │ (LLM)  │ │
│  └──────────┘  └──────────┘ └────────┘ │
└───────────┬─────────────────────────────┘
            │ Trust Boundary
┌───────────▼─────────────────────────────┐
│        Untrusted Zone (External)        │
│  ┌──────────┐  ┌──────────┐ ┌────────┐ │
│  │ Gemini   │  │ Google   │ │ GitHub │ │
│  │ API      │  │ Cal/Tasks│ │ API    │ │
│  └──────────┘  └──────────┘ └────────┘ │
└─────────────────────────────────────────┘
```

## 3. Threat Registry

| ID | Threat | Vector | Impact | Likelihood | Mitigation | Status |
|----|--------|--------|--------|-----------|------------|--------|
| TH-01 | Prompt Injection | Malicious user input manipulates LLM behavior | High | Medium | Input sanitization + system prompt hardening | Open |
| TH-02 | Credential Exposure | OAuth tokens leaked via logs or LLM context | Critical | Low | Token encryption (`app/core/crypto.py`) + log scrubbing | Mitigated |
| TH-03 | Insecure Output Handling | LLM generates malicious tool calls | High | Medium | Tool call validation + allowlist enforcement | Open |
| TH-04 | Database Injection | SQL injection via unsanitized queries | High | Low | Parameterized queries (SQLAlchemy) | Mitigated |
| TH-05 | Dependency Vulnerability | Known CVE in third-party packages | Medium | Medium | Regular `pip-audit` / `npm audit` in CI | Open |

## 4. Security Controls

| Control | Implementation | Status |
|---------|---------------|--------|
| Token Encryption | `app/core/crypto.py` (AES-256) | ✅ Active |
| OAuth Flow | `app/core/google_auth.py` | ✅ Active |
| Environment Variables | `.env` file (gitignored) | ✅ Active |
| Input Validation | Pydantic v2 models | ✅ Active |
| Prompt Injection Defense | System prompt hardening | 📋 Pending (Sprint 3) |

---

> **Note:** Full threat model elaboration is scheduled for Sprint 3 (Task T3.3). This seed document establishes the framework.
