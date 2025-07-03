import streamlit as st
from data_loader import load_data
from sidebar_dash  import sidebar_filter
from plot_utils import plot_pie_result
from plot_utils import plot_bar_goals

def main():
    st.title("LALIGA DATA")
    col1, col2 = st.columns(2)
    laliga_df = load_data()
    filtered = sidebar_filter(laliga_df)

    with col1:
        fig = plot_pie_result(laliga_df, filtered)
        st.plotly_chart(fig)

    with col2:
        fig = plot_bar_goals(laliga_df, filtered)
        st.plotly_chart(fig)

main()