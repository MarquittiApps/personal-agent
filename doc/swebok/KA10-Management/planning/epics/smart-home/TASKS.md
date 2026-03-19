# Technical Breakdown: EP-03 Smart Home

## Phase 1: Setup/Foundation
- [ ] Task 1.1: Environment and Canvas dependencies configuration (install and configure `react-konva` or `d3.js`).
- [ ] Task 1.2: Develop asset library (SVG) for Zigbee/Matter icons and register in code.
- [ ] Task 1.3: Design structured upload API in backend/Cloud Functions.

## Phase 2: Core Implementation
- [ ] Task 2.1: Implement base Canvas component with Zoom, Pan, and Drag-and-Drop support (Frontend).
- [ ] Task 2.2: Create image upload logic and interface for the dashboard.
- [ ] Task 2.3: Implement node in LangGraph for image analysis via Gemini 2.5 Pro.
- [ ] Task 2.4: Create system prompt for identifying zones of interest on the floor plan and structured return.

## Phase 3: Integration/UI
- [ ] Task 3.1: **[Dependency EP-08]** Update Gemini node in LangGraph to use "Tool Call" querying the RAG Engine (standards/NBR) and filtering the IoT Catalog by customer preference.
- [ ] Task 3.2: Implement suggestive device positioning API (anchored in standards returned from RAG) and integrate the response (X, Y, Type) with the Frontend Canvas.
- [ ] Task 3.3: Create editing flow (Human-in-the-loop) for the user to move the suggested icons rendered in the UI.
- [ ] Task 3.4: Implement YAML code generator for Home Assistant parameterized with the selected hardware.

## Phase 4: Testing and Polishing
- [ ] Task 4.1: Write unit tests for YAML logic generation.
- [ ] Task 4.2: Test Canvas usability on different screen sizes.
- [ ] Task 4.3: Validate multimodal node resilience and LangGraph response.

## QA & Security Check (Mandatory)
- [ ] **RBAC:** What Custom Claims are required for uploading and manipulating the IoT project? *(The user must be authenticated)*
- [ ] **Firestore:** Do new collections (e.g., Smart Home Projects) require updating `firestore.rules`? (Yes, users can only access their own projects)
- [ ] **GDPR:** Does the feature handle sensitive patient data? (In this case, sensitive residential projects; must have restricted Storage)
- [ ] **Critical Tests:** Identify paths that need test coverage: project upload/download authorization.
- [ ] **Cloud Functions:** Calls to Gemini API must be protected in Functions, not executed via client.

## Final Verification
- [ ] Floor plan upload works without crashes.
- [ ] AI positions sensors in logical rooms (e.g., PIR in corners, Thermostat in central zones).
- [ ] Export generates valid YAML.
- [ ] All acceptance criteria met.
- [ ] No console errors.
- [ ] firestore.rules updated.
- [ ] DoD met according to PRD.md.
