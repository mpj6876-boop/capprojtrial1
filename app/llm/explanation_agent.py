from app.models.explanation import ExplanationContext, ExplanationText
from .ollama_client import OllamaClient

class ExplanationAgent:

    def __init__(self):
        self.llm = OllamaClient()

    def explain(self, context: ExplanationContext) -> ExplanationText:
        prompt = f"""
You explain financial simulation results.
You never calculate or give advice.

Scenario: {context.scenario_name}
Baseline success: {context.baseline_success}
Scenario success: {context.scenario_success}

Failure summary:
{context.failure_summary}

Affected goals:
{context.affected_goals}

Recovery options:
{context.recovery_options}

Explain calmly in under {context.max_words} words.
"""
        return ExplanationText(summary=self.llm.generate(prompt))
