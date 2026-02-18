# Reference Implementations

Questa cartella contiene file di esplorazione e test creati dal team backend durante la fase di prototipazione.

Questi file **NON** fanno parte del production code, ma servono come **reference implementations** per:
- Testare integrazioni con MongoDB
- Testare Gemini API
- Esplorare architetture di routing
- Validare approcci di rischieste API

## Contenuto

| File | Scopo |
|------|-------|
| `connessione_MongoDP.py` | MongoDB connection exploration |
| `gemini.py` | Gemini API integration testing |
| `main.py` | FastAPI app exploration |
| `richieste.py` | API request examples |
| `routes.py` | Route definitions exploration |

## Utilizzo

Questi file possono essere usati come base per implementazioni ma **NON** devono essere usati direttamente in production.

Fare riferimento a:
- Production code: `backend/`
- Official implementations: `backend/database/`, `backend/ai/`, `backend/app/`

## Linea di Condotta

- ✅ Usare come learning reference
- ✅ Copiare pattern e strutture
- ❌ Non eseguire direttamente
- ❌ Non mergiare in production
