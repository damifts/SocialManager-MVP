# Prompt per Generazione Componenti AI

Usa questi prompt template con **v0.dev** o **Claude** per generare componenti coerenti con il progetto.

## 🎯 Prompt Generico Base

```
Crea un componente React/Next.js per Social Manager MVP con queste specifiche:

CONTESTO PROGETTO:
- Piattaforma per gestione contenuti social con AI
- Stack: Next.js 15, TypeScript, Tailwind CSS
- Design system: palette amber/brand principale, neutral per testi
- Icone: SOLO Lucide React (obbligatorio)

COMPONENTE DA CREARE:
[Descrivi qui il componente, es: "Dashboard analytics con grafici engagement"]

REQUISITI TECNICI:
- TypeScript strict
- "use client" se necessita interattività
- Tailwind con classi del design system (bg-brand-500, rounded-2xl, shadow-brand-lg)
- Import icone da 'lucide-react'
- Props type-safe
- Responsive (mobile-first)

STILE VISIVO:
- Bordi arrotondati (rounded-2xl per card)
- Ombre soffuse (shadow-brand-md)
- Palette: bg-neutral-50 per backgrounds, text-neutral-900 per testi
- Accent: brand-500 (amber) per bottoni/CTA
- Spacing generoso (p-6, gap-4)

ESEMPIO OUTPUT ATTESO:
File: components/NomeComponente.tsx con export default
```

## 📋 Prompt per Componenti Specifici

### Dashboard/Analytics
```
Crea un componente Dashboard per Social Manager MVP che mostri:
- 4 card metriche (views, likes, comments, shares)
- Grafico a linee per engagement settimanale
- Usa Lucide React per icone (Eye, Heart, MessageCircle, Share2)
- Palette: bg-neutral-50, card con bg-white, bordi rounded-2xl
- TypeScript + Tailwind
- Dati mock per ora
```

### Form/Editor
```
Crea PostEditor per Social Manager MVP con:
- Textarea per testo post
- Selector multi-piattaforma (LinkedIn, Twitter, Instagram)
- Date/time picker per programmazione
- Button "Genera con AI" (Sparkles icon da lucide-react)
- Validazione inline
- TypeScript + Tailwind design system
- State con React hooks
```

### Calendario
```
Crea Calendar component per Social Manager MVP che:
- Mostra mese corrente con post programmati
- Click su giorno per vedere dettagli
- Badge colorati per social (LinkedIn=blu, Twitter=azzurro, etc.)
- Navigazione mesi (ChevronLeft/Right da lucide-react)
- Responsive grid
- TypeScript + Tailwind con palette brand/neutral
```

### Lista/Tabella
```
Crea PostList component per Social Manager MVP:
- Tabella post con colonne: testo, social, data, status
- Filtri per social e status
- Actions (Edit, Delete con icone Pencil, Trash2 da lucide-react)
- Paginazione
- Empty state carino se nessun post
- TypeScript + Tailwind
```

### Modal/Dialog
```
Crea Modal component riutilizzabile per Social Manager MVP:
- Overlay backdrop con blur
- Card centrata con animazione fade-in
- Header con titolo e bottone close (X icon)
- Footer con actions (Cancel/Confirm)
- Accetta children per contenuto
- TypeScript generics per props
- Tailwind: rounded-3xl, shadow-2xl
```

## 🎨 Riferimenti Design System

**Colori principali da usare:**
- Backgrounds: `bg-neutral-50`, `bg-white`
- Testi: `text-neutral-900`, `text-neutral-600`
- Accents: `bg-brand-500`, `text-brand-600`
- Success: `bg-success-100`, `text-success-700`
- Borders: `border-neutral-200`

**Classi comuni:**
- Card: `rounded-2xl border border-neutral-200 bg-white p-6 shadow-sm`
- Button primary: `rounded-full bg-brand-500 px-6 py-3 text-white hover:bg-brand-600`
- Button secondary: `rounded-full border border-neutral-300 px-6 py-3 text-neutral-700`
- Input: `rounded-lg border border-neutral-300 px-4 py-3 focus:border-brand-500 focus:ring-2 focus:ring-brand-200`

**Icone Lucide React più usate:**
```typescript
import { 
  Sparkles,      // AI/generazione
  Calendar,      // Calendario
  BarChart3,     // Analytics
  Send,          // Pubblica/invia
  Eye,           // Views
  Heart,         // Likes
  MessageCircle, // Comments
  Share2,        // Shares
  Plus,          // Aggiungi
  Edit,          // Modifica (oppure Pencil)
  Trash2,        // Elimina
  Check,         // Conferma
  X,             // Chiudi
  ChevronLeft,   // Nav sinistra
  ChevronRight,  // Nav destra
  Loader2,       // Loading (con animate-spin)
} from "lucide-react";
```

## 💡 Tips

**Per v0.dev:**
- Allega screenshot se hai riferimenti visivi
- Specifica "Next.js App Router" se serve routing
- Chiedi varianti se non ti piace il primo risultato

**Per Claude:**
- Dai esempi di output desiderato
- Chiedi spiegazione del codice se complesso
- Puoi chiedere refactoring iterativi

**Workflow consigliato:**
1. Genera componente con AI
2. Copia in `frontend/components/NomeComponente.tsx`
3. Testa localmente con `npm run frontend:dev`
4. Aggiusta import/types se necessario
5. Committa su branch `feat/componente-x`

## 🚫 Cosa NON chiedere

- ❌ Altre librerie di icone (solo Lucide React)
- ❌ CSS custom o styled-components (solo Tailwind)
- ❌ JavaScript senza types (solo TypeScript)
- ❌ Dipendenze extra senza approvazione team
