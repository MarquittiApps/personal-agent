import unittest
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    """Graph state schema."""
    messages: list[str]
    current_node: str

class TestGraphState(unittest.TestCase):
    def test_state_initialization(self):
        # Checks if the initial state is loaded correctly
        initial_state: State = {"messages": [], "current_node": "start"}
        self.assertEqual(initial_state["current_node"], "start")
        self.assertEqual(len(initial_state["messages"]), 0)

    def test_simple_graph_transition(self):
        # Defines a simple graph to test state transitions
        def node_a(state: State) -> State:
            return {"messages": state["messages"] + ["Hello from Node A"], "current_node": "node_a"}
        
        builder = StateGraph(State)
        builder.add_node("node_a", node_a)
        builder.add_edge(START, "node_a")
        builder.add_edge("node_a", END)
        
        graph = builder.compile()
        
        # Executes the graph
        result = graph.invoke({"messages": [], "current_node": "start"})
        
        # Assertions
        self.assertEqual(result["current_node"], "node_a")
        self.assertIn("Hello from Node A", result["messages"])

if __name__ == '__main__':
    unittest.main()
