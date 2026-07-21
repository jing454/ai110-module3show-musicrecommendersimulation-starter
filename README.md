# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

overall idea: The program should correctly calculate the distance between preference the song's features and sum them up in order to be used for ranking...

---

## How The System Works

Explain your design in plain language.

We will track the `songs` that the users listen to. We will then find these features: acousticness, energy, danceability, valence, and tempo_bpm in each song. Then we can rank the range (spreadness) of each feature to check which is the best to use. We can then use the formula: score = 1 - abs(song_energy - user_pref_energy) to calculate the best songs that is similar to the user's taste which is stored in `UserProfile`. The higher the value means the more close the song's feature is to the user's taste. The `Recommender` can then show these songs from the highest value to the lowest.

Values that are greater than 0-1 scale like tempo will be calculated using the formula: 

# normalized_ratio = (bpm_song - min_bpm) / (max_bpm - min_bpm)
# normalized_ratio_target = (bpm_target - min_bpm) / (max_bpm - min_bpm)

we can then:

# score = 1 - abs(normalized_ratio_song - normalized_ratio_target)

This effectively standardlizes the ratio of 0-1 and calculates the farness of the scale of the song 

Additionally, target preference that is a str will be calculated by giving it a score (1 if correct, 0 if incorrect)

# SCORING ALGORITHM (MAX):

Genre: 30 pts (exact match)  
Mood: 22 pts (exact match)
Energy: 12 pts
Valence: 10 pts
Danceability: 8 pts
Tempo: 8pts


Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo

- What information does your `UserProfile` store

- How does your `Recommender` compute a score for each song

- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

Loading songs from data/songs.csv...
Loaded songs: 18

============================================
 TOP RECOMMENDATIONS                        
 For: genre=pop, mood=happy, energy=0.8     
============================================

 1. Sunrise City  -  Neon Echo
    Score: 63.76 / 90
    Why:
      - genre match (+30.0)
      - mood match (+22.0)
      - energy closeness (+11.8)

 2. Gym Hero  -  Max Pulse
    Score: 40.44 / 90
    Why:
      - genre match (+30.0)
      - energy closeness (+10.4)

 3. Rooftop Lights  -  Indigo Parade
    Score: 33.52 / 90
    Why:
      - mood match (+22.0)
      - energy closeness (+11.5)

 4. Concrete Kings  -  Blocktape
    Score: 12.00 / 90
    Why:
      - energy closeness (+12.0)

 5. Night Drive Loop  -  Neon Echo
    Score: 11.40 / 90
    Why:
      - energy closeness (+11.4)

============================================

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



