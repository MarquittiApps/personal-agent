import os
import json
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
import google_auth_oauthlib.flow
from app.core.database import get_db_connection
from app.core.crypto import encrypt_data

# Necessary to test locally on http instead of https
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

router = APIRouter(prefix="/auth", tags=["auth"])

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback")

# Necessary scopes for Calendar and Tasks and user info if needed
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/tasks'
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

# Temporary dictionary to maintain the PKCE code_verifier (valid for 1 worker in dev environment)
oauth_states = {}

@router.get("/google")
def login_google():
    try:
        client_config = get_client_config()
        flow = google_auth_oauthlib.flow.Flow.from_client_config(
            client_config, scopes=SCOPES
        )
        flow.redirect_uri = REDIRECT_URI
        
        # prompt='consent' and access_type='offline' force the sending of the refresh_token
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            prompt='consent'
        )
        
        # Saves the flow's code_verifier associated with the generated state
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
        
        # Restores the code_verifier generated in the login step
        if state in oauth_states:
            flow.code_verifier = oauth_states.pop(state)
        
        # Converts to http URL because of Insecure Transport; in prod it should be https
        authorization_response = str(request.url)
        flow.fetch_token(authorization_response=authorization_response)
        
        credentials = flow.credentials
        
        # Serialize credentials
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
        
        # Standardized User ID for the MVP
        user_id = "default_user"
        
        init_db() # ensures the table exists
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
        
        # Ideally redirect back to the frontend, but for a backend-only MVP at the moment we show success.
        return {
            "message": "Google Authentication successful. Tokens stored securely.",
            "next_steps": "You can close this tab and return to the application."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
