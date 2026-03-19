# Feature: Integração Omnibar & LLM Chat

**Épico:** EP-02 - Command Center (Web Dashboard)
**Status:** Done
**Criado:** 2026-03-18
**Atualizado:** 2026-03-18

## Visão
Fornecer ao usuário a porta de entrada principal para interagir com o ecossistema de IA, permitindo o envio de instruções em linguagem natural e o recebimento de respostas processadas por agentes em tempo real (streaming).

## Personas Impactadas
- **Solo-Builder (Usuário Principal):** Beneficia-se de uma interface fluida para orquestrar tarefas complexas sem sair do dashboard.

## User Story
> Como **Solo-Builder**, quero **enviar mensagens de texto em linguagem natural utilizando a omnibar** para que a **LLM interprete e execute as tarefas com as ferramentas e/ou agentes disponíveis**.

## Critérios de Aceite (BDD)

**Cenário 1: Envio e Feedback Imediato**
- **Dado** que o Command Center está carregado e conectado ao backend.
- **Quando** eu digito uma instrução na Omnibar e pressiono `Enter`.
- **Então** a Omnibar deve ser limpa, e minha mensagem deve aparecer instantaneamente na área de chat com o status "enviando".

**Cenário 2: Resposta em Streaming (Real-time)**
- **Dado** que uma requisição foi enviada para a LLM.
- **Quando** o backend LangGraph começa a gerar a resposta.
- **Então** eu devo ver o texto sendo "digitado" na tela em tempo real (streaming).

**Cenário 3: Execução de Ferramenta/Agente**
- **Dado** que eu solicito algo que exige uma ferramenta (ex: "Verifique o status do banco").
- **Quando** o Agente Supervisor identifica a intenção.
- **Então** a UI deve exibir um log visual ou indicador de que a ferramenta "Database Check" foi acionada.

## Fora do Escopo
- Entrada por Voz.
- Upload de arquivos multimídia (PDF, Imagens).
- Persistência de histórico entre sessões do navegador (focar na sessão atual).
- Markdown avançado (tabelas/gráficos).

## Notas de Design
- Utilizar a barra de comando central (Omnibar) com foco automático ao carregar a página.
- Estilo minimalista seguindo o tema Modern/Glassmorphism.

## Restrições Técnicas
- Comunicação via **WebSockets** obrigatória para streaming.
- Gerenciamento de estado de mensagens via **Zustand**.
- Segredos (API Keys) devem permanecer exclusivamente no backend.

## Riscos LGPD
- Minimização de dados: Não processar dados sensíveis de terceiros a menos que explicitamente solicitado pelo usuário em contexto privado.
