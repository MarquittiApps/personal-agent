import unittest
from unittest.mock import MagicMock, patch
from app.core.graph import compile_graph
from langgraph.checkpoint.base import BaseCheckpointSaver

class TestPersistence(unittest.TestCase):
    @patch('langgraph.checkpoint.postgres.PostgresSaver.from_conn_string')
    def test_compile_with_checkpointer(self, mock_from_conn_string):
        # Setup mock checkpointer
        mock_checkpointer = MagicMock(spec=BaseCheckpointSaver)
        mock_from_conn_string.return_value = mock_checkpointer
        
        # Simulates graph compilation with checkpointer
        from langgraph.graph import StateGraph, START, END
        from app.core.graph import State
        
        builder = StateGraph(State)
        builder.add_node("test", lambda x: x)
        builder.add_edge(START, "test")
        builder.add_edge("test", END)
        
        # Compiles with the mock
        graph = builder.compile(checkpointer=mock_checkpointer)
        
        # Checks if the graph has a checkpointer
        self.assertIsNotNone(graph.checkpointer)

if __name__ == '__main__':
    unittest.main()
