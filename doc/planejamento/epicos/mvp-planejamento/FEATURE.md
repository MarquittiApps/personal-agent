# Feature: MVP Planejamento Diário com IA

**Épico:** MVP de Planejamento (EP-07)
**Status:** Done
**Criado:** 2026-03-18
**Atualizado:** 2026-03-19

## Visão

Permitir que o usuário consulte e gerencie seus compromissos e tarefas (Google Calendar e Tasks) via chat conversacional, resultando em uma seção "Planejamento" consolidada com insights gerados por IA para otimizar o dia.

## Personas Impactadas

- **Solo-Builder / Consultor / Usuário Principal:** Consegue centralizar a governança de suas tarefas diárias sem precisar alternar entre ferramentas, recebendo sugestões de otimização de tempo diretamente na interface.

## User Story

> Como **Usuário Principal**, quero **enviar uma mensagem no chat perguntando meus compromissos e tarefas** para **obter um painel consolidado com insights gerados por IA que me ajudem a planejar meu dia de forma otimizada**.

## Critérios de Aceite (BDD)

**Cenário 1: Consulta via Chat**
- **Dado** que o usuário está no Command Center (chat)
- **Quando** o usuário digita "quais são os meus compromissos e tarefas para hoje?"
- **Então** o agente deve buscar os dados no Google Calendar e Google Tasks referentes à data solicitada e retornar o status no chat.

**Cenário 2: Exibição na Seção Planejamento**
- **Dado** que os dados de calendário e tarefas foram recuperados pelo agente
- **Quando** a resposta do chat é processada
- **Então** a seção "Planejamento" da aplicação deve refletir essas informações (listagem de eventos e tarefas).

**Cenário 3: Geração de Insights de IA**
- **Dado** que a seção Planejamento está populada com os dados do dia
- **Quando** os dados são apresentados
- **Então** o sistema deve exibir insights gerados por IA (ex: sugestões de prioridades, avisos de sobrecarga ou janelas de tempo livre).

**Cenário 4: Inserção de Dados (Calendar/Tasks)**
- **Dado** que o agente possui integração de escrita com as APIs do Google
- **Quando** o usuário solicita a adição de um novo evento ou tarefa via chat
- **Então** o agente deve inserir a informação no Google Calendar/Tasks e atualizar a interface de Planejamento.

## Fora do Escopo

- Qualquer integração ou funcionalidade que não seja estritamente relacionada ao Google Calendar e ao Google Tasks (ex: Microsoft Outlook, envio de e-mails, integrações com outros gerenciadores de tarefas).

## Notas de Design

- A seção "Planejamento" deverá ser perfeitamente integrada ao *Command Center* (Web Dashboard - EP-02), possivelmente utilizando um layout em painel lateral ou card expansível na Home.
- Necessário refletir o Design System já em andamento (shadcn/ui e Tailwind CSS, Dark Mode).

## Restrições Técnicas

- Implementação do fluxo OAuth2 para conexão segura com Google Calendar e Google Tasks.
- Criação de Tools/Ferramentas no LangGraph/Agente capazes de ler e escrever via APIs do Google.
- Atualização em tempo real do Frontend via WebSocket ou Server-Sent Events ao acionar os tools.

## Riscos LGPD

- O sistema vai lidar com tokens OAuth que garantem acesso a dados da agenda pessoal do usuário. É necessário criptografar armazenamentos sensíveis e definir consentimento explícito.
