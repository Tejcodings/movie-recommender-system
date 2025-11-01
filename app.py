import streamlit as st
import pandas as pd
import pickle
import requests

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    rec_movies = []
    rec_movies_poster= []
    for i in movies_list:
        rec_movies.append(movies_df.iloc[i[0]].title)
        rec_movies_poster.append(fetch_poster(movies_df.iloc[i[0]].movie_id))
    return rec_movies , rec_movies_poster

import requests

def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=462c8bc4450a3125d8f94845e0ad9ca6'
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None




movies_dict = pickle.load(open('movies.pkl','rb'))
movies_df = pd.DataFrame(movies_dict)

#similarity = pickle.load(open('similarity.pkl','rb'))
url = "https://drive.google.com/uc?export=download&id=1S8RZvEdr-o8ricLDUsCcTpFYtvNXtOTY"
response = requests.get(url)
similarity = pickle.load(response.content)



st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose a movie to recommend',
    movies_df['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.write("Poster not available")
