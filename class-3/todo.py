import streamlit as st

todoList = []
if 'todoList' not in st.session_state:
    st.session_state.todoList = []

input = st.text_input(label="Todo")

if st.button("Save"):
    st.session_state.todoList.append(input)

if len(st.session_state.todoList) > 0:
    for index, todo in enumerate(st.session_state.todoList):
        col1, col2 = st.columns([8, 2])
        with col1:
            st.write(f"{todo}")
        with col2:
            if st.button(label='❌', key=f"dtn_{index}"):
                st.session_state.todoList.pop(index)
                st.rerun()

else:
    st.info("Bahi!!! Saab Kaam Khatam")
