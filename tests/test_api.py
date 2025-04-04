import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_query(self):
        response = requests.post("http://127.0.0.1:5000/query", json={"query": "test query"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json())

if __name__ == "__main__":
    unittest.main()