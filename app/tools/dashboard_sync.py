from langchain_core.tools import tool
from typing import List, Dict, Optional

@tool
def update_planning_dashboard(
    daily_items: Optional[List[Dict[str, str]]] = None, 
    weekly_items: Optional[List[Dict[str, str]]] = None, 
    monthly_items: Optional[List[Dict[str, str]]] = None
) -> dict:
    """Atualiza o Dashboard de Planejamento visual do usuário (3 camadas: Diário, Semanal, Mensal).
    Deve ser chamada quando o usuário confirmar que quer atualizar o painel visual, usando os dados já disponíveis na conversa.
    Não espere dados perfeitos — use o que você já sabe. Se uma camada não tiver dados, envie lista vazia.
    
    Args:
        daily_items: Tarefas e eventos de HOJE. Cada item: {'id': str, 'title': str, 'status': 'pending'|'in_progress'|'completed'}.
        weekly_items: Metas e compromissos desta SEMANA. Mesmo formato.
        monthly_items: Objetivos e metas deste MÊS. Mesmo formato.
        
    Returns:
        dict: O payload da atualização enviado ao frontend.
    """
    
    payload = {
        "type": "DASHBOARD_UPDATE",
        "data": {
            "daily": daily_items or [],
            "weekly": weekly_items or [],
            "monthly": monthly_items or []
        }
    }
    
    return payload
