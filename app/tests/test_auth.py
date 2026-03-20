import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

class TestAuthAPI:

    @patch("app.api.auth.google_auth_oauthlib.flow.Flow.from_client_config")
    @patch("app.api.auth.get_client_config")
    def test_login_google_redirects(self, mock_config, mock_flow_cls):
        mock_config.return_value = {"web": {"client_id": "test", "client_secret": "test"}}
        mock_flow = MagicMock()
        mock_flow_cls.return_value = mock_flow
        mock_flow.authorization_url.return_value = ("https://accounts.google.com/o/oauth2/auth?test", "state123")
        mock_flow.code_verifier = "verifier123"

        response = client.get("/auth/google", follow_redirects=False)
        
        assert response.status_code == 307
        assert "accounts.google.com" in response.headers["location"]

    @patch("app.api.auth.google_auth_oauthlib.flow.Flow.from_client_config")
    @patch("app.api.auth.get_client_config")
    @patch("app.api.auth.get_db_connection")
    @patch("app.api.auth.encrypt_data")
    def test_callback_google_success(self, mock_encrypt, mock_db, mock_config, mock_flow_cls):
        mock_config.return_value = {"web": {"client_id": "test", "client_secret": "test"}}
        mock_encrypt.return_value = "encrypted_stuff"
        
        mock_flow = MagicMock()
        mock_flow_cls.return_value = mock_flow
        
        mock_creds = MagicMock()
        mock_creds.token = "token123"
        mock_creds.refresh_token = "refresh123"
        mock_creds.token_uri = "uri"
        mock_creds.client_id = "cid"
        mock_creds.client_secret = "csec"
        mock_creds.scopes = []
        mock_flow.credentials = mock_creds

        mock_conn = MagicMock()
        mock_db.return_value = mock_conn

        # Simular que o state existe no cache (PKCE)
        from app.api.auth import oauth_states
        oauth_states["state123"] = "verifier123"

        response = client.get("/auth/google/callback?code=123&state=state123")
        
        assert response.status_code == 200
        assert "sucesso" in response.json()["message"]
        mock_conn.commit.assert_called()

    @patch("app.api.auth.get_client_config")
    def test_login_google_error_missing_config(self, mock_config):
        mock_config.side_effect = ValueError("Credentials missing")
        
        response = client.get("/auth/google")
        assert response.status_code == 500
        assert "Credentials missing" in response.json()["detail"]
