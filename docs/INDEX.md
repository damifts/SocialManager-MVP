# Documentation Index

Central documentation hub for Social Manager MVP.

## Main Guides

### [README.md](../README.md) - Start Here! 🚀
Complete guide with:
- Quick start (setup scripts - 60 seconds)
- Setup automatizzato for team members
- Architecture overview
- Full configuration instructions
- Team responsibilities
- Troubleshooting
- Development guidelines

### [QUICKSTART.md](../QUICKSTART.md) - For Team Members ⚡
Simplified getting-started guide:
- How to run setup scripts
- What each script does
- Troubleshooting common issues
- No terminal experience needed!

### [CONTRIBUTING.md](../CONTRIBUTING.md)
Contribution guidelines for developers.

---

## Setup & Automation

### Setup Scripts

For automated environment setup across all platforms:
- **[setup.ps1](../setup.ps1)** - Windows PowerShell
- **[setup.bat](../setup.bat)** - Windows CMD
- **[setup.sh](../setup.sh)** - Mac/Linux Bash

Start scripts:
- **[start.ps1](../start.ps1)** - Windows PowerShell
- **[start.bat](../start.bat)** - Windows CMD
- **[start.sh](../start.sh)** - Mac/Linux Bash

See [QUICKSTART.md](../QUICKSTART.md) for usage.

### DevOps

- **[scripts/README.md](../scripts/README.md)** - Automation utilities
  - Webhook testing scripts
  - Integration testing
  - Development tools

---

## Technical Documentation

### Backend

- **[BACKEND.md](./BACKEND.md)** - Backend architecture and patterns
  - Directory structure
  - Data flow
  - DAO pattern
  - Configuration

- **[API.md](./API.md)** - API reference
  - Endpoints
  - Swagger docs location
  - Pydantic models

- **[DATABASE.md](./DATABASE.md)** - Database schema
  - Collections structure
  - Indexes
  - Querying examples
  - Migrations

### Testing

- **[tests/README.md](../tests/README.md)** - Test suite documentation
  - `verify_mongodb.py` - MongoDB connection test
  - `test_gemini.py` - Gemini API test
  - Future test structure

### Reference Code

- **[examples/](./examples/)** - Reference implementations
  - Backend exploration files
  - Use as learning reference only

---

## Quick Links

| Task | Reference |
|------|-----------|
| Setup project | [README.md - Quick Start](../README.md#quick-start) |
| Configure services | [README.md - Setup](../README.md#setup-completo) |
| Understand backend | [BACKEND.md](./BACKEND.md) |
| Query database | [DATABASE.md](./DATABASE.md) |
| Call APIs | [API.md](./API.md) |
| Run tests | [tests/README.md](../tests/README.md) |
| Add feature | [CONTRIBUTING.md](../CONTRIBUTING.md) |

---

## Project Structure

```
SocialManager-MVP/
├── README.md                    ← Start here
├── CONTRIBUTING.md              ← Contribution guidelines
├── requirements.txt             ← Puntatore a requirements-base.txt
├── requirements-base.txt        ← Dipendenze base
├── requirements-full.txt        ← Extras opzionali
├── .env.example                 ← Environment template
├── app.py                       ← Streamlit main app
├── backend/                     ← FastAPI backend
│   ├── main.py
│   ├── ai/                      ← AI/Gemini integration
│   ├── app/                     ← API routes
│   ├── dao/                     ← Data access objects
│   ├── database/                ← DB connection
│   └── schemas/                 ← Pydantic models
├── tests/                       ← Test suite
│   ├── test_gemini.py
│   └── verify_mongodb.py
└── docs/                        ← This documentation
    ├── API.md
    ├── BACKEND.md
    ├── DATABASE.md
    ├── INDEX.md                 ← You are here
    └── examples/                ← Reference code
```

---

## Support & Next Steps

1. **First time?** → Read [README.md](../README.md)
2. **Setting up?** → Follow "Setup Completo" in README
3. **Developing?** → Check [BACKEND.md](./BACKEND.md) + [CONTRIBUTING.md](../CONTRIBUTING.md)
4. **Debugging?** → See [README.md - Troubleshooting](../README.md#troubleshooting)

---

*Last Updated: Feb 18, 2026*
