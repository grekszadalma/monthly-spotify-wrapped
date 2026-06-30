from collections import Counter
from supabase_client import supabase
from collections import defaultdict


def get_plays(user_id):
    res = supabase.table("plays").select("*").eq("user_id", user_id).execute()
    return res.data


def minutes_listened(plays):
    return sum(p["duration_ms"] for p in plays) / 60000


def biggest_day(plays):
    days = {}

    for p in plays:
        day = p["played_at"][:10]
        days[day] = days.get(day, 0) + 1

    return max(days, key=days.get)


def top_songs(plays, n=5):
    c = Counter()

    for p in plays:
        key = (p["track_name"], p["artist_name"])
        c[key] += 1

    return [
        {
            "name": track,
            "artist": artist
        }
        for (track, artist), _ in c.most_common(n)
    ]


def top_artists(plays, n=5):
    c = Counter([p["artist_name"] for p in plays])
    return c.most_common(n)


def heatmap(plays):
    days = defaultdict(int)

    for p in plays:
        day = p["played_at"][:10]  # "2026-06-26"
        days[day] += p["duration_ms"] / 60000  # minutes

    return days