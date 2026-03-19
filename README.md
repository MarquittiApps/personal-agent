<div align="center">
  <h1>🧠 Personal AI Core</h1>
  <p>
    <b>A modular orchestration engine and personal AI ecosystem acting as a "second brain" and professional co-pilot.</b>
  </p>
  <p>
    <i>Integrates with your IDE via MCP and provides a high-performance Web Dashboard for complete control over your engineering, software development, and consultancy workflows.</i>
  </p>

<!-- Badges -->
<p>
  <img src="https://img.shields.io/badge/Status-Architecture_&_Planning-orange?style=flat-square" alt="Status" />
  <img src="https://img.shields.io/badge/LangGraph-Agentic_Minds-blue?style=flat-square" alt="LangGraph" />
  <img src="https://img.shields.io/badge/Gemini_2.5_Pro-Powered-purple?style=flat-square" alt="Gemini" />
  <img src="https://img.shields.io/badge/React-Web_Platform-61DAFB?style=flat-square&logo=react" alt="React" />
</p>
</div>

---

## ⚡ Overview

The **Personal AI Core** is designed to reduce administrative load, accelerate software development (specifically the **ClinicCare** SaaS), standardize physical/electrical infrastructure projects, and seamlessly merge personal organization with professional output.

It operates heavily on a **Meta-Agent** architecture that can dynamically write, create, and refine sub-agents or UI components on demand.

## 🏗️ Architecture & Modules

The system is separated into 6 key modules driven by a central Orchestrator (LangGraph + PostgreSQL Memory):

1. **Meta-Agent (Evolution Core):** Supervises and continuously self-improves the agent ecosystem. Capable of creating new tools and web UI components.
2. **Daily Planner (Assistant):** Manages time, communications, operations, and personal context.
3. **Software Development (ClinicCare):** Operates as a Senior Software Engineer via VS Code [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). Executes TDD, pull request reviews, and code generation.
4. **Smart Home & IoT:** Multimodal analysis of floor plans to design environments, generate BOMs (Bill of Materials), and output Home Assistant YAML configurations.
5. **Electrical & Infrastructure:** Technical support for electrical projects and IT/Networking/CCTV topology.
6. **Consultancy Management:** IT consultancy backoffice, proposal generation, and asset management.

## 🚀 Quick Start & Installation

### 1. Prerequisites
Before starting, ensure you have:
- Python 3.10+
- Node.js 18+ & npm
- PostgreSQL (for local LangGraph persistent memory)
- [Ollama](https://ollama.com/) (Optional, for local LLMs)

### 2. Setup & Diagnostic (Highly Recommended)
We provide a built-in diagnostic script to ensure your environment is correctly configured.

1. **Clone and Install:**
   ```bash
   git clone <your-repo-url> personal-ai-core
   cd personal-ai-core
   npm install
   ```

2. **Run the Doctor:**
   This script verifies runtimes, dependencies, services (Postgres/Ollama), and configuration files.
   ```bash
   npm run doctor
   ```

### 3. Manual Steps (If not using the Doctor)

1. **Backend / Agents Setup:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   ```bash
   cp .env.example .env
   # Edit .env to add your keys.
   ```

3. **Frontend Setup:**
   ```bash
   cd web
   npm install
   npm run dev
   ```

## 📖 Documentation & Guides

- **LLM Configuration:**
  - [Gemini API Setup Guide](./doc/infra/gemini-setup.md)
  - [Local LLM (Ollama) Setup Guide](./doc/infra/ollama-setup.md)
- **Developer Tutorials:**
  - [LLM Integration Tutorial](./doc/infra/ollama-setup.md)

## 📖 Usage & Interfaces

- **Web Dashboard:** Access `http://localhost:3000` (by default) to view your morning agenda, pending PR approvals, IoT Canvas, and DevOps board.
- **VS Code Extension (MCP):** The agent binds directly to your IDE workspace, capable of context-aware refactoring, task completion, and executing tests on the fly.

## 🤝 Rules & Conventions (Strict)

This project heavily enforces strict developmental and behavioral rules. Before contributing, read the core rules in **[`GEMINI.md`](./GEMINI.md)**.

### Language Standard:
- **All Source Code, Documentation, & Configs:** English (US).
- **App UI (i18n):** Supports English (US), Portuguese (Brazil), and Spanish.

### Commits & Git Flow:
We strictly follow **Atomic Commits** and **Conventional Commits** (`<type>[scope]: <description>`). Never mix features, fixes, and refactors into a single commit!

> **Note:** The `.agents/` directory is the actual "brain" of the ecosystem housing all prompt configurations, modular skills, and operational workflows. If the agent needs to "learn" something, it goes there.

---
*Built for the Solo-Builder.*
