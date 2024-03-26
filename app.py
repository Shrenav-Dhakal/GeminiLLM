import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv() #loading all the environment variables

genai.configure(os.getenv("GOOGLE_API_KEY"))

#function to load gemini pro model and get responses

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text



# Intialization of streamlit app

st.set_page_config("Q&A demo")
st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.write(response)

    











