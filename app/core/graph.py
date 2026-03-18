import os
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    """Estado principal do ecossistema Personal AI Core."""
    messages: List[str]
    next_action: str
    context: dict

def supervisor_node(state: State) -> State:
    """Nó supervisor responsável pelo roteamento inicial."""
    return {
        **state,
        "messages": state["messages"] + ["Supervisor: Analisando contexto..."],
        "next_action": "test_node"
    }

def test_node(state: State) -> State:
    """Nó de teste para verificação da infraestrutura."""
    return {
        **state,
        "messages": state["messages"] + ["Test Node: Infraestrutura funcionando!"],
        "next_action": "end"
    }

def get_graph_builder():
    """Constrói o grafo do sistema."""
    builder = StateGraph(State)
    
    # Adicionar nós
    builder.add_node("supervisor", supervisor_node)
    builder.add_node("test_node", test_node)
    
    # Definir fluxo
    builder.add_edge(START, "supervisor")
    builder.add_edge("supervisor", "test_node")
    builder.add_edge("test_node", END)
    
    return builder

def compile_graph(use_persistence=True):
    """Compila o grafo para execução com persistência opcional."""
    builder = get_graph_builder()
    
    if use_persistence:
        db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        try:
            # PostgresSaver.from_conn_string cria as tabelas automaticamente se não existirem
            checkpointer = PostgresSaver.from_conn_string(db_url)
            return builder.compile(checkpointer=checkpointer)
        except Exception as e:
            print(f"Falha ao configurar PostgresSaver: {e}. Compilando sem persistência.")
    
    return builder.compile()

if __name__ == '__main__':
    # Teste rápido de execução sem persistência para evitar erros de DB no log
    graph = compile_graph(use_persistence=False)
    initial_state = {"messages": [], "next_action": "start", "context": {}}
    result = graph.invoke(initial_state)
    print("Resultado da execução do grafo:")
    for msg in result["messages"]:
        print(f" - {msg}")
