# Implementation Plan: Integração Omnibar & LLM Chat

## Phase 1: Communication Infrastructure
- [ ] Task: Configure WebSocket endpoint in backend.
    - [ ] Create socket handler for LangGraph streaming events.
    - [ ] Implement event routing logic.
- [ ] Task: Set up chat state in frontend.
    - [ ] Create `chatStore.ts` using Zustand.
    - [ ] Implement WebSocket client connection hook.
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
