import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from src.data_loader import load_steam_data

# Set page config
st.set_page_config(page_title="Overview", page_icon="📊", layout="wide")

# Load data
steam_df = load_steam_data()

st.title("Overview")
st.write("This page provides an overview of the Steam Game Recommender.")

# Total Games
st.subheader("Total Games")
st.metric(label="Total Games", value=len(steam_df))

# Genre Distribution
st.subheader("Genre Distribution")
genre_counts = steam_df['genres'].str.split(';').explode().value_counts()
plt.figure(figsize=(10, 8))
sns.barplot(y=genre_counts.index, x=genre_counts.values, palette="viridis")
plt.title("Game Genre Distribution")
plt.xlabel("Number of Games")
plt.ylabel("Genres")
st.pyplot(plt)

# Top 10 Most Rated Games
st.subheader("Top 10 Most Rated Games")
most_rated = steam_df.nlargest(10, 'total_ratings')[['name', 'total_ratings']]
st.table(most_rated)

# Average Playtime Distribution
st.subheader("Average Playtime Distribution")
plt.figure(figsize=(12, 6))
sns.histplot(steam_df['average_playtime'], bins=30, kde=True, color="purple")
plt.title("Distribution of Average Playtime (Minutes)")
plt.xlabel("Average Playtime (Minutes)")
plt.ylabel("Frequency")
st.pyplot(plt)
