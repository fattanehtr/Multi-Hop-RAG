import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class MultiHopRetriever:
    def __init__(self, documents, embeddings):
        self.documents = documents
        self.embeddings = embeddings
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = nx.Graph()
        for i in range(len(self.documents)):
            graph.add_node(i)

        similarity_matrix = cosine_similarity(self.embeddings)
        for i in range(len(self.documents)):
            for j in range(i + 1, len(self.documents)):
                if similarity_matrix[i][j] > 0.5:  # آستانه شباهت
                    graph.add_edge(i, j)
        return graph

    def retrieve(self, query_embedding, hop_count=2):
        query_similarity = cosine_similarity([query_embedding], self.embeddings)[0]
        initial_retrieved_indices = np.argsort(query_similarity)[-5:]  # 5 سند برتر

        retrieved_indices = set(initial_retrieved_indices)
        for _ in range(hop_count):
            for index in list(retrieved_indices):
                neighbors = self.graph.neighbors(index)
                retrieved_indices.update(neighbors)
        return [self.documents[i] for i in retrieved_indices]