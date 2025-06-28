import streamlit as st

st.title("LoopKaka's Calculator")

num1 = st.number_input(label="Number 1", key="num1", step=1)
num2 = st.number_input(label="Number 2", key="num2", step=1)

operator = st.selectbox(label="Operator", options=["+", "-", "*", "/"])

result = None
if st.button("Calculator"):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    else:
        if num2 is not 0:
            result = num1 / num2
        else:
            result = "Bhai, Pagal hai kya, 0 se divide nahin hota!!!"

    st.write(f"Result 🏆 = {result}")


count = 0
if st.button("Click"):
    count = count + 1
    st.write(f"Count = {count}")
