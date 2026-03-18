# Breakdown Técnico: EP-01 Fundação Core

## Fase 1: Setup da Fundação
- [ ] Tarefa 1.1: Inicializar repositório Monorepo para `web/` e `server/`.
- [ ] Tarefa 1.2: Configurar Docker Compose com PostgreSQL e PgAdmin.
- [ ] Tarefa 1.3: Setup do servidor FastAPI com o core do LangGraph e endpoints iniciais.
- [ ] Tarefa 1.4: Configurar o template base do React com Vite, Tailwind CSS e shadcn/ui.

## Fase 2: Persistência e Estado
- [ ] Tarefa 2.1: Implementar `PostgresSaver` no LangGraph para memória de longo prazo.
- [ ] Tarefa 2.2: Criar store global no Frontend com Zustand (user, session, agentStatus).
- [ ] Tarefa 2.3: Implementar WebSocket no FastAPI para streaming de respostas.

## Fase 3: Segurança & RBAC
- [ ] Tarefa 3.1: Integrar autenticação básica (Firebase ou JWT).
- [ ] Tarefa 3.2: Definir permissões de acesso aos módulos (Personal, Dev, IoT).

## Verificação Final (DoD)
- [ ] Repositório compila e executa sem erros em modo dev.
- [ ] Banco de dados persiste sessões de chat corretamente.
- [ ] Linter e Type-check passando (tsc, eslint).
- [ ] DoD atendido conforme PRD.md.
