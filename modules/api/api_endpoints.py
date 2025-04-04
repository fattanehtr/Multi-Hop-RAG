from flask import Flask, request, jsonify
from modules.retrieval.multi_hop_retriever import MultiHopRetriever
from modules.nlp.text_processor import TextProcessor
from modules.llm.response_generator import ResponseGenerator
import json

app = Flask(__name__)


with open("data/hotpotqa.json", "r") as f:
    data = json.load(f)
documents = [item["context"] for item in data]
text_processor = TextProcessor()
embeddings = [text_processor.get_embedding(doc) for doc in documents]
retriever = MultiHopRetriever(documents, embeddings)
response_generator = ResponseGenerator("YOUR_API_KEY")

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    query = data["query"]
    query_embedding = text_processor.get_embedding(query)
    retrieved_documents = retriever.retrieve(query_embedding)
    response = response_generator.generate_response(query, retrieved_documents)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)