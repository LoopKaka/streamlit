import streamlit as st

home, about, help = st.tabs(tabs=["Home", "About", "Help"])

with home:
    st.write("I am in Home Tab")

with about:
    st.write("I am in About Tab")
