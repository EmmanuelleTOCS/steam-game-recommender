import streamlit as st
import pandas as pd

from src.data_loader import load_steam_data

# Set page config
st.set_page_config(page_title="Game Search", page_icon="🔎", layout="wide")

# Load data
steam_df = load_steam_data()

st.title("Game Search")
st.write("Explore game details.")

# Dropdown for game selection
selected_game = st.selectbox("Select a Game to Explore", steam_df["name"].sort_values())

# Display game details
game_details = steam_df[steam_df["name"] == selected_game]

if not game_details.empty:
    st.write(f"### Details for '{selected_game}'")
    st.dataframe(game_details.set_index("appid"), use_container_width=True)
else:
    st.write("No details available for this game.")
