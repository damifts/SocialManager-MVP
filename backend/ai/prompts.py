"""
Prompts e Ruoli Agente per Gemini AI
Issue #10, #13: BE Gemini definire prompt e ruolo agente

Questo file contiene i prompt template e i ruoli sistema
per la generazione di contenuti social.

TODO: Team AI
- Testare e ottimizzare prompt per ogni social
- Aggiungere varianti per toni diversi
- Sperimentare con few-shot examples
- A/B testing prompt performance
"""

from enum import Enum
from typing import Dict, Any


class SocialPlatform(Enum):
    """
    Piattaforme social supportate
    """
    LINKEDIN = "linkedin"
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"


class ToneOfVoice(Enum):
    """
    Toni di voce disponibili
    """
    PROFESSIONALE = "professionale"
    CASUAL = "casual"
    ISPIRAZIONALE = "ispirazionale"
    EDUCATIVO = "educativo"
    UMORISTICO = "umoristico"


# Issue #10: Ruolo sistema base
SYSTEM_ROLE = """Sei un esperto copywriter specializzato in contenuti per social media.
Il tuo compito è creare post coinvolgenti, autentici e ottimizzati per ogni piattaforma.

Linee guida generali:
- Scrivi in modo chiaro e diretto
- Usa storytelling quando appropriato
- Includi call-to-action efficaci
- Rispetta i limiti di caratteri per piattaforma
- Suggerisci hashtag rilevanti quando serve
"""


# Issue #10, #12: Prompt template per social specifici
SOCIAL_PROMPTS = {
    SocialPlatform.LINKEDIN: {
        "base": """
Crea un post per LinkedIn professionale.

Linee guida LinkedIn:
- Tono: {tone}
- Lunghezza ideale: 150-300 caratteri (max 3000)
- Usa paragrafi corti per leggibilità
- Prima riga cruciale (hook)
- CTA professionale
- Max 3-5 hashtag rilevanti

Tema: {topic}

Richieste aggiuntive: {additional_requirements}

Genera un post completo con:
1. Hook iniziale
2. Contenuto principale
3. CTA (se appropriato)
4. Hashtag suggeriti
""",
        "examples": [
            "💡 Insight professionale con storytelling",
            "🎯 Annuncio prodotto/servizio",
            "🚀 Condivisione successo/milestone"
        ]
    },
    
    SocialPlatform.TWITTER: {
        "base": """
Crea un tweet efficace.

Linee guida Twitter:
- Tono: {tone}
- Lunghezza: MAX 280 caratteri
- Diretto e conciso
- Usa emoji strategicamente
- Max 2-3 hashtag
- Considera thread se tema complesso

Tema: {topic}

Richieste aggiuntive: {additional_requirements}

Genera tweet (o thread se necessario) con:
1. Messaggio principale
2. Emoji appropriate
3. Hashtag rilevanti
""",
        "examples": [
            "🔥 Quick tip o insight",
            "❓ Domanda coinvolgente",
            "🧵 Thread informativo (se tema complesso)"
        ]
    },
    
    SocialPlatform.INSTAGRAM: {
        "base": """
Crea una caption per Instagram.

Linee guida Instagram:
- Tono: {tone}
- Lunghezza: 125-150 caratteri ideale (max 2200)
- Prima riga hook visivo
- Emoji usati liberamente
- Story-driven
- Hashtag: 5-10 mix (popolari + niche)
- CTA engagement (commenta, salva, condividi)

Tema: {topic}

Richieste aggiuntive: {additional_requirements}

Genera caption con:
1. Hook visivo (prima riga)
2. Story/contenuto
3. CTA engagement
4. Hashtag strategici

NOTE: Menziona che serve IMMAGINE (issue #16 - generazione immagini)
""",
        "examples": [
            "✨ Story personale visiva",
            "📸 Behind the scenes",
            "💬 Domanda per engagement"
        ]
    },
    
    SocialPlatform.FACEBOOK: {
        "base": """
Crea un post per Facebook.

Linee guida Facebook:
- Tono: {tone}
- Lunghezza: flessibile, ma conciso vince
- Tono conversazionale
- Favorisci engagement (commenti, reazioni)
- Emoji moderati
- Link e preview ok
- Hashtag meno importanti (max 2-3)

Tema: {topic}

Richieste aggiuntive: {additional_requirements}

Genera post con:
1. Incipit coinvolgente
2. Contenuto chiaro
3. Domanda o CTA per engagement
4. Hashtag (opzionale)
""",
        "examples": [
            "🎉 Evento o annuncio",
            "💬 Sondaggio o domanda",
            "📰 Condivisione articolo/news"
        ]
    }
}


