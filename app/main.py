from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import Orchestrator

app = FastAPI()

class SimulationRequest(BaseModel):
    income: float
    expenses: float
    goal_months: int

    enable_job_loss: bool = False
    job_loss_start: int = 3
    job_loss_duration: int = 6

    enable_inflation: bool = False
    inflation_rate: float = 0.15


@app.post("/run")
def run_simulation(req: SimulationRequest):
    return Orchestrator().run(req)
