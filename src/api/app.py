from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="Gov Convo Intel API", version="0.1.0")

class HealthResponse(BaseModel):
    status: str

@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "ok"}

@app.get("/areas/{code}/topics")
def get_topics(code: str, window: str = Query("90d")):
    # TODO: implement: fetch from Neo4j, filter tier='A'
    return {"area": code, "window": window, "topics": []}
