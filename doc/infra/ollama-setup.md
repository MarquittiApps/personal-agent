# Local LLM Setup Guide (Ollama)

This guide explains how to set up and use **local** Large Language Models (via [Ollama](https://ollama.com)) in the Personal AI Core, eliminating dependency on paid APIs during development and testing.

> **When to use local LLMs?**
> - During active development (to avoid API costs)
> - Offline integration testing
> - Experimenting with different open-source models

---

## 1. Prerequisites

| Requirement | Recommended Minimum |
|---|---|
| RAM | 8 GB (for Llama 3 8B) |
| Free Storage | 6 GB (for Llama 3 model) |
| OS | Windows 10/11, macOS 12+, Ubuntu 20.04+ |
| GPU (Optional) | NVIDIA with CUDA — significantly accelerates performance |

---

## 2. Automated Setup (Recommended)

### Windows (PowerShell)

```powershell
# From the project root
.\scripts\setup_local_llm.ps1
```

### Linux / macOS (bash)

```bash
# From the project root
bash scripts/setup_local_llm.sh
```

**The script will:**
1. Check for/install Ollama.
2. Download the default model (`llama3`).
3. Update your `.env` with `LLM_PROVIDER=ollama`.
4. Verify server connectivity.

---

## 3. Manual Setup

### 1. Install Ollama

- **Windows/macOS:** Download the installer from [ollama.com](https://ollama.com)
  ![Ollama Home](C:\Users\Luis Marquitti\.gemini\antigravity\brain\e616235c-9591-45a5-9f92-f408b299be95\ollama_home_1773943814893.png)
- **Linux:**
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

### 2. Download a Model

```bash
# Llama 3 (recommended — good balance of quality/speed)
ollama pull llama3

# Mistral (faster, smaller)
ollama pull mistral

# CodeLlama (better for code generation)
ollama pull codellama
```

### 3. Start Ollama Server

Ensure the Ollama application is running (check system tray) or run:
```bash
ollama serve
```
> Server will be available at `http://localhost:11434`

### 4. Configure `.env`

Edit your `.env` file in the project root:

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3
OLLAMA_BASE_URL=http://localhost:11434
```

### 5. Restart the Backend

```bash
npm run dev:backend
```

You should see in the console:
```
[LLM] Provider: ollama | Model: llama3 | URL: http://localhost:11434
[LLM] Ollama available at http://localhost:11434
```

---

## 4. Switching Between Providers

Edit your `.env` and restart the backend:

```env
# Switch back to Google AI (Default)
LLM_PROVIDER=google

# Use local Ollama
LLM_PROVIDER=ollama
```

---

## 5. Recommended Models

| Model | Command | RAM | Use Case |
|---|---|---|---|
| **llama3** | `ollama pull llama3` | 8 GB | General purpose (Default) |
| **mistral** | `ollama pull mistral` | 5 GB | Faster responses |
| **codellama** | `ollama pull codellama` | 8 GB | Code generation |
| **llama3:70b** | `ollama pull llama3:70b` | 48 GB | High quality (GPU recommended) |

---

## ⚠️ Known Limitations

### Function Calling (Tools)
Smaller local models might not correctly support **function calling** (using tools like `get_todays_calendar_events`).

- **llama3** — partial tool support (may work for simple tools)
- **mistral** — unstable tool support
- **codellama** — not recommended for tool use

> **Recommendation:** To test complex tool flows (Google Calendar, Tasks), use the `google` provider. For conversation and RAG, Ollama works great.

### Latency
Local models on CPU are significantly slower:
- NVIDIA GPU: 1-5 seconds per response
- CPU only: 10-60 seconds per response

---

## Troubleshooting

- **Error: `Ollama is not available at http://localhost:11434`**
  - Check if `ollama serve` is running.
  - Test connectivity: `curl http://localhost:11434/api/tags`
- **Error: `ValueError: Unknown provider`**
  - Verify `LLM_PROVIDER` in your `.env`. Accepted values: `google`, `ollama`.
- **Model not responding / timeout**
  - Ensure you have enough RAM for the selected model.
  - Try a smaller model (`mistral` instead of `llama3`).
