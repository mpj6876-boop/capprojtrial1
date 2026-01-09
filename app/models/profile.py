from pydantic import BaseModel
from typing import List

class Income(BaseModel):
    source: str
    monthly_amount: float
    stable: bool

class Expense(BaseModel):
    category: str
    monthly_amount: float
    mandatory: bool

class FinancialProfile(BaseModel):
    profile_id: str
    incomes: List[Income]
    expenses: List[Expense]
    risk_tolerance: str
    emergency_fund: float
