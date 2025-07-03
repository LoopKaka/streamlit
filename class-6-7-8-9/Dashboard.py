import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="🖥️"
)

st.write("# Dashboard 🖥️")

uploaded_csv = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_csv:
    try:
        df = pd.read_csv(uploaded_csv)

        st.subheader("Raw Data")
        st.dataframe(df)

        st.subheader("Bar Chart")
        st.bar_chart(df.set_index("Month"))

        st.subheader("Line Chart")
        st.line_chart(df.set_index("Month"))
    except Exception as e:
        st.error(f"Error: {e}")
