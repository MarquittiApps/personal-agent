# Threat Model — KA13

This document identifies security threats to the Personal AI Core using the **STRIDE** methodology, as governed by SWEBOK v4 KA 13 (Software Security).

## 1. Asset Definitions
- **User Data:** Interaction history, preferences, and semantic memory (Local DB).
- **Credentials:** API keys (Gemini, Google) and OAuth tokens.
- **System Config:** System prompts, governance rules, and `.env` files.

## 2. STRIDE Analysis

| Threat Category | Threat Description | Mitigation Strategy |
|-----------------|--------------------|---------------------|
| **Spoofing** | Unauthorized access to the local FastAPI or WebSocket server. | Implement local-only binding (localhost) and session tokens. |
| **Tampering** | **Prompt Injection:** An attacker (via untrusted input) tricks the LLM into bypassing safety rules. | Strict constitutional guardrails and output sanitization for tool calls. |
| **Repudiation** | An autonomous agent performs an action without a traceable audit log. | Mandatory structured logging of all agent thoughts and tool executions. |
| **Info Disclosure** | Leakage of private interaction history to third-party LLM providers. | **Local-First:** Keep sensitive context in local memory; use scrubbing for cloud inference. |
| **Denial of Service** | Infinite loops in reasoning consumes local CPU/RAM or exceeds API quotas. | Implement execution timeouts and "Operational Watchdog" interrupts. |
| **Elevation of Priv.** | Agent executes unauthorized system commands via a compromised tool registry. | Principle of Least Privilege: Tools bound to restricted scopes and verified inputs. |

## 3. Trust Boundaries
- **Boundary A:** User Browser <-> Backend (WebSocket).
- **Boundary B:** Backend <-> External APIs (Gemini, Google).
- **Boundary C:** Backend <-> Local Storage (PostgreSQL).

## 4. Security Requirements (Ref: SRS REQ-004, REQ-201)
- All interaction history must be encrypted at rest (AES-256).
- Use `no-vibe-coding` to ensure every new tool is security-audited.
