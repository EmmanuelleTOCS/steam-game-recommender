# app/pages/recommendations.py
import streamlit as st
from src.recommender import hybrid_recommend
from src.data_loader import load_steam_data
import sys
import os

# Ensure the parent directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Recommendations", page_icon="🎯", layout="wide")

# Load game data
steam_df = load_steam_data()

st.title("🎯 Recommendations")
st.write("Discover games similar to your favorites.")

# Dropdown for game selection
selected_game = st.selectbox("Select a Game for Recommendations", steam_df["name"].sort_values())

# Get recommendations
recommendations = hybrid_recommend(selected_game, n=10, alpha=0.6)

st.write(f"### 🔗 Recommended Games for '{selected_game}'")

# Display recommendations
for i, game in enumerate(recommendations, 1):
    st.markdown(f"""
    <div style="padding: 10px; border-radius: 10px; background-color: #333333; margin-bottom: 20px;">
        <h3 style="color: #FFFFFF;">{i}. {game['name']}</h3>
        <ul>
            <li><strong>Genres:</strong> {game['genres']}</li>
            <li><strong>Positive Ratings:</strong> {game['positive_ratings']}</li>
            <li><strong>Negative Ratings:</strong> {game['negative_ratings']}</li>
            <li><strong>Average Rating:</strong> {game['average_rating']}</li>
            <li><strong>Average Playtime:</strong> {game['average_playtime']}</li>
            <li><strong>Price:</strong> {game['price']}</li>
            <li><a href="{game['store_url']}" target="_blank" style="color: #00BFFF;">View on Steam</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Show a message if no games match the filters
if not recommendations:
    st.write("No recommendations found. Try adjusting your filters.")
