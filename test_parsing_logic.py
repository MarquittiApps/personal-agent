import json
import ast
import unittest

class TestParsingLogic(unittest.TestCase):
    def test_json_parsing(self):
        content_str = '{"type": "DASHBOARD_UPDATE", "data": {"items": []}}'
        output_dict = json.loads(content_str)
        self.assertEqual(output_dict["type"], "DASHBOARD_UPDATE")
        self.assertIsInstance(output_dict["data"]["items"], list)

    def test_ast_fallback_parsing(self):
        # Python dict style string (single quotes)
        content_str = "{'type': 'DASHBOARD_UPDATE', 'data': {'items': [1, 2, 3]}}"
        try:
            output_dict = json.loads(content_str)
        except Exception:
            output_dict = ast.literal_eval(content_str)

        self.assertEqual(output_dict["type"], "DASHBOARD_UPDATE")
        self.assertEqual(output_dict["data"]["items"], [1, 2, 3])

    def test_invalid_parsing(self):
        content_str = "not a json or dict"
        with self.assertRaises(Exception):
            try:
                output_dict = json.loads(content_str)
            except Exception:
                output_dict = ast.literal_eval(content_str)

if __name__ == "__main__":
    unittest.main()
