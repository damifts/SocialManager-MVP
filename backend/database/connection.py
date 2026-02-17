"""
MongoDB Connection Manager
Issue #18, #19: Creare e verificare connessione MongoDB

TODO: Team Backend
- Installare MongoDB localmente (issue #11)
- Configurare variabili env (MONGO_URI, MONGO_DB_NAME)
- Testare connessione con script verify_mongodb.py
"""

import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Configurazione MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "social_manager_db")

# Client globale MongoDB
_mongo_client: AsyncIOMotorClient | None = None
_database = None


async def connect_to_mongodb():
    """
    Stabilisce connessione con MongoDB
    
    Issue #18: Implementazione connessione
    TODO: 
    - Gestire autenticazione se MongoDB richiede credenziali
    - Configurare pool di connessioni
    - Aggiungere retry logic
    """
    global _mongo_client, _database
    
    try:
        _mongo_client = AsyncIOMotorClient(
            MONGO_URI,
            serverSelectionTimeoutMS=5000,
            maxPoolSize=10,
            minPoolSize=1
        )
        
        # Issue #19: Test connessione con ping
        await _mongo_client.admin.command('ping')
        
        _database = _mongo_client[MONGO_DB_NAME]
        print(f"✅ Connesso a MongoDB: {MONGO_DB_NAME}")
        
        return _database
        
    except ConnectionFailure as e:
        print(f"❌ Errore connessione MongoDB: {e}")
        print("💡 Verificare che MongoDB sia in esecuzione (issue #11)")
        raise
    except Exception as e:
        print(f"❌ Errore generico MongoDB: {e}")
        raise


async def close_mongodb_connection():
    """
    Chiude connessione MongoDB
    """
    global _mongo_client
    if _mongo_client:
        _mongo_client.close()
        print("✅ Connessione MongoDB chiusa")


def get_database():
    """
    Restituisce database MongoDB corrente
    
    Returns:
        Database MongoDB instance
    
    Raises:
        RuntimeError: Se database non è connesso
    """
    if _database is None:
        raise RuntimeError("Database non connesso. Chiamare connect_to_mongodb() prima.")
    return _database


async def verify_connection() -> bool:
    """
    Issue #19: Verifica connessione con ping e query semplice
    
    Returns:
        bool: True se connessione OK, False altrimenti
    
    TODO:
    - Testare latency connessione
    - Verificare permessi utente
    - Controllare spazio disponibile
    """
    try:
        db = get_database()
        
        # Ping test
        await db.client.admin.command('ping')
        
        # Query semplice test
        collections = await db.list_collection_names()
        print(f"✅ Connessione OK. Collections: {collections}")
        
        return True
        
    except Exception as e:
        print(f"❌ Verifica connessione fallita: {e}")
        return False


# Utility per uso in Streamlit (sincrono)
def get_database_sync():
    """
    Versione sincrona per compatibilità Streamlit
    
    TODO: Valutare se usare motor o pymongo sincrono per Streamlit
    """
    return _database
