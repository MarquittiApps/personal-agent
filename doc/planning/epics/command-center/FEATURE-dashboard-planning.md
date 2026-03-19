# Feature: 3-Layer Planning Dashboard

**Epic:** EP-02 - Command Center (Web Dashboard)
**Status:** Draft
**Created:** 2026-03-19
**Updated:** 2026-03-19

## Vision

Provide an interactive dashboard within the Command Center that acts as a visual guide for 3-spiral/layer planning (daily, weekly, monthly). This dashboard must be reactive to chat conversations, updating itself whenever there are approved planning changes in the session.

## Impacted Personas

- **Solo-Builder (Main User):** Keeps the context of their short to long-term goals always visible and synchronized with conversational commands.

## User Story

> As a **Solo-Builder**, I want to **view and iterate on my planning across three horizons (daily, weekly, and monthly)** to **keep my goals always organized and visually synchronized with the decisions made via chat**.

## Acceptance Criteria (BDD)

**Scenario 1: Viewing the 3 Layers**
- **Given** that I am in the Command Center and I open the Planning Dashboard.
- **When** the interface loads.
- **Then** I must see three distinct sections or views corresponding to the Daily, Weekly, and Monthly focus.

**Scenario 2: Proactive AI Prompt**
- **Given** that I interacted with the chat (e.g., added tasks, changed an event, or decided on a new focus for the week).
- **When** the AI finishes processing my request.
- **Then** the AI must ask if I want to update the Planning Dashboard to reflect the changes made.

**Scenario 3: Synchronization and Refresh**
- **Given** that I confirmed the Dashboard update via chat.
- **When** the AI processes the confirmation via LangGraph/Backend.
- **Then** the Dashboard on screen must receive the new state via WebSocket and update in real-time.

## Out of Scope

- Team management or multiple users (single-player only).
- Multi-device real-time visual synchronization without web refresh (focus only on the current Command Center session).

## Design Notes

- Follow the same Minimal/Modern/Glassmorphism as the current Command Center.
- Use clean cards for daily items and macro progress markers for the monthly.

## Technical Constraints

- Deep integration with Zustand for local global state.
- Proactive update via WebSocket from the backend to the dashboard in the frontend.

## GDPR Risks

- Personal goals and annotations may contain PII or sensitive business plans. Data must transit encrypted and, preferably, not be logged in cleartext in telemetry systems.
