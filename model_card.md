# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Music recommender 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

The point of the recommender is to recommend similar songs that the user prefer or has listened to.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The models will take in your preference/music you listen to. The recommender will then score each feature (genre, energy, mood, etc.) by a specific value based on these features that you listen to in a song. The recommender will then order these from highest to lowest scored. It will then display these songs to you in the sorted order. 
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset we use includes 18 different music/songs with different features. For example, there are songs from happy to sad to lofi. The dataset contains all different scale of energy, tempo_bpm, etc.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system displays the preference based on the energy way more than any other features. Anyone who wants the songs based on the song's energy will really like this recommender while people who focus on genre may not. 
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

After the changes to the weight of the genre and the energy, the energy is now the dominant effect. In our results, many songs win first due to it's closeness to the energy rather than the genre itself. Therefore, you may end up having songs that does not fit the user's genre. Additionally, upbeat songs with the combination of energy, happiness, and danceability scores higher than moderate, niche, or mellow music.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

The recommender behaves as expected in most of the cases except the cases of closeness between energy and genre. For example, some songs solely lost the 1st spot due to other songs having closer energy while having nothing to do with the genre taste of the user. 

## user profile tested

Happy pop vs. chill lofi
Everything fits prefectly. No issues no nothing 

sad + high energy vs. sad + low_energy
The low energy user score ended up being more domainant compared to the high energy. Problem arises since it favors low_energy more than high_energy when direction shouldnt matter


wants classical (high energy) vs wants metal (low energy)
The algorithm favors the energy more than the genre. As a result, the song with the more preferable energy value is picked rather than the genre. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would probably make an setting where the user can choose how much weight they would prefer for each feature. This will help the recommender give recommendations more closely to the user's preference. Additionally, i will try to solve more edge cases to ensure that most or all edge cases are covered. I can also add more songs to the dataset as well. 
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned about how recommender systems work and how they're not always accurate and will always have downfalls. Recommender systems rank each music using scores and rank them from highest score to the lowest. 