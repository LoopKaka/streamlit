import streamlit as st

st.title("Hello World")
st.header("Streamlit Playlist")
st.subheader("LoopKaka's Channel")

isClick = st.button("Click")

st.write(f"Click Hua = {isClick}")

if st.button("Subscribe"):
    st.warning("Like ")
