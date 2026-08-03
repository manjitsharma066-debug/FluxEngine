from pydantic import BaseModel


class DecisionResult(BaseModel):
    intent: str
    domain: str
    confidence: float