import unittest
import tempfile
import json
import sys
from pathlib import Path

# Ensure the project package directory is on sys.path so tests can import `main`
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import main


class TestMain(unittest.TestCase):
    def test_get_messages_seed(self):
        a = main.get_messages(3, seed=42)
        b = main.get_messages(3, seed=42)
        self.assertEqual(a, b)
        self.assertEqual(len(a), 3)

    def test_load_messages_from_text_file(self):
        with tempfile.NamedTemporaryFile('w+', delete=False, encoding='utf-8') as f:
            f.write("one\n\n two \nthree\n")
            path = f.name
        try:
            msgs = main.load_messages_from_file(path)
            self.assertEqual(msgs, ["one", "two", "three"])
        finally:
            Path(path).unlink()

    def test_load_messages_from_json_file(self):
        with tempfile.NamedTemporaryFile('w+', delete=False, encoding='utf-8', suffix='.json') as f:
            json.dump(["a", "b"], f)
            path = f.name
        try:
            msgs = main.load_messages_from_file(path)
            self.assertEqual(msgs, ["a", "b"])
        finally:
            Path(path).unlink()


if __name__ == '__main__':
    unittest.main()
