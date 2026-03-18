# Track Specification: Local Environment Doctor Script

## 1. Context
- **Project:** Personal AI Core.
- **Goal:** Implement an automated diagnostic script (`scripts/doctor.py`) to verify local environment readiness (runtimes, dependencies, services, connectivity).

## 2. Requirements
- Check Node.js (>=18) and Python (>=3.10) versions.
- Verify `node_modules` and virtual environment existence.
- Validate `.env` files presence.
- Test connectivity to PostgreSQL (5432) and Ollama (11434).
- Informative CLI output with correction suggestions.

## 3. Tech Stack
- **Language:** Python.
- **Dependencies:** `psycopg2-binary`, `requests`, `python-dotenv`.

## 4. Acceptance Criteria
- [ ] Script runs correctly and identifies missing dependencies.
- [ ] Script verifies database connection successfully.
- [ ] Script verifies Ollama service availability.
- [ ] Exit code 0 on success, 1 on critical failure.
