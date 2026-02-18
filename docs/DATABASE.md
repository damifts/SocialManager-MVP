# Database Schema

## Collections

### `posts`

Main collection for social media posts.

```javascript
{
  _id: ObjectId,
  title: String,
  content: String,
  social_targets: [String],        // ["LinkedIn", "Instagram", "Twitter"]
  tone: String,                     // "Professionale", "Ispirazionale", ...
  status: String,                   // "draft", "scheduled", "published"
  created_at: DateTime,
  scheduled_at: DateTime,
  published_at: DateTime,
  metadata: {
    views: Number,
    likes: Number,
    comments: Number,
    shares: Number
  }
}
```

## Indexes

For optimal performance:

```javascript
db.posts.createIndex({ "status": 1 })
db.posts.createIndex({ "scheduled_at": 1 })
db.posts.createIndex({ "social_targets": 1 })
db.posts.createIndex({ "created_at": -1 })
```

## Sample Data

```javascript
db.posts.insertOne({
  title: "Welcome to Social Manager",
  content: "Manage all your social media in one place",
  social_targets: ["LinkedIn", "Instagram"],
  tone: "Professionale",
  status: "draft",
  created_at: new Date(),
  metadata: {
    views: 0,
    likes: 0
  }
})
```

## Querying

### By Status
```python
await post_dao.find_many({"status": "draft"})
```

### By Date Range
```python
await post_dao.find_many({
    "created_at": {"$gte": start_date, "$lt": end_date}
})
```

### By Social Target
```python
await post_dao.find_many({
    "social_targets": "LinkedIn"
})
```

## Migrations

Future: Use Alembic or equivalent for schema migrations.

For now, manual schema management via MongoDB Compass or CLI.
