# Tasks: Omnibar & LLM Chat Integration

## Phase 1: Communication Setup (Backend)
- [ ] Task 1.1: Configure WebSocket endpoint in FastAPI/Node for LangGraph event streaming.
- [ ] Task 1.2: Implement message routing middleware in the Graph stream.
- [ ] Task 1.3: Validate sending of partial tokens via socket.

## Phase 2: State and UI (Frontend)
- [ ] Task 2.1: Create `chatStore.ts` (Zustand) to manage message array and connection status.
- [ ] Task 2.2: Refactor `Omnibar.tsx` component to trigger events via WebSocket.
- [ ] Task 2.3: Implement `ChatMessage.tsx` component with support for progressive rendering (streaming).

## Phase 3: Visual Feedback and Polishing
- [ ] Task 3.1: Add visual indicators for "Thinking..." or "Calling Tool".
- [ ] Task 3.2: Implement auto-scroll in the chat area when receiving new tokens.
- [ ] Task 3.3: Add connection error handling (Reconnection logic).

## Phase 4: Testing and Polishing
- [ ] Task 4.1: Write unit tests for the Zustand store.
- [ ] Task 4.2: Test response latency in a local environment.
- [ ] Task 4.3: Validate that secrets are not leaking in the WebSocket payload.

---

## QA & Security Check (Role: QA)

### Mandatory Checklist:
- [ ] **RBAC:** Verify if the authenticated user has permission to invoke the Supervisor Agent.
- [ ] **Firestore:** Ensure that chat logs (if optional recording exists) respect the subcollection structure per user.
- [ ] **GDPR:** Validate if the log cleaning script is ignoring sensitive data.
- [ ] **Critical Tests:** Simulate internet drop during streaming and validate if the UI does not freeze.

## Final Verification (DoD)
- [ ] Code compiled and error-free.
- [ ] Unit tests passing.
- [ ] Documentation updated in the module's README.
- [ ] Code style validated.
