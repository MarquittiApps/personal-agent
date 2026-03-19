"""
Testes unitários para app/core/llm_factory.py

Execute: pytest app/tests/test_llm_factory.py -v
"""

import pytest
import os
from unittest.mock import patch, MagicMock

# Importar o módulo uma vez
import app.core.llm_factory as factory


class TestGetLlm:
    """Testa a factory get_llm() para os diferentes providers."""

    @patch("app.core.llm_factory.ChatGoogleGenerativeAI")
    def test_google_provider_returns_google_genai(self, mock_google_cls):
        """LLM_PROVIDER=google → deve retornar ChatGoogleGenerativeAI."""
        mock_llm = MagicMock()
        mock_google_cls.return_value = mock_llm
        
        with patch.dict("os.environ", {"LLM_PROVIDER": "google", "GOOGLE_MODEL": "gemini-2.5-flash"}):
            result = factory.get_llm()

            mock_google_cls.assert_called()
            assert result is mock_llm

    @patch("app.core.llm_factory.ChatGoogleGenerativeAI")
    def test_google_provider_is_default(self, mock_google_cls):
        """Sem LLM_PROVIDER definido → deve usar google como padrão."""
        mock_llm = MagicMock()
        mock_google_cls.return_value = mock_llm
        
        # Usa patch.dict com clear=True para garantir ambiente limpo
        with patch.dict("os.environ", {"GOOGLE_MODEL": "gemini-2.5-flash"}, clear=True):
            result = factory.get_llm()
            assert result is mock_llm

    @patch("app.core.llm_factory.ChatOllama")
    @patch("app.core.llm_factory._check_ollama_health")
    def test_ollama_provider_returns_chat_ollama(self, mock_health, mock_ollama_cls):
        """LLM_PROVIDER=ollama → deve retornar ChatOllama com params corretos."""
        mock_llm = MagicMock()
        mock_ollama_cls.return_value = mock_llm
        
        env = {
            "LLM_PROVIDER": "ollama",
            "OLLAMA_MODEL": "llama3",
            "OLLAMA_BASE_URL": "http://localhost:11434",
        }
        with patch.dict("os.environ", env):
            result = factory.get_llm()

            mock_ollama_cls.assert_called_with(model="llama3", base_url="http://localhost:11434")
            assert result is mock_llm

    def test_unknown_provider_raises_value_error(self):
        """Provider desconhecido → deve levantar ValueError com mensagem clara."""
        with patch.dict("os.environ", {"LLM_PROVIDER": "anthropic"}):
            with pytest.raises(ValueError, match="Provider desconhecido: 'anthropic'"):
                factory.get_llm()

    @patch("urllib.request.urlopen")
    @patch("urllib.request.Request")
    def test_ollama_health_check_failure_does_not_raise(self, mock_request, mock_urlopen):
        """Se Ollama offline, health-check apenas loga warning — não deve levantar exceção."""
        mock_urlopen.side_effect = Exception("Connection refused")
        
        # Não deve levantar exceção
        factory._check_ollama_health("http://localhost:99999")
