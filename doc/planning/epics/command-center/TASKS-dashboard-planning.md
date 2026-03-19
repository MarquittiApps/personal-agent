# Technical Breakdown: 3-Layer Planning Dashboard

## Phase 1: Setup/Foundation
- [ ] Task 1.1: Design the base UI component for the Dashboard in the frontend (`web/src/components/dashboard/PlanningDashboard.tsx`), separating the 3 layers into smaller components (Daily, Weekly, Monthly view).
- [ ] Task 1.2: Configure the initial state in Zustand to store goals in the 3 layers, with update *actions* based on structured JSON payloads.

## Phase 2: Core Implementation (Backend / Agent)
- [ ] Task 2.1: Update the *system prompt* in the Agent (LangGraph / `app/core/`) to instruct it to proactively ask if the dashboard should be updated when planning-related transactions occur.
- [ ] Task 2.2: Create or adapt a Tool in the backend that receives updates (added or revised) from the Agent and generates a structured planning output.

## Phase 3: Integration/UI (WebSocket & Frontend)
- [ ] Task 3.1: Configure the backend to emit a specific WebSocket event (e.g., `DASHBOARD_UPDATE`) containing the planning structure (JSON), logging securely (without leaking PII).
- [ ] Task 3.2: Configure a listener for the `DASHBOARD_UPDATE` event in the frontend (`web/src/lib/useSocket.ts`), triggering the formatted payload directly into the Zustand *store* to update the UI instantly.

## Phase 4: Testing and Polishing
- [ ] Task 4.1: End-to-end test interacting with the chat (e.g., "Reserve tomorrow afternoon for the thesis and readjust the weekly goal").
- [ ] Task 4.2: Confirm the update question trigger, answer affirmatively, and verify if the visual dashboard reflects the new Daily/Weekly layout without reloading the page.

## Final Verification
- [ ] All acceptance criteria met
- [ ] No browser console errors (WebSockets / Store bindings)
- [ ] GDPR & logs audited (confidential goal information not logged openly)
- [ ] DoD met (according to Product_Roadmap.md)

---

## QA & Security Checklist

- [ ] **RBAC:** Ensure in the interface and WS that only the logged-in user's data (active token) is rendered in the planning.
- [ ] **Data Stores:** Where will the layer state be persisted? If it's in PostgreSQL, it's necessary to create a new table/model and routes to load the initial state upon the first opening of the screen.
- [ ] **Critical Tests:** Test the parsing of JSON payloads received from the Agent. If the LLM returns faulty JSON or incorrect types, the dashboard should not break, handling everything with fallbacks (Zod / Validation Schemas).
- [ ] **Backend:** Isolate the planning route or tool to never send critical or executive commands that do not belong to the dashboard *view* feature.
