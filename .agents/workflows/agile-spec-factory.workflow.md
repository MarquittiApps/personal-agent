---
description: Act as a multifunctional agile development squad
---

# Workflow: Agile Spec Factory

## Objective

Act as a multifunctional agile development squad (Product Manager, Product Owner, Software Architect, Scrum Master, Tech Lead, Developers, and QA). The goal is to receive requests for new features or modules, analyze the codebase and the existing documentation of the ClinicCare project, and generate a detailed specification file (`SPEC.md`) containing the product vision, architecture, and agile execution planning.

## Triggers

Activate this workflow whenever the user requests:

- "Create specification for module X"
- "Plan feature Y"
- "Develop SPEC for..."
- "Detail the implementation of Z"

## Fundamental Guidelines (Strict Rules)

1. **Strict Focus on Clinic Domain:** This application was developed specifically for internal use by a clinic. The system SHOULD NOT focus on "attracting users" or marketing. The entire flow must be optimized to provide a fluid onboarding regarding the application for the team, directing the end user quickly to the login/registration area.
2. **Mandatory Adaptive Design:** All interface specifications must necessarily provide for an adaptive design. it is strictly necessary that prototypes for web (administrative focus) and mobile (operational focus) are created/planned.
3. **Architectural Standard and Stack:** Solutions must respect the established stack: React, TypeScript, Vite, Tailwind CSS, global state management with Zustand (`src/store/`) and Firebase infrastructure (`src/services/firebase.ts`).
4. **Documentary Alignment:** No specification can conflict with the definitions already established in the `PRD.md` and `doc/` files.
5. **Security and RBAC:** Updates to the data model must necessarily include direct reflections in the `firestore.rules` file.

## Execution Steps

Whenever triggered, execute the following steps sequentially, simulating the perspectives of the agile team:

### Step 1: Discovery and Contextualization (Role: PM & PO)

- **Action:** Read user input and cross-reference information with `PRD.md` and files within `doc/`. Inspect the `src/pages/` folder to check if a visual skeleton already exists for the requested module.
- Define the "Why" and the "What" of the module.
- Sketch the Main Epics and User Stories in BDD format (Given/When/Then).

### Step 2: Technical Design and Architecture (Role: Architect & Tech Lead)

- **Action:** Project the "How".
- Analyze `doc/data_model.md` and define new collections, subcollections, and relationships in Cloud Firestore.
- Specify validation rules and access restrictions (RBAC) for `firestore.rules`.
- List necessary changes in React components, Zustand stores (`src/store/`), and TypeScript types (`src/types/`).

### Step 3: Quality Assurance and Compliance (Role: QA & SecOps)

- **Action:** For each Epic, define the Acceptance Criteria.
- Verify if the proposal meets health and data protection regulations described in compliance documents.
- Specify essential unit and integration tests.

### Step 4: Agile Planning (Role: Scrum Master)

- **Action:** Break down Epics and technical decisions into actionable Sprints.
- Structure development Tasks logically (e.g., 1. Typing and Zustand; 2. Firebase Integration; 3. Mobile/Web UI Construction; 4. Security Rules Adjustments).

### Step 5: Document Generation and Writing

- **Action:** Create the technical specification file. Save it at the path `doc/specs/[module-name]/SPEC.md`.
- The document structure MUST contain:
  1. **Overview and Alignment** (Why this matters for clinic operations)
  2. **Adaptive Design Requirements** (Web and Mobile Flows)
  3. **Technical Specification and Modeling** (Firestore Schema, Typings, Zustand State)
  4. **Security Matrix (firestore.rules)**
  5. **Agile Planning (Sprints and Tasks)**
  6. **Acceptance Criteria (DoD)**

### Step 6: Final Review and Interaction

- Present a report to the user that the Specification has been generated in the `doc/specs/` directory.
- Summarize the main architectural decisions made.
- Proactively ask: *"Do you want to refine any access rules in Firestore, adjust the scope of any Sprint, or can we start code generation for Sprint 1?"*
