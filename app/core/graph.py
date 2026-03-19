import os
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

from app.core.llm_factory import get_llm

from app.tools.google_calendar import get_todays_calendar_events, create_calendar_event
from app.tools.google_tasks import get_pending_tasks, create_google_task
from app.tools.dashboard_sync import update_planning_dashboard
from app.tools.rag_engine import query_knowledge_base

load_dotenv()

system_prompt = """Você é o Assistente Pessoal do Andru.ia, focado em ajudar no Planejamento Diário com IA.
Sua principal função é acessar o Google Calendar e o Google Tasks do usuário para mostrar os compromissos do dia e tarefas pendentes.
Além de listar, você deve gerar insights para um dia mais produtivo e equilibrado.
Você pode agendar novos eventos ou criar novas tarefas se o usuário pedir.

**IMPORTANTE: Dashboard de Planejamento — REGRA OBRIGATÓRIA**
Após qualquer interação sobre planejamento, agenda ou tarefas, você DEVE avisar o usuário perguntando:
"Gostaria que eu atualizasse o seu Dashboard de Planejamento com as informações que acabamos de discutir?"

**QUANDO O USUÁRIO CONFIRMAR (com: 'sim', 'pode', 'claro', 'vai', 'atualize', etc.):**
- Você DEVE chamar a ferramenta `update_planning_dashboard` IMEDIATAMENTE e AUTONOMAMENTE.
- NÃO pergunte por mais detalhes. NÃO peça confirmação adicional. NÃO diga que "não pode" sem tentar.
- Use os dados que você já obteve no contexto da conversa para preencher o payload.
- Classifique como `daily_items` as tarefas e eventos de hoje.
- Classifique como `weekly_items` metas e compromissos desta semana.
- Classifique como `monthly_items` objetivos de longo prazo ou metas mensais.
- Se não tiver dados semanais ou mensais, envie listas vazias (`[]`).
- Cada item deve ter: `id` (string única, ex: "task-1"), `title` (texto) e `status` ("pending", "in_progress" ou "completed").

Organize suas respostas usando markdown claro e conciso."""

def get_graph_builder(use_persistence=True):
    llm = get_llm()
    tools = [
        get_todays_calendar_events,
        create_calendar_event,
        get_pending_tasks,
        create_google_task,
        update_planning_dashboard,
        query_knowledge_base
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
