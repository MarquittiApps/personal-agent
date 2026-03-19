# Environment Setup — KA03

Governed by SWEBOK v4 — KA 03 (Software Construction). This document centralizes the setup for AI providers and infrastructure.

## 1. Gemini API Setup
To use Gemini multimodal capabilities:
1. Obtain an API Key from Google AI Studio.
2. Add to `.env`: `GOOGLE_API_KEY=your_key_here`.
3. Reference: [Gemini Documentation](https://ai.google.dev/).

## 2. Ollama (Local LLM) Setup
For local-first inference:
1. Install Ollama: [ollama.com](https://ollama.com/).
2. Pull required models:
   - `ollama pull llama3`
   - `ollama pull phi3`
3. Ensure the Ollama service is running on `localhost:11434`.

## 3. Database (PostgreSQL + pgvector)
Managed via Docker Compose:
```bash
docker-compose up -d db
```
Ensure `pgvector` extension is enabled in the database.
