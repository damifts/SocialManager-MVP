# API Reference

## Base URL

```
http://localhost:8000
```

## Endpoints

### Documented Routes

See [backend/app/routes.py](../backend/app/routes.py) for current implementation.

## Swagger UI

Interactive API documentation available at:

```
http://localhost:8000/docs
```

## Pydantic Models

### PostCreate

Located in [backend/schemas/post.py](../backend/schemas/post.py)

```python
class PostCreate(BaseModel):
    title: str
    content: str
    social_targets: List[str]  # ["LinkedIn", "Instagram", "Twitter"]
    tone: str  # "Professionale", "Ispirazionale", etc.
    scheduled_at: Optional[datetime] = None
```

## Development

API starts with:

```bash
python -m uvicorn main:app --reload --app-dir backend --port 8000
```
