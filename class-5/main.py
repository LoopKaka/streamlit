import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader

uploaded_file = st.file_uploader(label="Upload File")

if uploaded_file:
    file_details = {
        'file_name': uploaded_file.name,
        'file_size': f"{round(uploaded_file.size / (1024 * 1024), 1)} MB",
        'file_type': uploaded_file.type
    }

    'file_details', file_details

    if uploaded_file.type.startswith('image'):
        img = Image.open(uploaded_file)
        st.image(image=img, caption=uploaded_file.name)

    if uploaded_file.type == 'application/pdf':
        reader = PdfReader(uploaded_file)
        text = reader.pages[0].extract_text()
        st.write(text)
