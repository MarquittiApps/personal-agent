---
name: swebok-security-checklist
description: "Mandatory security checklist for all code changes, enforcing SWEBOK KA13 (Software Engineering Security) and the project's THREAT_MODEL.md."
---

# Rule: SWEBOK Security Checklist

## Objective

Ensure every code change is evaluated against security threats before deployment. This rule operationalizes SWEBOK KA13 (Software Engineering Security) and the project's `THREAT_MODEL.md` into actionable pre-flight checks.

## Triggers (When to Activate)

- **Always** when modifying code that handles:
  - Authentication or authorization.
  - User input (forms, API params, file uploads).
  - Database queries (SQL, ORM operations).
  - External API calls.
  - Secrets, tokens, or credentials.
  - File system operations.
- Before any PR that touches `app/` or `web/` directories.
- When adding new dependencies.

## Security Checklist

### A. Input Validation (OWASP A03)

- [ ] All user input is validated server-side using Pydantic v2 models (backend) or Zod schemas (frontend).
- [ ] Input length, type, and format constraints are explicitly defined.
- [ ] File uploads are validated for type, size, and content.
- [ ] No raw user input is interpolated into SQL, shell commands, or templates.

### B. Authentication & Authorization (OWASP A01, A07)

- [ ] Authentication endpoints use secure token patterns (JWT with rotation, httpOnly cookies).
- [ ] Authorization checks are present on every protected endpoint.
- [ ] No privilege escalation paths exist (user cannot access admin routes).
- [ ] Session management follows security best practices (expiry, revocation).
- [ ] Password hashing uses bcrypt or argon2 (never MD5, SHA-1).

### C. Data Protection (OWASP A02, A04)

- [ ] Sensitive data is encrypted at rest and in transit (TLS 1.2+).
- [ ] No secrets, API keys, or credentials in source code or committed files.
- [ ] Environment variables are used for all configuration secrets.
- [ ] Database connections use parameterized queries (never string concatenation).
- [ ] PII is handled according to data minimization principles.

### D. Dependency Security (OWASP A06)

- [ ] New dependencies are from reputable, maintained sources.
- [ ] `pip audit` (backend) or `npm audit` (frontend) shows no critical vulnerabilities.
- [ ] No dependencies are pinned to `*` or `latest` — versions are locked.
- [ ] License compatibility is verified (no GPL in proprietary modules).

### E. API Security (OWASP A05, A09)

- [ ] Rate limiting is configured on public-facing endpoints.
- [ ] CORS is restricted to known origins (no wildcard `*` in production).
- [ ] Error responses do not leak internal implementation details (stack traces, DB structure).
- [ ] API versioning is consistent with `ARCHITECTURE_VIEWS.md`.

### F. Infrastructure Security

- [ ] Docker containers run as non-root users.
- [ ] Database ports are not exposed to the public network.
- [ ] Health check endpoints do not expose sensitive system information.
- [ ] Logging does not capture sensitive data (passwords, tokens, PII).

## Threat Model Cross-Reference

When a security check fails, cross-reference with `doc/swebok/KA13-Security/THREAT_MODEL.md`:

| Check Category | Related Threat IDs |
|----------------|-------------------|
| Input Validation | THR-001 (Injection attacks) |
| Auth & Authz | THR-002 (Broken authentication) |
| Data Protection | THR-003 (Data exposure), THR-004 (Credential leakage) |
| Dependencies | THR-005 (Supply chain attack) |
| API Security | THR-006 (Excessive data exposure) |

## Failure Protocol

1. **CRITICAL** (Auth bypass, SQL injection, credential leak): **Block deployment**. Fix immediately.
2. **HIGH** (Missing input validation, insecure dependency): **Block PR merge**. Fix before review.
3. **MEDIUM** (Missing rate limiting, verbose errors): **Track as issue**. Fix within current sprint.
4. **LOW** (Informational headers, CORS refinement): **Track as technical debt**. Fix within 2 sprints.

## What Not to Do (Don'ts)

- **Never** commit `.env` files, API keys, or secrets to the repository.
- **Never** disable security middleware for "development convenience" without a toggle.
- **Never** trust client-side validation as the only validation layer.
- **Never** use `eval()`, `exec()`, or dynamic code execution with user input.
- **Never** log passwords, tokens, or full credit card numbers.
