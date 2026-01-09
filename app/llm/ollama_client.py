import requests

class OllamaClient:
    def __init__(self, model = "mistral:7b-instruct-q4_0"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt):
        r = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.2
        })

        data = r.json()

        # Works across all Ollama versions
        if "response" in data:
            return data["response"]
        if "message" in data and "content" in data["message"]:
            return data["message"]["content"]

        # Fallback for future versions
        for k, v in data.items():
            if isinstance(v, str):
                return v

        return ""
