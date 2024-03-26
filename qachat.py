import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv() #loading all the environment variables

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


st.set_page_config("QA bot")
st.header("Gemini QA chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
button = st.button("Submit your answer: ")

if button and input:
    response = get_gemini_response(input)

    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("Chat history is: ")

for role, text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")















