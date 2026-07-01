import requests
import base64
from supabase_client import supabase
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

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
            "redirect_uri": REDIRECT_URI,
        },
    )

    return response.json()

def exchange_code_for_tokens(code):

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
            "redirect_uri": REDIRECT_URI,
        },
    )

    tokens = r.json()
    print(tokens)
    return r.json()

def refresh_access_token(refresh_token):
   
    r = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    print("STATUS:", r.status_code)
    print("RESPONSE:", r.json())

    data = r.json()

    if "access_token" not in data:
        raise Exception(f"Spotify refresh failed: {data}")

    return data["access_token"]

def get_refresh_token(user_id):
    res = supabase.table("users") \
        .select("refresh_token") \
        .eq("user_id", user_id) \
        .single() \
        .execute()

    return res.data["refresh_token"]