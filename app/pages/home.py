import streamlit as st
import random

st.set_page_config(page_title="Welcome to Steam Game Recommender", page_icon="🎮", layout="wide")

# Add a title and welcome message
st.title("🎮 Welcome to the Steam Game Recommender")
st.write("Discover your next favorite game with personalized recommendations and insights!")

# Add some highlight sections
st.markdown("""
<style>
.home-section {
    padding: 20px;
    margin-bottom: 30px;
    background-color: #333333;
    border-radius: 15px;
    color: white;
}
.home-section h2 {
    color: #00BFFF;
}
.home-section p {
    color: #CCCCCC;
}
.home-button {
    background-color: #00BFFF;
    color: white;
    padding: 10px 20px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
}
.home-button:hover {
    background-color: #007ACC;
    color: white;
}
</style>

<div class="home-section">
    <h2>🔥 Discover Trending Games</h2>
    <p>Explore the hottest games based on player reviews, playtime, and ratings.</p>
    <a href="/recommendations" class="home-button">View Recommendations</a>
</div>

<div class="home-section">
    <h2>📊 Game Analytics</h2>
    <p>Dive into game trends, genre popularity, and player insights.</p>
    <a href="/pages/analytics" class="home-button">Explore Analytics</a>
</div>

<div class="home-section">
    <h2>🔎 Search for Games</h2>
    <p>Find detailed information about your favorite games.</p>
    <a href="/pages/search" class="home-button">Start Searching</a>
</div>

<div class="home-section">
    <h2>📝 About the Platform</h2>
    <p>Learn how this recommendation system works and how it can help you discover amazing games.</p>
    <a href="/pages/overview" class="home-button">Learn More</a>
</div>

""", unsafe_allow_html=True)
