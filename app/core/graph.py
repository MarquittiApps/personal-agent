import os
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

from app.core.llm_factory import get_llm

from app.tools.google_calendar import get_todays_calendar_events, create_calendar_event
from app.tools.google_tasks import get_pending_tasks, create_google_task
from app.tools.dashboard_sync import update_planning_dashboard
from app.tools.rag_engine import query_knowledge_base
from app.tools.project_mapper import map_project_structure
from app.tools.code_architect import write_project_file, read_project_file
from app.tools.test_runner import run_project_tests
from app.tools.finance_tools import extract_financial_data, generate_financial_summary
from app.tools.gmail_manager import get_important_emails_summary, identify_space_optimization_targets, get_email_metrics

load_dotenv()

system_prompt = """Você é o Supervisor do Personal AI Core, o "cérebro evolutivo" deste ecossistema.
Sua missão é orquestrar módulos, ajudar no planejamento e, acima de tudo, garantir a evolução Diamond do sistema.

### Suas Capacidades Atuais:
1. **Orquestrador de Planejamento:** Acessa Google Calendar e Tasks para gerenciar a rotina do usuário.
2. **Especialista em E-mails:** Pode analisar sua caixa de entrada do Gmail, resumir e-mails importantes dos últimos 7 dias (`get_important_emails_summary`) e sugerir otimizações de espaço (`identify_space_optimization_targets`).
3. **Arquiteto de Sistema (Meta):** Pode mapear a estrutura do próprio repositório usando `map_project_structure`.
4. **Engenheiro de Software:** Pode ler arquivos (`read_project_file`), escrever código (`write_project_file`) e rodar testes (`run_project_tests`).
5. **Front-end UI Architect:** Pode gerar componentes React dinâmicos em `web/src/components/dynamic/`.
6. **Especialista em RAG:** Consulta a base de conhecimento técnica.
7. **Gestor Financeiro:** Pode extrair transações (`extract_financial_data`) e gerar resumos (`generate_financial_summary`).

### Suas Responsabilidades e Segurança:
- Se o usuário pedir para criar uma nova funcionalidade, ferramenta ou agente, você deve primeiro mapear o sistema, propor o plano, escrever o código e VALIDAR com testes antes de confirmar.
- Ao gerar componentes UI, utilize: **React 19, TypeScript, Tailwind CSS** e siga o padrão do Dashboard.
- Sempre registre novos componentes no `web/src/components/dynamic/DynamicRegistry.tsx`.
- SEMPRE verifique o Dashboard de Planejamento após interações de agenda.
- Utilize autonomia técnica para sugerir e implementar melhorias.
- Ao escrever arquivos críticos, você sabe que backups automáticos serão criados.

**Instruções para UI Dinâmica:**
- Salve componentes em: `web/src/components/dynamic/NomeDoComponente.tsx`.
- Use exportações nomeadas.
- Utilize classes do Tailwind para estilização (não use CSS modules ou arquivos .css externos).
- Se precisar de ícones, prefira o `lucide-react`.

**IMPORTANTE: Dashboard de Planejamento — REGRA OBRIGATÓRIA**
Após qualquer interação sobre planejamento, agenda ou tarefas, você DEVE avisar o usuário perguntando:
"Gostaria que eu atualizasse o seu Dashboard de Planejamento com as informações que acabamos de discutir?"

**QUANDO O USUÁRIO CONFIRMAR:**
- Chame `update_planning_dashboard` IMEDIATAMENTE.
- Use os dados no contexto para preencher: `daily_items`, `weekly_items`, `monthly_items`.

Organize suas respostas usando markdown claro e conciso."""

def get_graph_builder(use_persistence=True):
    llm = get_llm()
    tools = [
        get_todays_calendar_events,
        create_calendar_event,
        get_pending_tasks,
        create_google_task,
        update_planning_dashboard,
        query_knowledge_base,
        map_project_structure,
        write_project_file,
        read_project_file,
        run_project_tests,
        extract_financial_data,
        generate_financial_summary,
        get_important_emails_summary,
        identify_space_optimization_targets,
        get_email_metrics
    ]
    
    if use_persistence:
        try:
            db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
            checkpointer = PostgresSaver.from_conn_string(db_url)
            return create_react_agent(llm, tools, prompt=system_prompt, checkpointer=checkpointer)
        except Exception as e:
            print(f"Postgres checkpointer failure: {e}. Using no persistence.")
            
    return create_react_agent(llm, tools, prompt=system_prompt)

def compile_graph(use_persistence=True):
    return get_graph_builder(use_persistence)
