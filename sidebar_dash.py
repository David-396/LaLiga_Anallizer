import streamlit as st


def sidebar_filter(df):
    st.sidebar.header("data filters")
    st.sidebar.write('choose team and season')
    teams_list = sorted(df['team'].unique().tolist())
    selected_team = st.sidebar.selectbox('select team', teams_list, index=0)

    seasons_list = sorted(df['season'].unique().tolist())
    selected_season = st.sidebar.selectbox('select season', seasons_list, index=0)

    choosed = {'team':selected_team, 'season':selected_season}
    return choosed