from fastapi import FastAPI
from routes import *


app = FastAPI()


app.include_router(
    router,
    prefix="/users",
    tags=["Utente"]
)

