# Command Center Architecture (EP-02)

## Overview
The Command Center is the primary user interface for the Personal AI Core, built with React, TypeScript, and Vite.

## Components
- **MainLayout:** Manages the overall application structure, including the sidebar and main content area.
- **Sidebar:** Handles navigation between different modules.
- **SystemDashboard:** Displays real-time system metrics and agent health status.
- **Omnibar:** The command input interface for interacting with AI agents.

## State Management
- **useChatStore (Zustand):** Manages chat history and streaming interaction state.
- **useSystemStore (Zustand):** Manages system status and agent health data.

## AI Interaction
- **Mock Streaming (Phase 3):** Simulated WebSocket interaction in `src/lib/socket.ts` that mimics real-time streaming responses from a backend.

## Testing
- **Vitest + React Testing Library:** Unit and component testing with `jsdom` environment.
