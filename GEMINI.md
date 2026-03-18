# GEMINI.md — Personal AI Core (Meta-Instructional Ecosystem)

Este repositório é o "cérebro" e motor de orquestração do **Personal AI Core**, um ecossistema modular de inteligência artificial projetado para atuar como co-piloto profissional em engenharia, TI e gestão pessoal.

---

## 📂 Estrutura do Ecossistema (.agents/)

A inteligência deste repositório está centralizada na pasta `.agents/`, organizada em três pilares fundamentais:

### 1. Skills (`.agents/skills/`)
Instruções especializadas por domínio. Antes de executar qualquer tarefa específica (ex: UI Design, Segurança, Diagnóstico), consulte a skill correspondente.
- **Andru.ia Core:** Skills prefixadas com números (ex: `00-andruia-consultant`) são fundamentais para o diagnóstico e arquitetura de novos projetos. **Idioma Mandatório: ESPAÑOL**.
- **Specialized Skills:** Abrangem desde `ui-ux-pro-max` até `mcp-builder` e `playwright-skill`.

### 2. Workflows (`.agents/workflows/`)
Procedimentos Operacionais Padrão (SOPs) para tarefas multi-etapas.
- **`/planning`:** Workflow de planejamento SCRUM para épicos e features (ver `planning.workflow.md`).
- **`/docs`:** Gestão e geração de documentação técnica.
- **`/rules`:** Gestão e evolução das regras do sistema.

### 3. Rules (`.agents/rules/`)
Regras de governança e comportamento global para o agente.
- **Commits Atômicos:** Obrigatório seguir o `commits.md` (Conventional Commits + Atomicidade Rigorosa).

---

## 🛠️ Diretrizes de Desenvolvimento (Conventional & Atomic)

Ao atuar neste repositório ou em projetos derivados:

1.  **Atomicidade de Commits:** Cada commit deve realizar apenas UMA unidade lógica de alteração. Nunca misture features, fixes e refactorings no mesmo commit.
2.  **Conventional Commits:** Use `<tipo>[escopo]: <descrição>` (ex: `feat(skill): add new rbac logic`).
3.  **Linguagem de Contexto:**
    - O **PRD.md** e **Workflows** utilizam **Português (Brasil)**.
    - As **Skills Andru.ia** utilizam **Espanhol**.
    - Identificadores de código e documentação técnica de baixo nível devem ser em **Inglês**.

---

## 🚀 Como Iniciar

1.  **Diagnóstico Inicial:** Sempre que o usuário solicitar uma nova ação ou projeto, verifique se a skill `@00-andruia-consultant` (em espanhol) ou o workflow `/planning` (em português) deve ser invocado primeiro.
2.  **Contexto do Produto:** Leia o `PRD.md` na raiz para entender a visão de longo prazo do **Personal AI Core** e do SaaS **ClinicCare**.
3.  **Human-in-the-Loop:** Siga as interrupções solicitadas nos workflows para garantir a validação do usuário antes de prosseguir com implementações automáticas.

---

## 🧠 Visão do Meta-Agente (Auto-Evolução)

Conforme descrito no **PRD.md (Seção 5.1)**, este sistema deve ser capaz de evoluir a si mesmo.
- Se você identificar um padrão repetitivo, sugira a criação de uma nova **Skill** ou **Workflow**.
- Utilize as regras em `.agents/rules/` para garantir que a evolução do sistema mantenha o padrão de qualidade "Diamante".
