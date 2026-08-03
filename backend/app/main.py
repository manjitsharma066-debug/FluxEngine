from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.refund.routes import router as refund_router

app = FastAPI(
    title="FluxEngine API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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