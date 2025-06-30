import streamlit as st

count = 0
if st.button("Click"):
    count = count + 1
    st.write(f"Count = {count}")


"st.session_state before create >>", st.session_state


if 'count' not in st.session_state:
    # st.session_state['count'] = 0
    st.session_state.count = 0

if 'name' not in st.session_state:
    st.session_state.name = 'LoopKaka'

if 'isClciked' not in st.session_state:
    st.session_state.isClciked = False

if st.button("Click 2"):
    st.session_state.count = st.session_state.count + 1
    st.write(f"Count = {st.session_state.count}")

"st.session_state after create >>", st.session_state

# Delete

del st.session_state.name

"st.session_state delete >>", st.session_state

for key in st.session_state:
    st.write(f"Key {key}, value {st.session_state[key]}")
    del st.session_state[key]

"st.session_state delete All >>", st.session_state
