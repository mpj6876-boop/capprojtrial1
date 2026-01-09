class OutcomeParser:
    def parse(self, baseline, scenario):
        base_end = baseline[-1]
        scn_end = scenario[-1]

        worst_cash = min(p["cash_balance"] for p in scenario)
        worst_networth = min(p["net_worth"] for p in scenario)

        recovery_month = None
        for p in scenario:
            if p["net_worth"] >= 0:
                recovery_month = p["month"]
                break

        return {
            "baseline_final_networth": base_end["net_worth"],
            "scenario_final_networth": scn_end["net_worth"],
            "worst_cash_balance": worst_cash,
            "worst_networth": worst_networth,
            "recovery_month": recovery_month
        }
