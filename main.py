import streamlit as st
import requests

api_key = "L87LXPHQ9oN33InyB897nkEa99TIiJqvbULBIwVR"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)


