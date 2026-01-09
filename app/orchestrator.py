from app.engines.simulation_engine import SimulationEngine
from app.engines.failure_detector import FailureDetector
from app.engines.recovery_engine import RecoveryEngine
from app.models.scenario import Scenario
from app.llm.recovery_agent import RecoveryAgent
from app.engines.outcome_parser import OutcomeParser
from app.llm.advice_agent import AdviceAgent




class Orchestrator:

    def run(self, req):
        engine = SimulationEngine()

        baseline = engine.run(req.goal_months, req.income, req.expenses)

        scenarios = []

        if req.enable_job_loss:
            scenarios.append(Scenario(
                name="Job Loss",
                start_month=req.job_loss_start,
                duration=req.job_loss_duration,
                income_multiplier=0.0
            ))

        if req.enable_inflation:
            scenarios.append(Scenario(
                name="Inflation",
                start_month=1,
                duration=req.goal_months,
                expense_multiplier=1 + req.inflation_rate
            ))


        scenario_result = engine.run(req.goal_months, req.income, req.expenses, scenarios)
        parser = OutcomeParser()
        outcome = parser.parse(baseline, scenario_result)

        advice = AdviceAgent().generate(outcome)

        failure = FailureDetector().detect(scenario_result)

       

        if failure:
            recovery = RecoveryAgent().generate(failure, req)
        else:
            recovery = None
        
    

        return {
            "baseline": baseline,
            "scenario": scenario_result,
            "failure": failure,
            "recovery_options": recovery,
            "outcome_summary":outcome,
            "advice":advice
        }
