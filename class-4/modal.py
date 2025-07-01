import streamlit as st


@st.dialog("Dialog Example")
def someFunction():
    if st.button("Yes"):
        st.toast("Thank You 🏆")
    if st.button("No"):
        st.rerun()


if st.button("Open Dialog"):
    someFunction()
