import pandas
import plotly.express as px
import matplotlib.pyplot as plt


def plot_pie_result(df, filters):
    mask = (df['team'] == filters['team']) & (df['season'] ==  filters['season'])
    filtered_df = df[mask]

    result_counts = filtered_df['result'].value_counts().reset_index()
    result_counts.columns = ['result', 'count']

    fig = px.pie(result_counts, names='result', values='count', title='match results')
    return fig


def plot_bar_goals(df, filters):
    mask = (df['team'] == filters['team']) & (df['season'] ==  filters['season'])
    filtered_df = df[mask]

    goals_counts = filtered_df['gf'].value_counts().reset_index()
    goals_counts.columns = ['gf', 'count']

    fig =  px.bar(goals_counts, x='gf', y='count', title='goals number', labels={'gf':'Goals scored', 'count':'matches played'}, color='gf')
    return fig