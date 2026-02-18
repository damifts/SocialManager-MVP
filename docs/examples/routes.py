from fastapi import APIRouter
from richieste import *
from pydantic import BaseModel


router = APIRouter()


class instagramDataInterface(BaseModel):
    url_risorsa: str
    caption: str
    user_id: str
    creation_id: str


@router.get("/")
def retrive_profile():
    return retriveUserReq()


@router.post("/createPost")
def create_draft(dati : instagramDataInterface):
    ric = CreateMediaReq(dati.url_risorsa,dati.caption,dati.user_id)
    return ric
    

@router.post("/PostMedia")
def postMedia(dati: instagramDataInterface):
    ric = PostMediaReq(dati.user_id, dati.creation_id)
    return ric

