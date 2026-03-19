# Feature: Smart Home Module (Multimodal Canvas)

**Epic:** EP-03
**Status:** In Progress
**Created:** 2026-03-18
**Updated:** 2026-03-19

## Vision
Provide an interactive interface where the user can upload architectural plans (PDF/Image) and receive intelligent suggestions for positioning IoT devices (Zigbee/Matter) via multimodal AI.

## Impacted Personas
- **IoT Architect / Automation Engineer:** To automate sensor coverage design.

## User Story
> As an **automation designer**, I want to **upload a floor plan** so **that the AI suggests the ideal positioning of sensors and generates the YAML code for Home Assistant.**

## Acceptance Criteria (BDD)

**Scenario 1: Upload and Multimodal Processing**
- **Given** the Smart Home Canvas on the dashboard
- **When** the user uploads a JPG image of the plan
- **Then** the Gemini 2.5 Pro agent must identify rooms and doors.

**Scenario 2: Visual Device Suggestion**
- **Given** the processed plan
- **When** the AI finishes reasoning
- **Then** icons of suggested sensors with coverage zones must be rendered on the Canvas (Konva/D3).

**Scenario 3: Deliverable Generation**
- **Given** the project approved by the user
- **When** the user clicks "Export"
- **Then** the system must generate a YAML file compatible with Home Assistant.

## Out of Scope
- Actual automation of physical devices (only YAML code generation).
- Automatic device recognition from generic plans without clear scale.

## Design Notes
- Frontend: Use the project's design system (`Specs_UX_UI.md`) for the canvas container. The interactive canvas can use `react-konva` with zoom, pan, and drag-and-drop support.

## Technical Constraints
- Backend: LangGraph with computer vision node (Gemini API 2.5 Pro).
- Support for Drag-and-Drop of IoT components on the canvas.
- External API integrations and calls (Gemini) must be made via Cloud Functions/Backend, never by the client.

## GDPR Risks
- Uploading the architectural plan may reveal private information about the user's residence.
- Mitigations: Images should not be used to train the model, without permanent cloud storage unless strictly necessary (or implement periodic deletion and encryption at rest).
