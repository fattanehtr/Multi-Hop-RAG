import requests

class ResponseGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/completions"

    def generate_response(self, query, retrieved_documents):
        prompt = f"Question: {query}\n\nContext: {retrieved_documents}\n\nAnswer:"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "max_tokens": 150
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()["choices"][0]["text"].strip()