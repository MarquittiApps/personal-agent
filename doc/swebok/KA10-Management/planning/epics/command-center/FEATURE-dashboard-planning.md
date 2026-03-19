# Feature: Dashboard de Planejamento 3-Camadas

**Épico:** EP-02 - Command Center (Web Dashboard)
**Status:** Draft
**Criado:** 2026-03-19
**Atualizado:** 2026-03-19

## Visão

Fornecer um dashboard interativo dentro do Command Center que atue como um guia visual para o planejamento em 3 espirais/camadas (diária, semanal, mensal). Este dashboard deve ser reativo às conversas no chat, atualizando-se sempre que houver mudanças de planejamento aprovadas na sessão.

## Personas Impactadas

- **Solo-Builder (Usuário Principal):** Mantém o contexto de seus objetivos de curto a longo prazo sempre visível e sincronizado com os comandos conversacionais.

## User Story

> Como **Solo-Builder**, quero **visualizar e iterar sobre meu planejamento em três horizontes (diário, semanal e mensal)** para **manter meus objetivos sempre organizados e sincronizados visualmente com as decisões tomadas via chat**.

## Critérios de Aceite (BDD)

**Cenário 1: Visualização das 3 Camadas**
- **Dado** que estou no Command Center e abro o Dashboard de Planejamento.
- **Quando** a interface carregar.
- **Então** devo ver três seções ou visualizações distintas correspondentes ao foco Diário, Semanal e Mensal.

**Cenário 2: Prompt Proativo da IA**
- **Dado** que interagi com o chat (ex: adicionei tarefas, mudei um evento ou decidi um novo foco da semana).
- **Quando** a IA terminar de processar minha requisição.
- **Então** a IA deve perguntar se desejo atualizar o Dashboard de Planejamento para refletir as mudanças realizadas.

**Cenário 3: Sincronização e Refresh**
- **Dado** que confirmei a atualização do Dashboard via chat.
- **Quando** a IA processar a confirmação via LangGraph/Backend.
- **Então** o Dashboard em tela deve receber o novo estado via WebSocket e se atualizar em tempo real.

## Fora do Escopo

- Gestão de equipes ou múltiplos usuários (apenas single-player).
- Sincronização visual em tempo real multi-dispositivo sem refresh via web (foco apenas na sessão atual do Command Center).

## Notas de Design

- Seguir o mesmo Minimal/Modern/Glassmorphism do Command Center atual.
- Utilizar cards limpos para os itens diários e marcadores de progresso macro para o mensal.

## Restrições Técnicas

- Integração profunda com Zustand para estado global local.
- Atualização proativa via WebSocket do backend para o dashboard no frontend.

## Riscos LGPD

- As metas e anotações pessoais podem conter PII ou planos de negócios sensíveis. Dados devem transitar encriptados e, preferencialmente, não serem logados em texto claro nos sistemas de telemetria.
