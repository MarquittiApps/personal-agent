# Architecture Views — Personal AI Core

> **Version:** 1.0  
> **Last Updated:** 2026-03-19  
> **Governed by:** SWEBOK v4 — KA 02 (Software Architecture)  
> **Model:** 4+1 View Model (Kruchten)

---

## 1. Logical View

The system is organized into 6 functional modules led by a Supervisor Agent:

```
┌─────────────────────────────────────────────────────┐
│                  Supervisor Agent                    │
│              (Meta-Agent / Orchestrator)             │
├────────┬────────┬────────┬────────┬────────┬────────┤
│ Daily  │  Dev   │ Smart  │ Elec.  │  IT    │  RAG   │
│Planner │  Ops   │ Home   │ Infra  │ Ops    │ Engine │
│(EP-07) │(EP-04) │(EP-03) │(EP-05) │(EP-05) │(EP-08) │
└────────┴────────┴────────┴────────┴────────┴────────┘
```

**Key Components:**
- **Reasoning Engine:** LangGraph graph with state management and tool calling
- **Tool Registry:** Modular tool definitions in `app/tools/`
- **RAG Engine:** Vector search via pgvector in `app/core/rag_engine.py`
- **LLM Factory:** Model-agnostic interface in `app/core/llm_factory.py`

## 2. Process View

```
User Input (WebSocket/Chat)
    │
    ▼
┌──────────────┐     ┌──────────────────┐
│  FastAPI      │────▶│  LangGraph       │
│  WebSocket    │     │  State Machine   │
│  Handler      │     │  (graph.py)      │
└──────────────┘     └───────┬──────────┘
                             │
                    ┌────────┼────────┐
                    ▼        ▼        ▼
              ┌─────────┐ ┌───────┐ ┌──────────┐
              │ Gemini   │ │Ollama │ │ Tools    │
              │ API      │ │ Local │ │ Registry │
              └─────────┘ └───────┘ └──────────┘
```

**Concurrency:** Async event loop (FastAPI/uvicorn) handles WebSocket connections. LangGraph manages agent state transitions with Human-in-the-Loop interrupts.

## 3. Development View

```
personal-agent/
├── app/                    # Backend (Python/FastAPI)
│   ├── api/                # REST endpoints
│   ├── core/               # Core services (DB, LLM, graph, RAG)
│   ├── models/             # Pydantic data models
│   ├── tools/              # Agent tool definitions
│   └── tests/              # Backend tests
├── web/                    # Frontend (React/TypeScript/Vite)
│   └── src/
│       ├── components/     # UI components
│       ├── pages/          # Route pages
│       ├── store/          # Zustand stores
│       └── types/          # TypeScript types
├── doc/                    # Documentation
│   ├── swebok/             # SWEBOK governance artifacts
│   ├── specs/              # Feature specifications
│   └── planning/           # Epics, backlog, planning
├── .agents/                # Agent configuration
│   ├── rules/              # Governance rules
│   ├── skills/             # Agent skills
│   └── workflows/          # Agent workflows
└── conductor/              # Conductor track management
```

## 4. Physical View

```
┌──────────────────────┐      ┌──────────────────┐
│  Development Machine │      │  Cloud Services  │
│                      │      │                  │
│  ┌────────────────┐  │      │  ┌────────────┐  │
│  │ FastAPI Server │  │◀────▶│  │ Gemini API │  │
│  │ (localhost)    │  │      │  └────────────┘  │
│  └────────────────┘  │      │                  │
│  ┌────────────────┐  │      │  ┌────────────┐  │
│  │ PostgreSQL     │  │      │  │ Vercel     │  │
│  │ (Docker)       │  │      │  │ (Frontend) │  │
│  └────────────────┘  │      │  └────────────┘  │
│  ┌────────────────┐  │      │                  │
│  │ Ollama (Local) │  │      │  ┌────────────┐  │
│  │ LLM Inference  │  │      │  │ GitHub     │  │
│  └────────────────┘  │      │  │ (VCS)      │  │
│  ┌────────────────┐  │      │  └────────────┘  │
│  │ Vite Dev       │  │      └──────────────────┘
│  │ Server (Web)   │  │
│  └────────────────┘  │
└──────────────────────┘
```

**Local-first principle:** User data and interaction history remain on encrypted local volumes (PostgreSQL on Docker). Cloud APIs are used only for LLM inference and deployment.

## 5. Scenarios (+1 View)

See [PRD.md Section 6](file:///c:/devWorkspace/personal-agent/PRD.md) for detailed use cases:
- Morning Dashboard scenario (EP-07)
- Visual Review and Approval (EP-03)
- Continuous Evolution (EP-06)

---

> **ADRs:** Significant architectural decisions are documented as individual ADR files in this directory. See `ADR-001-*.md` onwards.
