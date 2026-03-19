---
name: swebok-compliance-master
description: "Master governance rule enforcing SWEBOK v4 Knowledge Area compliance across all development activities."
---

# Rule: SWEBOK v4 Compliance Master

## Objective

Ensure every development activity in the Personal AI Core project is traceable to at least one SWEBOK v4 Knowledge Area (KA). This rule acts as the root governance policy — all other SWEBOK rules derive authority from this one.

## SWEBOK Knowledge Areas (Reference)

| ID | Knowledge Area | Governance Doc |
|----|----------------|----------------|
| KA01 | Software Requirements | `doc/swebok/KA01-Requirements/SRS.md` |
| KA02 | Software Architecture & Design | `doc/swebok/KA02-Architecture/ARCHITECTURE_VIEWS.md` |
| KA03 | Software Construction | `.agents/rules/no-vibe-coding.md` |
| KA04 | Software Testing | `.agents/rules/ai-collaboration.md` §Automated Testing |
| KA05 | Software Maintenance | `doc/swebok/KA10-Management/DEVELOPMENT_PLAN.md` |
| KA09 | Software Engineering Process | `doc/swebok/KA09-Process/CONSTITUTION.md` |
| KA10 | Software Engineering Management | `doc/swebok/KA10-Management/DEVELOPMENT_PLAN.md` |
| KA12 | Software Quality | `doc/swebok/KA12-Quality/QUALITY_PLAN.md` |
| KA13 | Software Engineering Security | `doc/swebok/KA13-Security/THREAT_MODEL.md` |

## Triggers (When to Activate)

- **Always** — this rule is active for every agent interaction that produces or modifies code, documentation, or configuration.
- Before creating a new feature, fix, or refactor.
- Before approving a Pull Request or merge.
- During architecture or design discussions.

## Essential Rules

### 1. Traceability Mandate
Every code change **MUST** be traceable to a requirement in `SRS.md` (REQ-NNN format). If no requirement exists, the agent must:
1. Propose a new REQ-NNN entry.
2. Get user approval.
3. Register it in `SRS.md` before implementing.

### 2. Artifact Pre-Check
Before modifying any core module, the agent **MUST** verify these documents are current:
- [ ] `SRS.md` — requirement exists for the change
- [ ] `ARCHITECTURE_VIEWS.md` — design is consistent
- [ ] `CONSTITUTION.md` — change meets Definition of Done

### 3. KA Tagging in Commits
Commits that relate to specific SWEBOK governance activities should reference the KA in the commit body:
```
feat(auth): add JWT refresh token rotation

Refs: REQ-012 | KA13-Security
```

### 4. Living Documentation
All `doc/swebok/` documents are **living documents**. When a code change impacts a KA document, the agent **MUST** update the document in the same commit or in an immediately following atomic commit.

### 5. Conflict Resolution
When rules conflict, precedence order is:
1. `CONSTITUTION.md` (supreme law)
2. `swebok-compliance-master.md` (this rule)
3. `no-vibe-coding.md`
4. `swebok-quality-gates.md`
5. `swebok-security-checklist.md`
6. Other `.agents/rules/` files

## What Not to Do (Don'ts)

- **Never** implement a feature without a traceable requirement.
- **Never** skip the artifact pre-check for "quick fixes" — all changes are equal.
- **Never** treat `doc/swebok/` as read-only historical docs — they must evolve with the code.
- **Never** merge a PR that introduces untraceable code.
