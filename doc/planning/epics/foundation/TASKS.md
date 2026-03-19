# Technical Breakdown: EP-01 Core Foundation

## Phase 1: Foundation Setup
- [ ] Task 1.1: Initialize Monorepo for `web/` and `server/`.
- [ ] Task 1.2: Configure Docker Compose with PostgreSQL and PgAdmin.
- [ ] Task 1.3: Setup FastAPI server with LangGraph core and initial endpoints.
- [ ] Task 1.4: Configure React base template with Vite, Tailwind CSS, and shadcn/ui.

## Phase 2: Persistence and State
- [ ] Task 2.1: Implement `PostgresSaver` in LangGraph for long-term memory.
- [ ] Task 2.2: Create global store in the Frontend with Zustand (user, session, agentStatus).
- [ ] Task 2.3: Implement WebSocket in FastAPI for streaming responses.

## Phase 3: Security & RBAC
- [ ] Task 3.1: Integrate basic authentication (Firebase or JWT).
- [ ] Task 3.2: Define access permissions for modules (Personal, Dev, IoT).

## Final Verification (DoD)
- [ ] Repository compiles and runs without errors in dev mode.
- [ ] Database correctly persists chat sessions.
- [ ] Linter and Type-check passing (tsc, eslint).
- [ ] DoD met according to PRD.md.
