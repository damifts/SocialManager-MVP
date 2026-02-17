# Contributing

Grazie per il contributo al Social Manager MVP!

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
requirements.txt    # Dipendenze Python
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

Apri una issue o chiedi nel canale del team!
