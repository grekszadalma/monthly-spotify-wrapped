from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from auth import get_auth_url, get_token
from spotify import get_top_tracks, get_top_artists

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Spotify Wrapped Backend Running"}


@app.get("/login")
def login():
    return RedirectResponse(get_auth_url())


@app.get("/callback")
def callback(code: str):
    token_data = get_token(code)
    return token_data


@app.get("/wrapped")
def wrapped(access_token: str):
    tracks = get_top_tracks(access_token)
    artists = get_top_artists(access_token)

    return {
        "top_tracks": tracks,
        "top_artists": artists
    }