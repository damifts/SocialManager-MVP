from backend.ai.gemini_config import *

def test_gemini_connection() -> bool:
    """
    Issue #15: Testa connessione e setup Gemini
    
    Returns:
        bool: True se connessione OK
        
    TODO: Chiamare questo test all'avvio app
    """
    try:
        config = get_gemini_config()
        
        # Test semplice generazione
        response = config.model.generate_content(
            "Di' ciao in una parola",
            generation_config={"max_output_tokens": 10}
        )
        
        print(f"✅ Gemini setup OK! Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ Errore setup Gemini: {e}")
        return False
