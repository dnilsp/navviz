import unittest
import os
import networkx as nx
from navviz.output import output_graph

class TestOutputFormatting(unittest.TestCase):
    def setUp(self):
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(["/home", "/about", "/dashboard"])

    def test_output_terminal(self):
        # Capture printed output
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            output_graph(self.graph, "terminal")
            output = out.getvalue()
            self.assertIn("/home", output)
            self.assertIn("/about", output)
            self.assertIn("/dashboard", output)
        finally:
            sys.stdout = saved_stdout

    def test_output_pdf(self):
        # Remove PDF if it exists
        pdf_path = "navigation_graph.pdf"
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        output_graph(self.graph, "pdf")
        self.assertTrue(os.path.exists(pdf_path))
        # Clean up
        os.remove(pdf_path)

if __name__ == "__main__":
    unittest.main()
