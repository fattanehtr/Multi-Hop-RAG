import unittest
from modules.llm.response_generator import ResponseGenerator

class TestLLM(unittest.TestCase):
    def setUp(self):
        self.response_generator = ResponseGenerator("YOUR_API_KEY")

    def test_generate_response(self):
        response = self.response_generator.generate_response("test query", ["document 1", "document 2"])
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

if __name__ == "__main__":
    unittest.main()