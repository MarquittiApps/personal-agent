# SPEC: Local Environment Doctor Script

## 1. Overview and Alignment
To ensure stability and ease of onboarding in the **Personal AI Core**, this module provides a diagnostic script ("Doctor") that validates the local environment. This is crucial to avoid silent execution errors caused by missing dependencies or incorrect environment configurations.

## 2. Design Requirements
- **Interface:** CLI with colored output (Green for OK, Red for Error, Yellow for Warning).
- **Suggestions:** Each error must be accompanied by an actionable correction instruction.

## 3. Technical Specification
### Verification Components:
1. **Runtimes:**
   - Node.js >= 18.0.0
   - Python >= 3.10.0
2. **Dependencies:**
   - Does the `node_modules` folder exist?
   - Does the Python virtual environment (`venv` or `.venv`) exist?
   - Are the packages from `requirements.txt` installed?
3. **Local Services (Ports):**
   - PostgreSQL (5432)
   - Ollama (11434)
4. **Configuration Files:**
   - `.env` in the root or backend.
   - Is `.env.example` synchronized?
5. **Connectivity:**
   - Successful connection to the configured database.

## 4. Agile Planning (Tasks)
- [ ] **Task 1:** Create `scripts/doctor.py` with basic runtime validations.
- [ ] **Task 2:** Add validation of `.env` files and installed packages.
- [ ] **Task 3:** Implement verification of ports and active services.
- [ ] **Task 4:** Integrate into `package.json` and document in `README.md`.

## 5. Acceptance Criteria (DoD)
- The script runs in less than 5 seconds.
- Clearly reports the status of each item.
- Returns a non-zero exit code if there are critical failures.
