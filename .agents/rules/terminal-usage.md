---
name: terminal-usage
description: "Padroniza a execução de comandos no terminal e define o ecossistema de ferramentas do projeto."
---

# Terminal & Ecosystem Rules

Para evitar falhas de execução e garantir a portabilidade do trabalho dos Agentes de IA, siga rigorosamente as instruções abaixo.

## 🖥️ Shell & Environment (Windows/PowerShell)
O projeto está sendo executado em um ambiente **Windows 10/11** utilizando **PowerShell**.
- **Operador de Encadeamento:** Utilize `;` ou execute comandos separadamente. **NUNCA** utilize `&&` (estilo Bash/Linux).
- **Caminhos:** Utilize `\` para caminhos locais (ex: `app\main.py`).
- **Scripts:** Utilize `.\scripts\nome.ps1` para scripts PowerShell.

## 🛠️ Ecossistema de Ferramentas (Comandos Disponíveis)

### 🐍 Python (Backend & Scripts)
- **Interpretador:** Utilize `python` (verifique se o venv está ativo).
- **Gerenciador de Pacotes:** `pip`.
- **Comandos Principais:**
    - `python scripts\doctor.py`: Validação de infraestrutura.
    - `pytest`: Execução de testes unitários.
    - `uvicorn app.main:app --reload`: Servidor de desenvolvimento.

### 📦 Node.js / NPM (Frontend)
- **Diretório:** Sempre execute comandos dentro da pasta `web\`.
- **Gerenciador:** `npm`.
- **Comandos Principais:**
    - `npm install`: Instalar dependências.
    - `npm run dev`: Iniciar servidor Vite.
    - `npm run build`: Gerar build de produção.
    - `npm test`: Executar Vitest.

### 🤖 IA & Automação
- **Jules CLI:** `jules` (para tarefas remotas).
- **GitHub CLI:** `& "C:\Program Files\GitHub CLI\gh.exe"` (Utilize o caminho absoluto se `gh` não estiver no PATH).
- **Ollama:** `ollama run <model>` (para testes locais).

### 🐳 Infraestrutura
- **Docker:** `docker-compose up -d`.

## ⚠️ Boas Práticas (Do's & Don'ts)
- **Do:** Verifique a existência de um arquivo antes de tentar executá-lo com `ls` ou `Test-Path`.
- **Do:** Use aspas duplas em caminhos com espaços.
- **Don't:** Não assuma que comandos Linux (ex: `export`, `grep -P`, `which`) funcionam sem adaptação no PowerShell. Utilize `Set-Style`, `Select-String` ou `Get-Command` se necessário.
- **Don't:** Não tente executar `npm` na raiz do projeto; o frontend está isolado em `web\`.
