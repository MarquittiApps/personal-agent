# Technical Breakdown: EP-08 RAG Knowledge Base & Catalogs

## Phase 1: Setup/Foundation (Infrastructure)
- [ ] Task 1.1: Configure `pgvector` extension in current PostgreSQL or provision external Vector DB.
- [ ] Task 1.2: Configure ORM/Data Schema for IoT Products (Brands, Types, Specs, Payload).
- [ ] Task 1.3: Develop documentation schema for chunks and metadata in the DB.

## Phase 2: Core Implementation (RAG Pipeline)
- [ ] Task 2.1: Create Document Loading pipeline (PDF parse and OCR for dense texts like NBRs).
- [ ] Task 2.2: Implement intelligent text splitting and indexing generating embeddings via API.
- [ ] Task 2.3: Implement Semantic Retrieval endpoint (tool/retriever) exposable to LangGraph.

## Phase 3: Integration/UI
- [ ] Task 3.1: Create forms in the `Command Center` (Dashboard) for basic IoT Hardware Catalog CRUD.
- [ ] Task 3.2: Create view for uploading and managing Regulatory Documents consumed by the RAG engine.

## Phase 4: Testing and Polishing
- [ ] Task 4.1: Retriever unit tests: validate search precision (Top-K) for key NBR-5410 questions.
- [ ] Task 4.2: Ensure friendly fallback when RAG does not return relevant results.

## QA & Security Check (Mandatory)
- [ ] **RBAC:** Only 'Admin' or 'Architect' users can feed the Catalog and standards PDFs.
- [ ] **Firestore/Postgres:** `Row Level Security` (RLS) if using Supabase; protect catalog CRUD routes.
- [ ] **GDPR:** Sanitize logs to not store sensitive prompts that use this RAG if there are embedded personal data.
- [ ] **Cloud Functions:** Heavy chunking process should not run on simple Cloud Functions but on more powerful instances, or delegated to specific cloud services with queues (Inngest/PubSub).

## Final Verification
- [ ] Uploading a standard generates embeddings in the vector DB.
- [ ] Test semantic query via API returns the excerpt of the loaded standard.
- [ ] IoT device inclusion saves with the structured JSON/YAML correctly.
- [ ] All acceptance criteria met.
- [ ] DoD met according to PRD.md.
