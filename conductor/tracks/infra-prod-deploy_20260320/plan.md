# Implementation Plan: Infraestrutura de Produção e Ciclo de Deploy (v2.0)

## Objective
Estabelecer a infraestrutura de produção escalável e segura (Zero-Trust) para o Personal Agent, automatizando o ciclo de deploy via GitHub Actions para GCP (Cloud Run) e Firebase Hosting, com persistência no Supabase.

## Key Files & Context
- `app/`: Código-fonte do Backend (FastAPI).
- `web/`: Código-fonte do Frontend (React/Vite).
- `.github/workflows/`: Pipelines de CI/CD.
- `docker-compose.yml`: Referência para a infraestrutura local (Docker).
- `requirements.txt`: Dependências do Backend.

---

## Phase 1: Segurança e Identidade (Workload Identity Federation)
Configurar a conexão segura entre GitHub e Google Cloud Platform sem o uso de chaves Service Account JSON.

- [ ] Task: Criar Guia de Configuração `docs/deploy/setup-wif.md` (Comandos GCP CLI).
- [ ] Task: Definir segredos no GitHub Actions (`GCP_PROJECT_ID`, `GCP_WIF_PROVIDER`).
- [ ] Task: Testar autenticação básica em um workflow de teste (`test-auth.yml`).
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Setup e Segurança'

## Phase 2: Dockerização e Pipeline de Backend (Cloud Run)
Criar imagem Docker multi-stage otimizada e configurar deploy automático.

- [ ] Task: Criar `backend.Dockerfile` (Multi-stage build, python:3.11-slim, usuário não-root).
- [ ] Task: Criar workflow `.github/workflows/deploy-backend.yml` (Build, Scan, Push, Deploy).
- [ ] Task: Integrar GCP Secret Manager no Cloud Run para injeção de `GOOGLE_API_KEY`.
- [ ] Task: Configurar *Startup CPU Boost* e limites de memória/CPU no deploy.
- [ ] Task: Adicionar scan de vulnerabilidades (Trivy) no build docker.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Dockerização e Backend'

## Phase 3: Pipeline de Frontend (Firebase Hosting)
Configurar deploy automático do React (Vite) com suporte a canais de preview.

- [ ] Task: Criar Guia de Configuração `docs/deploy/firebase-setup.md`.
- [ ] Task: Configurar `firebase.json` com políticas de Cache-Control e redirecionamento de SPA.
- [ ] Task: Criar workflow `.github/workflows/deploy-frontend.yml` (Build, Deploy Production/Preview).
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Frontend e Firebase Hosting'

## Phase 4: Supabase e Integração de Dados (pgvector)
Validar persistência vetorial e garantir pooling de conexões em produção.

- [ ] Task: Criar Guia de Configuração `docs/deploy/supabase-config.md` (Scripts SQL).
- [ ] Task: Atualizar `app/core/config.py` (ou similar) para suportar pooling do Supavisor (porta 6543).
- [ ] Task: Implementar script de verificação de extensão `pgvector` no startup do backend.
- [ ] Task: Conductor - User Manual Verification 'Phase 4: Supabase e Integração'

## Phase 5: Observabilidade e Documentação Operacional
Finalizar guias de usuário e validar logs e monitoramento.

- [ ] Task: Criar `docs/deploy/secret-manager-guide.md` (Guia de gerenciamento de segredos).
- [ ] Task: Validar logs unificados no Cloud Logging.
- [ ] Task: Revisar Definition of Done (DoD) para a track completa.
- [ ] Task: Conductor - User Manual Verification 'Phase 5: Finalização'
