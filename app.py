import streamlit as st
import pickle
import pandas as pd
import requests
import os

# --- Configuration ---
st.set_page_config(page_title="Movie Mentor", layout="wide")

# --- Theme Toggle ---
theme = st.radio("Choose Theme", ["Light", "Dark"], horizontal=True)

# --- Custom CSS ---
def inject_custom_css(theme="light"):
    dark_blue = "#00008B"

    if theme == "dark":
        st.markdown(f"""
            <style>
            html, body, .stApp {{
                background-color: #000000;
                color: orange !important;
            }}
            * {{
                color:orange !important;
            }}
            .movie-box {{
                height: 175px;
                padding: 15px;
                background-color: #121212;
                border-radius: 10px;
                text-align: center;
                margin: 10px;
                box-shadow: 0 0 10px #222;
                color: white !important;
            }}
            /* Override selectbox/dropdown */
            .stSelectbox div[data-baseweb="select"] * {{
                color: black !important;
                background-color: white !important;
            }}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <style>
            html, body, .stApp {{
                background-color: orange;
                color: {dark_blue} !important;
            }}
            * {{
                color: {dark_blue} !important;
            }}
            .movie-box {{
                padding: 15px;
                background-color: #ffcc80;
                border-radius: 10px;
                text-align: center;
                margin: 10px;
                box-shadow: 0 0 8px #444;
                color: {dark_blue} !important;
            }}
            </style>
        """, unsafe_allow_html=True)

inject_custom_css(theme.lower())

# --- Display App Logo/Image Safely ---
image_path = "d503307c-aba6-4fba-9fdd-34f4ba26986a.png"
if os.path.exists(image_path):
    st.image(image_path, caption="Movie Mentor", width=150)
else:
    st.warning("Logo image not found. Please make sure the image file exists.")

# --- TMDB API Credentials ---
API_KEY = 'ba27e317366f6e92bf9f5e93b27b0aa7'
READ_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYTI3ZTMxNzM2NmY2ZTkyYmY5ZjVlOTNiMjdiMGFhNyIsIm5iZiI6MTc0NDM4MzI4Mi4xNzYsInN1YiI6IjY3ZjkyZDMyN2Y3MGFjMWEyMWQ5NWE5ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3mBsxCP2th6zPtUVqYlDXJcBq3lBN9Jw3aooLeG2gVI'

# --- Load Data ---
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Fetch Poster ---
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "Authorization": f"Bearer {READ_ACCESS_TOKEN}",
        "accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://via.placeholder.com/150x225?text=No+Image"
    except Exception as e:
        st.warning(f"Failed to load poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/150x225?text=No+Image"

# --- Recommend Movies ---
def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_titles = [movies.iloc[i[0]]['title'] for i in movie_list]
    recommended_posters = [fetch_poster(movies.iloc[i[0]]['id']) for i in movie_list]
    return recommended_titles, recommended_posters

# --- Movie Details ---
def get_details(title):
    movie = movies[movies['title'] == title].iloc[0]
    return {
        'Title': movie['title'],
        'Overview': movie.get('overview', 'No overview available.'),
        'Genres': movie.get('genres', 'N/A'),
        'Tagline': movie.get('tagline', ''),
        'Release Date': movie.get('release_date', 'Unknown')
    }

def display_movie_details():
    st.subheader("📘 Movie Details")
    title = st.selectbox("Select a Movie", movies['title'].values)
    if st.button("Show Details"):
        info = get_details(title)
        st.markdown(f"""<div class="movie-box">
        <h3>{info['Title']}</h3>
        <p><strong>Overview:</strong> {info['Overview']}</p>
        <p><strong>Genres:</strong> {info['Genres']}</p>
        <p><strong>Tagline:</strong> {info['Tagline']}</p>
        <p><strong>Release Date:</strong> {info['Release Date']}</p>
        </div>""", unsafe_allow_html=True)

# --- Browse All Movies ---
def paging_movies():
    st.subheader("📚 Browse All Movies")
    page_size = 10
    total_movies = len(movies)
    page = st.number_input("Page", min_value=1, max_value=(total_movies // page_size) + 1, step=1) - 1
    start = page * page_size
    end = start + page_size
    for i in range(start, min(end, total_movies)):
        st.markdown(f"""<div class="movie-box">{i + 1}. {movies.iloc[i]['title']}</div>""", unsafe_allow_html=True)

# --- Recommendation UI ---
def recommendation_ui():
    selected_movie = st.selectbox("🎥 Select a movie to get recommendations:", movies['title'].values)
    if st.button("Show Recommendations"):
        names, posters = recommend(selected_movie)
        st.markdown("### 💡 Top Recommended Movies")
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.markdown(f"""<div class="movie-box">
                    <img src="{posters[i]}" width="150"><br>
                    <strong>{names[i]}</strong>
                </div>""", unsafe_allow_html=True)

# --- Main App ---
def main():
    st.title("🎬 Welcome to Movie Mentor")
    st.markdown("Get movie recommendations and explore movie details.")
    tabs = st.tabs(["🔍 Recommendations", "📘 Movie Details", "📚 Browse All"])

    with tabs[0]:
        recommendation_ui()
    with tabs[1]:
        display_movie_details()
    with tabs[2]:
        paging_movies()

if __name__ == '__main__':
    main()
