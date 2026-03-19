---
description: "Governance workflow to ensure every task follows the SWEBOK v4 Quality Gates and compliance protocols."
---

# SWEBOK Governance Workflow

This workflow ensures that the **Personal AI Core** maintains a "Diamond" quality standard by enforcing SWEBOK v4 Knowledge Area checks at every stage of development.

## 1. Task Initiation (KA10 Management)
1. Read the current Track (`spec.md` and `plan.md`).
2. Verify if the task is clearly defined and scoped.
3. Check for open dependencies or blockers.

## 2. Requirements Check (KA01 Requirements)
1. Identify the REQ-NNN associated with this task in `doc/swebok/KA01-Requirements/SRS.md`.
2. If no requirement exists, use the **SWEBOK Requirements Analyst** skill to create and register it.
3. // turbo
   Verify the requirement is in 'Approved' status.

## 3. Architecture & Design Check (KA02 Architecture)
1. Consult `doc/swebok/KA02-Architecture/ARCHITECTURE_VIEWS.md` to ensure the planned change respects the system structure.
2. If the change impacts architecture (e.g., new module, new API pattern), use the **SWEBOK Architect** skill to update the views.

## 4. Construction & Quality Gates (KA03 & KA12)
1. Invoke the rule `.agents/rules/no-vibe-coding.md` before writing any code.
2. Declare the implementation strategy and wait for user acknowledgment (if required by rule).
3. Implement the changes following atomic commit rules.
4. Apply the checks in `.agents/rules/swebok-quality-gates.md` periodically.

## 5. Security Pre-flight (KA13 Security)
1. Run the checklist in `.agents/rules/swebok-security-checklist.md`.
2. Cross-reference with `doc/swebok/KA13-Security/THREAT_MODEL.md` for potential impact.

## 6. Verification & Closure (KA04 Testing)
1. Run all relevant tests (`pytest`, `vitest`, `playwright`).
2. // turbo
   Capture test output as evidence of compliance.
3. Update `doc/swebok/KA01-Requirements/TRACEABILITY_MATRIX.md` with the new REQ-to-Code mapping.
4. Finalize the task in `PROGESS.md` and commit with standard prefixes.
