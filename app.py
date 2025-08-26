import streamlit as st
import pickle 
import pandas as pd

# Load movie data
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

# Page config
st.set_page_config(page_title="🎥 Movie Recommender", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .main-title {
            font-size: 52px;
            color: #FF4B4B;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .recommend-title {
            font-size: 28px;
            margin-top: 30px;
            font-weight: 600;
        }
        .movie-box {
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 12px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #333;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            color: gray;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🎬 Movie Recommendetion System</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/252/252035.png", width=100)
st.sidebar.title("🎈 About")
st.sidebar.info(
    "This app recommends 5 similar movies based on your selection. "
    "It uses content-based filtering powered by cosine similarity."
)

# Select a movie
selected_movie_name = st.selectbox('🎞️ Select a Movie', movies['title'].values)

# Recommend button
if st.button('🍿 Recommend Movies'):
    recommendations = recommend(selected_movie_name)
    st.markdown(f'<div class="recommend-title">🔝 Top 5 Recommendations for <span style="color:#FF4B4B;">{selected_movie_name}</span></div>', unsafe_allow_html=True)
    
    # Layout in columns
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"<div class='movie-box'>{recommendations[i]}</div>", unsafe_allow_html=True)


# 🎉 Fun animations
st.success("Here are your recommendations! 🎬")
st.balloons()  # Balloons animation
st.snow()      # Snow effect ❄️
# Footer
st.markdown('<div class="footer">Made By Ayush Kumar Maurya ❤️</div>', unsafe_allow_html=True)
