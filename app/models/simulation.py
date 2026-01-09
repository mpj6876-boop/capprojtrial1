from pydantic import BaseModel
from typing import List, Optional

class MonthlySnapshot(BaseModel):
    month: int
    income: float
    expenses: float
    savings: float
    net_worth: float
    emergency_fund: float

class GoalProgress(BaseModel):
    goal_id: str
    contributed: float
    remaining: float
    completed: bool
    expected_completion_month: Optional[int]

class SimulationResult(BaseModel):
    simulation_id: str
    monthly_projection: List[MonthlySnapshot]
    goals: List[GoalProgress]
    success: bool
