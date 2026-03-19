# Track Specification: Integração Omnibar & LLM Chat

## 1. Context
- **Project:** Personal AI Core.
- **Track:** Chat Integration (WebSocket Streaming).
- **Goal:** Implement real-time communication between the Command Center Omnibar and the LangGraph backend.

## 2. Requirements
- Real-time message sending via WebSocket.
- Streaming responses from LLM (token by token).
- Visual indicators for thinking/tool execution.
- Session-based state management with Zustand.

## 3. Tech Stack
- **Frontend:** React, Zustand, WebSocket API.
- **Backend:** FastAPI/Python (LangGraph).

## 4. Acceptance Criteria
- [ ] Messages sent via Omnibar appear in chat history.
- [ ] LLM responses render progressively (streaming).
- [ ] System status (thinking/tool call) is visually represented.
- [ ] Connection errors are handled gracefully.
