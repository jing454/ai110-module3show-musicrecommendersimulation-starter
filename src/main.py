"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # --- Formatted output ---
    width = 44
    prefs = f"genre={user_prefs.get('genre')}, mood={user_prefs.get('mood')}, energy={user_prefs.get('energy')}"

    print()
    print("=" * width)
    print(" TOP RECOMMENDATIONS".ljust(width))
    print(f" For: {prefs}".ljust(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print()
        print(f" {rank}. {song['title']}  -  {song['artist']}")
        print(f"    Score: {score:.2f} / 90")
        print(f"    Why:")
        # explanation is a comma-joined list of reasons; show each on its own line.
        for reason in explanation.split(", "):
            print(f"      - {reason}")

    print()
    print("=" * width)


if __name__ == "__main__":
    main()
