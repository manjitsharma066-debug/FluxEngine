from pydantic import BaseModel


class RefundRequest(BaseModel):
    order_id: str
    reason: str