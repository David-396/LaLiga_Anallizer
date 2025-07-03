import streamlit as st
from data_loader import load_data
from sidebar_dash  import sidebar_filter
from plot_utils import plot_pie_result

def main():
    st.title("LALIGA DATA")

    laliga_df = load_data()
    print(laliga_df.empty)

    filtered = sidebar_filter(laliga_df)
    fig = plot_pie_result(laliga_df, filtered)
    st.plotly_chart(fig)

main()