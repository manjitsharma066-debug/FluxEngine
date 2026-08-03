from app.agents.avil.router import AVILRouter
from app.models.decision import DecisionResult


class DAAMEngine:

    def __init__(self):
        self.router = AVILRouter()

    def detect_intent(self, request):

        reason = request["reason"].lower()

        refund_keywords = [
            "refund",
            "damaged",
            "wrong",
            "return"
        ]

        for keyword in refund_keywords:

            if keyword in reason:

                return DecisionResult(
                    intent="refund",
                    domain="ecommerce",
                    confidence=0.98
                )

        return DecisionResult(
            intent="unknown",
            domain="ecommerce",
            confidence=0.50
        )

    def process_refund(self, order_id, reason):

        request = {
            "order_id": order_id,
            "reason": reason
        }

        decision = self.detect_intent(request)

        adapter = self.router.get_adapter(
            decision.domain
        )

        return adapter.process(order_id, reason)