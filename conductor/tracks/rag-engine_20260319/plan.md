# Implementation Plan: Base de Conhecimento RAG & Catálogos

**Track ID:** rag-engine_20260319
**Spec:** spec.md
**Created:** 2026-03-19
**Status:** [ ] Not Started

## Overview

Dividido em Setup do DB, Pipeline Core de RAG (LangChain + Vector DB), Integração no Frontend (Dashboard CRUD) e Testes.

## Phase 1: Setup/Fundação (Infraestrutura)
Configurar ORM e provisionar Vector DB para RAG e Produtos IoT.
### Tasks
- [ ] Task 1.1: Configurar a extensão `pgvector` no PostgreSQL atual.
- [ ] Task 1.2: Configurar ORM/Schema de dados para Produtos IoT.
- [ ] Task 1.3: Desenvolver esquema de documentação abstrata (chunks/metadata).
### Verification
- [ ] Migrations rodaram e DB suporta embeds e o catálogo relacional.

## Phase 2: Implementação Core (RAG Pipeline)
Criação do pipeline de embedding e endpoints de busca.
### Tasks
- [ ] Task 2.1: Criar pipeline de Document Loading (parse PDF, OCR).
- [ ] Task 2.2: Implementar text splitting inteligente e indexação gerando embeddings.
- [ ] Task 2.3: Implementar API de Retrieval Semântico exponível ao LangGraph.
### Verification
- [ ] Teste local de upload de PDF gera embeddings com sucesso.

## Phase 3: Integração/UI
Criar views no Command Center para gerenciar o DB.
### Tasks
- [ ] Task 3.1: Criar formulários no `Command Center` (Dashboard) para CRUD básico do Catálogo de Hardware IoT.
- [ ] Task 3.2: Criar view para upload de Documentos Regulatórios consumidos pela engine RAG.
### Verification
- [ ] Navegação completa entre tabelas do Catálogo e uploaders na interface web.

## Phase 4: Testes e Polimento
Assegurar qualidade do RAG e segurança das rotas (RBAC/RLS).
### Tasks
- [ ] Task 4.1: Testes unitários do retriever para garantir alta precisao do Top-K.
- [ ] Task 4.2: Testes de RBAC/RLS no uploader e CRUD de Catálogo.
- [ ] Task 4.3: Implementar fallback amigável quando o RAG retorner sem match ou vazio.
### Verification
- [ ] Cobertura validada e permissões de segurança checadas no test suite local.

## Final Verification
- [ ] All acceptance criteria met
- [ ] Tests passing
- [ ] Documentation updated (if applicable)
- [ ] Ready for review
