from fastapi import APIRouter
from app.models.refund import RefundRequest
from app.agents.daam.engine import DAAMEngine

router = APIRouter()

daam = DAAMEngine()


@router.post("/check")
def refund(request: RefundRequest):

    result = daam.process_refund(
        request.order_id,
        request.reason
    )

    return {
        "order_id": request.order_id,
        **result,
        "processed_by": "FluxEngine"
    }