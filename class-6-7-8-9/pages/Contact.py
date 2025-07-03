import streamlit as st
from pydantic import ValidationError, BaseModel, EmailStr, Field

st.set_page_config(
    page_title="Contact",
    page_icon="🏠"
)

st.write("# Contact 🏠")

# with st.form("Contact", clear_on_submit=True):
#     name = st.text_input("Name", placeholder="Enter Name")
#     email = st.text_input("Email", placeholder="Enter Email")
#     message = st.text_area("Message", placeholder="Enter Message")

#     isSendClicked = st.form_submit_button("Send")

# if isSendClicked:
#     if not name or not email or not message:
#         st.error("Bhai !!! All fields are manadatory")
#     else:
#         st.success(f"Thank you {name}, For contacting")


class ContactModel(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    message: str = Field(min_length=5)


with st.form("Contact", clear_on_submit=True):
    name = st.text_input("Name", placeholder="Enter Name")
    email = st.text_input("Email", placeholder="Enter Email")
    message = st.text_area("Message", placeholder="Enter Message")

    isSendClicked = st.form_submit_button("Send")

if isSendClicked:
    try:
        form = ContactModel.model_validate({
            'name': name,
            'email': email,
            'message': message
        })
        st.success(f"Thank You {name}")
    except ValidationError as error:
        for err in error.errors():
            st.error(f"Error in {err['loc'][0]}: {err['msg']}")
