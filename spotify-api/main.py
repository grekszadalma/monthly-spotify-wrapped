from fastapi import FastAPI
from auth import get_auth_url, get_token
from sync import sync_tracks, update_refresh_token
from tokens import exchange_code_for_tokens
from analytics import (
    get_plays,
    minutes_listened,
    biggest_day,
    top_songs,
    top_artists,
    heatmap
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 1. login URL
@app.get("/login")
def login():
    return {"url": get_auth_url()}


# 2. callback
@app.get("/callback")
def callback(code: str):
    update_refresh_token(code)
    return "OK"


# 3. sync endpoint (run daily via cron)
@app.get("/sync/{user_id}")
def sync(user_id: str, access_token: str):
    sync_tracks(user_id, access_token)
    return {"status": "synced"}


# 4. wrapped endpoint (FINAL OUTPUT)
@app.get("/wrapped/{user_id}")
def wrapped(user_id: str):
    plays = get_plays(user_id)

    return {
        "minutes_listened": minutes_listened(plays),
        "biggest_day": biggest_day(plays),
        "heatmap": heatmap(plays),
        "top_songs": top_songs(plays),
        "top_artists": top_artists(plays)
    }