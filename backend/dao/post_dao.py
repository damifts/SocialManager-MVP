"""
Post DAO - Data Access Object per gestione Post
Issue #16, #20-25: Implementazione CRUD per Post

Estende BaseDAO con metodi specifici per Post
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from .base_dao import BaseDAO
from ..database import get_database


class PostDAO(BaseDAO):
    """
    DAO per gestione Post social
    
    TODO: Team Backend
    - Implementare ricerca per social_target
    - Filtrare per status (draft, scheduled, published)
    - Query per date range (calendario)
    - Aggregazioni per analytics
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
        social_target: str,
        data_programmazione: Optional[datetime] = None,
        status: str = "draft"
    ) -> str:
        """
        Issue #21: Crea nuovo post
        
        Args:
            testo: Contenuto del post
            social_target: Social network target (LinkedIn, Twitter, etc.)
            data_programmazione: Data pubblicazione programmata
            status: draft, scheduled, published
            
        Returns:
            str: ID del post creato
            
        TODO:
        - Validare testo (lunghezza per social)
        - Validare social_target (enum)
        - Generare preview automatica
        """
        post_data = {
            "testo": testo,
            "social_target": social_target,
            "status": status,
            "created_at": datetime.utcnow()
        }
        
        if data_programmazione:
            post_data["data_programmazione"] = data_programmazione
        
        return await self.insert_one(post_data)
    
    
    async def get_posts_by_social(self, social_target: str) -> List[Dict[str, Any]]:
        """
        Issue #22: Trova post per social network
        
        Args:
            social_target: Social network
            
        Returns:
            List[Dict]: Lista post
        """
        return await self.find_many(
            filter_query={"social_target": social_target},
            sort=[("created_at", -1)]  # Più recenti prima
        )
    
    
    async def get_posts_by_status(self, status: str) -> List[Dict[str, Any]]:
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
            
        TODO: Implementare per calendario editoriale (issue #7, #8)
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
        """
        Issue #23: Pubblica post (cambia status e imposta published_at)
        
        Args:
            post_id: ID post
            
        Returns:
            bool: True se pubblicato
            
        TODO:
        - Integrare con API social network
        - Notificare utente
        - Log pubblicazione
        """
        return await self.update_by_id(
            post_id,
            {
                "status": "published",
                "published_at": datetime.utcnow()
            }
        )
    
    
    async def search_posts(self, search_text: str) -> List[Dict[str, Any]]:
        """
        Issue #22: Ricerca full-text nei post
        
        Args:
            search_text: Testo da cercare
            
        Returns:
            List[Dict]: Post trovati
            
        TODO:
        - Creare text index su MongoDB
        - Ottimizzare per performance
        """
        # Ricerca semplice con regex (TODO: usare text index)
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
            
        TODO: Implementare per dashboard analytics (issue #8)
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
