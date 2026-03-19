# Feature: Local LLM Integration (Ollama)

**Epic:** EP-01 — Core Foundation & Infrastructure
**Status:** Ready
**Created:** 2026-03-19
**Updated:** 2026-03-19

---

## Vision

Allow the agent to use models like Llama 3 via Ollama locally, without depending on paid APIs, for fast development and testing. The solution will include an automated configuration script and an onboarding tutorial to facilitate adoption.

---

## Impacted Personas

- **Developer (Solo-Builder):** Can quickly iterate on agent behavior without incurring Google or Anthropic API costs during local development and testing.

---

## User Story

> As a **Personal AI Core developer**, I want to **configure the agent to use Ollama locally** to **reduce API costs during development and iterate faster in testing.**

---

## Acceptance Criteria (BDD)

**Scenario 1: Setup via Script and Tutorial**
- **Given** that a script (`scripts/setup_local_llm.sh`) and a tutorial (`doc/guides/local-llm-setup.md`) exist
- **When** the developer follows the tutorial and runs the configuration script
- **Then** the configured models (e.g., `llama3`, `mistral`) become available locally and ready for use by the agent

**Scenario 2: Routing to Local Model**
- **Given** that Ollama is running locally with a model available
- **When** the agent receives a message and the `LLM_PROVIDER=ollama` variable is configured
- **Then** the agent responds using the configured local model, without calling external APIs (Google AI, OpenAI, etc.)

**Scenario 3: Graceful Fallback**
- **Given** that Ollama is not available locally
- **When** the agent is initialized
- **Then** the system logs a clear error and falls back to the provider configured in `LLM_PROVIDER` (default: `google`)

---

## Out of Scope

- Model fine-tuning or weight adjustment
- Integration with alternative cloud providers like Amazon Bedrock or Azure OpenAI
- Model selection UI in the React dashboard
- Automated comparative assessment (benchmarks) between models

---

## Technical Constraints

- The backend uses **LangGraph + LangChain** — the solution must maintain compatibility with the `BaseChatModel` interface
- Provider abstraction must be done in `app/core/graph.py`, replacing `ChatGoogleGenerativeAI` with a factory function
- The local model must be configurable via environment variables (e.g., `LLM_PROVIDER`, `OLLAMA_MODEL`, `OLLAMA_BASE_URL`)

---

## Design Notes

- Use `langchain_ollama.ChatOllama` which natively implements `BaseChatModel`
- The LLM factory must support: `google` (default), `ollama`
- Configuration via `.env`: `LLM_PROVIDER=ollama`, `OLLAMA_MODEL=llama3`, `OLLAMA_BASE_URL=http://localhost:11434`

---

## Risks

- **Tool compatibility:** Smaller local models may not support function calling (tool use) correctly — document known limitations in the tutorial
- **Performance:** Local models on CPU are slower — there is no response SLA for local mode
