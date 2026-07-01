import requests
import base64
from supabase_client import supabase

def get_tokens(code):
    auth = base64.b64encode(
        f"{CLIENT_ID}:{CLIENT_SECRET}".encode()
    ).decode()

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:8000/callback",
        },
    )

    return response.json()

def exchange_code_for_tokens(code):
    import requests, base64

    auth = base64.b64encode(
        f"{CLIENT_ID}:{CLIENT_SECRET}".encode()
    ).decode()

    r = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:8000/callback",
        },
    )

    return r.json()

def refresh_access_token(refresh_token):
    import requests

    r = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    return r.json()["access_token"]

def get_refresh_token(user_id):
    res = supabase.table("users") \
        .select("refresh_token") \
        .eq("user_id", user_id) \
        .single() \
        .execute()

    return res.data["refresh_token"]