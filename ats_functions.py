# ats_functions.py
import google.generativeai as genai

def get_gemini_response(input):
    model = genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content(input)
    return response.text

def generate_ats_prompt(resume_text, job_description):
    return f"""
    Hey! Act like a skilled or very experienced ATS (Application Tracking System)
    with a deep understanding of the tech field, software engineering, data science, 
    data analysis, and big data engineering. Your task is to evaluate the resume 
    based on the given job description. Considering the highly competitive job 
    market, provide the best assistance for improving the resumes. Assign the 
    percentage matching based on JD and the missing keywords with high accuracy.

    Resume: {resume_text}
    Description: {job_description}

    I want the response in one single string having the structure
    {{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
    """