# Issue #10: Prompt per toni di voce
TONE_MODIFIERS = {
    ToneOfVoice.PROFESSIONALE: """
Usa un tono professionale:
- Linguaggio formale ma accessibile
- Evita slang eccessivo
- Focus su value proposition
- Credibilità e autorevolezza
""",
    
    ToneOfVoice.CASUAL: """
Usa un tono casual e amichevole:
- Linguaggio informale ma rispettoso
- Conversazionale
- Emoji moderati
- Personale e autentico
""",
    
    ToneOfVoice.ISPIRAZIONALE: """
Usa un tono ispirazionale e motivazionale:
- Messaggi positivi e uplifting
- Storytelling emozionale
- Call to action motivanti
- Visione e obiettivi
""",
    
    ToneOfVoice.EDUCATIVO: """
Usa un tono educativo e informativo:
- Condividi conoscenza utile
- Step-by-step quando possibile
- Esempi pratici
- Valore educativo chiaro
""",
    
    ToneOfVoice.UMORISTICO: """
Usa un tono leggero e umoristico:
- Battute appropriate
- Giochi di parole
- Ironia sottile
- Mantieni professionalità di base
"""
}


def build_prompt(
    social: SocialPlatform,
    topic: str,
    tone: ToneOfVoice = ToneOfVoice.PROFESSIONALE,
    additional_requirements: str = ""
) -> str:
    """
    Issue #10, #12: Costruisce prompt completo per Gemini
    
    Args:
        social: Piattaforma social target
        topic: Tema/argomento del post
        tone: Tono di voce desiderato
        additional_requirements: Richieste extra utente
        
    Returns:
        str: Prompt completo per Gemini
        
    TODO:
    - Aggiungere few-shot examples dinamici
    - Personalizzazione brand voice
    - Context injection (post precedenti, analytics)
    """
    # Base prompt per social
    base_prompt = SOCIAL_PROMPTS[social]["base"]
    
    # Modifier per tone
    tone_modifier = TONE_MODIFIERS[tone]
    
    # Combina tutto
    full_prompt = f"""{SYSTEM_ROLE}

{tone_modifier}

{base_prompt.format(
    tone=tone.value,
    topic=topic,
    additional_requirements=additional_requirements or "Nessuna richiesta specifica"
)}
"""
    
    return full_prompt


def get_social_guidelines(social: SocialPlatform) -> Dict[str, Any]:
    """
    Restituisce linee guida per social specifico
    
    Args:
        social: Piattaforma social
        
    Returns:
        Dict: Linee guida e best practices
        
    TODO: Usare per validazione post generato
    """
    guidelines = {
        SocialPlatform.LINKEDIN: {
            "max_chars": 3000,
            "ideal_chars": 200,
            "max_hashtags": 5,
            "emoji_usage": "moderato",
            "cta_important": True
        },
        SocialPlatform.TWITTER: {
            "max_chars": 280,
            "ideal_chars": 240,
            "max_hashtags": 3,
            "emoji_usage": "strategico",
            "cta_important": False
        },
        SocialPlatform.INSTAGRAM: {
            "max_chars": 2200,
            "ideal_chars": 150,
            "max_hashtags": 30,  # limit tecnico
            "recommended_hashtags": "8-12",
            "emoji_usage": "libero",
            "cta_important": True
        },
        SocialPlatform.FACEBOOK: {
            "max_chars": 63206,  # limite tecnico
            "ideal_chars": 250,
            "max_hashtags": 3,
            "emoji_usage": "moderato",
            "cta_important": True
        }
    }
    
    return guidelines.get(social, {})


# Issue #13: Prompt per generazione immagini (TODO futuro)
IMAGE_GENERATION_PROMPT = """
TODO: Issue #16 - Generazione immagini

Quando implementato, usare questo prompt per generare
descrizioni immagini da passare a:
- DALL-E
- Midjourney API
- Stable Diffusion
- Gemini Pro Vision

Template:
"Genera un'immagine per social media: {description}
Stile: {style}
Mood: {mood}
Dimensioni: {aspect_ratio}"
"""
