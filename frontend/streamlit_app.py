import streamlit as st

st.title("AI Legal Document Simplifier (Demo)")
uploaded_file = st.file_uploader("Upload a legal document (PDF/DOCX/Image)")
if uploaded_file:
    st.write("Original Text: [Sample Text Placeholder]")
    st.write("Simplified Text: [AI Output Placeholder]")

