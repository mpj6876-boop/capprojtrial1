from app.llm.ollama_client import OllamaClient

class AdviceAgent:

    def generate(self, outcome):
        prompt = f"""
You are a conservative financial advisor.
Use only the data below.
Give 3–5 short practical suggestions.

{outcome}
"""
        text = OllamaClient().generate(prompt)
        return [a.strip("- ").strip() for a in text.split("\n") if a.strip()]
