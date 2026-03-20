import os
import json
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
import google_auth_oauthlib.flow
from app.core.database import get_db_connection
from app.core.crypto import encrypt_data

# Necessário para testar localmente em http em vez de https
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

router = APIRouter(prefix="/auth", tags=["auth"])

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback")

# Scopes necessários para Calendar e Tasks e informações de usuário se necessário
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/tasks',
    'https://www.googleapis.com/auth/gmail.readonly'
]

def get_client_config():
    if not CLIENT_ID or not CLIENT_SECRET:
        raise ValueError("Google OAuth credentials missing (GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET).")
    return {
        "web": {
            "client_id": CLIENT_ID,
            "project_id": "personal-ai-core",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": CLIENT_SECRET,
            "redirect_uris": [REDIRECT_URI]
        }
    }

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_credentials (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(255) UNIQUE NOT NULL,
            token_data TEXT NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# Dicionário temporário para manter o code_verifier do PKCE (válido para 1 worker em ambiente dev)
oauth_states = {}

@router.get("/google")
def login_google():
    try:
        client_config = get_client_config()
        flow = google_auth_oauthlib.flow.Flow.from_client_config(
            client_config, scopes=SCOPES
        )
        flow.redirect_uri = REDIRECT_URI
        
        # prompt='consent' e access_type='offline' forçam o envio do refresh_token
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            prompt='consent'
        )
        
        # Salva o code_verifier do fluxo associado ao state gerado
        if hasattr(flow, 'code_verifier'):
            oauth_states[state] = flow.code_verifier
            
        return RedirectResponse(authorization_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/google/callback")
def callback_google(request: Request):
    state = request.query_params.get("state")
    code = request.query_params.get("code")
    
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code missing.")
    
    try:
        client_config = get_client_config()
        flow = google_auth_oauthlib.flow.Flow.from_client_config(
            client_config, scopes=SCOPES, state=state
        )
        flow.redirect_uri = REDIRECT_URI
        
        # Restaura o code_verifier gerado no step de login
        if state in oauth_states:
            flow.code_verifier = oauth_states.pop(state)
        
        # Converte em URL http por conta do Insecure Transport em prod deverá ser https
        authorization_response = str(request.url)
        flow.fetch_token(authorization_response=authorization_response)
        
        credentials = flow.credentials
        
        # Serializar credenciais
        creds_data = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
        
        creds_json = json.dumps(creds_data)
        encrypted_token = encrypt_data(creds_json)
        
        # User ID padronizado para o MVP
        user_id = "default_user"
        
        init_db() # garante que a tabela existe
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO user_credentials (user_id, token_data)
            VALUES (%s, %s)
            ON CONFLICT (user_id) 
            DO UPDATE SET token_data = EXCLUDED.token_data, updated_at = CURRENT_TIMESTAMP
        """, (user_id, encrypted_token))
        
        conn.commit()
        cur.close()
        conn.close()
        
        # Idealmente redirecionar de volta pro frontend, mas num MVP backend-only no momento exibimos sucesso.
        return {"message": "Autenticação Google realizada com sucesso. Tokens armazenados de modo seguro.", "next_steps": "Pode fechar esta aba e retornar à aplicação."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
