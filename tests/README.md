# Tests Directory

Test suite per Social Manager MVP.

## Setup Rapido

Per eseguire i test dopo il setup automatico:

```powershell
python tests/verify_mongodb.py
```

**Nota:** per test MongoDB/Gemini serve installare le extras:
`SM_FULL=1 .\setup.ps1` (oppure `pip install -r requirements-full.txt`).

---

## Test Files

### `verify_mongodb.py`
Verifica la connessione a MongoDB locale.

```bash
python tests/verify_mongodb.py
```

**Output atteso:**
```
✅ Connected! Status: {...}
```

### `test_gemini.py`
Testa l'integrazione con Gemini API.

```bash
python tests/test_gemini.py
```

**Prerequisiti:**
- `GEMINI_API_KEY` in `.env`

**Output atteso:**
```
✅ Working! Message: "Hello..."
```

## Running All Tests

```bash
# Verifica tutte le connessioni
python tests/verify_mongodb.py
python tests/test_gemini.py
```

## Future Test Structure

Quando il progetto cresce:
```
tests/
├── __init__.py
├── unit/
│   ├── test_dao.py
│   ├── test_generator.py
│   └── test_schemas.py
├── integration/
│   ├── test_mongodb_integration.py
│   └── test_gemini_integration.py
└── fixtures/
    └── sample_data.py
```
