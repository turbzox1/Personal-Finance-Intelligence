from fastapi import FastAPI

app = FastAPI(
    title="Personal Finance Intelligence API",
    description="Backend API for the Personal Finance Intelligence Platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Personal Finance Intelligence API is running 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }