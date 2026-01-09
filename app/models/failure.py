from enum import Enum
from pydantic import BaseModel
from typing import List

class FailureType(str, Enum):
    CASH_FLOW = "cash_flow_failure"
    GOAL_INFEASIBLE = "goal_infeasible"
    LIQUIDITY = "liquidity_failure"

class FailureEvent(BaseModel):
    failure_type: FailureType
    start_month: int
    duration_months: int
    affected_goals: List[str]
    description: str
