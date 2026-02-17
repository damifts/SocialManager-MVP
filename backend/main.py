from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from app.routes import router as api_router

app = FastAPI(title="Social Manager API", version="0.1.0")

# CORS middleware per comunicazione con frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check
@app.get("/")
def root():
    return {"status": "ok", "message": "Social Manager API"}


# TODO: Andrea/Filippo - Integrare LangChain e OpenAI/Gemini per generazione reale
class GenerateRequest(BaseModel):
    prompt: str
    social_target: str = "linkedin"


class GenerateResponse(BaseModel):
    generated_text: str
    timestamp: datetime


@app.post("/generate", response_model=GenerateResponse)
def generate_content(request: GenerateRequest):
    """
    Endpoint mock per generazione contenuti AI.
    Restituisce testo finto per sbloccare il Frontend.
    """
    # TODO: Sostituire con chiamata vera a LangChain/OpenAI
    mock_text = f"[MOCK] Post generato per {request.social_target} basato su: {request.prompt[:50]}..."
    return GenerateResponse(
        generated_text=mock_text,
        timestamp=datetime.now()
    )


app.include_router(api_router, prefix="/api")
