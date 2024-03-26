import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv() #loading all the environment variables

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#function to load gemini pro vision model and get responses

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config("Image Demo")
st.header("Gemini Image Application")

input = st.text_input("Input Prompt: ", key="input")

uploaded = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])
image = ""
if uploaded is not None:
    image = Image.open(uploaded)
    st.image(image, caption="uploaded file", use_column_width=True)

button = st.button("Tell me about the image")

## if submit is clicked
if button:
    response = get_gemini_response(input, image)

    st.subheader("The response is : ")
    st.write(response)