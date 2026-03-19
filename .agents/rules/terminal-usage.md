---
name: terminal-usage
description: "Standardizes the execution of commands in the terminal and defines the project's tool ecosystem."
---

# Terminal & Ecosystem Rules

To avoid execution failures and ensure the portability of the AI Agents' work, strictly follow the instructions below.

## 🖥️ Shell & Environment (Windows/PowerShell)
The project is running in a **Windows 10/11** environment using **PowerShell**.
- **Chaining Operator:** Use `;` or execute commands separately. **NEVER** use `&&` (Bash/Linux style).
- **Paths:** Use `\` for local paths (e.g., `app\main.py`).
- **Scripts:** Use `.\scripts\name.ps1` for PowerShell scripts.

## 🛠️ Tool Ecosystem (Available Commands)

### 🐍 Python (Backend & Scripts)
- **Interpreter:** Use `python` (verify if the venv is active).
- **Package Manager:** `pip`.
- **Main Commands:**
    - `python scripts\doctor.py`: Infrastructure validation.
    - `pytest`: Unit test execution.
    - `uvicorn app.main:app --reload`: Development server.

### 📦 Node.js / NPM (Frontend)
- **Directory:** Always run commands inside the `web\` folder.
- **Manager:** `npm`.
- **Main Commands:**
    - `npm install`: Install dependencies.
    - `npm run dev`: Start Vite server.
    - `npm run build`: Generate production build.
    - `npm test`: Run Vitest.

### 🤖 IA & Automation
- **Jules CLI:** `jules` (for remote tasks).
- **GitHub CLI:** `& "C:\Program Files\GitHub CLI\gh.exe"` (Use absolute path if `gh` is not in the PATH).
- **Ollama:** `ollama run <model>` (for local tests).

### 🐳 Infrastructure
- **Docker:** `docker-compose up -d`.

## ⚠️ Best Practices (Do's & Don'ts)
- **Do:** Verify the existence of a file before trying to run it with `ls` or `Test-Path`.
- **Do:** Use double quotes in paths with spaces.
- **Don't:** Do not assume that Linux commands (e.g., `export`, `grep -P`, `which`) work without adaptation in PowerShell. Use `Set-Style`, `Select-String`, or `Get-Command` if necessary.
- **Don't:** Do not try to run `npm` in the project root; the frontend is isolated in `web\`.
