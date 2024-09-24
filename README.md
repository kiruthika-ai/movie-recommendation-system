# movie-recommendation-system
movie recommendation system using collabrative filtering

### 2. *Technology Stack*
   - *Programming Language*: Python
   - *Libraries and Frameworks*:
     - *Streamlit*: “Streamlit is used for building the web app interface, which allows users to interact with the recommendation system.”
     - *Pickle*: “The pickle library is used to store and load pre-computed data such as movie lists and similarity scores.”
     - *Pandas*: “Pandas is used to handle the movie dataset and manipulate data for display and recommendations.”
   - *External Libraries*:
     - *Cosine Similarity*: “The similarity between movies is calculated using cosine similarity based on their features.”

### 3. *Dataset Explanation*
   - *Movie Dataset*: “The dataset contains thousands of movies with fields like movie ID, title, genre, original language, overview, popularity, release date, vote average, and vote count.”
   - *Data Usage*: “The recommendation system uses these features to calculate similarity between movies.”

### 4. *Recommendation System Methodology*
   - *Collaborative Filtering Approach*: 
     - “The system uses a collaborative filtering approach, where recommendations are made based on similarities between movies. It compares movies by calculating cosine similarity between their features.”
   - *Cosine Similarity*:
     - “Cosine similarity is used to measure how similar two movies are based on the vectors representing their features (such as genres, language, popularity). The system returns the top 5 most similar movies based on this score.”
   - *Example*:
     - “If a user selects a movie, the system computes the distance between that movie and others, and suggests movies that are the most similar based on predefined criteria.”

### 5. *User Interface*
   - *Streamlit Integration*: “The user interacts with the system via a web interface created using Streamlit. The app is simple and intuitive, allowing users to select a movie from a dropdown and receive recommendations.”
   - *Logo and Theme*: 
     - “I customized the app with a logo that appears on the top left and applied a theme with brown and black color schemes to match the logo. The font is a sans-serif type for clarity and a professional look.”
   - *Social Sharing Feature*:
     - “I’ve added a social sharing feature where users can share their selected movie or a recommended movie directly to social media platforms like Twitter, Facebook, WhatsApp, LinkedIn, or via email.”
   - *Feedback Feature*:
     - “There’s also a feedback feature where users can give a thumbs-up or thumbs-down based on whether they liked the recommendations.”
