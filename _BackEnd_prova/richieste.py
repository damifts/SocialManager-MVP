import httpx
import os
from dotenv import load_dotenv
from connession_mongo_Db import *


load_dotenv()

Token_segreto = os.getenv("ACCOUNT_TOKEN")


def retriveUserReq():
 url_base = "https://graph.instagram.com/v24.0/me"

 params = {"fields":
           "user_id,username,profile_picture_url,followers_count", 
           "access_token":
           Token_segreto
 }

 req = httpx.get(url=url_base,params=params)

 res = req.json()

 return res





def CreateMediaReq(url_risorsa, caption, user_id):
 url_base = f"https://graph.instagram.com/v24.0/{user_id}/media"

 headers = {
 
 "Authorization": f"Bearer {Token_segreto}",
 "Accept" : "application/json",
 "Content-type": "application/json",
 
}

 payload = {
 "image_url" : url_risorsa,
 "caption": caption
 
}
 
 req = httpx.post(url=url_base,headers=headers,json=payload, timeout=30.0)

 res = req.json()

 return res





def PostMediaReq(user_id,media_id):
  url_base = f"https://graph.instagram.com/v24.0/{user_id}/media_publish"

  headers = {
 
   "Authorization": f"Bearer {Token_segreto}",
   "Accept" : "application/json",
   "Content-type": "application/json",
 
    }

  payload = {
   "creation_id" : media_id,
  }

  req = httpx.post(url=url_base, params=payload,headers=headers)

  res = req.json()

  return res


def getAllPost(user_id):
 url_base = f"https://graph.instagram.com/v24.0/{user_id}/media"

 params = {
  "fields": "id,caption,media_url",
  "access_token": Token_segreto,
  "limit": 20,
    }
 
 req = httpx.get(url=url_base, params=params)

 ris = req.json()

 return ris 