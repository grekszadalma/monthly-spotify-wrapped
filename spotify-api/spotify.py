import requests


def get_top_tracks(access_token):
    url = "https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=10"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    return requests.get(url, headers=headers).json()


def get_top_artists(access_token):
    url = "https://api.spotify.com/v1/me/top/artists?time_range=short_term&limit=10"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    return requests.get(url, headers=headers).json()