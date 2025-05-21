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
st.markdown(
    """
    <p style='font-size:45px; font-weight:bold;'>
        <span style='color:#FF0000;'>Filmy</span> 
        <span style='color:##FFFFFF;'>AI</span> 
        <span style='color:#3b3b3b;'>- Basic Version</span> 
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("A basic :rainbow[movie recommendation system] which can recommend :blue-background[5 top movies] that you may like")
st.divider()

st.subheader("Choose a movie :)")
selected_movie_name = st.selectbox(
    "",
    movies['title'].values)

if st.button("Recommend"):
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

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown(
    "<p style='color:#3b3b3b; font-size:45px; font-weight:bold;'>Developed by Debottam Ghosh</p>",
    unsafe_allow_html=True
)
