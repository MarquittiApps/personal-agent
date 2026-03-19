# Breakdown Técnico: Dashboard de Planejamento 3-Camadas

## Fase 1: Setup/Fundação
- [ ] Tarefa 1.1: Desenhar o componente base de UI para o Dashboard no frontend (`web/src/components/dashboard/PlanningDashboard.tsx`), separando as 3 camadas em componentes menores (Daily, Weekly, Monthly view).
- [ ] Tarefa 1.2: Configurar o estado inicial no Zustand para armazenar as metas nas 3 camadas, com *actions* de atualização baseadas em payloads JSON estruturados.

## Fase 2: Implementação Core (Backend / Agente)
- [ ] Tarefa 2.1: Atualizar o *system prompt* no Agente (LangGraph / `app/core/`) para instruí-lo a proativamente perguntar se o dashboard deve ser atualizado quando transações relacionadas a planejamento ocorrerem.
- [ ] Tarefa 2.2: Criar ou adaptar Tool no backend que recebe do Agente as atualizações (adicionadas ou revisadas) e gera um output de planejamento estruturado.

## Fase 3: Integração/UI (WebSocket & Frontend)
- [ ] Tarefa 3.1: Configurar no backend a emissão de um evento WebSocket específico (ex: `DASHBOARD_UPDATE`) contendo a estrutura (JSON) do planejamento, logando de forma segura (sem vazar PII).
- [ ] Tarefa 3.2: Configurar no frontend (`web/src/lib/useSocket.ts`) um listener para o evento `DASHBOARD_UPDATE`, disparando o payload formatado diretamente na *store* do Zustand para atualizar a UI instantaneamente.

## Fase 4: Testes e Polimento
- [ ] Tarefa 4.1: Teste de ponta-a-ponta interagindo com o chat (ex: "Reserve amanhã de tarde para o TCC e reajuste a meta da semana").
- [ ] Tarefa 4.2: Confirmar o gatilho da pergunta sobre atualização, responder afirmativamente, e atestar se o dashboard visual reflete o novo layout Diário/Semanal sem recarregar a página.

## Verificação Final
- [ ] Todos os critérios de aceite atendidos
- [ ] Sem erros no console do navegador (WebSockets / Store bindings)
- [ ] LGPD & logs auditados (informações confidenciais de metas não logadas abertamente)
- [ ] DoD atendido (conforme Product_Roadmap.md)

---

## Checklist QA & Segurança

- [ ] **RBAC:** Garantir na interface e WS que apenas os dados do usuário logado (token ativo) sejam renderizados no planejamento.
- [ ] **Data Stores:** O estado das camadas será persistido onde? Se for no PostgreSQL, é necessário criar uma nova tabela/model e rotas para carregar o estado inicial na primeira abertura da tela.
- [ ] **Testes Críticos:** Testar o parseamento de payloads JSON recebidos do Agente. Se a LLM retornar JSON defeituoso ou tipos incorretos, o dashboard não deve quebrar, tratando tudo com fallbacks (Zod / Schemas de validação).
- [ ] **Backend:** Isolar a rota ou tool de planejamento para nunca enviar comandos críticos ou executivos que não competem à feature de dashboard de *view*.
