class SimulationEngine:

    def run(self, months, income, expenses, scenarios=None):
        cash = 0
        debt = 0
        projection = []

        for month in range(1, months + 1):

            eff_income, eff_expenses = income, expenses

            if scenarios:
                for sc in scenarios:
                    if sc.start_month <= month < sc.start_month + sc.duration:
                        eff_income *= sc.income_multiplier
                        eff_expenses *= sc.expense_multiplier

            surplus = eff_income - eff_expenses

            # If surplus negative → burn cash first, then debt
            if surplus < 0:
                if cash > 0:
                    burn = min(cash, abs(surplus))
                    cash -= burn
                    remaining = abs(surplus) - burn
                    debt += remaining
                else:
                    debt += abs(surplus)

            # If surplus positive → pay debt first, then grow cash
            else:
                if debt > 0:
                    pay = min(debt, surplus)
                    debt -= pay
                    surplus -= pay
                cash += surplus

            net_worth = cash - debt

            projection.append({
                "month": month,
                "income": eff_income,
                "expenses": eff_expenses,
                "cash_balance": cash,
                "debt": debt,
                "net_worth": net_worth
            })

        return projection
