# Implementation Plan: LLM Configuration & Local Setup Documentation

## Phase 1: Core Configuration Docs
- [x] Task: Create Gemini API Setup Guide.
    - [x] Write `doc/infra/gemini-setup.md`.
    - [x] Include screenshots/links for Google AI Studio.
    - [x] Document `.env` variable requirements.
- [x] Task: Create Local LLM (Ollama) Setup Guide.
    - [x] Write `doc/infra/ollama-setup.md`.
    - [x] Include installation steps for Win/Mac/Linux.
    - [x] List recommended models for this project.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Core Docs' (Protocol in workflow.md)

## Phase 2: Integration & Examples
- [x] Task: Create Integration Tutorial.
    - [x] Write `doc/tutorials/llm-integration.md`.
    - [x] Provide code examples for LangGraph nodes using Gemini.
    - [x] Explain provider switching logic (Cloud vs Local).
- [x] Task: Implement Example Connectivity Scripts.
    - [x] Create `scripts/tests/test_gemini_api.py`.
    - [x] Create `scripts/tests/test_ollama_local.py`.
- [x] Task: Generate Architecture Diagrams.
    - [x] Create Mermaid diagrams in the documentation.
- [x] Task: Conductor - User Manual Verification 'Phase 2: Integration & Examples' (Protocol in workflow.md)

## Phase 3: Final Review & Cleanup
- [x] Task: Verify all links and code blocks.
- [x] Task: Update main `README.md` to link to new documentation.
- [x] Task: Conductor - User Manual Verification 'Final Documentation Audit' (Protocol in workflow.md)
