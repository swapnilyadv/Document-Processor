import requests

class GeminiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.gemini.com/v1"

    def send_document(self, document_text):
        url = f"{self.base_url}/documents"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "text": document_text
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def generate_summary(self, document_id, prompt):
        url = f"{self.base_url}/summarize"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "document_id": document_id,
            "prompt": prompt
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()