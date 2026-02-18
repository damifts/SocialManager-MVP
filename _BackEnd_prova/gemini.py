from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import re
import json


# ── Caricamento variabili ambiente ────────────────────────────────────────────
if not load_dotenv():
    raise Exception("Non hai inserito la API key")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise Exception("API key mancante")

client = genai.Client()

# ── System instruction ────────────────────────────────────────────────────────
SYSTEM_INSTRUCTION = """
Sei un social media manager AI.
Il tuo compito è assistere l'utente nella creazione, modifica e programmazione di post Instagram.
Devi generare testo (caption), hashtag e call-to-action coerenti con il tema, il tono e il target forniti dall'utente.
Rispondi SEMPRE e SOLO in questo formato, senza testo aggiuntivo:

CAPTION: <testo della caption>
HASHTAGS: <lista hashtag separati da spazi>
CALL-TO-ACTION: <frase di invito all'azione>
"""

# ── Helpers ───────────────────────────────────────────────────────────────────
def valida_data(data_str: str) -> bool:
    """Verifica che la data rispetti il formato gg/mm/aaaa."""
    return bool(re.fullmatch(r"\d{2}/\d{2}/\d{4}", data_str))


def input_data() -> str:
    """Chiede la data finché non è valida."""
    while True:
        data = input("Inserisci la data di pubblicazione (gg/mm/aaaa): ").strip()
        if valida_data(data):
            return data
        print("  ⚠  Formato non valido. Usa gg/mm/aaaa (es. 25/12/2025).\n")


def input_si_no(domanda: str) -> bool:
    """Chiede sì/no e restituisce True per sì."""
    while True:
        risposta = input(domanda).strip().lower()
        if risposta in ("sì", "si", "s", "yes", "y"):
            return True
        if risposta in ("no", "n"):
            return False
        print("  ⚠  Rispondi con 'sì' o 'no'.\n")


def genera_testo(tema: str, data_post: str, tono: str) -> str:
    """
    Invia il prompt a Gemini e restituisce il testo generato.
    La system instruction viene passata tramite config, non history.
    """
    chat = client.chats.create(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        )
    )

    prompt = (
        f"Crea un post Instagram sul tema '{tema}' "
        f"da pubblicare il {data_post}, con tono {tono}."
    )

    try:
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        raise RuntimeError(f"Errore nella generazione del testo: {e}") from e


def genera_immagine(tema: str, tono: str) -> str | None:
    """
    Genera un'immagine con Imagen 3 e la salva come PNG.
    Restituisce il path del file salvato, oppure None in caso di errore.
    """
    prompt_img = (
        f"Fotografia professionale per un post Instagram sul tema '{tema}', "
        f"tono {tono}. Stile pulito, moderno, adatto ai social."
    )

    try:
        response = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=prompt_img,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="1:1",          # formato quadrato per Instagram
                safety_filter_level="block_some",
                person_generation="allow_adult",
            )
        )

        # Salva i byte base64 come file PNG
        image_bytes = response.generated_images[0].image.image_bytes
        path_img = "immagine_generata.png"
        with open(path_img, "wb") as f:
            f.write(image_bytes)

        return path_img

    except Exception as e:
        print(f"  ⚠  Impossibile generare l'immagine: {e}")
        return None


# ── Funzione principale ───────────────────────────────────────────────────────
def genera_post_utente() -> None:
    print("\n── Social Media Manager AI ──────────────────────────────────────\n")

    # Input utente
    tema      = input("Inserisci il tema del post: ").strip()
    data_post = input_data()
    tono      = input("Inserisci il tono desiderato (es. amichevole, professionale): ").strip()
    ha_immagine = input_si_no("Hai già un'immagine da usare? (sì/no): ")

    print("\n⏳ Generazione caption in corso...\n")

    # Generazione testo
    try:
        caption_data = genera_testo(tema, data_post, tono)
    except RuntimeError as e:
        print(f"❌ {e}")
        return

    # Generazione immagine (solo se l'utente non ne ha una)
    image_path = None
    if not ha_immagine:
        print("⏳ Generazione immagine in corso...\n")
        image_path = genera_immagine(tema, tono)

    # Output a schermo
    print("── Output generato da Gemini ─────────────────────────────────────\n")
    print(caption_data)

    if image_path:
        print(f"\n✅ Immagine salvata in: {image_path}")
    elif not ha_immagine:
        print("\n⚠  Generazione immagine non riuscita. Usa un'immagine propria.")

    # Salvataggio JSON
    post_data = {
        "tema":         tema,
        "data":         data_post,
        "tono":         tono,
        "caption_text": caption_data,
        "image":        image_path if image_path else (
                            "fornita dall'utente" if ha_immagine
                            else "generazione fallita"
                        )
    }

    output_file = "post_generato.json"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=4)
        print(f"\n💾 Dati salvati in '{output_file}'.")
    except OSError as e:
        print(f"\n⚠  Impossibile salvare il file JSON: {e}")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    genera_post_utente() 