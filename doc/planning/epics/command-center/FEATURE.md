# Feature: Omnibar & LLM Chat Integration

**Epic:** EP-02 - Command Center (Web Dashboard)
**Status:** Done
**Created:** 2026-03-18
**Updated:** 2026-03-18

## Vision
Provide the user with the main entry point to interact with the AI ecosystem, allowing the sending of natural language instructions and the receiving of responses processed by agents in real-time (streaming).

## Impacted Personas
- **Solo-Builder (Main User):** Benefits from a fluid interface to orchestrate complex tasks without leaving the dashboard.

## User Story
> As a **Solo-Builder**, I want to **send natural language text messages using the omnibar** so that the **LLM interprets and executes tasks with the available tools and/or agents**.

## Acceptance Criteria (BDD)

**Scenario 1: Sending and Immediate Feedback**
- **Given** that the Command Center is loaded and connected to the backend.
- **When** I type an instruction in the Omnibar and press `Enter`.
- **Then** the Omnibar must be cleared, and my message must instantly appear in the chat area with the status "sending".

**Scenario 2: Streaming Response (Real-time)**
- **Given** that a request has been sent to the LLM.
- **When** the LangGraph backend starts generating the response.
- **Then** I must see the text being "typed" on the screen in real-time (streaming).

**Scenario 3: Tool/Agent Execution**
- **Given** that I request something that requires a tool (e.g., "Check the database status").
- **When** the Supervisor Agent identifies the intent.
- **Then** the UI must display a visual log or indicator that the "Database Check" tool was triggered.

## Out of Scope
- Voice Input.
- Upload of multimedia files (PDF, Images).
- History persistence between browser sessions (focus on the current session).
- Advanced Markdown (tables/graphs).

## Design Notes
- Use the central command bar (Omnibar) with auto-focus when loading the page.
- Minimalist style following the Modern/Glassmorphism theme.

## Technical Constraints
- Communication via **WebSockets** mandatory for streaming.
- Message state management via **Zustand**.
- Secrets (API Keys) must remain exclusively on the backend.

## GDPR Risks
- Data minimization: Do not process sensitive third-party data unless explicitly requested by the user in a private context.
