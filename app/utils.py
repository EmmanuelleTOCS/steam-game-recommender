import pandas as pd
from src.data_loader import load_steam_data

def get_all_games():
    df = load_steam_data()
    return df['name'].sort_values().tolist()
