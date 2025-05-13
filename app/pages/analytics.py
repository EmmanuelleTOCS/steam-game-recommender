import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Ensure the parent directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_steam_data

st.set_page_config(page_title="Game Analytics", page_icon="📊", layout="wide")

# Load game data
steam_df = load_steam_data()

st.title("📊 Game Analytics")
st.write("Explore game trends, ratings, and popularity.")

# Top 10 Most Popular Genres
st.write("### 🎮 Top 10 Most Popular Genres")
top_10_genres = steam_df["genres"].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(y=top_10_genres.index, x=top_10_genres.values, palette="viridis")
plt.title("Top 10 Most Popular Genres")
plt.xlabel("Number of Games")
plt.ylabel("Genres")
st.pyplot(plt.gcf())
plt.clf()

# Top 10 Most Played Games
st.write("### ⏰ Top 10 Most Played Games")
top_10_played = steam_df.nlargest(10, "average_playtime")

plt.figure(figsize=(12, 6))
sns.barplot(y=top_10_played["name"], x=top_10_played["average_playtime"], palette="viridis")
plt.title("Top 10 Most Played Games")
plt.xlabel("Average Playtime (minutes)")
plt.ylabel("Game Names")
st.pyplot(plt.gcf())
plt.clf()

# Top 10 Most Rated Games
st.write("### ⭐ Top 10 Most Rated Games")
top_10_rated = steam_df.nlargest(10, "positive_ratings")

plt.figure(figsize=(12, 6))
sns.barplot(y=top_10_rated["name"], x=top_10_rated["positive_ratings"], palette="viridis")
plt.title("Top 10 Most Rated Games")
plt.xlabel("Positive Ratings")
plt.ylabel("Game Names")
st.pyplot(plt.gcf())
plt.clf()
