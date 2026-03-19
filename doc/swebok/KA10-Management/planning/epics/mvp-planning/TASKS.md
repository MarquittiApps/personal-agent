# Technical Breakdown: Daily Planning MVP with AI (EP-07)

## Phase 1: Setup/Foundation
- [x] Task 1.1: Configure project in the Google Cloud Console and enable APIs (Google Calendar API and Google Tasks API).
- [x] Task 1.2: Implement OAuth2 authentication flow in the backend (`app/`) to securely capture and store tokens (Access Token and Refresh Token) in PostgreSQL.

## Phase 2: Core Implementation (Backend / Agent)
- [x] Task 2.1: Develop the Tool (LangGraph) to fetch the day's appointments via Google Calendar API.
- [x] Task 2.2: Develop the Tool (LangGraph) to fetch, create, and update tasks via Google Tasks API.
- [x] Task 2.3: Develop the Tool (LangGraph) to schedule new events in Google Calendar.
- [x] Task 2.4: Update the Meta-Agent / Personal Assistant system prompt to use these tools, analyze the returned data, and generate proactive insights (time windows, overload).

## Phase 3: Integration/UI (Frontend)
- [x] Task 3.1: Update the `app/main.py` file to ensure the LLM responds correctly in the WebSocket session (partial integration already exists, only final tests are needed).
- [x] Task 3.2: Ensure the frontend integration with the websocket can render markdown tables or lists, as the agent will respond in this format (validation in `web/`).

## Phase 4: Manual Tests
- [x] Task 4.1: Start the backend (`uvicorn app.main:app --reload`) and the frontend (`npm run dev`).
- [x] Task 4.2: Run the OAuth flow and obtain the token.
- [x] Task 4.3: Send the message "what are my tasks and appointments for today?" via the web interface.
- [x] Task 4.4: Validate if the LLM triggered the tools correctly and assembled the response in the frontend formatted in Markdown or lists.

## Final Verification
- [x] All acceptance criteria met
- [x] No console errors
- [x] Encryption of tokens at rest verified
- [x] DoD met (according to Product_Roadmap.md)

---

## QA & Security Checklist

- [x] **RBAC/Auth:** The system must ensure that each user exclusively accesses authorized Google accounts with their respective Access Token.
- [x] **Data Stores:** OAuth tokens *must* be encrypted at rest in the database (PostgreSQL).
- [x] **GDPR and Privacy:** Titles and descriptions of events and tasks represent sensitive data (PII). System logs must not store the cleartext content of Google API responses, masking information in telemetry logs.
- [x] **Critical Tests:** Test the scenario where the refresh token is invalid or revoked by the user in the Google panel, requiring reauthentication without breaking the agent's chat.
- [x] **Cloud Functions/Backend:** Communication with Google will be done strictly via authenticated backend, never exposing sensitive tokens to the frontend (React).
