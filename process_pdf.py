# process_pdf.py
import streamlit as st
import PyPDF2 as pdf
import time

def input_pdf_text(uploaded_file):
    with st.spinner("Processing file..."):
        time.sleep(3)  # Simulating processing time
        reader = pdf.PdfReader(uploaded_file)
        text = ''.join([reader.pages[page].extract_text() for page in range(len(reader.pages))])
    return text
