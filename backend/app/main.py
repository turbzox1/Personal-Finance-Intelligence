from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend API for the Personal Finance Intelligence Platform",
)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "debug": settings.DEBUG,
        "version": settings.APP_VERSION,
    }