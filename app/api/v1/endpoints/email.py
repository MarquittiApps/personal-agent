from fastapi import APIRouter, HTTPException
from app.tools.gmail_manager import get_email_metrics

router = APIRouter(prefix="/email", tags=["email"])

@router.get("/metrics")
async def email_metrics():
    """Retorna métricas de e-mail para o Dashboard."""
    try:
        metrics = get_email_metrics.invoke({})
        if "error" in metrics:
            raise HTTPException(status_code=500, detail=metrics["error"])
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
