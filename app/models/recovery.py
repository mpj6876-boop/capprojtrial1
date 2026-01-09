from pydantic import BaseModel
from typing import List, Optional
from .simulation import SimulationResult
from .failure import FailureEvent

class RecoveryOption(BaseModel):
    option_id: str
    name: str
    description: str
    tradeoff: str
    simulated_result: SimulationResult

class RecoveryAnalysis(BaseModel):
    failure: FailureEvent
    options: List[RecoveryOption]
    recommended_option_id: Optional[str]
