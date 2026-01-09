from app.llm.ollama_client import OllamaClient

class RecoveryAgent:

    def generate(self, failure, req):
        prompt = f"""
You are a financial recovery assistant.
You must suggest recovery actions only.
Do not calculate numbers.
Use short bullet points.

Failure: {failure}
Monthly Income: {req.income}
Monthly Expenses: {req.expenses}
Goal Months: {req.goal_months}

Suggest 3–5 realistic recovery strategies.
"""

        text = OllamaClient().generate(prompt)

        return [{"strategy": s.strip("- ").strip()} for s in text.split("\n") if s.strip()]
