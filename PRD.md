Product Requirements Document (PRD)

Produto: Personal AI Core (Assistente Pessoal Modular com Especializações em Engenharia e TI)
Status: Arquitetura / Planejamento Web
Data: Março de 2026

1. Visão Geral (Overview)

O Personal AI Core é um ecossistema de inteligência artificial de uso pessoal, projetado para atuar como um "segundo cérebro" e co-piloto profissional. Operando de forma integrada ao ambiente de trabalho (VS Code via Model Context Protocol - MCP) e acessível através de uma Aplicação Web moderna, o sistema orquestra múltiplas responsabilidades através de uma arquitetura baseada em módulos (Sub-agentes).

O sistema intercala perfeitamente entre a organização da vida pessoal, o desenvolvimento de software (com foco no SaaS ClinicCare), o design de projetos elétricos e de automação, e a gestão operacional de uma consultoria de TI. Mais do que um conjunto fixo de ferramentas, o sistema possui uma arquitetura evolutiva, gerenciada por um Meta-Agente capaz de criar e melhorar outros agentes.

2. Declaração do Problema (Problem Statement)

Um profissional multidisciplinar (Engenheiro/Desenvolvedor/Consultor) sofre com a fragmentação de contexto e a sobrecarga cognitiva. O tempo é desperdiçado transitando entre o planejamento do dia a dia (e-mails, reuniões), o desenvolvimento complexo de software full-stack, e a elaboração de propostas e topologias para infraestrutura física (redes, elétrica, automação residencial). Ferramentas isoladas não compartilham contexto. Além disso, a falta de um painel de controle unificado (Web Dashboard) torna difícil visualizar o panorama geral das operações simultâneas.

3. Público-Alvo e Persona (Target Audience)

Usuário Principal (O "Solo-Builder" / Consultor Multi-disciplinar): Um profissional que gerencia uma rotina intensa envolvendo desenvolvimento de produtos próprios (SaaS), consultoria B2B (TI, Redes, CFTV) e projetos de engenharia física (Elétrica/Automação).

Uso Futuro: Pode ser expandido para atuar como um "funcionário digital" para outros membros da equipe da consultoria ou do ClinicCare.

4. Visão do Produto e Objetivos (Vision & Goals)

Visão: Centralizar a gestão da vida profissional e pessoal num único fluxo "Agentic", acessível via Web e IDE, onde um orquestrador central entende a intenção do usuário, aciona o módulo correto, mantém a memória de longo prazo e evolui o próprio sistema criando novas habilidades.

Objetivos:

Reduzir a carga administrativa diária em 80%.

Acelerar o ciclo de desenvolvimento do ClinicCare com IA e RAG.

Padronizar a entrega de projetos físicos (Elétrica, Automação, Infra de TI).

Garantir a evolução contínua do sistema, permitindo que a IA crie novos agentes automaticamente.

Prover uma Interface Web centralizada de alta performance para visualização de relatórios, aprovação de tarefas (Human-in-the-Loop) e upload de arquivos (ex: plantas arquitetônicas).

5. Arquitetura de Módulos (System Modules)

O sistema é dividido em 6 módulos principais, liderados por um Agente Supervisor:

5.1. Módulo Supervisor e de Evolução Contínua (Meta-Agente)

Responsabilidade: Orquestrar, gerenciar e evoluir todo o ecossistema de agentes.

Capacidades: Roteamento de tarefas, Auto-melhoria baseada em logs, e criação autônoma de novos sub-agentes e interfaces.

5.2. Módulo Core: Assistente Pessoal (Daily Planner)

Responsabilidade: Gerenciamento do tempo, comunicação e contexto pessoal.

5.3. Módulo de Desenvolvimento de Software (Foco: ClinicCare)

Responsabilidade: Atuar como Engenheiro de Software Sênior para o SaaS principal, executando TDD, revisando PRs e interagindo via VS Code (MCP).

5.4. Módulo de Automação Residencial e IoT

Responsabilidade: Planejamento e design de projetos de Smart Homes.

Capacidades: Análise multimodal de plantas baixas para sugestão de posicionamento de sensores (PIR, Iluminação). Geração de código YAML para Home Assistant.

5.5. Módulo de Projetos Elétricos e Infraestrutura

Responsabilidade: Apoio à elaboração de projetos elétricos e infraestrutura de TI (redes/CFTV).

5.6. Módulo de Gestão de Consultoria TI

Responsabilidade: Backoffice operacional, elaboração de propostas e controle de ativos.

6. Casos de Uso e User Stories

Dashboard Matinal Web (Assistente Pessoal):

