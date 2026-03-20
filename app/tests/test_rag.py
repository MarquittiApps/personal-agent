import pytest
from unittest.mock import patch, MagicMock
from app.tools.rag_engine import query_knowledge_base
from app.core.rag_engine import add_iot_product, update_knowledge_base

class TestRAGEngine:

    @patch("app.core.rag_engine.get_db_connection")
    def test_add_iot_product(self, mock_db):
        """Testa inserção de produto IoT."""
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchone.return_value = [1, "2024-01-01", "2024-01-01"]

        result = add_iot_product(
            name="Smart Bulb RGB",
            brand="HueLike",
            protocol="Zigbee",
            payload_yaml="on: true\nbrightness: 100",
            metadata={"version": "1.0"}
        )
        assert "status" in result
        assert result["status"] == "success"
        assert "id" in result

    @patch("app.core.rag_engine.get_db_connection")
    @patch("app.core.rag_engine.get_embeddings")
    def test_query_knowledge_base(self, mock_get_embeddings, mock_db):
        """Testa busca semântica."""
        mock_emb = MagicMock()
        mock_get_embeddings.return_value = mock_emb
        mock_emb.embed_query.return_value = [0.0] * 1536
        
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        mock_cur.fetchall.return_value = [
            ("Conteúdo teste", {"source": "pdf"}, "fake.pdf", 0.9)
        ]

        results = query_knowledge_base.invoke({"query": "como configurar zigbee?"})
        assert "Conteúdo teste" in results
        mock_emb.embed_query.assert_called_once()
        
    @patch("app.core.rag_engine.PyPDFLoader")
    @patch("app.core.rag_engine.get_embeddings")
    @patch("app.core.rag_engine.get_db_connection")
    @patch("os.path.exists")
    def test_update_knowledge_base_mock(self, mock_exists, mock_db, mock_get_embeddings, mock_loader):
        """Testa pipeline de upload mockado."""
        mock_exists.return_value = True
        mock_emb = MagicMock()
        mock_get_embeddings.return_value = mock_emb
        mock_emb.embed_query.return_value = [0.1] * 1536
        
        mock_conn = MagicMock()
        mock_db.return_value = mock_conn
        
        # Mock do loader retornando 1 documento
        mock_doc = MagicMock()
        mock_doc.page_content = "Conteúdo de teste para RAG."
        mock_doc.metadata = {"page": 1}
        mock_loader.return_value.load.return_value = [mock_doc]
        
        result = update_knowledge_base("fake.pdf")
        assert "status" in result
        assert result["status"] == "success"
        mock_emb.embed_query.assert_called()
