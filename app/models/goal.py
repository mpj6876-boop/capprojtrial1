from pydantic import BaseModel

class FinancialGoal(BaseModel):
    goal_id: str
    name: str
    target_amount: float
    timeframe_months: int
    priority: int
    flexible: bool
