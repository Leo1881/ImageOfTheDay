import streamlit as st
import requests

api_key = "L87LXPHQ9oN33InyB897nkEa99TIiJqvbULBIwVR"
url = "https://api.nasa.gov/planetary/apod?api_key=L87LXPHQ9oN33InyB897nkEa99TIiJqvbULBIwVR"

request = requests.get(url)
content = request.json()

print(content)

st.set_page_config(layout="wide")

st.header("Astronomy Picture Of The Day")
st.image(content["url"])
detail = content["explanation"]
st.write(detail)


