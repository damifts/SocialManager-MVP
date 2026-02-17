from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/posts")
def list_posts():
    return {"items": []}
