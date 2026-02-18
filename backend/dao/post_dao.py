"""
Post DAO - Data Access Object per gestione Post
Issue #16, #20-25: Implementazione CRUD per Post

Estende BaseDAO con metodi specifici per Post
"""

from typing import List, Dict, Any, Optional,TypedDict
from datetime import datetime
from .base_dao import BaseDAO
from ..database import get_database
from enum import Enum
class PostStatus(str, Enum):
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    FAILED = "failed"
class PostMetadata(TypedDict):
    views: int
    likes: int
    comments: int
    shares: int
class mediaPost:
        _id: str
        title: str
        content: str
        social_targets: str  
        status: PostStatus    
        created_at: datetime
        scheduled_at: datetime
        published_at: datetime
        metadata: PostMetadata
class PostDAO(BaseDAO):
    """
    DAO per gestione Post social
    

    """
    
    def __init__(self):
        """
        Inizializza PostDAO con collection 'posts'
        """
        db = get_database()
        super().__init__(db["posts"])
    
    
    async def create_post(
        self, 
        testo: str, 
        data_programmazione: Optional[datetime] = None,
        status: PostStatus = PostStatus.DRAFT
    ) -> str:
        """Issue #21: Crea nuovo post con validazione Instagram"""
        
        # 1. Validazioni
        if not testo or not testo.strip():
            raise ValueError("Il contenuto del post non può essere vuoto")
        
        if len(testo) >= 2200:
            raise ValueError("Testo troppo lungo per Instagram (Max 2200 caratteri)")

        # 2. Generazione Preview (Logica corretta)
        def genera_preview(t: str, length: int = 50) -> str:
            return t[:length] + "..." if len(t) > length else t

        # 3. Preparazione Dati
        # Usiamo utcnow() per consistenza del database
        post_data = {
            "title": genera_preview(testo, 30), # Usiamo la preview come titolo se manca
            "content": testo,
            "status": status,
            "metadata": { # Inizializziamo i metadati a zero
                "views": 0, "likes": 0, "comments": 0, "shares": 0
            },
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        
        # 4. Logica Programmazione
        if data_programmazione:
            post_data["scheduled_at"] = data_programmazione
            # Se c'è una data, lo stato diventa automaticamente SCHEDULED
            if status == PostStatus.DRAFT:
                post_data["status"] = PostStatus.SCHEDULED
        
        return await self.insert_one(post_data)
    
    """async def get_posts_by_social(self, social_target: str) -> List[Dict[str, Any]]:
  
        Issue #22: Trova post per social network
        
        Args:
            social_target: Social network
            
        Returns:
            List[Dict]: Lista post
        """"""
        return await self.find_many(
            filter_query={"social_target": social_target},
            sort=[("created_at", -1)]  # Più recenti prima
        )"""
    
    
    async def get_posts_by_status(self, status: PostStatus) -> List[Dict[str, Any]]:
        """
        Issue #22: Trova post per status
        
        Args:
            status: draft, scheduled, published
            
        Returns:
            List[Dict]: Lista post
        """
        return await self.find_many(
            filter_query={"status": status},
            sort=[("created_at", -1)]
        )
    
    
    async def get_scheduled_posts(
        self, 
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict[str, Any]]:
        """
        Issue #22: Trova post programmati in range date
        
        Args:
            start_date: Data inizio
            end_date: Data fine
            
        Returns:
            List[Dict]: Post programmati
            

        """
        filter_query = {"status": "scheduled"}
        
        if start_date or end_date:
            date_filter = {}
            if start_date:
                date_filter["$gte"] = start_date
            if end_date:
                date_filter["$lte"] = end_date
            
            filter_query["data_programmazione"] = date_filter
        
        return await self.find_many(
            filter_query=filter_query,
            sort=[("data_programmazione", 1)]  # Ordine cronologico
        )
    
    
    async def update_post_status(self, post_id: str, new_status: str) -> bool:
        """
        Issue #23: Aggiorna status post
        
        Args:
            post_id: ID post
            new_status: Nuovo status
            
        Returns:
            bool: True se aggiornato
        """
        return await self.update_by_id(
            post_id,
            {"status": new_status}
        )
    
    
    async def publish_post(self, post_id: str) -> bool:
        """Issue #23: Pubblica post e aggiorna timestamp"""
        return await self.update_by_id(
            post_id,
            {
                "status": PostStatus.PUBLISHED,
                "published_at": datetime.now()
            }
        )
    
    
    async def search_posts(self, search_text: str) -> List[Dict[str, Any]]:
        """
        Issue #22: Ricerca full-text nei post
        
        Args:
            search_text: Testo da cercare
            
        Returns:
            List[Dict]: Post trovati
            

        """

        filter_query = {
            "testo": {"$regex": search_text, "$options": "i"}
        }
        
        return await self.find_many(filter_query)
    
    
    async def get_analytics_data(self, social_target: Optional[str] = None) -> Dict[str, Any]:
        """
        Aggregazione dati per analytics
        
        Args:
            social_target: Filtra per social (opzionale)
            
        Returns:
            Dict: Dati aggregati
            

        """
        match_stage = {}
        if social_target:
            match_stage = {"social_target": social_target}
        
        pipeline = [
            {"$match": match_stage},
            {"$group": {
                "_id": "$status",
                "count": {"$sum": 1}
            }}
        ]
        
        cursor = self.collection.aggregate(pipeline)
        results = await cursor.to_list(length=None)
        
        return {
            "by_status": results,
            "total": sum(r["count"] for r in results)
        }
