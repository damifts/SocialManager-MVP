from backend.ai.generator import *

# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    generator = ContentGenerator()

    prompt = input("Inserisci il prompt per il post: ").strip()
    if not prompt:
        print("Prompt vuoto.")
        exit()

    post = generator.generate_post(prompt)

    print("\n--- Post generato ---\n")
    print(post)

    publish = input("\nVuoi pubblicarlo su Instagram? (s/n): ").lower()

    if publish in ("s", "si", "y", "yes"):
        image_url = input("Inserisci URL immagine pubblica: ").strip()
        result = generator.publish_post(post, image_url)
        print("\nRisultato pubblicazione:")
        print(result)
