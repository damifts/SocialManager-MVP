from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(title="Social Manager API", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Social Manager API"}


app.include_router(api_router, prefix="/api")
