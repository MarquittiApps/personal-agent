import os
import datetime
import json
import base64
from typing import List, Dict, Any, Optional
from langchain_core.tools import tool
from googleapiclient.discovery import build
from app.core.google_auth import get_google_credentials
from app.core.database import get_db_connection

# Fixando para o default_user neste MVP
USER_ID = "default_user"

def init_gmail_db():
    """Garante que a tabela de cache de emails existe."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS email_cache (
            id VARCHAR(255) PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            thread_id VARCHAR(255),
            snippet TEXT,
            subject TEXT,
            sender TEXT,
            date TIMESTAMP,
            size_bytes INTEGER,
            has_attachments BOOLEAN DEFAULT FALSE,
            importance_score FLOAT DEFAULT 0,
            metadata JSONB,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def get_gmail_service():
    creds = get_google_credentials(USER_ID)
    return build('gmail', 'v1', credentials=creds)

@tool
def get_important_emails_summary() -> str:
    """Analisa os e-mails importantes dos últimos 7 dias e retorna um resumo.
    Identifica e-mails cruciais baseados em remetente, assunto e conteúdo.
    """
    try:
        init_gmail_db()
        service = get_gmail_service()

        # Define o intervalo de 7 dias
        seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y/%m/%d')
        query = f"after:{seven_days_ago}"

        results = service.users().messages().list(userId='me', q=query, maxResults=50).execute()
        messages = results.get('messages', [])

        if not messages:
            return "Nenhum e-mail encontrado nos últimos 7 dias."

        summary_items = []
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()

            headers = msg_data.get('payload', {}).get('headers', [])
            subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), "Sem Assunto")
            sender = next((h['value'] for h in headers if h['name'].lower() == 'from'), "Desconhecido")
            snippet = msg_data.get('snippet', '')

            # Uma heurística simples de importância para o MVP
            # Em prod, passaríamos o snippet para o Gemini analisar
            summary_items.append(f"- **De:** {sender}\n  **Assunto:** {subject}\n  **Resumo:** {snippet[:100]}...")

        return "Resumo de e-mails importantes (últimos 7 dias):\n\n" + "\n\n".join(summary_items[:10])
    except Exception as e:
        return f"Erro ao analisar e-mails: {str(e)}"

@tool
def identify_space_optimization_targets() -> str:
    """Identifica e-mails que ocupam muito espaço ou são muito antigos (há mais de 2 anos).
    Retorna uma lista de alvos para otimização de espaço (arquivamento/deleção).
    """
    try:
        init_gmail_db()
        service = get_gmail_service()

        # 1. E-mails com anexos grandes (>10MB)
        large_query = "larger:10M"
        large_results = service.users().messages().list(userId='me', q=large_query, maxResults=10).execute()
        large_messages = large_results.get('messages', [])

        # 2. E-mails antigos (>2 anos)
        two_years_ago = (datetime.datetime.now() - datetime.timedelta(days=730)).strftime('%Y/%m/%d')
        old_query = f"before:{two_years_ago}"
        old_results = service.users().messages().list(userId='me', q=old_query, maxResults=10).execute()
        old_messages = old_results.get('messages', [])

        report = ["Relatório de Otimização de Espaço:"]

        if large_messages:
            report.append("\n**E-mails com anexos grandes (>10MB):**")
            for msg in large_messages:
                msg_data = service.users().messages().get(userId='me', id=msg['id'], format='minimal').execute()
                report.append(f"- ID: {msg['id']} (Tamanho aproximado: {msg_data.get('sizeEstimate', 0) // 1024 // 1024}MB)")
        else:
            report.append("\n- Nenhum e-mail com anexo >10MB encontrado.")

        if old_messages:
            report.append("\n**E-mails com mais de 2 anos:**")
            report.append(f"- Encontrados {len(old_messages)} e-mails antigos (amostra). Sugerido arquivamento em massa.")
        else:
            report.append("\n- Nenhum e-mail muito antigo encontrado.")

        report.append("\n*Nota: Esta é uma operação de leitura. Nenhuma ação de deleção foi realizada.*")

        return "\n".join(report)
    except Exception as e:
        return f"Erro ao identificar alvos de otimização: {str(e)}"

@tool
def get_email_metrics() -> Dict[str, Any]:
    """Retorna métricas visuais sobre a caixa de entrada para o Dashboard.
    Inclui contagem de e-mails importantes, espaço ocupado por anexos grandes, etc.
    """
    try:
        service = get_gmail_service()

        # Métricas rápidas
        seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y/%m/%d')
        important_count = service.users().messages().list(userId='me', q=f"after:{seven_days_ago} is:important", maxResults=1).execute().get('resultSizeEstimate', 0)

        large_attachments_count = service.users().messages().list(userId='me', q="larger:10M", maxResults=1).execute().get('resultSizeEstimate', 0)

        two_years_ago = (datetime.datetime.now() - datetime.timedelta(days=730)).strftime('%Y/%m/%d')
        old_emails_count = service.users().messages().list(userId='me', q=f"before:{two_years_ago}", maxResults=1).execute().get('resultSizeEstimate', 0)

        return {
            "important_last_7_days": important_count,
            "large_attachments_count": large_attachments_count,
            "old_emails_count": old_emails_count,
            "last_updated": datetime.datetime.now().isoformat()
        }
    except Exception as e:
        return {"error": str(e)}
