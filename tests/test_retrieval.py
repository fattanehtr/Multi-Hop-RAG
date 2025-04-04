import unittest
from modules.retrieval.multi_hop_retriever import MultiHopRetriever
from modules.nlp.text_processor import TextProcessor

class TestRetrieval(unittest.TestCase):
    def setUp(self):
        self.documents = ["document 1", "document 2", "document 3", "document 4"]
        self.text_processor = TextProcessor()
        self.embeddings = [self.text_processor.get_embedding(doc) for doc in self.documents]
        self.retriever = MultiHopRetriever(self.documents, self.embeddings)

    def test_retrieve(self):
        query_embedding = self.text_processor.get_embedding("query")
        retrieved_documents = self.retriever.retrieve(query_embedding)
        self.assertIsInstance(retrieved_documents, list)
        self.assertTrue(len(retrieved_documents) > 0)

if __name__ == "__main__":
    unittest.main()