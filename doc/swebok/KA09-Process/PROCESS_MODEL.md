# Process Model — Personal AI Core

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 09 (SE Process)

---

## 1. Life Cycle Model

**Model:** Agile (Iterative & Incremental) with SWEBOK governance overlay.

Due to the Requirements Volatility (SWEBOK KA 07) inherent in AI-powered systems, an Agile life cycle is mandated. New LLM capabilities emerge frequently, requiring rapid adaptation.

## 2. Development Flow

```
  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ Specify  │────▶│  Plan    │────▶│  Tasks   │────▶│Implement │────▶│ Verify   │
  │ (KA 01)  │     │ (KA 02)  │     │ (KA 10)  │     │ (KA 04)  │     │ (KA 05)  │
  └──────────┘     └──────────┘     └──────────┘     └──────────┘     └─────┬────┘
       ▲                                                                     │
       │                        ◀────────── Doc-Sync (KA 09) ──────────────┘
       │
  CONSTITUTION.md (Governance Anchor)
```

## 3. Quality Gates

Each phase transition requires passing through a quality gate:

| Gate | From → To | Checks |
|------|-----------|--------|
| G1 | Specify → Plan | SRS entry exists with acceptance criteria |
| G2 | Plan → Tasks | ADR documented for significant decisions |
| G3 | Tasks → Implement | Task breakdown approved, no spec conflicts |
| G4 | Implement → Verify | Tests written, lint clean, security checklist |
| G5 | Verify → Done | All DoD criteria met (see CONSTITUTION.md) |

## 4. Configuration Items (Versioned)

Per SWEBOK KA 08, the following items are version-controlled:

| Item | Location | Format |
|------|----------|--------|
| Source Code | `app/`, `web/` | Git |
| AI Model References | `.env`, `app/core/llm_factory.py` | Git |
| System Prompts | `app/core/graph.py` | Git |
| Database Schemas | PostgreSQL migrations | Git |
| Agent Rules | `.agents/rules/` | Git |
| Agent Skills | `.agents/skills/` | Git |
| SWEBOK Artifacts | `doc/swebok/` | Git |

---

> **Governance:** Process changes require an ADR and CONSTITUTION.md amendment.
