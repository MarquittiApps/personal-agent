import unittest
from unittest.mock import patch, MagicMock
import json
from app.core.rag_engine import add_iot_product, get_iot_products, update_iot_product, delete_iot_product

class TestCatalogCRUD(unittest.TestCase):

    @patch('app.core.rag_engine.get_db_connection')
    def test_add_iot_product_success(self, mock_get_db):
        mock_conn = MagicMock()
        mock_cur = mock_conn.cursor.return_value
        mock_cur.fetchone.return_value = (1, '2026-03-19', '2026-03-19')
        mock_get_db.return_value = mock_conn

        result = add_iot_product(
            name="Smart Switch",
            brand="Sonoff",
            protocol="WiFi",
            payload_yaml="power: on",
            metadata={"location": "living room"}
        )

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["id"], 1)
        mock_cur.execute.assert_called()
        mock_conn.commit.assert_called()

    @patch('app.core.rag_engine.get_db_connection')
    def test_get_iot_products(self, mock_get_db):
        mock_conn = MagicMock()
        mock_cur = mock_conn.cursor.return_value
        mock_cur.fetchall.return_value = [
            (1, "Device 1", "Brand A", "Zigbee", "payload: {}", {}, "date", "date")
        ]
        mock_get_db.return_value = mock_conn

        results = get_iot_products()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Device 1")

    @patch('app.core.rag_engine.get_db_connection')
    def test_update_iot_product(self, mock_get_db):
        mock_conn = MagicMock()
        mock_cur = mock_conn.cursor.return_value
        mock_cur.fetchone.return_value = (1,)
        mock_get_db.return_value = mock_conn

        result = update_iot_product(1, name="Updated Name")
        self.assertEqual(result["status"], "success")
        mock_conn.commit.assert_called()

    @patch('app.core.rag_engine.get_db_connection')
    def test_delete_iot_product(self, mock_get_db):
        mock_conn = MagicMock()
        mock_cur = mock_conn.cursor.return_value
        mock_cur.fetchone.return_value = (1,)
        mock_get_db.return_value = mock_conn

        result = delete_iot_product(1)
        self.assertEqual(result["status"], "success")
        mock_conn.commit.assert_called()

if __name__ == '__main__':
    unittest.main()
