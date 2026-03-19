# Breakdown Técnico: MVP Planejamento Diário com IA (EP-07)

## Fase 1: Setup/Fundação
- [x] Tarefa 1.1: Configurar projeto no Google Cloud Console e habilitar APIs (Google Calendar API e Google Tasks API).
- [x] Tarefa 1.2: Implementar fluxo de autenticação OAuth2 no backend (`app/`) para capturar e armazenar tokens (Access Token e Refresh Token) com segurança no PostgreSQL.

## Fase 2: Implementação Core (Backend / Agente)
- [x] Tarefa 2.1: Desenvolver a Tool (LangGraph) para buscar compromissos do dia via Google Calendar API.
- [x] Tarefa 2.2: Desenvolver a Tool (LangGraph) para buscar, criar e atualizar tarefas via Google Tasks API.
- [x] Tarefa 2.3: Desenvolver a Tool (LangGraph) para agendar novos eventos no Google Calendar.
- [x] Tarefa 2.4: Atualizar o prompt de sistema do Meta-Agente / Assistente Pessoal para utilizar essas ferramentas, analisar os dados retornados e gerar insights proativos (janelas de tempo, sobrecarga).

## Fase 3: Integração/UI (Frontend)
- [x] Tarefa 3.1: Atualizar o arquivo `app/main.py` para garantir que o LLM responda corretamente na sessão de WebSocket (já existe integração parcial, apenas testes finais são necessários).
- [x] Tarefa 3.2: Garantir que a integração do frontend com o websocket possa renderizar tabelas markdown ou listas, uma vez que o agent vai responder neste formato (validação em `web/`).

## Fase 4: Testes Manuais
- [x] Tarefa 4.1: Levantar o backend (`uvicorn app.main:app --reload`) e o frontend (`npm run dev`).
- [x] Tarefa 4.2: Fazer o fluxo de OAuth rodar e obter o token.
- [x] Tarefa 4.3: Mandar a mensagem "quais são as minhas tarefas e compromissos de hoje?" via web interface.
- [x] Tarefa 4.4: Validar se a LLM acionou as tools corretamente e montou a resposta no frontend formatada em Markdown ou listas.

## Verificação Final
- [x] Todos os critérios de aceite atendidos
- [x] Sem erros no console
- [x] Criptografia de tokens em repouso verificada
- [x] DoD atendido (conforme Product_Roadmap.md)

---

## Checklist QA & Segurança

- [x] **RBAC/Auth:** O sistema deve assegurar que cada usuário acesse exclusivamente as contas Google autorizadas com seu respectivo Access Token.
- [x] **Data Stores:** Tokens OAuth *devem* ser criptografados em repouso no banco de dados (PostgreSQL).
- [x] **LGPD e Privacidade:** Títulos e descrições de eventos e tarefas representam dados sensíveis (PII). Os logs do sistema não devem armazenar o conteúdo em texto claro das respostas da API do Google, mascarando informações nos logs de telemetria.
- [x] **Testes Críticos:** Testar o cenário onde o refresh token é inválido ou revogado pelo usuário no painel do Google, exigindo reautenticação sem quebrar o chat do agente.
- [x] **Cloud Functions/Backend:** A comunicação com o Google será feita estritamente via backend autenticado, nunca expondo tokens sensíveis para o frontend (React).
