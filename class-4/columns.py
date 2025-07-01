import streamlit as st

col1, col2, col3 = st.columns(
    spec=[1, 2, 3], border=True, gap="large", vertical_alignment="bottom")

with col1:
    st.write(f"I am in col1")

with col2:
    st.write(f"I am in col2")
    st.number_input(label="test")

with col3:
    st.write(f"I am in col3")
