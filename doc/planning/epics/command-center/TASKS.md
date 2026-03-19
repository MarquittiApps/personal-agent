# Tasks: Integração Omnibar & LLM Chat

## Fase 1: Setup de Comunicação (Backend)
- [ ] Tarefa 1.1: Configurar endpoint de WebSocket no FastAPI/Node para streaming de eventos do LangGraph.
- [ ] Tarefa 1.2: Implementar middleware de roteamento de mensagens na stream do Grafo.
- [ ] Tarefa 1.3: Validar envio de tokens parciais via socket.

## Fase 2: Estado e UI (Frontend)
- [ ] Tarefa 2.1: Criar `chatStore.ts` (Zustand) para gerenciar array de mensagens e status de conexão.
- [ ] Tarefa 2.2: Refatorar componente `Omnibar.tsx` para disparar eventos via WebSocket.
- [ ] Tarefa 2.3: Implementar componente `ChatMessage.tsx` com suporte a renderização progressiva (streaming).

## Fase 3: Feedback Visual e Polimento
- [ ] Tarefa 3.1: Adicionar indicadores visuais de "Pensando..." ou "Chamando Ferramenta".
- [ ] Tarefa 3.2: Implementar auto-scroll na área de chat ao receber novos tokens.
- [ ] Tarefa 3.3: Adicionar tratamento de erros de conexão (Reconnection logic).

## Fase 4: Testes e Polimento
- [ ] Tarefa 4.1: Escrever testes unitários para a store do Zustand.
- [ ] Tarefa 4.2: Testar latência de resposta em ambiente local.
- [ ] Tarefa 4.3: Validar se segredos não estão vazando no payload do WebSocket.

---

## QA & Segurança Check (Papel: QA)

### Checklist Obrigatório:
- [ ] **RBAC:** Verificar se o usuário autenticado tem permissão para invocar o Agente Supervisor.
- [ ] **Firestore:** Garantir que logs de chat (se houver gravação opcional) respeitem a estrutura de subcoleções por usuário.
- [ ] **LGPD:** Validar se o script de limpeza de logs está ignorando dados sensíveis.
- [ ] **Testes Críticos:** Simular queda de internet durante o streaming e validar se a UI não trava.

## Verificação Final (DoD)
- [ ] Código compilado e sem erros.
- [ ] Testes unitários passando.
- [ ] Documentação atualizada no README do módulo.
- [ ] Estilo de código validado.
