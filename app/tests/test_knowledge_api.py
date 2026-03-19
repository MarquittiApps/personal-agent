import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

class TestKnowledgeAPI(unittest.TestCase):

    @patch('app.api.v1.endpoints.knowledge.query_knowledge_base')
    def test_query_rag_endpoint(self, mock_query):
        mock_query.return_value = [
            {"content": "Norma NBR-5410", "metadata": {"page": 1}, "source": "nbr5410.pdf", "score": 0.9}
        ]

        response = client.post(
            "/api/v1/knowledge/query",
            json={"query": "O que diz a NBR-5410?", "top_k": 5}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["content"], "Norma NBR-5410")

    @patch('app.api.v1.endpoints.knowledge.add_iot_product')
    def test_create_device_endpoint(self, mock_add):
        mock_add.return_value = {
            "status": "success",
            "id": 101,
            "name": "Smart Hub",
            "brand": "IoT-Go",
            "protocol": "Matter",
            "payload_yaml": "type: hub",
            "metadata": {},
            "created_at": "2026-03-19T00:00:00",
            "updated_at": "2026-03-19T00:00:00"
        }

        response = client.post(
            "/api/v1/knowledge/catalog",
            json={
                "name": "Smart Hub",
                "brand": "IoT-Go",
                "protocol": "Matter",
                "payload_yaml": "type: hub",
                "metadata": {}
            }
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["id"], 101)

    @patch('app.api.v1.endpoints.knowledge.get_iot_products')
    def test_list_devices_endpoint(self, mock_get):
        mock_get.return_value = [
            {"id": 1, "name": "Device 1", "brand": "B1", "protocol": "P1", "payload_yaml": "y1", "metadata": {}, "created_at": "2026-03-19T00:00:00", "updated_at": "2026-03-19T00:00:00"}
        ]

        response = client.get("/api/v1/knowledge/catalog")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

if __name__ == '__main__':
    unittest.main()
