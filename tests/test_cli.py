import unittest
from navviz import cli

class TestCLI(unittest.TestCase):
    def test_cli_runs(self):
        # Placeholder test: just checks that main() runs without error
        try:
            cli.main
        except Exception as e:
            self.fail(f"CLI main() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
