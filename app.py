import pickle
import streamlit as st
import pandas as pd

# Display logo
st.image("C:\\Users\\Kiruthika\\OneDrive\\Desktop\\recoomen 2\\logo.png", width=250)

# Define light and dark themes
light_theme = {
    "primaryColor": "#F5F5DC",
    "backgroundColor": "#F5F5DC",
    "textColor": "#3B2A0D",
    "secondaryBackgroundColor": "#FFFDD0",
    "headerColor": "#000000"  # Dark Black for headers
}

dark_theme = {
    "primaryColor": "#1E1E1E",
    "backgroundColor": "#2E2E2E",
    "textColor": "#FFFFFF",
    "secondaryBackgroundColor": "#3A3A3A",
    "headerColor": "#FFFFFF"  # White for headers
}

# Toggle for dark mode
dark_mode = st.sidebar.checkbox("Enable Dark Mode")

# Select the theme based on the toggle
theme = dark_theme if dark_mode else light_theme

# Apply the selected theme
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {theme['backgroundColor']};
        color: {theme['textColor']};
        font-family: sans-serif;
    }}
    .sidebar {{
        background-color: {theme['secondaryBackgroundColor']};
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {theme['headerColor']};  /* Header color */
    }}
    </style>
    """,
    unsafe_allow_html=True
)



# Set up the app title
st.title("MOVIE MAVEN")

# Load movie data
movies = pickle.load(open('C:\\Users\\Kiruthika\\OneDrive\\Desktop\\recoomen 2\\movies_list.pkl', 'rb'))
movie_list = movies['title'].values
similarity = pickle.load(open('C:\\Users\\Kiruthika\\OneDrive\\Desktop\\recoomen 2\\similarity.pkl', 'rb'))

# Load additional movie dataset for social sharing
movies_data = pd.read_csv('C:\\Users\\Kiruthika\\OneDrive\\Desktop\\recoomen 2\\dataset.csv')






# Define recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:  # Skip the first one as it's the selected movie itself
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

# Define function to display recommendation page
def display_recommendation():
    st.write("ESCAPE INTO THE MOVIE MIRAGE")
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)
    
    if st.button('Show Recommendation'):
        recommended_movie_names = recommend(selected_movie)
        st.write("Recommended Movies:")
        for i in recommended_movie_names:
            st.write(i)

# Define function to display social sharing page
def display_social_sharing():
    st.header("Share Your Favorite Movies")
    selected_movie_title = st.selectbox("Select a movie to get details:", movies_data['title'])
    selected_movie = movies_data[movies_data['title'] == selected_movie_title].iloc[0]
    
    st.title(selected_movie['title'])
    st.write(f"Genre: {selected_movie['genre']}")
    st.write(f"Original Language: {selected_movie['original_language']}")
    st.write(f"Overview: {selected_movie['overview']}")
    st.write(f"Popularity: {selected_movie['popularity']}")
    st.write(f"Release Date: {selected_movie['release_date']}")
    st.write(f"Vote Average: {selected_movie['vote_average']} ({selected_movie['vote_count']} votes)")

    # Share buttons for the selected movie
    st.write("Share this movie on platforms 🚀:")
    st.markdown(f"[Share on Twitter](https://twitter.com/intent/tweet?text=Check out this movie: {selected_movie['title']}. {selected_movie['overview']})")
    st.markdown(f"[Share on Facebook](https://www.facebook.com/sharer/sharer.php?u={selected_movie['title']} - {selected_movie['overview']})")
    st.markdown(f"[Share on WhatsApp](https://api.whatsapp.com/send?text=Check out this movie: {selected_movie['title']}. {selected_movie['overview']})")
    st.markdown(f"[Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url={selected_movie['title']} - {selected_movie['overview']})")
    st.markdown(f"[Share via Email](mailto:?subject=Check out this movie&body=I found this movie interesting: {selected_movie['title']}. {selected_movie['overview']})")

# Define function to display feedback page
def display_feedback():
    st.header("We Value Your Feedback")
    feedback = st.radio('Do you like this recommendation?', ['👍', '👎'])
    if feedback == '👍':
        st.write('Thanks for your positive feedback!')
    elif feedback == '👎':
        st.write('Sorry you didn’t like it, we’ll improve.')

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [ "Movie Recommendation", "Social Sharing 🚀", "Feedback"])

# Navigation logic

if page == "Movie Recommendation":
    display_recommendation()
elif page == "Social Sharing 🚀":
    display_social_sharing()
elif page == "Feedback":
    display_feedback()





