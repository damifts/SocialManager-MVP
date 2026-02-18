"""
Script di verifica installazione e connessione MongoDB
Issue #11, #19: Verificare installazione MongoDB locale e connessione

Esegui questo script per testare:
- MongoDB installato e in esecuzione
- Connessione dal progetto Python
- Permessi lettura/scrittura
- Performance base

Usage:
    python verify_mongodb.py
"""

import asyncio
import sys
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError


async def verify_mongodb():
    """
    Verifica completa MongoDB
    """
    print("=" * 60)
    print("🔍 VERIFICA MONGODB - Social Manager MVP")
    print("=" * 60)
    print()
    
    # Test 1: Connessione
    print("📡 Test 1: Connessione MongoDB...")
    try:
        client = AsyncIOMotorClient(
            "mongodb://localhost:27017",
            serverSelectionTimeoutMS=5000
        )
        
        # Ping database
        await client.admin.command('ping')
        print("   ✅ Connessione OK!")
        
    except ConnectionFailure:
        print("   ❌ ERRORE: Impossibile connettersi a MongoDB")
        print("   💡 Verifica che MongoDB sia in esecuzione:")
        print("      Windows: Controlla servizio MongoDB in Task Manager")
        print("      Mac: brew services start mongodb-community")
        print("      Linux: sudo systemctl start mongod")
        return False
    except ServerSelectionTimeoutError:
        print("   ❌ ERRORE: Timeout connessione")
        print("   💡 MongoDB potrebbe non essere in ascolto su localhost:27017")
        return False
    except Exception as e:
        print(f"   ❌ ERRORE: {e}")
        return False
    
    print()
    
    # Test 2: Info server
    print("ℹ️  Test 2: Informazioni Server...")
    try:
        server_info = await client.server_info()
        print(f"   ✅ Versione MongoDB: {server_info.get('version')}")
        print(f"   ✅ Sistema: {server_info.get('os', {}).get('type')}")
    except Exception as e:
        print(f"   ⚠️  Impossibile ottenere info server: {e}")
    
    print()
    
    # Test 3: Database test
    print("💾 Test 3: Operazioni Database...")
    try:
        # Crea database di test
        db = client["test_social_manager"]
        test_collection = db["test_posts"]
        
        # Insert test
        print("   - Test INSERT...")
        test_doc = {
            "testo": "Post di test",
            "social": "linkedin",
            "created_at": datetime.utcnow()
        }
        result = await test_collection.insert_one(test_doc)
        inserted_id = result.inserted_id
        print(f"   ✅ Documento inserito: {inserted_id}")
        
        # Read test
        print("   - Test READ...")
        found_doc = await test_collection.find_one({"_id": inserted_id})
        if found_doc:
            print(f"   ✅ Documento letto: {found_doc['testo']}")
        
        # Update test
        print("   - Test UPDATE...")
        await test_collection.update_one(
            {"_id": inserted_id},
            {"$set": {"testo": "Post aggiornato"}}
        )
        updated_doc = await test_collection.find_one({"_id": inserted_id})
        print(f"   ✅ Documento aggiornato: {updated_doc['testo']}")
        
        # Delete test
        print("   - Test DELETE...")
        await test_collection.delete_one({"_id": inserted_id})
        deleted_doc = await test_collection.find_one({"_id": inserted_id})
        if deleted_doc is None:
            print("   ✅ Documento eliminato")
        
        # Cleanup
        await db.drop_collection("test_posts")
        print("   ✅ Tutti i test CRUD completati!")
        
    except Exception as e:
        print(f"   ❌ ERRORE operazioni database: {e}")
        return False
    
    print()
    
    # Test 4: Collections esistenti
    print("📋 Test 4: Database Structure...")
    try:
        # Database principale
        main_db = client["social_manager_db"]
        collections = await main_db.list_collection_names()
        
        if collections:
            print(f"   ✅ Collections esistenti: {', '.join(collections)}")
        else:
            print("   ℹ️  Nessuna collection ancora (normale per prima installazione)")
        
    except Exception as e:
        print(f"   ⚠️  Impossibile listare collections: {e}")
    
    print()
    
    # Test 5: Performance
    print("⚡ Test 5: Performance Base...")
    try:
        import time
        db = client["social_manager_db"]
        test_collection = db["performance_test"]
        
        # Insert performance
        start = time.time()
        docs = [{"index": i, "data": "test"} for i in range(100)]
        await test_collection.insert_many(docs)
        insert_time = (time.time() - start) * 1000
        
        # Read performance
        start = time.time()
        cursor = test_collection.find().limit(100)
        await cursor.to_list(length=100)
        read_time = (time.time() - start) * 1000
        
        print(f"   ✅ INSERT 100 docs: {insert_time:.2f}ms")
        print(f"   ✅ READ 100 docs: {read_time:.2f}ms")
        
        # Cleanup
        await db.drop_collection("performance_test")
        
    except Exception as e:
        print(f"   ⚠️  Test performance fallito: {e}")
    
    print()
    print("=" * 60)
    print("✅ VERIFICA COMPLETATA - MongoDB pronto per l'uso!")
    print("=" * 60)
    print()
    print("📝 Prossimi step:")
    print("   1. Configura MONGO_URI nel file .env")
    print("   2. Avvia app Streamlit: streamlit run app.py")
    print("   3. Inizia a sviluppare! 🚀")
    print()
    
    client.close()
    return True


if __name__ == "__main__":
    print()
    success = asyncio.run(verify_mongodb())
    
    if not success:
        print()
        print("🔗 Risorse utili:")
        print("   - Install MongoDB: https://www.mongodb.com/try/download/community")
        print("   - Docs MongoDB: https://www.mongodb.com/docs/")
        print("   - Docs Motor (Python): https://motor.readthedocs.io/")
        print()
        sys.exit(1)
    
    sys.exit(0)
