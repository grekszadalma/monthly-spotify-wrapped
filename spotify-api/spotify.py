import requests


def get_top_tracks_short(access_token):
    url = "https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=50"

    headers = {"Authorization": f"Bearer {access_token}"}

    return requests.get(url, headers=headers).json()

def get_top_tracks_mid(access_token):
    url = "https://api.spotify.com/v1/me/top/tracks?time_range=mid_term"

    headers = {"Authorization": f"Bearer {access_token}"}

    return requests.get(url, headers=headers).json()


def get_top_artists(access_token):
    url = "https://api.spotify.com/v1/me/top/artists?time_range=short_term&limit=10"

    headers = {"Authorization": f"Bearer {access_token}"}

    return requests.get(url, headers=headers).json()


def get_recently_played(access_token):
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=50"

    headers = {"Authorization": f"Bearer {access_token}"}

    return requests.get(url, headers=headers).json()