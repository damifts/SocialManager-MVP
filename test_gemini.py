"""
Script di test Gemini AI
Issue #15: BE Gemini Setup

Esegui questo script per testare:
- API key Gemini configurata
- Connessione a Google AI
- Generazione base funzionante

Usage:
    python test_gemini.py
"""

import sys
import os
from dotenv import load_dotenv

load_dotenv()

def test_gemini():
    """
    Test setup Gemini AI
    """
    print("=" * 60)
    print("🤖 TEST GEMINI AI - Social Manager MVP")
    print("=" * 60)
    print()
    
    # Test 1: API Key
    print("🔑 Test 1: API Key...")
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("   ❌ ERRORE: GEMINI_API_KEY non configurata!")
        print()
        print("   📝 Come configurare:")
        print("   1. Vai su: https://makersuite.google.com/app/apikey")
        print("   2. Crea una API key")
        print("   3. Aggiungi nel file .env:")
        print("      GEMINI_API_KEY=your_key_here")
        print()
        return False
    
    print(f"   ✅ API Key trovata: {api_key[:10]}...")
    print()
    
    # Test 2: Import libreria
    print("📦 Test 2: Import libreria...")
    try:
        import google.generativeai as genai
        print("   ✅ google-generativeai importato correttamente")
    except ImportError:
        print("   ❌ ERRORE: google-generativeai non installato")
        print("   💡 Installa con: pip install google-generativeai")
        return False
    
    print()
    
    # Test 3: Configurazione
    print("⚙️  Test 3: Configurazione Gemini...")
    try:
        genai.configure(api_key=api_key)
        print("   ✅ Gemini configurato")
    except Exception as e:
        print(f"   ❌ ERRORE configurazione: {e}")
        return False
    
    print()
    
    # Test 4: Generazione semplice
    print("🎨 Test 4: Generazione contenuto...")
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        response = model.generate_content(
            "Di' ciao in una frase breve e professionale",
            generation_config={"max_output_tokens": 50}
        )
        
        generated_text = response.text
        print(f"   ✅ Gemini Response: {generated_text}")
        
    except Exception as e:
        print(f"   ❌ ERRORE generazione: {e}")
        print("   💡 Verifica:")
        print("      - API key valida")
        print("      - Account Google AI configurato")
        print("      - Connessione internet")
        return False
    
    print()
    
    # Test 5: Parametri avanzati
    print("🔧 Test 5: Parametri avanzati...")
    try:
        generation_config = {
            "temperature": 0.9,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 100,
        }
        
        response = model.generate_content(
            "Scrivi un tweet creativo su tecnologia (max 280 caratteri)",
            generation_config=generation_config
        )
        
        print(f"   ✅ Tweet generato ({len(response.text)} caratteri):")
        print(f"   {response.text}")
        
    except Exception as e:
        print(f"   ⚠️  Test parametri fallito: {e}")
    
    print()
    print("=" * 60)
    print("✅ TEST COMPLETATO - Gemini AI pronto per l'uso!")
    print("=" * 60)
    print()
    print("📝 Prossimi step:")
    print("   1. Testa generazione post in app Streamlit")
    print("   2. Personalizza prompt in backend/ai/prompts.py")
    print("   3. Ottimizza temperature e parametri per use case")
    print()
    
    return True


if __name__ == "__main__":
    print()
    success = test_gemini()
    
    if not success:
        print()
        print("🔗 Risorse utili:")
        print("   - Google AI Studio: https://makersuite.google.com/")
        print("   - Docs Gemini API: https://ai.google.dev/docs")
        print("   - Python SDK: https://github.com/google/generative-ai-python")
        print()
        sys.exit(1)
    
    sys.exit(0)
