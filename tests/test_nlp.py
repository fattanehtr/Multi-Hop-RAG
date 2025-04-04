import numpy as  np
import unittest
from modules.nlp.text_processor import TextProcessor

class TestNLP(unittest.TestCase):
    def setUp(self):
        self.text_processor = TextProcessor()

    def test_get_embedding(self):
        embedding = self.text_processor.get_embedding("test text")
        self.assertIsInstance(embedding, np.ndarray)
        self.assertEqual(embedding.shape[1], 768)

if __name__ == "__main__":
    unittest.main()