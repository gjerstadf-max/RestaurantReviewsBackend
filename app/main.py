from fastapi import FastAPI

app = FastAPI(
    title="Restaurant Reviews API",
    version="0.1.0"
)

@app.get("/ping")
def ping():
    return {"message": "pong"}
