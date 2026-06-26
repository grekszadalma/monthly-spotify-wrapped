import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"

# authentification
def get_auth_url():

    # this tells spotify what we want authorization for
    scopes = "user-top-read user-read-recently-played"



    ### Creates a URL string ###
    # AUTH_URL: constant, beginning of the url (uses the authorize API of Spotify) 
    # Response type: After the user logs in, send me an authorization code
    # Client ID: This identifies which Spotify application is making the request (Which app we created in Spotify Developer Dashboard)
    # Scope: What we want permission to access
    # Redirect URI: After the user logs in, send them back here.

    return (
        f"{AUTH_URL}"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&scope={scopes}"
        f"&redirect_uri={REDIRECT_URI}"
    )

# get the access token
def get_token(code: str):
    auth_header = base64.b64encode(
        f"{CLIENT_ID}:{CLIENT_SECRET}".encode()
    ).decode()

    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    return response.json()