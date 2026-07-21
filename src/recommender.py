from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: Optional[bool] = None       #optional
    target_acoustic: Optional[float] = None      #changed to float (AI)
    target_tempo: Optional[float] = None         #tempo is not on scale of 0-1 so must use formula in README.md
    target_valence: Optional[float] = None
    target_danceability: Optional[float] = None


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    print(f"Loading songs from {csv_path}...")

    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness"}

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # Scoring algorithm from README.md "SCORING ALGORITHM (MAX)".
    # Categorical features (genre, mood) score all-or-nothing on an exact match.
    # Numeric features score proportionally to closeness:
    #   points = weight * (1 - abs(song_value - target_value))   (clamped to >= 0)
    score = 0.0
    reasons: List[str] = []

    # --- Categorical: exact match or nothing ---
    if "genre" in user_prefs and song.get("genre") == user_prefs["genre"]:
        score += 30.0
        reasons.append(f"genre match (+30.0)")

    if "mood" in user_prefs and song.get("mood") == user_prefs["mood"]:
        score += 22.0
        reasons.append(f"mood match (+22.0)")

    # --- Numeric (0-1 scale): weight * (1 - abs(diff)) ---
    numeric_features = [
        ("energy", 12.0),
        ("valence", 10.0),
        ("danceability", 8.0),
    ]
    for feature, weight in numeric_features:
        if feature in user_prefs and feature in song:
            closeness = max(0.0, 1.0 - abs(song[feature] - user_prefs[feature]))
            points = weight * closeness
            score += points
            reasons.append(f"{feature} closeness (+{points:.1f})")

    # --- Tempo: not on a 0-1 scale, so normalize both onto 0-1 first (README.md) ---
    if "tempo_bpm" in user_prefs and "tempo_bpm" in song:
        min_bpm, max_bpm = 60.0, 180.0
        span = max_bpm - min_bpm
        norm_song = (song["tempo_bpm"] - min_bpm) / span
        norm_target = (user_prefs["tempo_bpm"] - min_bpm) / span
        closeness = max(0.0, 1.0 - abs(norm_song - norm_target))
        points = 8.0 * closeness
        score += points
        reasons.append(f"tempo closeness (+{points:.1f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k as (song, score, explanation), highest first."""
    # Score every song, building (song, score, explanation) tuples.
    scored = [
        (song, score, ", ".join(reasons) if reasons else "no matching features")
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    # Highest score first, then keep the top k.
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
