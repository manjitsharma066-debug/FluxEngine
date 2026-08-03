from app.adapters.ecommerce.refund_adapter import EcommerceRefundAdapter


class AVILRouter:

    def __init__(self):
        self.adapters = {
            "ecommerce": EcommerceRefundAdapter()
        }

    def get_adapter(self, domain: str):

        if domain not in self.adapters:
            raise Exception(f"{domain} adapter not found.")

        return self.adapters[domain]