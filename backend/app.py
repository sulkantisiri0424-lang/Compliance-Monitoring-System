from fastapi import FastAPI

app = FastAPI(
    title="Compliance Monitoring System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Compliance Monitoring System API is Running Successfully!"
    }

@app.get("/health")
def health():
    return {
        "status": "OK"
    }
