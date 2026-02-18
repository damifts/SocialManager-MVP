import os
from google import genai
from google.genai.types import GenerateContentConfig
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY non trovata nel file .env")

client = genai.Client(api_key=api_key)


class InstagramPost:
    def __init__(self, caption: str, hashtags: str, cta: str):
        self.caption = caption
        self.hashtags = hashtags
        self.cta = cta

    def to_dict(self):
        return {"caption": self.caption, "hashtags": self.hashtags, "cta": self.cta}

    def __str__(self):
        return f"{self.caption}\n\n{self.hashtags}\n\n{self.cta}"


class InstagramAgent:
    SYSTEM_PROMPT = """Sei un social media manager esperto.
Dato un prompt dell'utente, crea un post Instagram.
Rispondi SOLO in questo formato, senza testo aggiuntivo o emoticon:

CAPTION: <testo della caption>
HASHTAGS: <lista hashtag separati da spazi>
CALL-TO-ACTION: <frase di invito all'azione>"""

    def __init__(self):
        self.chat = client.chats.create(
            model="gemini-2.5-flash-lite",
            config=GenerateContentConfig(system_instruction=self.SYSTEM_PROMPT)
        )

    def generate_post(self, user_prompt: str) -> InstagramPost:
        response = self.chat.send_message(user_prompt)
        text = response.text.strip()

        lines = {}
        for line in text.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                lines[key.strip().upper()] = value.strip()

        return InstagramPost(
            caption=lines.get("CAPTION", ""),
            hashtags=lines.get("HASHTAGS", ""),
            cta=lines.get("CALL-TO-ACTION", "")
        )


if __name__ == "__main__":
    agent = InstagramAgent()
    prompt = input("Inserisci il prompt per il post: ").strip()
    if prompt:
        post = agent.generate_post(prompt)
        print("\n--- Post generato ---\n")
        print(post)
    else:
        print("Prompt vuoto.")