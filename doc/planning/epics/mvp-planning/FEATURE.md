# Feature: Daily Planning MVP with AI

**Epic:** Planning MVP (EP-07)
**Status:** Done
**Created:** 2026-03-18
**Updated:** 2026-03-19

## Vision

Allow the user to view and manage their appointments and tasks (Google Calendar and Tasks) via conversational chat, resulting in a consolidated "Planning" section with AI-generated insights to optimize the day.

## Impacted Personas

- **Solo-Builder / Consultant / Main User:** Can centralize the governance of their daily tasks without having to switch between tools, receiving time optimization suggestions directly on the interface.

## User Story

> As the **Main User**, I want to **send a message in the chat asking about my appointments and tasks** to **get a consolidated dashboard with AI-generated insights that help me plan my day in an optimized way**.

## Acceptance Criteria (BDD)

**Scenario 1: Inquiry via Chat**
- **Given** that the user is in the Command Center (chat)
- **When** the user types "what are my appointments and tasks for today?"
- **Then** the agent must fetch the Google Calendar and Google Tasks data for the requested date and return the status in the chat.

**Scenario 2: Display in Planning Section**
- **Given** that the calendar and task data have been retrieved by the agent
- **When** the chat response is processed
- **Then** the "Planning" section of the application must reflect this information (listing of events and tasks).

**Scenario 3: AI Insight Generation**
- **Given** that the Planning section is populated with the day's data
- **When** the data is presented
- **Then** the system must display AI-generated insights (e.g., priority suggestions, overload warnings, or free time windows).

**Scenario 4: Data Insertion (Calendar/Tasks)**
- **Given** that the agent has write integration with Google APIs
- **When** the user requests the addition of a new event or task via chat
- **Then** the agent must insert the information into Google Calendar/Tasks and update the Planning interface.

## Out of Scope

- Any integration or functionality that is not strictly related to Google Calendar and Google Tasks (e.g., Microsoft Outlook, sending emails, integrations with other task managers).

## Design Notes

- The "Planning" section should be perfectly integrated into the *Command Center* (Web Dashboard - EP-02), possibly using a side panel layout or expandable card on the Home screen.
- Necessary to reflect the Design System already in progress (shadcn/ui and Tailwind CSS, Dark Mode).

## Technical Constraints

- Implementation of the OAuth2 flow for secure connection with Google Calendar and Google Tasks.
- Creation of Tools in LangGraph/Agent capable of reading and writing via Google APIs.
- Real-time update of the Frontend via WebSocket or Server-Sent Events when triggering the tools.

## GDPR Risks

- The system will handle OAuth tokens that grant access to data from the user's personal calendar. It is necessary to encrypt sensitive storage and define explicit consent.
