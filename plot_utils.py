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