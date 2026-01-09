from app.models.failure import FailureEvent, FailureType

class FailureDetector:
    def detect(self, projection):
        for p in projection:
            if p["cash_balance"] == 0 and p["net_worth"] < 0:
                return {
                    "type": "Liquidity Collapse",
                    "month": p["month"],
                    "deficit": abs(p["net_worth"]),
                    "reason": "Cash exhausted while expenses exceed income"
                }
        return None