Como usuário, abro a aplicação web pela manhã e vejo um painel unificado gerado pelo Meta-Agente contendo compromissos do dia, PRs pendentes de aprovação e e-mails sumarizados.

Revisão e Aprovação Visual (Human-in-the-Loop):

Como arquiteto IoT, faço upload de uma planta baixa no portal web. O agente de Automação processa a imagem e renderiza na tela uma sobreposição interativa com os sensores Zigbee sugeridos, aguardando minha aprovação ou ajuste via drag-and-drop.

Evolução Contínua e Criação de Módulos:

Como usuário, solicito ao Meta-Agente uma nova integração. Ele codifica a lógica no backend e sugere um novo componente React para o meu painel web.

7. Estratégia de Interface Web e Prototipação (UX/UI & React)

Para garantir uma experiência de usuário (UX) premium, fluida e escalável, a aplicação web seguirá diretrizes modernas de engenharia de front-end.

7.1. Metodologia de Design e Prototipação

Prototipação no Figma: Todas as telas críticas passarão por wireframing e prototipação de alta fidelidade no Figma antes da codificação, garantindo alinhamento visual.

Design System Unificado: Adoção de uma biblioteca de componentes robusta (ex: shadcn/ui ou Radix UI) adaptada para um tema coeso (Dark/Light mode automático), garantindo acessibilidade (WCAG 2.1 AA) e consistência.

Atomic Design: Estruturação da interface em Átomos (botões, inputs), Moléculas (cards de sensores) e Organismos (painéis de plantas baixas), permitindo fácil reutilização pela IA geradora de código.

7.2. Arquitetura Frontend (React)

Framework Core: React (via Vite ou Next.js) utilizando TypeScript rigoroso para segurança de tipos.

Gerenciamento de Estado: Zustand para o estado global do cliente (leve e performático, ideal para dashboards) e React Query / SWR ou assinaturas do Firebase para sincronização de dados do agente em tempo real.

Estilização: Tailwind CSS para agilidade na criação de layouts responsivos e manutenção simplificada de estilos utilitários.

Visualização de Dados e Plantas (Canvas): Utilização de bibliotecas como react-konva ou d3.js para renderizar as plantas baixas arquitetônicas de forma interativa (zoom, pan, drag-and-drop de nós IoT).

7.3. Estrutura de Telas Previstas (Views)

Command Center (Home): Feed de inteligência contendo notificações assíncronas dos agentes, caixa de entrada unificada e barra de comando (Omnibar) para prompts globais.

Smart Home Canvas: Tela dedicada ao upload de PDFs/Imagens de plantas, com visualizador 2D interativo das zonas de cobertura de sensores e gerador de BOM (Bill of Materials).

DevOps Board: Visualizador integrado com Jira e GitHub focado no ClinicCare, exibindo status de builds, análises de bugs (IQP) geradas pela IA e diffs de código propostos.

Operations Hub: Gestão de orçamentos da consultoria de TI e relatórios elétricos.

8. Requisitos Técnicos e Stack (Tech Stack Geral)

Frontend Web: React 18+, TypeScript, Tailwind CSS, shadcn/ui, Zustand.

Framework de Agentes: LangGraph (Python/JS) orquestrando o fluxo e interrupções (Human-in-the-Loop).

Integração IDE: Model Context Protocol (MCP) para comunicação segura com VS Code.

Cérebros / LLMs: Gemini 2.5 Pro (raciocínio, visão computacional sobre plantas) e LLMs locais (Ollama).

Memória Persistente: PostgreSQL (PostgresSaver) para histórico de sessões do LangGraph.

Infraestrutura: Vercel (Frontend) + FastAPI/Node Express (Backend) com WebSocket para streaming de respostas dos agentes para o React.

9. Marcos e Entregáveis (Milestones)

Fase 1: Prototipação e Fundação Core:

Desenho das telas no Figma (Command Center e Smart Home Canvas).

Setup do repositório React + Tailwind e do backend LangGraph com PostgreSQL.

Fase 2: MVP da Aplicação Web e Automação:

Integração da autenticação e estado global (Zustand).

Lançamento do visualizador de plantas baixas interagindo com o agente multimodal do Gemini.

Fase 3: Integração Profunda (IDE + Web):

O Agente atua no VS Code (ClinicCare) via MCP e reflete seus diagnósticos e PRs no Web Dashboard.

Fase 4: Auto-Expansão (Meta-Agente):

O sistema atinge a capacidade de programar, testar e sugerir novos componentes React para si mesmo na aplicação web, adaptando-se a novas áreas de consultoria.