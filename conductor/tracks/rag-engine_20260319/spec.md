# Specification: Base de Conhecimento RAG & Catálogos

**Track ID:** rag-engine_20260319
**Type:** feature
**Created:** 2026-03-19
**Status:** Draft

## Summary
Criar a engine fundamental de Knowledge Base (RAG) para o ecossistema e gerenciar banco de dados relacional de catálogo inteligente de hardware IoT.

## Context
O ecossistema ClinicCare/Personal AI Core necessita de RAG (Vector DB) para basear decisões da IA em normas (ex. NBR-5410) reais, e um CRUD para o Catálogo de dispositivos IoT, servindo o épico Smart Home e sistemas futuros.

## User Story
Como Agente de IA do ClinicCare, quero ter acesso a um banco vetorial com normas regulatórias e um catálogo de hardwares para fundamentar minhas decisões com dados do mundo real.

## Acceptance Criteria
- [ ] Ingestão de Normas Técnicas via PDF gera chunks semânticos e embeddings no Vector DB.
- [ ] Consulta RAG via LangGraph retorna as regras aplicáveis.
- [ ] Gerenciamento do Catálogo Inteligente via Painel salva Marcas, Protocolos e Payloads YAML base.

## Dependencies
- PostgrSQL com pgvector ou Pinecone/outro VectorDB

## Out of Scope
- Implantação de fine-tuning baseada nas normas.

## Technical Notes
- Backend: LangChain/LlamaIndex com text splitter robusto.
- Postgres com `pgvector` e ORM Prisma/Drizzle.
- RLS e restriçao de acessos nos uploads de manuais.
