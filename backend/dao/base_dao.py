"""
Base DAO (Data Access Object)
Issue #16, #20: Creazione DAO e struttura CRUD

Questa classe base fornisce metodi CRUD generici per tutte le entità.
Ogni DAO specifico estende questa classe.
"""

from typing import TypeVar, Generic, List, Dict, Any, Optional
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from datetime import datetime

T = TypeVar('T')


class BaseDAO(Generic[T]):
    """
    DAO base con operazioni CRUD
    
    Issue #20: Definire struttura DAO per gestione dati
    TODO:
    - Aggiungere validazione con Pydantic
    - Implementare paginazione
    - Aggiungere cache per query frequenti
    - Logging operazioni
    """
    
    def __init__(self, collection: AsyncIOMotorCollection):
        """
        Inizializza DAO con collection MongoDB
        
        Args:
            collection: Collection MongoDB
        """-
        self.collection = collection
    
    
    # Issue #21: Implementare metodi per inserire documenti
    async def insert_one(self, document: Dict[str, Any]) -> str:
        """
        Inserisce un nuovo documento
        
        Args:
            document: Documento da inserire
            
        Returns:
            str: ID del documento inserito
            
        TODO:
        - Validare documento prima di inserire
        - Aggiungere timestamp automatici (created_at)
        - Gestire duplicati
        """
        if "created_at" not in document:
            document["created_at"] = datetime.utcnow()
        
        result = await self.collection.insert_one(document)
        return str(result.inserted_id)
    
    
    async def insert_many(self, documents: List[Dict[str, Any]]) -> List[str]:
        """
        Inserisce multipli documenti
        
        Args:
            documents: Lista di documenti
            
        Returns:
            List[str]: Lista di ID inseriti
            
        TODO:
        - Batch insert ottimizzato
        - Rollback in caso di errori parziali
        """
        for doc in documents:
            if "created_at" not in doc:
                doc["created_at"] = datetime.utcnow()
        
        result = await self.collection.insert_many(documents)
        return [str(id) for id in result.inserted_ids]
    
    
    # Issue #22: Implementare metodi per leggere documenti (filtri, query)
    async def find_one(self, filter_query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Trova un documento
        
        Args:
            filter_query: Filtro MongoDB
            
        Returns:
            Optional[Dict]: Documento trovato o None
            
        TODO:
        - Convertire _id in string
        - Proiezione campi
        - Cache risultati
        """
        document = await self.collection.find_one(filter_query)
        if document and "_id" in document:
            document["_id"] = str(document["_id"])
        return document
    
    
    async def find_by_id(self, document_id: str) -> Optional[Dict[str, Any]]:
        """
        Trova documento per ID
        
        Args:
            document_id: ID del documento
            
        Returns:
            Optional[Dict]: Documento o None
        """
        try:
            obj_id = ObjectId(document_id)
            return await self.find_one({"_id": obj_id})
        except Exception as e:
            print(f"Errore conversione ID: {e}")
            return None
    
    
    async def find_many(
        self, 
        filter_query: Dict[str, Any] = None,
        limit: int = 100,
        skip: int = 0,
        sort: List[tuple] = None
    ) -> List[Dict[str, Any]]:
        """
        Trova multipli documenti con filtri
        
        Args:
            filter_query: Filtro MongoDB
            limit: Limite risultati
            skip: Skip risultati (paginazione)
            sort: Ordinamento [(campo, direzione), ...]
            
        Returns:
            List[Dict]: Lista documenti
            
        TODO:
        - Implementare paginazione cursor-based
        - Aggiungere aggregation pipeline
        - Full-text search
        """
        if filter_query is None:
            filter_query = {}
        
        cursor = self.collection.find(filter_query).limit(limit).skip(skip)
        
        if sort:
            cursor = cursor.sort(sort)
        
        documents = await cursor.to_list(length=limit)
        
        # Converti ObjectId in string
        for doc in documents:
            if "_id" in doc:
                doc["_id"] = str(doc["_id"])
        
        return documents
    
    
    async def count(self, filter_query: Dict[str, Any] = None) -> int:
        """
        Conta documenti che matchano filtro
        
        Args:
            filter_query: Filtro MongoDB
            
        Returns:
            int: Numero documenti
        """
        if filter_query is None:
            filter_query = {}
        
        return await self.collection.count_documents(filter_query)
    
    
    # Issue #23: Implementare metodi per aggiornare documenti esistenti
    async def update_one(
        self, 
        filter_query: Dict[str, Any], 
        update_data: Dict[str, Any]
    ) -> bool:
        """
        Aggiorna un documento
        
        Args:
            filter_query: Filtro per trovare documento
            update_data: Dati da aggiornare
            
        Returns:
            bool: True se aggiornato, False altrimenti
            
        TODO:
        - Aggiungere updated_at automatico
        - Validare update_data
        - Versioning dei documenti
        """
        update_data["updated_at"] = datetime.utcnow()
        
        result = await self.collection.update_one(
            filter_query,
            {"$set": update_data}
        )
        
        return result.modified_count > 0
    
    
    async def update_by_id(self, document_id: str, update_data: Dict[str, Any]) -> bool:
        """
        Aggiorna documento per ID
        
        Args:
            document_id: ID documento
            update_data: Dati da aggiornare
            
        Returns:
            bool: True se aggiornato
        """
        try:
            obj_id = ObjectId(document_id)
            return await self.update_one({"_id": obj_id}, update_data)
        except Exception as e:
            print(f"Errore aggiornamento: {e}")
            return False
    
    
    async def update_many(
        self, 
        filter_query: Dict[str, Any], 
        update_data: Dict[str, Any]
    ) -> int:
        """
        Aggiorna multipli documenti
        
        Args:
            filter_query: Filtro
            update_data: Dati da aggiornare
            
        Returns:
            int: Numero documenti aggiornati
        """
        update_data["updated_at"] = datetime.utcnow()
        
        result = await self.collection.update_many(
            filter_query,
            {"$set": update_data}
        )
        
        return result.modified_count
    
    
    # Issue #24, #25: Implementare metodi per cancellare documenti
    async def delete_one(self, filter_query: Dict[str, Any]) -> bool:
        """
        Cancella un documento
        
        Args:
            filter_query: Filtro
            
        Returns:
            bool: True se cancellato
            
        TODO:
        - Soft delete (flag deleted_at invece di rimozione)
        - Backup prima di cancellare
        - Cascade delete per relazioni
        """
        result = await self.collection.delete_one(filter_query)
        return result.deleted_count > 0
    
    
    async def delete_by_id(self, document_id: str) -> bool:
        """
        Cancella documento per ID
        
        Args:
            document_id: ID documento
            
        Returns:
            bool: True se cancellato
        """
        try:
            obj_id = ObjectId(document_id)
            return await self.delete_one({"_id": obj_id})
        except Exception as e:
            print(f"Errore cancellazione: {e}")
            return False
    
    
    async def delete_many(self, filter_query: Dict[str, Any]) -> int:
        """
        Cancella multipli documenti
        
        Args:
            filter_query: Filtro
            
        Returns:
            int: Numero documenti cancellati
            
        TODO:
        - Conferma utente per cancellazioni massive
        - Log audit di cancellazioni
        """
        result = await self.collection.delete_many(filter_query)
        return result.deleted_count
    
    
    # Utility methods
    async def exists(self, filter_query: Dict[str, Any]) -> bool:
        """
        Verifica se esiste documento che matcha filtro
        
        Args:
            filter_query: Filtro
            
        Returns:
            bool: True se esiste
        """
        count = await self.collection.count_documents(filter_query, limit=1)
        return count > 0
