import os
import datetime
from langchain_core.tools import tool
from googleapiclient.discovery import build
from app.core.google_auth import get_google_credentials

# Fixando para o default_user neste MVP
USER_ID = "default_user"

@tool
def get_todays_calendar_events() -> str:
    """Busca os compromissos do usuário no Google Calendar previstos para o dia de hoje."""
    try:
        creds = get_google_credentials(USER_ID)
        service = build('calendar', 'v3', credentials=creds)

        # Determina o início e fim do dia atual (em UTC por simplicidade ou fuso local)
        # Assumindo execução no fuso local:
        now = datetime.datetime.now()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
        end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat() + 'Z'

        events_result = service.events().list(
            calendarId='primary',
            timeMin=start_of_day,
            timeMax=end_of_day,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])

        if not events:
            return "Nenhum compromisso marcado para hoje."

        output = ["Compromissos para hoje:"]
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            # formata p/ facilitar leitura "14:00 - Reunião"
            time_str = start.split('T')[1][:5] if 'T' in start else 'Dia inteiro'
            output.append(f"- {time_str}: {event['summary']}")
            
        return "\n".join(output)
    except Exception as e:
        return f"Erro ao buscar o calendário: {str(e)}"
