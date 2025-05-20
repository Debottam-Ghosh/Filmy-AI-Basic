import streamlit as st
import pickle
import pandas as pd
from utils.file_loader import download_and_load_similarity

# Download and load the similarity matrix from Google Drive
file_id = '11p2btcTWMVr2Y1lArVfsp7LCGic3-e3D'
similarity = download_and_load_similarity(file_id)

# Load movies dictionary and create DataFrame
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit app UI
st.title(":red[Filmy] AI (Basic)",divider="gray")

selected_movie_name = st.selectbox(
    "Choose a movie :)",
    movies['title'].values)

if st.button("Ask Filmy AI"):
    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        similarity_index = similarity[movie_index]
        five_recommended = sorted(
            list(enumerate(similarity_index)),
            reverse=True, key=lambda x: x[1])[1:6]

        recommended = [movies.iloc[i[0]].title for i in five_recommended]
        return recommended

    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
