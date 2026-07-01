from datetime import datetime, timezone
from supabase_client import supabase
from spotify import get_recently_played
from tokens import refresh_access_token, get_refresh_token, exchange_code_for_tokens



def parse_time(t: str) -> datetime:
    return datetime.fromisoformat(
        t.replace("Z", "+00:00").replace(" ", "T")
    ).astimezone(timezone.utc)


def get_last_sync(user_id):
    res = supabase.table("sync_state") \
        .select("last_synced_at") \
        .eq("user_id", user_id) \
        .maybe_single() \
        .execute()

    if not res.data:
        return None

    return res.data["last_synced_at"]


def update_last_sync(user_id, ts):
    supabase.table("sync_state").upsert({
        "user_id": user_id,
        "last_synced_at": ts.isoformat()
    }).execute()

def update_refresh_token(code: str):
    tokens = exchange_code_for_tokens(code)

    refresh_token = tokens.get("refresh_token")

    if not refresh_token:
        raise Exception(f"No refresh token returned: {tokens}")

    supabase.table("users").upsert({
        "user_id": "testuser",
        "refresh_token": refresh_token
    }).execute()

def sync_tracks(user_id):
    refresh_token = get_refresh_token(user_id)
    access_token = refresh_access_token(refresh_token)

    data = get_recently_played(access_token)

    last_sync_raw = get_last_sync(user_id)
    last_sync = parse_time(last_sync_raw) if last_sync_raw else datetime(1970, 1, 1, tzinfo=timezone.utc)

    max_seen = last_sync

    for item in data.get("items", []):
        played_at = parse_time(item["played_at"])

        if played_at <= last_sync:
            continue

        track = item["track"]

        supabase.table("plays").insert({
            "user_id": user_id,
            "track_id": track["id"],
            "track_name": track["name"],
            "artist_name": track["artists"][0]["name"],
            "album_image": track["album"]["images"][0]["url"],
            "played_at": played_at.isoformat(),
            "duration_ms": track["duration_ms"]
        }).execute()

        if played_at > max_seen:
            max_seen = played_at

    update_last_sync(user_id, max_seen)