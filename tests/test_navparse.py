import unittest
import os
import tempfile
from navviz.parser import parse_navigation

class TestNavigationParsing(unittest.TestCase):
    def test_parse_navigation_react_routes(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample React file with <Route path="/home" />
            react_file = os.path.join(tmpdir, "App.jsx")
            with open(react_file, "w", encoding="utf-8") as f:
                f.write('<Route path="/home" component={Home} />\n<Route path="/about" />')
            routes = parse_navigation(tmpdir, "react")
            self.assertIn("/home", routes)
            self.assertIn("/about", routes)

    def test_parse_navigation_react_path_colon(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample React file with path: "/dashboard"
            react_file = os.path.join(tmpdir, "routes.js")
            with open(react_file, "w", encoding="utf-8") as f:
                f.write('const route = { path: "/dashboard", component: Dashboard };')
            routes = parse_navigation(tmpdir, "react")
            self.assertIn("/dashboard", routes)

    def test_parse_navigation_empty(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            routes = parse_navigation(tmpdir, "react")
            self.assertEqual(routes, [])

if __name__ == "__main__":
    unittest.main()
