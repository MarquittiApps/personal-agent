import json
import google.oauth2.credentials
from app.core.database import get_db_connection
from app.core.crypto import decrypt_data, encrypt_data
from google.auth.transport.requests import Request

def get_google_credentials(user_id: str) -> google.oauth2.credentials.Credentials:
    """Busca as credenciais do Google para o usuário no banco de dados e as formata."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT token_data FROM user_credentials WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if not row:
        raise ValueError(f"Credenciais não encontradas para o usuário {user_id}. Faça login no Google primeiro.")
        
    encrypted_token = row[0]
    token_json = decrypt_data(encrypted_token)
    creds_data = json.loads(token_json)
    
    creds = google.oauth2.credentials.Credentials(
        token=creds_data.get('token'),
        refresh_token=creds_data.get('refresh_token'),
        token_uri=creds_data.get('token_uri'),
        client_id=creds_data.get('client_id'),
        client_secret=creds_data.get('client_secret'),
        scopes=creds_data.get('scopes')
    )
    
    # Refresh automático
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        # Atualiza o banco com o novo access token
        new_creds_data = {
            'token': creds.token,
            'refresh_token': creds.refresh_token,
            'token_uri': creds.token_uri,
            'client_id': creds.client_id,
            'client_secret': creds.client_secret,
            'scopes': creds.scopes
        }
        new_encrypted = encrypt_data(json.dumps(new_creds_data))
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE user_credentials SET token_data = %s, updated_at = CURRENT_TIMESTAMP WHERE user_id = %s", 
                    (new_encrypted, user_id))
        conn.commit()
        cur.close()
        conn.close()
        
    return creds
