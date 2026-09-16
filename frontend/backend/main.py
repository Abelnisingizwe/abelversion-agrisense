from fastapi import FastAPI

app = FastAPI(
    title="ABELVERSION AGRISENSE API",
    description="Data-Driven Smart Agriculture Advisory System for Rwanda",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "system": "ABELVERSION AGRISENSE",
        "status": "online",
        "phase": "Data-Driven Agriculture Advisory"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
