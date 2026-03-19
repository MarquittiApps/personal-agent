import os
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from app.tools.google_calendar import get_todays_calendar_events, create_calendar_event
from app.tools.google_tasks import get_pending_tasks, create_google_task

load_dotenv()

system_prompt = """Você é o Assistente Pessoal do Andru.ia, focado em ajudar no Planejamento Diário com IA.
Sua principal função é acessar o Google Calendar e o Google Tasks do usuário para mostrar os compromissos do dia e tarefas pendentes.
Além de listar, você deve gerar insights para um dia mais produtivo e equilibrado.
Você pode agendar novos eventos ou criar novas tarefas se o usuário pedir.
Organize suas respostas usando markdown claro e conciso."""

def get_graph_builder(use_persistence=True):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
    tools = [
        get_todays_calendar_events,
        create_calendar_event,
        get_pending_tasks,
        create_google_task
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
