# Specification: Infraestrutura de Produção e Ciclo de Deploy (v2.0)

## Overview
Implementar a infraestrutura de produção para o ecossistema **Personal Agent**, garantindo uma arquitetura *Zero-Trust*, escalabilidade serverless e custos otimizados. O ciclo de vida será automatizado via GitHub Actions, integrando o backend no **Google Cloud Run**, persistência no **Supabase**, inteligência via **Gemini API** e frontend no **Firebase Hosting**.

## Functional Requirements
- **Backend (Cloud Run):** Deploy automático do FastAPI (Python 3.11+) via GitHub Actions.
- **Frontend (Firebase Hosting):** Deploy automático do React (Vite) via GitHub Actions, com suporte a canais de preview para Pull Requests.
- **Banco de Dados (Supabase):** Configuração de persistência vetorial com `pgvector` e pooling de conexões (Supavisor).
- **Segurança (Zero-Trust):** 
    - Uso de *Workload Identity Federation (WIF)* para autenticação entre GitHub e GCP (sem Service Account Keys).
    - Uso de *GCP Secret Manager* para injeção dinâmica de segredos no Cloud Run.
- **Observabilidade:** Monitoramento básico via Cloud Logging.

## Non-Functional Requirements
- **Performance:** Imagem Docker otimizada (< 200MB) e uso de *Startup CPU Boost* no Cloud Run.
- **Escalabilidade:** Escalonamento automático (0 a N instâncias) para controle de custos.
- **Segurança:** Scan de vulnerabilidades (Trivy) e análise estática (CodeQL/Snyk) no pipeline CI/CD.

## Acceptance Criteria
- [ ] **Build Docker Otimizado:** Backend dockerizado com multi-stage build passando no scan de vulnerabilidades.
- [ ] **Pipeline CI/CD (GitHub Actions):** 
    - Push na branch `main` dispara deploy automático para Produção (Cloud Run + Firebase).
    - Abrir PR dispara deploy de preview no Firebase Hosting.
- [ ] **Segredos Seguros:** Nenhuma chave Service Account JSON ou segredos sensíveis no repositório. O Cloud Run consome segredos do Secret Manager.
- [ ] **Conectividade:** Backend conectando com sucesso ao Supabase (pgvector) e à API do Gemini em produção.
- [ ] **Documentação Operacional:** Pasta `docs/deploy/` com guias de configuração para WIF, Secret Manager, Firebase e Supabase.

## Out of Scope
- Configuração de Domínio Personalizado (uso de URLs geradas automaticamente por Cloud Run/Firebase).
- Configuração de WAF (Cloud Armor).
- Implementação de Testes de Carga.
