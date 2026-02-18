# Contributing

Grazie per il contributo al Social Manager MVP!

## 🚀 Setup Iniziale

### Per Team Members (Setup Rapido)

```powershell
# Windows PowerShell
.\setup.ps1

# Avvio applicazione
.\start.ps1

# Oppure Windows CMD
setup.bat
start.bat

# Oppure Mac/Linux
bash setup.sh
bash start.sh
```

Leggi **[QUICKSTART.md](QUICKSTART.md)** per guida dettagliata.

### Per Developers (Setup Manuale)

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux: .venv\Scripts\activate (Windows)
pip install -r requirements-base.txt
```

---

## Flusso di lavoro Git

1. **Crea un branch dedicato** dalla `main`:
   ```bash
   git checkout -b feat/nome-feature
   # oppure
   git checkout -b fix/nome-bug
   ```

2. **Descrivi chiaramente lo scopo** nella PR con:
   - Cosa fa la feature/fix
   - Perché è necessaria
   - Eventuali dipendenze aggiunte

3. **Aggiorna la documentazione** se tocchi:
   - Dipendenze (vedi `DEPENDENCIES.md`)
   - Setup o configurazione
   - API o interfacce pubbliche

## Naming Convention Branch

- `feat/...` - Nuove feature
- `fix/...` - Bug fix
- `refactor/...` - Refactoring senza cambio funzionalità
- `docs/...` - Solo documentazione
- `chore/...` - Task di manutenzione

## Dipendenze

- Segui le regole in `DEPENDENCIES.md`
- **IMPORTANTE**: Per le icone usa SOLO `lucide-react` (installato di default)
- Riporta in PR la motivazione della nuova libreria

## Convenzioni Codice

### Backend (Python)
- Usa type hints dove possibile
- Segui PEP 8 per lo style
- Commenta con `# TODO: Nome - Descrizione` per task futuri
- Schema Pydantic per tutti i modelli dati

### Frontend (TypeScript)
- Usa TypeScript strict mode
- Componenti in `components/` con naming PascalCase
- Utilities in `lib/` con naming camelCase
- Icone: usa solo `lucide-react`
- Commenta con `// TODO: Nome - Descrizione`

## Struttura Cartelle

```
app.py              # Streamlit main app
requirements.txt    # Puntatore a requirements-base.txt
requirements-base.txt  # Dipendenze base
requirements-full.txt  # Extras opzionali
.streamlit/
  config.toml       # Config Streamlit
backend/
  schemas/          # Modelli Pydantic
  app/              # Logica business (opzionale)
pages/              # Streamlit multi-page (se serve)
```

## Testing

- Python: test con `pytest` (da configurare)
- Streamlit: test con `streamlit-testing` library
- Segnala in PR se hai aggiunto test

## Review Process

- Almeno 1 approvazione richiesta per merge
- I reviewer controllano:
  - Coerenza con architettura
  - Dipendenze giustificate
  - Documentazione aggiornata
  - TODO assegnati se necessario

## Domande?

Vedi la **[Documentazione Completa](README.md#-documentazione-progetto)**:
- [QUICKSTART.md](QUICKSTART.md) - Guida rapida per team members
- [docs/API.md](docs/API.md) - API Backend
- [docs/BACKEND.md](docs/BACKEND.md) - Architettura backend
- [docs/DATABASE.md](docs/DATABASE.md) - Database schema
- [scripts/README.md](scripts/README.md) - DevOps & webhooks

O apri una issue nel repository!
