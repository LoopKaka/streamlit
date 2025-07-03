import streamlit as st
import requests

if st.button("Tell Me A Joke"):
    try:
        resp = requests.get(
            "https://official-joke-api.appspot.com/random_joke")
        if resp.status_code == 200:
            joke = resp.json()
            st.toast("Bahi!! Ek Joke Sunn")
            st.markdown(f"**{joke['setup']}**")
            st.markdown(f"*{joke['punchline']}*")
        else:
            st.error("Bahi !! Kuch to galat hai iss API main")
    except Exception as e:
        st.error(f"Error: {e}")
