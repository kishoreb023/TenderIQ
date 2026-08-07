from fastapi import FastAPI

app = FastAPI(
    title="TenderIQ API",
    description="AI-Powered Tender Intelligence & Bid Decision Support Platform",
    version="1.0.0"
)


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