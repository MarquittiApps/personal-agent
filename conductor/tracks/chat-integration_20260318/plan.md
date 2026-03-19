# Implementation Plan: Integração Omnibar & LLM Chat

## Phase 1: Communication Infrastructure
- [x] Task: Configure WebSocket endpoint in backend.
    - [x] Create socket handler for LangGraph streaming events.
    - [x] Implement event routing logic.
- [x] Task: Set up chat state in frontend.
    - [x] Create `chatStore.ts` using Zustand.
    - [x] Implement WebSocket client connection hook.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Connectivity' (Protocol in workflow.md)

## Phase 2: Core Messaging & Streaming
- [ ] Task: Refactor Omnibar for message dispatch.
    - [ ] Integrate Omnibar with `chatStore`.
    - [ ] Implement message sending via socket.
- [ ] Task: Implement Streaming Message Component.
    - [ ] Create `ChatMessage` with progressive text rendering.
    - [ ] Handle real-time token updates from state.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Streaming Functional' (Protocol in workflow.md)

## Phase 3: UX & Feedback
- [ ] Task: Implement Agent Status Indicators.
    - [ ] Visual feedback for "thinking" and "tool execution".
    - [ ] Auto-scroll to latest message.
- [ ] Task: Error Handling & Reconnection.
    - [ ] Graceful degradation on connection loss.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Final Polish' (Protocol in workflow.md)
