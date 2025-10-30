import unittest
import os
import tempfile
from navviz.parser import detect_project_type

class TestProjectTypeDetection(unittest.TestCase):
    def test_detect_react(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            open(os.path.join(tmpdir, "package.json"), "w").close()
            open(os.path.join(tmpdir, "App.jsx"), "w").close()
            self.assertEqual(detect_project_type(tmpdir), "react")

    def test_detect_node(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            open(os.path.join(tmpdir, "package.json"), "w").close()
            self.assertEqual(detect_project_type(tmpdir), "node")

    def test_detect_python(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            open(os.path.join(tmpdir, "requirements.txt"), "w").close()
            self.assertEqual(detect_project_type(tmpdir), "python")

    def test_detect_angular(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            open(os.path.join(tmpdir, "angular.json"), "w").close()
            self.assertEqual(detect_project_type(tmpdir), "angular")

    def test_detect_flutter(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            open(os.path.join(tmpdir, "pubspec.yaml"), "w").close()
            self.assertEqual(detect_project_type(tmpdir), "flutter")

    def test_detect_unknown(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.assertEqual(detect_project_type(tmpdir), "unknown")

if __name__ == "__main__":
    unittest.main()
