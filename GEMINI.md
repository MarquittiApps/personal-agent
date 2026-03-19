# GEMINI.md — Personal AI Core (Meta-Instructional Ecosystem)

This repository is the "brain" and orchestration engine of the **Personal AI Core**, a modular artificial intelligence ecosystem designed to act as a professional co-pilot in engineering, IT, and personal management.

---

## 📂 Ecosystem Structure (.agents/)

The intelligence of this repository is centralized in the `.agents/` folder, organized into three fundamental pillars:

### 1. Skills (`.agents/skills/`)
Specialized instructions by domain. Before performing any specific task (e.g., UI Design, Security, Diagnostics), consult the corresponding skill.
- **Andru.ia Core:** Skills prefixed with numbers (e.g., `00-andruia-consultant`) are fundamental for the diagnosis and architecture of new projects. **Mandatory Language: ENGLISH** (Previously Spanish).
- **Specialized Skills:** Range from `ui-ux-pro-max` to `mcp-builder` and `playwright-skill`.

### 2. Workflows (`.agents/workflows/`)
Standard Operating Procedures (SOPs) for multi-step tasks.
- **`/planning`:** SCRUM planning workflow for epics and features (see `planning.workflow.md`).
- **`/docs`:** Management and generation of technical documentation.
- **`/rules`:** Management and evolution of system rules.

### 3. Rules (`.agents/rules/`)
Governance and global behavior rules for the agent.
- **Atomic Commits:** Mandatory to follow `commits.md` (Conventional Commits + Rigorous Atomicity).

---

## 🛠️ Development Guidelines (Conventional & Atomic)

When acting in this repository or derivative projects:

1.  **Commit Atomicity:** Each commit must perform only ONE logical unit of change. Never mix features, fixes, and refactorings in the same commit.
2.  **Conventional Commits:** Use `<type>[scope]: <description>` (e.g., `feat(skill): add new rbac logic`).
3.  **Context Language:**
    - All documentation, including **PRD.md**, **Workflows**, and **Skills**, must be in **US English**.
    - Code identifiers and low-level technical documentation must be in **English**.
    - UI supports multiple languages via i18n (English, Portuguese, Spanish).

---

## 🚀 How to Start

1.  **Initial Diagnosis:** Whenever the user requests a new action or project, check if the skill `@00-andruia-consultant` or the workflow `/planning` should be invoked first.
2.  **Product Context:** Read the `PRD.md` in the root to understand the long-term vision of the **Personal AI Core** and the **ClinicCare** SaaS.
3.  **Human-in-the-Loop:** Follow the requested interruptions in the workflows to ensure user validation before proceeding with automatic implementations.

---

## 🧠 Meta-Agent Vision (Auto-Evolution)

As described in the **PRD.md (Section 5.1)**, this system must be capable of evolving itself.
- If you identify a repetitive pattern, suggest the creation of a new **Skill** or **Workflow**.
- Use the rules in `.agents/rules/` to ensure the system's evolution maintains the "Diamond" quality standard.
