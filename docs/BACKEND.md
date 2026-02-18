# Backend Architecture

## Overview

Backend is organized around three main layers:

### 1. **Controllers/Routes** (`backend/app/routes.py`)
FastAPI endpoints that handle HTTP requests.

### 2. **Business Logic** (`backend/ai/`, `backend/dao/`)
- `ai/`: Content generation using Gemini AI
- `dao/`: Data Access Objects for MongoDB operations

### 3. **Infrastructure** (`backend/database/`, `backend/schemas/`)
- `database/`: MongoDB connection management
- `schemas/`: Pydantic models for validation

## Directory Structure

```
backend/
├── main.py                   # FastAPI app entry point
├── ai/
│   ├── __init__.py
│   ├── gemini_config.py      # Gemini API configuration
│   ├── generator.py          # Post generation logic
│   └── prompts.py            # System prompts & tones
├── app/
│   ├── __init__.py
│   └── routes.py             # API endpoints
├── dao/
│   ├── __init__.py
│   ├── base_dao.py           # Base MongoDB operations
│   └── post_dao.py           # Post-specific operations
├── database/
│   ├── __init__.py
│   └── connection.py         # MongoDB connection
└── schemas/
    ├── __init__.py
    └── post.py               # Pydantic models
```

## Data Flow

```
Request → routes.py → dao/post_dao.py → database/connection.py → MongoDB
                    ↓
                  ai/generator.py → Gemini API
```

## Key Patterns

### DAO Pattern
Base class `BaseDAO` provides CRUD operations:
```python
await base_dao.insert_one({"title": "Test"})
await base_dao.find_many({"status": "draft"})
await base_dao.update_one({"_id": id}, {"status": "published"})
await base_dao.delete_one({"_id": id})
```

### AI Generation
Prompts are defined in `prompts.py` with tone variations:
```python
TONES = {
    "professionale": "...",
    "informativo": "...",
    "ispirazionale": "...",
}
```

## Configuration

Environment variables (`.env`):
```env
MONGO_URI=mongodb://localhost:27017
MONGO_DB=socialmanager
GEMINI_API_KEY=sk-xxx
```

## Testing

Run backend tests:
```bash
python tests/verify_mongodb.py      # MongoDB connection test
python tests/test_gemini.py         # Gemini API test
```
