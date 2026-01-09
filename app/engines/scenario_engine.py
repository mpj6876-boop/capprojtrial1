class ScenarioEngine:

    def apply(self, income, expense, scenario, month):
        if scenario.start_month <= month <= scenario.start_month + scenario.duration_months:
            for impact in scenario.impacts:
                if impact.variable == "income":
                    income = self._apply_op(income, impact)
                elif impact.variable == "expense":
                    expense = self._apply_op(expense, impact)
        return income, expense

    def _apply_op(self, base, impact):
        if impact.operation == "set":
            return impact.value
        if impact.operation == "add":
            return base + impact.value
        if impact.operation == "multiply":
            return base * impact.value
        return base
