from typing import Optional
from pydantic import BaseModel

class Scenario(BaseModel):
    name: str
    start_month: int
    duration: int
    income_multiplier: float = 1.0
    expense_multiplier: float = 1.0
