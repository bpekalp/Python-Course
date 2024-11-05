import streamlit as st
import json
import requests
import os

with open("secrets/nasa.json") as file:
    nasaCredentials = file.read()

nasaCredentials = json.loads(nasaCredentials)

nasaEmail = nasaCredentials["email"]
nasaKey = nasaCredentials["apikey"]
url = f"https://api.nasa.gov/planetary/apod?api_key={nasaKey}"

apodResponse = requests.get(url)
apodContent = apodResponse.json()

title = apodContent["title"]
imgUrl = apodContent["url"]
desc = apodContent["explanation"]
date = apodContent["date"]
copyr = apodContent["copyright"]

imgResponse = requests.get(imgUrl)
img = imgResponse.content

if not os.path.exists("bonus/nasaApod/images"):
    os.makedirs("bonus/nasaApod/images")

imgPath = f"bonus/nasaApod/images/{date}.png"
with open(imgPath, "wb") as file:
    file.write(img)

st.header(title)
st.image(imgPath)
st.write(desc)
st.text(f"Copyright: {copyr}")
