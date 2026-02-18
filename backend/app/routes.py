from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.app.richieste import RichiesteClient


router = APIRouter()


class InstagramMediaPayload(BaseModel):
    url_risorsa: str
    caption: str
    user_id: str
    creation_id: str


def _raise_service_error() -> None:
    raise HTTPException(
        status_code=503,
        detail="Si e verificato un errore all'interno del server, riprova piu tardi",
    )


@router.get("/")
@router.get("/profile")
def retrieve_profile():
    result = RichiesteClient.retrieve_user()
    if not result:
        _raise_service_error()
    return result


@router.post("/createPost")
def create_draft(payload: InstagramMediaPayload):
    result = RichiesteClient.create_media(
        payload.url_risorsa,
        payload.caption,
        payload.user_id,
    )
    if not result:
        _raise_service_error()
    return result


@router.post("/PostMedia")
def post_media(payload: InstagramMediaPayload):
    result = RichiesteClient.publish_media(payload.user_id, payload.creation_id)
    if not result:
        _raise_service_error()
    return result

