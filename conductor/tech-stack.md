# Technical Context (tech-stack.md)

## Frontend Web
- **Framework:** React 18+, TypeScript.
- **Styling:** Tailwind CSS, shadcn/ui.
- **State:** Zustand (Client-side), React Query (Sync).
- **Visualization:** react-konva / d3.js (Smart Home Canvas).

## Backend & Agentics
- **Framework:** LangGraph (Python/JS) com nodes determinísticos e reativos.
- **RAG Engine:** LangChain (RecursiveCharacterTextSplitter, PyPDFLoader).
- **LLMs:** Gemini 2.5 Pro (Multimodal), Ollama (Local).
- **Database:** PostgreSQL (pg16) com pgvector e PostgresSaver (Memória Persistente).
- **Streaming:** WebSockets para streaming de respostas.

## Integration
- **IDE:** Model Context Protocol (MCP) para VS Code.
- **Infra:** Vercel (Web), Docker (Local).
