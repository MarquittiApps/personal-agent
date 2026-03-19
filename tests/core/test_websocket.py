import unittest
import json
from fastapi.testclient import TestClient
from app.main import app

class TestWebSocket(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_websocket_chat_connection(self):
        with self.client.websocket_connect("/ws/chat") as websocket:
            # Envia uma mensagem de teste
            websocket.send_text(json.dumps({"text": "Teste de conexão"}))
            
            # Recebe a resposta (espera-se tokens ou status antes do end)
            data = websocket.receive_json()
            self.assertIn(data["type"], ["token", "status", "end"])
            
            # Continua recebendo até o fim
            while data["type"] != "end":
                data = websocket.receive_json()
            
            self.assertEqual(data["type"], "end")

if __name__ == '__main__':
    unittest.main()
