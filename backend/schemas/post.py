from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    """Schema base per un Post social."""
    testo: str = Field(..., min_length=1, max_length=3000, description="Contenuto del post")
    social_target: str = Field(..., description="Piattaforma target (linkedin, twitter, etc.)")
    data_programmazione: Optional[datetime] = Field(None, description="Data/ora programmazione")


class PostCreate(PostBase):
    """Schema per creazione nuovo post."""
    pass


class Post(PostBase):
    """Schema completo post con metadata."""
    id: str
    created_at: datetime
    status: str = "draft"  # draft, scheduled, published
    
    class Config:
        from_attributes = True


# TODO: Danilo - Aggiungere campi per analytics (engagement, reach, etc.)
class PostAnalytics(BaseModel):
    """Schema per metriche post pubblicato."""
    post_id: str
    views: int = 0
    likes: int = 0
    comments: int = 0
    shares: int = 0
