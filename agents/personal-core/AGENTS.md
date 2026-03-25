# Sub-agents Registry

This registry tracks all formally defined agents within the `personal-agent` ecosystem that the `personal-core` orchestrator can delegate tasks to.

## Active Sub-agents:

### 1. `swebok-pm` (Product Management)
- **Role:** Requirements Analyst & Agile Scrum Master.
- **Trigger:** When the User wants a new feature, epic, or project planned.
- **Output:** PRDs, user stories, acceptance criteria, `/doc/planejamento/` artifacts.

### 2. `swebok-architect`
- **Role:** Software & Systems Architect.
- **Trigger:** When technical requirements, architecture design, logic patterns, and database planning are needed.
- **Output:** ADRs, C4 Model Diagrams, Technical Specs.

### 3. `fullstack-developer`
- **Role:** The Coder.
- **Trigger:** When the architecture and requirements are confirmed and the system needs to be implemented.
- **Output:** Application Code, Component configurations, Git Commits.

### 4. `qa-auditor`
- **Role:** Quality Assurance & Auditor.
- **Trigger:** Before merging code, when tests are required, or when an issue is reported in production.
- **Output:** Bug reports, test scripts, compliance audits against SWEBOK standard.

## Future / Planned Agents:
- **`financial-controller`:** A future agent designed to analyze personal spending, invoices, and bank integrations.
- **`personal-planner`:** A future agent for managing the user's personal routines, calendars, and habits.
