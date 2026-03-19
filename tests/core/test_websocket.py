import unittest
import json
from fastapi.testclient import TestClient
from app.main import app

class TestWebSocket(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_websocket_chat_connection(self):
        with self.client.websocket_connect("/ws/chat") as websocket:
            # Send a test message
            websocket.send_text(json.dumps({"text": "Connection test"}))
            
            # Receive response (expecting tokens or status before end)
            data = websocket.receive_json()
            self.assertIn(data["type"], ["token", "status", "end"])
            
            # Continue receiving until end
            while data["type"] != "end":
                data = websocket.receive_json()
            
            self.assertEqual(data["type"], "end")

if __name__ == '__main__':
    unittest.main()
