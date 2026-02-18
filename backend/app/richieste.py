import httpx
import os
from dotenv import load_dotenv


load_dotenv()

Token_segreto = os.getenv("INSTAGRAM_ACCESS_TOKEN")


class richiesteClass:


  def retriveUserReq():
   url_base = "https://graph.instagram.com/v24.0/me"
  
   params = {"fields":
             "user_id,username,profile_picture_url,followers_count", 
             "access_token":Token_segreto,
   }
  
  
   try:
  
  
     req = httpx.get(url=url_base,params=params)
     req.raise_for_status()
  
     res = req.json()
  
     return res
  
   except Exception:
    return False
  

 
  def CreateMediaReq(url_risorsa : str, caption : str, user_id : str):

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
      
      try:
      
        req = httpx.post(url=url_base,headers=headers,json=payload, timeout=30.0)

        req.raise_for_status()

        res = req.json()

        return res
      except Exception:
        return False





  def PostMediaReq(user_id : str,media_id : str):
      url_base = f"https://graph.instagram.com/v24.0/{user_id}/media_publish"

      headers = {
    
      "Authorization": f"Bearer {Token_segreto}",
      "Accept" : "application/json",
      "Content-type": "application/json",
    
        }

      payload = {
      "creation_id" : media_id,
      }

      try:

        req = httpx.post(url=url_base, params=payload,headers=headers)

        req.raise_for_status()

        res = req.json()

        return res
      
      except Exception:
       return False
  

  def getAllPost(user_id : str):
    url_base = f"https://graph.instagram.com/v24.0/{user_id}/media"

    params = {
      "fields": "id,caption,media_url",
      "access_token": Token_segreto,
      "limit": 20,
        }
    
    try:
    
      req = httpx.get(url=url_base, params=params)

      req.raise_for_status()

      ris = req.json()

      return ris

    except Exception:
      return False
