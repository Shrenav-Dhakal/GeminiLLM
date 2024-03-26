import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv() #loading all the environment variables

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded):
    if uploaded is not None:
        bytes_data = uploaded.getvalue()

        image_parts = [
            {
                'mime_type':uploaded.type,
                'data':bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

st.set_page_config("Gemini Health App")
st.header("GEMINI HEALTH APPLICATION")

input = st.text_input("Input: ", key="input")
uploaded = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
image = ""
if uploaded is not None:
    image = Image.open(uploaded)
    st.image(image, caption="Uploaded image", use_column_width=True)

submit = st.button("Tell me total calories")

input_prompt = """

You are a health expert. You need to see the food items from the image and calculate the total calories,
also provide the details of every food items with calories intake using
below format

1. Item 1 - no of calories
2. Item 2  no of calories

"""

## if submit button is clicked

if submit:
    image_data = input_image_setup(uploaded)
    response = get_gemini_response(input, image_data, input_prompt)
    st.subheader("The answer is: ")
    st.write(response.text)


