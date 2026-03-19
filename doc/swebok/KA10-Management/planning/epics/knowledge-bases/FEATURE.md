# Feature: RAG Knowledge Base & Catalogs

**Epic:** EP-08
**Status:** Backlog
**Created:** 2026-03-19
**Updated:** 2026-03-19

## Vision

Create the fundamental Knowledge Base engine (RAG - Retrieval-Augmented Generation) for the entire Personal AI Core / ClinicCare ecosystem. This module will be responsible for storing, chunking, vectorizing, and retrieving technical standards (such as NBR-5410) in PDFs and managing a relational database of an intelligent IoT hardware catalog (brands, models, YAML payloads).

## Impacted Personas

- **AI Agents (Meta-Persona):** The ecosystem itself gains long-term vector memory to base its decisions on technical standards, without hallucinating.
- **Engineers/Automation Architect:** Can trust that the designed projects (in EP-03) are technically feasible and following the real catalog they work with.

## User Story

> As the **ClinicCare AI Agent**, I want to **have access to a vector database with regulatory standards and a hardware catalog** to **base my decisions (such as generating Smart Home Projects) on real-world data.**

## Acceptance Criteria (BDD)

**Scenario 1: Ingestion of Technical Standards**
- **Given** the Knowledge Base administration panel
- **When** an engineer uploads a PDF of NBR-5410
- **Then** the system must extract the text, generate semantic chunks, create embeddings, and store them in the Vector DB (e.g., pgvector or Pinecone).

**Scenario 2: Semantic Query by the Agent (RAG)**
- **Given** LangGraph in execution to prepare an electrical/residential project
- **When** the agent needs to evaluate the proximity of outlets in a wet area
- **Then** the RAG query node must search for the most relevant applicable rule, injecting it into the prompt.

**Scenario 3: Intelligent Catalog Management**
- **Given** the system database
- **When** a new hardware device is registered via API/Panel
- **Then** it must have attributes defined as Category, Protocol (Zigbee/Matter), Brand, Pinout, and its Base YAML Payload.

## Out of Scope

- Implementing fine-tuning based on standards (we will use only RAG via in-context learning/tools).

## Design Notes

- N/A for complex end-user UI; interface will be mostly internal (CRUDs in React/Tailwind on the Dashboard).
- Vector DB Decision: Recommended Postgres with `pgvector` extension to consolidate relational and vector state and avoid startup lock-in, as well as aligning with Prisma/Drizzle.

## Technical Constraints

- The *Document Loader* and *Text Splitter* (LangChain/LlamaIndex) process needs to be optimized so as not to lose tables from technical PDFs.
- *Embeddings* require APIs (e.g., `text-embedding-3-large` or equivalent).

## GDPR Risks

- Does not involve patient data. However, manuals or PDFs with restricted copyrights can only be consumed internally under appropriate license.
