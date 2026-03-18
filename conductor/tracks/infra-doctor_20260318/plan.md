# Implementation Plan: Local Environment Doctor Script

## Phase 1: Foundation & Runtime Checks
- [x] Task: Create initial script structure and version checks.
    - [x] Create `scripts/doctor.py`.
    - [x] Implement Node.js version check.
    - [x] Implement Python version check.
- [x] Task: Add directory and config file validations.
    - [x] Verify `node_modules` directory.
    - [x] Verify Python virtual environment.
    - [x] Verify `.env` and `.env.example` presence.

## Phase 2: Services & Connectivity
- [x] Task: Implement service health checks.
    - [x] Implement PostgreSQL port availability check.
    - [x] Implement Ollama API health check.
- [x] Task: Implement database connection verification.
    - [x] Use `app/core/database.py` logic to test connection.
- [x] Task: Final CLI Polish & Integration.
    - [x] Add colored output and suggestions.
    - [x] Add `npm run doctor` shortcut in root `package.json`.

## Phase 3: Verification & Documentation
- [x] Task: Add unit tests for the doctor script.
    - [x] Mock system calls and subprocesses.
- [x] Task: Update documentation.
    - [x] Add "Local Setup Check" section to `README.md`.
- [x] Task: Conductor - User Manual Verification 'Local Environment Doctor' (Protocol in workflow.md)
