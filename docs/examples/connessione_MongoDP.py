# Importa la classe MongoClient da pymongo per connettersi a MongoDB
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime
from dotenv import load_dotenv


import os
load_dotenv()
uri=os.getenv("MONGO_URI")
db_name=os.getenv("DB_NAME")
#------------------------------------------DAO-------------------------------------------

class PostIG_DAO:

  def __init__(self, uri: str, db_name: str):
    try:
        self.client = MongoClient(uri)
        self.client.admin.command("ping")
        print("Connessione a MongoDB riuscita")

        self.db = self.client[db_name]
        self.collection = self.db["posts"]

    except Exception as e:
        print(f"Errore di connessione: {e}")
        self.client = None
        self.collection = None

    # CREATE
    def create_post(self, testo: str, hashtags: list, image_url: str, data_pubblicazione: datetime, status: str):

        post = {
            "testo": testo,
            "hashtags": hashtags,
            "image_url": image_url,
            "data_pubblicazione": data_pubblicazione,
            "status": status
        }

        result = self.collection.insert_one(post)
        return result.inserted_id #id che identifica quello specifico oggetto post

    # READ - tutti i post
    def get_all_posts(self):
        return list(self.collection.find())

    # UPDATE
    def update_post(self, post_id, nuovi_dati: dict):
        return self.collection.update_one(
            {"_id": post_id},
            {"$set": nuovi_dati}
        )

    # DELETE
    def delete_post(self, post_id):
        return self.collection.delete_one({"_id": post_id})

    # CHIUSURA
    def close(self):
        if self.client:
            self.client.close()