from app.services.refund_service import check_refund


class EcommerceRefundAdapter:

    def process(self, order_id: str, reason: str):
        return check_refund(order_id, reason)