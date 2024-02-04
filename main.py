# app.py
import streamlit as st
from process_pdf import input_pdf_text
from ats_functions import get_gemini_response, generate_ats_prompt

# Set site header
st.set_page_config(
    page_title="ResuMate Insight",
    page_icon="🚀",
    layout="centered",
)

# Main title and description
st.title("Smart ATS")
st.text("Enhance Your Resume with Intelligent Tracking System")

# Input for Job Description
jd = st.text_input("Paste the Job Description")

# File uploader for resume
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"], help="Please upload the pdf")

# Submit button
submit = st.button("Submit")

# Handle submission
if submit:
    if uploaded_file is not None:
        # Extract text from uploaded resume
        resume_text = input_pdf_text(uploaded_file)

        # Generate ATS prompt
        ats_prompt = generate_ats_prompt(resume_text, jd)

        # Get response from Gemini
        response = get_gemini_response(ats_prompt)

        # Display response
        st.subheader("Analysis Results:")
        st.info(response)
    else:
        st.warning("Please upload a resume")
