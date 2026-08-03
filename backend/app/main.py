from fastapi import FastAPI
from app.api.refund.routes import router as refund_router

app = FastAPI(
    title="FluxEngine API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to FluxEngine 🚀",
        "status": "Running",
        "version": "1.0.0"
    }

app.include_router(
    refund_router,
    prefix="/refund",
    tags=["Refund"]
)