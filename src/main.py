"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs, MAX_SCORE


# Distinct example user preference profiles to demo the recommender.
USER_PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.4},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
}


# Adversarial / edge-case profiles: designed to probe whether the scoring logic
# can be "tricked" into producing results that contradict the stated preference.
# Each comment notes what the profile exposes.
ADVERSARIAL_PROFILES = {
    # Conflict: asks for high energy AND a sad mood. The only sad song is
    # low-energy, so the +22 mood match buries the 12-point energy signal and
    # the top pick ends up being the LOWEST-energy track.
    "Contradiction (energy 0.9 + sad)": {"mood": "sad", "energy": 0.9},

    # Genre dominance: every numeric pref points at a quiet, sad, low-energy
    # song, but the +30 genre bonus makes a happy, high-energy pop track win.
    "Genre Trap": {"genre": "pop", "mood": "sad", "energy": 0.1},

    # No signal: every song scores 0.0, so the stable sort silently returns the
    # first rows of the CSV as if they were ranked recommendations.
    "Ghost (empty prefs)": {},

    # Case sensitivity: categorical match is exact-string, so "Pop"/"Happy"
    # silently fail to match "pop"/"happy" and this behaves like Ghost.
    "CapsLock": {"genre": "Pop", "mood": "Happy"},

    # Substring: "pop" never matches the genre "indie pop", even though a human
    # would expect it to.
    "Substring": {"genre": "pop", "mood": "happy", "energy": 0.76},

    # Unscored field: acousticness is in the data but never scored, so this
    # preference is a silent no-op.
    "Acoustic Lover": {"genre": "lofi", "acousticness": 0.95},

    # Out-of-range values: closeness clamps at 0, so nonsensical input produces
    # a silent all-zeros result rather than an error or warning.
    "OutOfBounds": {"energy": 1.5, "valence": -0.3, "tempo_bpm": 300},

    # Non-existent categories: a typo in genre/mood degrades silently into a
    # confident-looking but meaningless ranking.
    "Nonsense": {"genre": "polka", "mood": "existential"},
}


def print_recommendations(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print a formatted, ranked list of the top k recommendations for one profile."""
    width = 44
    prefs = ", ".join(f"{key}={value}" for key, value in user_prefs.items())

    print()
    print("=" * width)
    print(f" {name.upper()}".ljust(width))
    print(f" For: {prefs}".ljust(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(
        recommend_songs(user_prefs, songs, k=k), start=1
    ):
        print()
        print(f" {rank}. {song['title']}  -  {song['artist']}")
        print(f"    Score: {score:.2f} / {MAX_SCORE:.0f}")
        print(f"    Why:")
        # explanation is a comma-joined list of reasons; show each on its own line.
        for reason in explanation.split(", "):
            print(f"      - {reason}")

    print()
    print("=" * width)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Run the recommender once per example profile.
    for name, user_prefs in USER_PROFILES.items():
        print_recommendations(name, user_prefs, songs)

    # Adversarial / edge-case profiles — see how the scoring logic behaves when
    # preferences conflict, don't match, or point at unscored fields.
    print()
    print("#" * 44)
    print("# ADVERSARIAL / EDGE-CASE PROFILES")
    print("#" * 44)
    for name, user_prefs in ADVERSARIAL_PROFILES.items():
        print_recommendations(name, user_prefs, songs)


if __name__ == "__main__":
    main()
