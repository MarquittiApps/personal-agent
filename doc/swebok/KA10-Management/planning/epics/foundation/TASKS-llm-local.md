# Tasks: Local LLM Integration (Ollama)

**Feature:** FEATURE-llm-local.md
**Epic:** EP-01 — Core Foundation & Infrastructure
**Created:** 2026-03-19

---

## Phase 1: Foundation — LLM Provider Abstraction

- [ ] **1.1** Create `app/core/llm_factory.py` with a `get_llm()` function that returns a `BaseChatModel` based on the `LLM_PROVIDER` environment variable
  - Support: `google` (default) → `ChatGoogleGenerativeAI`, `ollama` → `ChatOllama`
  - Read variables: `LLM_PROVIDER`, `OLLAMA_MODEL` (default: `llama3`), `OLLAMA_BASE_URL` (default: `http://localhost:11434`)
- [ ] **1.2** Refactor `app/core/graph.py` to use `get_llm()` from the factory instead of hardcoded `ChatGoogleGenerativeAI`
- [ ] **1.3** Add `langchain-ollama` dependency to `requirements.txt`
- [ ] **1.4** Update `.env.example` with the new variables: `LLM_PROVIDER`, `OLLAMA_MODEL`, `OLLAMA_BASE_URL`

---

## Phase 2: Automated Setup Script

- [ ] **2.1** Create `scripts/setup_local_llm.sh` (Linux/macOS) and `scripts/setup_local_llm.ps1` (Windows/PowerShell) that:
  - Detects and installs Ollama (if not installed)
  - Pulls the default model (`llama3` or `mistral`)
  - Adds the variables to the local `.env`
  - Verifies if the Ollama server is responding at `http://localhost:11434/api/tags`
- [ ] **2.2** Add error handling to scripts: display clear message if Ollama does not initialize correctly

---

## Phase 3: Fallback & Resilience

- [ ] **3.1** Implement graceful fallback in `llm_factory.py`: if `LLM_PROVIDER=ollama` but the server is not available, log warning and return `None` (the `graph.py` should handle and log the error)
- [ ] **3.2** Add Ollama health-check in FastAPI startup (`app/main.py`): log availability of the configured provider upon starting

---

## Phase 4: Documentation and Tutorial

- [ ] **4.1** Create `doc/guides/local-llm-setup.md` with step-by-step tutorial:
  - Prerequisites (minimum recommended hardware)
  - Ollama installation
  - How to run the setup script
  - How to switch between providers via `.env`
  - Known limitations (function calling in smaller models)
  - Recommended models by use: llama3 (default), mistral (faster), codellama (code)
- [ ] **4.2** Update the main `README.md` with "Development with Local LLM" section

---

## Phase 5: Testing

- [ ] **5.1** Create `app/tests/test_llm_factory.py` with unit tests (pytest):
  - Scenario: `LLM_PROVIDER=google` → returns `ChatGoogleGenerativeAI`
  - Scenario: `LLM_PROVIDER=ollama` → returns `ChatOllama` with correct parameters
  - Scenario: unknown provider → throws `ValueError` with clear message
- [ ] **5.2** Manual integration test: run `pytest app/tests/test_llm_factory.py` and verify result
- [ ] **5.3** Test agent end-to-end with `LLM_PROVIDER=ollama` and Ollama running locally

---

## ✅ Final Verification (DoD)

- [ ] `get_llm()` correctly returns `ChatGoogleGenerativeAI` or `ChatOllama` based on `LLM_PROVIDER`
- [ ] `graph.py` no longer contains hardcoded `ChatGoogleGenerativeAI`
- [ ] Setup scripts work on Windows (PowerShell) and Linux/macOS (bash)
- [ ] `doc/guides/local-llm-setup.md` tutorial complete and reviewed
- [ ] `test_llm_factory.py` unit tests passing (`pytest`)
- [ ] `.env.example` updated with new variables
- [ ] No errors in the console when starting the backend with both providers

---

## 🔒 QA & Security Check

- **RBAC:** ✅ N/A — development infrastructure feature, no user data access
- **Sensitive Data:** ⚠️ `OLLAMA_BASE_URL` should not be exposed in logs — ensure the factory does not log credentials
- **Critical Tests:** Cover fallback path (Ollama offline) and happy path (both providers)
- **Cloud Functions:** ✅ N/A — exclusively local execution
