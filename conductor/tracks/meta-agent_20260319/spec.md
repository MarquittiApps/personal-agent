# Specification: EP-06 Meta-Agent (Self-Evolution)

**Track ID:** meta-agent_20260319
**Type:** feature
**Status:** Draft
**Created:** 2026-03-19

## 1. Visão Geral
O módulo Meta-Agent é o "cérebro evolutivo" do Personal AI Core. Sua missão é transcender a função de um assistente fixo, tornando-se um orquestrador capaz de analisar o próprio código, identificar falhas (via logs) e gerar novos sub-agentes ou componentes de interface de forma autônoma ou semi-autônoma (Human-in-the-Loop).

### Alinhamento Estratégico
- **Automação Técnica:** Reduzir a necessidade de intervenção manual para expansão do sistema.
- **Especialização:** Permitir que o sistema crie "experts" sob demanda para novos domínios de engenharia.

## 2. Arquitetura do Agente
O Meta-Agent será implementado como um `Supervisor` no LangGraph, utilizando um padrão de roteamento dinâmico.

### Fluxo no LangGraph
1. **Input:** Solicitação do usuário (ex: "Crie um agente para monitorar consumo de energia").
2. **Analysis Node:** O Meta-Agent mapeia o estado atual do repositório (`ProjectAnalyzerTool`).
3. **Planning Node:** Define se a solução requer uma nova Tool, um novo Node no grafo ou um novo componente React.
4. **Execution Node:** Gera o código necessário utilizando prompts especializados de codificação.
5. **Validation Node:** Executa linters e testes unitários no código gerado.
6. **Approval Node:** Interrompe o fluxo para validação humana (HITL) antes de persistir no branch principal.

### Prompts Sugeridos
- **System Prompt:** "Você é o Supervisor do Personal AI Core. Seu objetivo é manter a integridade Diamond do sistema enquanto expande suas capacidades. Você tem acesso total de leitura e escrita ao repositório, mas deve validar cada alteração com testes."

## 3. Especificação Técnica

### Endpoints FastAPI (novos)
- `POST /api/v1/meta/evolve`: Inicia um processo de auto-expansão.
- `GET /api/v1/meta/status`: Acompanha o progresso da geração de código/agentes.

### Modelos Pydantic
```python
class EvolutionRequest(BaseModel):
    intent: str
    context_files: List[str] = []

class GenerationResult(BaseModel):
    files_created: List[str]
    tests_passed: bool
    diff: str
```

### Esquema de Banco de Dados
Não é necessária persistência relacional imediata para a lógica, mas logs de evolução serão armazenados na tabela `agent_evolution_logs`.

## 4. Design de Tooling
- **`ProjectMapper`**: Varre diretórios e extrai assinaturas de funções/classes atuais.
- **`CodeArchitect`**: Escreve arquivos `.py` ou `.tsx` seguindo os styleguides de `conductor/code_styleguides/`.
- **`TestRunner`**: Dispara `pytest` ou `vitest` e retorna o traceback em caso de erro.
- **`GitManager`**: Cria branches temporários para as evoluções sugeridas.

## 5. Roadmap de Execução

### Sprint 1: Core Meta-Agent Logic (Fundação)
- [ ] Implementar o Node de Supervisão no LangGraph.
- [ ] Criar a Tool `ProjectMapper` para leitura de contexto.
- [ ] Endpoint de status da evolução.

### Sprint 2: Self-Creation & Validation
- [ ] Implementar `CodeArchitect` Tool (File Write).
- [ ] Integração com `TestRunner` para auto-correção.
- [ ] Fluxo de Interrupção Humana (HITL) para revisão de Diff.

### Sprint 3: UI Generation
- [ ] Prompts especializados para React + Tailwind.
- [ ] Geração dinâmica de componentes na pasta `web/src/components/dynamic/`.

## 6. Critérios de Aceite (DoD)
- [ ] O Meta-Agent consegue explicar a estrutura atual do projeto sem alucinações.
- [ ] O Agente consegue criar um novo arquivo de "Hello World" e um teste correspondente que passe.
- [ ] Toda alteração de código é precedida por um branch `evolution/[task]`.
- [ ] Compatibilidade garantida com Ollama (local) e Gemini (nuvem).
