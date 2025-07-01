import streamlit as st

gender = None
with st.popover(label="Example Popover"):
    st.markdown("Loop Kaka Popover")
    gender = st.radio(label="Gender", options=["Male", "Female"])

st.write(f"Gender = {gender}")
