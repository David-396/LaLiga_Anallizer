import pandas as pd
import streamlit as st



def load_data():
    url = 'https://raw.githubusercontent.com/David-396/LaLiga.csv/refs/heads/main/matches_full.csv'
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error("error loading data")
        return pd.DataFrame()