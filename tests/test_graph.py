import unittest
import networkx as nx
from navviz.graph import build_graph

class TestGraphGeneration(unittest.TestCase):
    def test_build_graph_nodes(self):
        nav_data = ["/home", "/about", "/dashboard"]
        G = build_graph(nav_data)
        self.assertIsInstance(G, nx.DiGraph)
        self.assertEqual(set(G.nodes), set(nav_data))
        self.assertEqual(len(G.edges), 0)  # No edges yet

    def test_build_graph_empty(self):
        nav_data = []
        G = build_graph(nav_data)
        self.assertIsInstance(G, nx.DiGraph)
        self.assertEqual(len(G.nodes), 0)
        self.assertEqual(len(G.edges), 0)

if __name__ == "__main__":
    unittest.main()
