Esta é a especificação (spec) técnica atualizada e refinada para o projeto **Personal Agent**. Ela foi desenhada para servir como o "plano mestre" de implementação para um agente de IA ou desenvolvedor DevOps, focando em máxima segurança, automação e clareza operacional.

---

# Feature: Infraestrutura de Produção e Ciclo de Deploy (v2.0)

## 1. Descrição Geral
Implementar a infraestrutura de produção para o ecossistema **Personal Agent**, garantindo uma arquitetura *Zero-Trust*, escalabilidade serverless e custos otimizados. O ciclo de vida será automatizado via GitHub Actions, integrando o backend no **Google Cloud Run**, persistência no **Supabase**, inteligência via **Gemini API** e frontend no **Firebase Hosting**.

## 2. Stack Tecnológica de Produção
* **Backend:** FastAPI (Python 3.11+) em Google Cloud Run.
* **Frontend:** React (Vite) em Firebase Hosting.
* **Banco de Dados:** PostgreSQL + `pgvector` no Supabase (Transaction Mode).
* **LLM:** Gemini 2.0 Flash via Google AI Studio.
* **Segurança:** Workload Identity Federation (WIF) e GCP Secret Manager.
* **CI/CD:** GitHub Actions.

---

## 3. Objetivos Técnicos e Backlog de Tarefas

### Tarefa 1: Autenticação e Segurança (WIF)
**Objetivo:** Eliminar o uso de chaves Service Account JSON no GitHub.
* **Ação do Agente:** Tentar configurar via gcloud CLI o *Workload Identity Pool* e o *Provider OIDC*.
* **Documentação Obrigatória:** Se o agente não possuir permissões para execução direta no GCP, ele **deve** gerar um arquivo `docs/deploy/setup-wif.md` com os comandos exatos e capturas de tela conceituais de como configurar o vínculo entre GitHub e GCP Console.

### Tarefa 2: Dockerização Multi-Stage Otimizada
**Objetivo:** Imagem < 200MB e tempo de boot (Cold Start) reduzido.
* **Ação do Agente:** Criar `backend.Dockerfile` com dois estágios:
    1.  `builder`: Instala pacotes de sistema e dependências via `pip` ou `uv`.
    2.  `runtime`: Base `python:3.11-slim`, copiando apenas os artefatos compilados.
* **Configuração:** Definir usuário não-root e ajustar variáveis `PYTHONUNBUFFERED=1` e `PYTHONDONTWRITEBYTECODE=1`.

### Tarefa 3: Pipeline de Backend (Cloud Run)
**Objetivo:** Deploy automático com injeção segura de segredos.
* **Ação do Agente:** Criar `.github/workflows/deploy-backend.yml`.
* **Especificações de Deploy:**
    * Habilitar *Startup CPU Boost*.
    * Configurar segredos via referências diretas ao Secret Manager (ex: `GOOGLE_API_KEY=secrets/GEMINI_KEY:latest`).
* **Manual do Usuário:** Criar `docs/deploy/secret-manager-guide.md` detalhando quais segredos devem ser criados manualmente no painel do GCP.

### Tarefa 4: Pipeline de Frontend (Firebase Hosting)
**Objetivo:** Canais de preview para PRs e produção para a branch `main`.
* **Ação do Agente:** Criar `.github/workflows/deploy-frontend.yml` e configurar o `firebase.json` com políticas de cache (headers de `Cache-Control`).
* **Manual do Usuário:** Criar `docs/deploy/firebase-setup.md` explicando como inicializar o projeto no console do Firebase e obter o `FIREBASE_SERVICE_ACCOUNT_TOKEN` (se necessário).

### Tarefa 5: Integração com Supabase (pgvector)
**Objetivo:** Garantir persistência vetorial e pooling de conexões.
* **Ação do Agente:** Atualizar a lógica de conexão para usar a string do Supavisor (porta `6543`) e garantir que a extensão `pgvector` seja validada no startup.
* **Manual do Usuário:** Criar `docs/deploy/supabase-config.md` com o SQL script necessário para habilitar as extensões e criar as tabelas vetoriais iniciais.

---

## 4. Política de Contingência (Documentação como Código)

**Regra de Ouro para o Agente:**
Para qualquer tarefa que exija interação manual com dashboards de terceiros ou permissões que o Agente não possui no ambiente atual, ele deve obrigatoriamente:
1.  **Parar a implementação técnica.**
2.  **Criar um Guia de Configuração Passo a Passo** em Markdown na pasta `docs/deploy/`.
3.  **Especificar os "Inputs" necessários:** Ex: "Copie a URL de conexão do Supabase e cole no Secret Manager do Google Cloud com o nome `DB_URL`".

---

## 5. Critérios de Aceite
1.  **Push na main** dispara o build Docker, push para o Artifact Registry e atualização do Cloud Run.
2.  **PR aberto** gera uma URL única de preview no Firebase Hosting.
3.  **Logs do Cloud Run** mostram o Agente conectando ao Supabase e à API do Gemini sem erros de credenciais.
4.  **Segurança:** O repositório GitHub não contém nenhuma string sensível ou arquivo `.json` de chaves.
5.  **Documentação:** A pasta `docs/deploy/` contém guias completos para um usuário leigo replicar o ambiente.

---
