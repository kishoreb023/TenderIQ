from fastapi import FastAPI

import app.models

from app.api.routes.tenders import router as tender_router
from app.api.routes.companies import router as company_router
from app.api.routes.tender_documents import router as tender_document_router
app = FastAPI(
    title="TenderIQ API",
    description="AI-Powered Tender Intelligence & Bid Decision Support Platform",
    version="1.0.0"
)


app.include_router(tender_router)
app.include_router(company_router)
app.include_router(tender_document_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to TenderIQ API 🚀",
        "status": "Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }