from fastapi import APIRouter, HTTPException
from backend.app.richieste import richiesteClass
from pydantic import BaseModel


router = APIRouter()



class instagramDataInterface(BaseModel):
    url_risorsa: str
    caption: str
    user_id: str
    creation_id: str


@router.get("/")
def retrive_profile():
    ric = richiesteClass.retriveUserReq()
    if not ric:
        raise HTTPException(
            status_code=503,
            detail="Si è verificato un errore all'interno del server, riprova più tardi"
        )
    return ric



@router.post("/createPost")
def create_draft(dati : instagramDataInterface):
    ric = richiesteClass.CreateMediaReq(dati.url_risorsa,dati.caption,dati.user_id)
    if not ric:
        raise HTTPException(
            status_code=503,
            detail="Si è verificato un errore all'interno del server, riprova più tardi"
        )
    return ric
    
@router.post("/PostMedia")
def postMedia(dati: instagramDataInterface):
    ric = richiesteClass.PostMediaReq(dati.user_id, dati.creation_id)
    if not ric:
        raise HTTPException(
            status_code=503,
            detail="Si è verificato un errore all'interno del server, riprova più tardi"
        )
    return ric

