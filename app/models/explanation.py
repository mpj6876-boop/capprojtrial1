from pydantic import BaseModel
from typing import List, Optional

class ExplanationContext(BaseModel):
    scenario_name: str
    baseline_success: bool
    scenario_success: bool
    failure_summary: Optional[str]
    affected_goals: List[str]
    recovery_options: List[dict]
    max_words: int = 120

class ExplanationText(BaseModel):
    summary: str
