---
name: tech-stack
description: "Defines the mandatory architecture and technologies of the project to avoid library hallucinations."
---

# Tech Stack Rules

Whenever acting on the Personal AI Core, the agent MUST respect the defined technological stack to ensure compatibility and maintainability.

## Core Technologies
- **Backend:** Python 3.12+ (FastAPI).
- **Frontend:** React 19+ (Vite, TypeScript, Tailwind).
- **Database:** PostgreSQL with `pgvector` extension (via Docker).
- **Local AI:** Ollama (Llama 3, Phi-3).
- **AI Orchestration:** LangChain / LangGraph.

## Library Choice Rules
1. **Preference for Natives:** Always prefer standard Python libraries or integrated React modules.
2. **Data Standard:** Use `Pydantic v2` for data schemas in the backend and `Zod` in the frontend.
3. **ORM/Query Builder:** Use the standard already established in the project (Drizzle or Prisma). **NEVER** introduce a new ORM without prior consultation.
4. **State in the Frontend:** Use `Zustand` for simple global state.

## What Not to Do (Don'ts)
- Do not use AI libraries other than LangChain/LangGraph unless the Spec explicitly asks for it.
- Do not introduce UI components outside of `Tailwind CSS`.
- Do not suggest the use of NoSQL databases (MongoDB, etc.) for relational data.
