import streamlit as st
import sys
import os

# Ensure the parent directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_steam_data
from src.recommender import hybrid_recommend

# Set the default page to "home" if not set
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# Redirect to home if the current page is "home"
if st.session_state["current_page"] == "home":
    st.set_page_config(page_title="Welcome to Steam Game Recommender", page_icon="🎮", layout="wide")
    st.title("🎮 Welcome to the Steam Game Recommender")
    st.write("Discover your next favorite game with personalized recommendations and insights!")
    
    # Links to different sections
    st.markdown("""
    <a href="/home" style="color: #00BFFF; font-size: 18px;">Go to Home Page</a>
    """, unsafe_allow_html=True)
else:
    st.set_page_config(page_title="Steam Game Recommender", page_icon="🎮", layout="wide")
    # Load game data
    steam_df = load_steam_data()

    # Dropdown for game selection
    selected_game = st.selectbox("Select a Game", steam_df["name"].sort_values())

    # Filters
    st.sidebar.title("🔍 Filter Options")
    selected_genre = st.sidebar.selectbox("Filter by Genre", ["All"] + sorted(steam_df["genres"].unique()))
    min_rating = st.sidebar.slider("Minimum Average Rating", 0.0, 1.0, 0.0, 0.1)
    max_price = st.sidebar.slider("Maximum Price", 0.0, 60.0, 60.0, 0.5)
    sort_option = st.sidebar.selectbox("Sort by", ["Relevance", "Average Rating", "Positive Ratings", "Playtime"])

    # Get recommendations
    recommendations = hybrid_recommend(selected_game, n=50, alpha=0.6)

    # Apply filters
    if selected_genre != "All":
        recommendations = [game for game in recommendations if selected_genre in game["genres"]]

    recommendations = [game for game in recommendations if float(game["average_rating"]) >= min_rating]
    recommendations = [game for game in recommendations if game["price"] == "Free" or float(game["price"][1:]) <= max_price]

    # Sort recommendations
    if sort_option == "Average Rating":
        recommendations.sort(key=lambda x: float(x["average_rating"]), reverse=True)
    elif sort_option == "Positive Ratings":
        recommendations.sort(key=lambda x: x["positive_ratings"], reverse=True)
    elif sort_option == "Playtime":
        recommendations.sort(key=lambda x: int(x["average_playtime"].split()[0]), reverse=True)

    st.write(f"### 🔗 Recommended Games for '{selected_game}'")

    # Display recommendations as detailed cards
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
