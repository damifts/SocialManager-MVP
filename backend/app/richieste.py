import os

import httpx
from dotenv import load_dotenv


load_dotenv()

TOKEN_SEGRETO = os.getenv("INSTAGRAM_ACCESS_TOKEN", "")
BASE_URL = "https://graph.instagram.com/v24.0"
DEFAULT_TIMEOUT = httpx.Timeout(10.0, connect=5.0)


def _auth_headers() -> dict:
    return {
        "Authorization": f"Bearer {TOKEN_SEGRETO}",
        "Accept": "application/json",
        "Content-type": "application/json",
    }


def _safe_request(method: str, url: str, **kwargs):
    try:
        response = httpx.request(method, url, timeout=DEFAULT_TIMEOUT, **kwargs)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError:
        return None


class RichiesteClient:
    @staticmethod
    def retrieve_user():
        if not TOKEN_SEGRETO:
            return None
        url = f"{BASE_URL}/me"
        params = {
            "fields": "user_id,username,profile_picture_url,followers_count",
            "access_token": TOKEN_SEGRETO,
        }
        return _safe_request("GET", url, params=params)

    @staticmethod
    def create_media(url_risorsa: str, caption: str, user_id: str):
        if not TOKEN_SEGRETO:
            return None
        url = f"{BASE_URL}/{user_id}/media"
        payload = {"image_url": url_risorsa, "caption": caption}
        return _safe_request("POST", url, headers=_auth_headers(), json=payload)

    @staticmethod
    def publish_media(user_id: str, media_id: str):
        if not TOKEN_SEGRETO:
            return None
        url = f"{BASE_URL}/{user_id}/media_publish"
        payload = {"creation_id": media_id}
        return _safe_request("POST", url, headers=_auth_headers(), params=payload)

    @staticmethod
    def get_all_posts(user_id: str):
        if not TOKEN_SEGRETO:
            return None
        url = f"{BASE_URL}/{user_id}/media"
        params = {
            "fields": "id,caption,media_url",
            "access_token": TOKEN_SEGRETO,
            "limit": 20,
        }
        return _safe_request("GET", url, params=params)


richiesteClass = RichiesteClient
