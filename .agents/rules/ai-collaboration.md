---
name: ai-collaboration
description: "Collaboration protocols between the user and the ecosystem's AI Agents."
---

# AI Collaboration Protocol

This protocol defines how the Personal AI Core IAs must act to maximize autonomy and quality.

## Development Cycle (Standard)
1. **Research:** The Agent must ALWAYS read the `Tracks` (`spec.md` and `plan.md`) before proposing any code change.
2. **Strategy:** Before coding, the Agent must explain the strategy (e.g., "I will create endpoint X in file Y and test Z").
3. **Execution:** The Agent must make surgical changes, respecting the principle of **Atomicity**.
4. **Validation:** Each implementation MUST be accompanied by its respective unit or integration test.

## Versioning Rules (Skills: `commit`)
1. **Atomic Commits:** Each commit must represent a logical unit of change. If you change backend and frontend in distinct tasks, create two commits.
2. **Conventional Commits:** Use the `<type>(scope): <message>` standard.
    - `feat`: New features.
    - `fix`: Bug fixes.
    - `docs`: Documentation changes.
    - `test`: Addition or refactoring of tests.
    - `refactor`: Code change that neither alters behavior nor fixes a bug.

## Documentation Rules
- Always update `PROGRESS.md` or the Track status after completing a significant task.
- If a new skill is created, it must be properly documented in `.agents/skills/<name>/SKILL.md`.

## Automated Testing (MANDATORY)
- No functionality is considered complete without tests that validate it.
- Use `pytest` for the backend and `vitest` or `playwright` for the frontend.
- The Agent must ALWAYS run the tests before considering the task finished.
