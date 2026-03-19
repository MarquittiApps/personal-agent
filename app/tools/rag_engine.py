from langchain_core.tools import tool
from app.core.rag_engine import query_knowledge_base as _query_knowledge_base

@tool
def query_knowledge_base(query: str):
    """
    Realiza busca semântica no Vector DB para responder perguntas baseadas em normas técnicas (PDFs)
    e catálogo de hardware IoT. Use esta ferramenta quando precisar de informações precisas
    sobre NBRs, especificações de hardware ou protocolos de automação.
    """
    results = _query_knowledge_base(query)

    if isinstance(results, dict) and "error" in results:
        return f"Erro ao consultar a base de conhecimento: {results['error']}"

    formatted_results = []
    for res in results:
        formatted_results.append(f"Conteúdo: {res['content']}\nFonte: {res.get('source', 'Desconhecida')}\n---")

    return "\n".join(formatted_results)
