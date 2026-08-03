from app.agents.avil.router import AVILRouter


class DAAMEngine:

    def __init__(self):
        self.router = AVILRouter()

    def detect_domain(self, request):

        """
        Future:
        - AI Classification
        - Elastic Search
        - Intent Detection

        Current MVP:
        Always returns ecommerce.
        """

        return "ecommerce"

    def process_refund(self, order_id, reason):

        request = {
            "order_id": order_id,
            "reason": reason
        }

        domain = self.detect_domain(request)

        adapter = self.router.get_adapter(domain)

        return adapter.process(order_id, reason)