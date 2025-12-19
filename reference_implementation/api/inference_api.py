from fastapi import FastAPI

app = FastAPI()

@app.post("/query")
def query(payload: dict):
    # This endpoint is intentionally minimal.
    # Real systems plug retrieval, validation,
    # and approval workflows here.
    return {
        "status": "reference_only",
        "note": "Architecture demonstration endpoint"
    }