##Working on to implement chatbot on streamlit
import streamlit as st

# Streamlit app
st.title("PDF Uploader")

# Upload file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
