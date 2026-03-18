import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Adiciona a raiz ao path para importar scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from scripts.doctor import check_python_version, check_node_version, check_service_port

class TestDoctorScript(unittest.TestCase):
    
    @patch('sys.version_info')
    def test_check_python_version_ok(self, mock_version):
        mock_version.major = 3
        mock_version.minor = 11
        mock_version.__ge__.return_value = True
        self.assertTrue(check_python_version())

    @patch('subprocess.check_output')
    def test_check_node_version_ok(self, mock_subprocess):
        mock_subprocess.return_value = b"v18.15.0"
        self.assertTrue(check_node_version())

    @patch('subprocess.check_output')
    def test_check_node_version_fail(self, mock_subprocess):
        mock_subprocess.return_value = b"v16.0.0"
        self.assertFalse(check_node_version())

    @patch('socket.socket')
    def test_check_service_port_open(self, mock_socket):
        # Simula porta aberta
        mock_socket_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_socket_instance
        self.assertTrue(check_service_port(5432, "PostgreSQL"))

    @patch('socket.socket')
    def test_check_service_port_closed(self, mock_socket):
        # Simula porta fechada (ConnectionRefusedError)
        mock_socket_instance = MagicMock()
        mock_socket_instance.connect.side_effect = ConnectionRefusedError()
        mock_socket.return_value.__enter__.return_value = mock_socket_instance
        self.assertFalse(check_service_port(5432, "PostgreSQL"))

if __name__ == '__main__':
    unittest.main()
