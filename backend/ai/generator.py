"""
Gemini Content Generator
Issue #12: BE Gemini Generazione Post

Servizio principale per generazione contenuti con Gemini AI
"""

from typing import Dict, Any, Optional
from .gemini_config import get_gemini_config, GeminiConfig
from .prompts import (
    build_prompt,
    SocialPlatform,
    ToneOfVoice,
    get_social_guidelines
)


class ContentGenerator:
    """
    Issue #12, #6: Generatore contenuti AI
    
    Gestisce la generazione di post social tramite Gemini AI
    con prompt ottimizzati per ogni piattaforma.
    
    TODO: Team AI (Andrea, Filippo)
    - Implementare retry logic per errori API
    - Cache risposte per prompt simili
    - Streaming response per UI real-time
    - Feedback loop per migliorare prompt
    - A/B testing varianti
    """
    
    def __init__(self):
        """
        Inizializza generatore con configurazione Gemini
        """
        self.config: GeminiConfig = get_gemini_config()
    
    
    async def generate_post(
        self,
        topic: str,
        social: str,
        tone: str = "professionale",
        additional_requirements: str = "",
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Issue #12: Genera post per social network
        
        Args:
            topic: Tema/argomento del post
            social: Piattaforma target (linkedin, twitter, instagram, facebook)
            tone: Tono di voce (professionale, casual, ispirazionale, educativo, umoristico)
            additional_requirements: Richieste extra dell'utente
            temperature: Creatività (0.0-1.0, default 0.7)
            
        Returns:
            Dict con:
                - generated_text: Testo generato
                - social_target: Social network
                - tone: Tono usato
                - metadata: Info aggiuntive (hashtag, lunghezza, etc.)
                - success: bool
                - error: messaggio errore (se presente)
                
        TODO:
        - Validare lunghezza rispetto a limiti social
        - Estrarre hashtag automaticamente
        - Suggerire emoji se non presenti
        - Score qualità post (engagement prediction)
        """
        try:
            # Converti stringhe in enum
            social_platform = SocialPlatform(social.lower())
            tone_voice = ToneOfVoice(tone.lower())
            
            # Costruisci prompt specifico
            prompt = build_prompt(
                social=social_platform,
                topic=topic,
                tone=tone_voice,
                additional_requirements=additional_requirements
            )
            
            # Configura temperature
            self.config.update_temperature(temperature)
            
            # Genera contenuto con Gemini
            model = self.config.get_model()
            response = model.generate_content(
                prompt,
                generation_config=self.config.generation_config,
                safety_settings=self.config.safety_settings
            )
            
            # Estrai testo generato
            generated_text = response.text
            
            # Ottieni linee guida social
            guidelines = get_social_guidelines(social_platform)
            
            # Metadata
            metadata = {
                "char_count": len(generated_text),
                "max_chars": guidelines.get("max_chars", 0),
                "ideal_chars": guidelines.get("ideal_chars", 0),
                "within_limits": len(generated_text) <= guidelines.get("max_chars", 99999),
                "hashtag_count": generated_text.count("#"),
                "emoji_count": sum(1 for c in generated_text if ord(c) > 127 and ord(c) < 10000)
            }
            
            return {
                "success": True,
                "generated_text": generated_text,
                "social_target": social,
                "tone": tone,
                "metadata": metadata,
                "prompt_used": prompt  # Debug
            }
            
        except ValueError as e:
            return {
                "success": False,
                "error": f"Parametri non validi: {e}",
                "generated_text": ""
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Errore generazione: {e}",
                "generated_text": ""
            }
    
    
    async def generate_variations(
        self,
        topic: str,
        social: str,
        count: int = 3
    ) -> list[Dict[str, Any]]:
        """
        Genera multiple varianti dello stesso post
        
        Args:
            topic: Tema post
            social: Piattaforma
            count: Numero varianti (max 5)
            
        Returns:
            List[Dict]: Lista varianti generate
            
        TODO: Issue #6 - GUI per selezionare tra varianti
        """
        variations = []
        temperatures = [0.5, 0.7, 0.9][:count]  # Temperature diverse = variazioni
        
        for i, temp in enumerate(temperatures):
            result = await self.generate_post(
                topic=topic,
                social=social,
                temperature=temp
            )
            
            if result["success"]:
                result["variation_number"] = i + 1
                variations.append(result)
        
        return variations
    
    
    async def improve_post(
        self,
        original_text: str,
        social: str,
        improvement_goals: str
    ) -> Dict[str, Any]:
        """
        Migliora un post esistente
        
        Args:
            original_text: Testo originale
            social: Piattaforma
            improvement_goals: Cosa migliorare (es: "più breve", "più engaging")
            
        Returns:
            Dict: Post migliorato
            
        TODO: Feature per editing assistito
        """
        prompt = f"""Migliora questo post per {social}:

Post originale:
{original_text}

Obiettivi miglioramento:
{improvement_goals}

Genera versione migliorata mantenendo il messaggio core.
"""
        
        try:
            model = self.config.get_model()
            response = model.generate_content(
                prompt,
                generation_config=self.config.generation_config
            )
            
            return {
                "success": True,
                "improved_text": response.text,
                "original_text": original_text
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    
    # Issue #16: Generazione immagini (TODO futuro)
    async def generate_image_description(
        self,
        post_text: str,
        social: str
    ) -> Dict[str, Any]:
        """
        TODO: Issue #16 - Genera descrizione per immagine
        
        Args:
            post_text: Testo del post
            social: Piattaforma (per aspect ratio giusto)
            
        Returns:
            Dict: Descrizione immagine per DALL-E/Midjourney
        """
        # Placeholder per sviluppo futuro
        return {
            "success": False,
            "error": "Feature generazione immagini non ancora implementata",
            "todo": "Issue #16 - Integrare con DALL-E o Stable Diffusion"
        }


# Singleton instance
_generator: Optional[ContentGenerator] = None


def get_content_generator() -> ContentGenerator:
    """
    Restituisce singleton ContentGenerator
    
    Returns:
        ContentGenerator: Generatore contenuti
    """
    global _generator
    
    if _generator is None:
        _generator = ContentGenerator()
    
    return _generator
