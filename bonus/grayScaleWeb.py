import streamlit as st
from PIL import Image

st.header("Grayscale Converter")
st.subheader("Say Cheese!")
cameraImage = st.camera_input("Take a photo", label_visibility="hidden")

st.write("Here is your converted image:")
if cameraImage:
    grayScaleImage = Image.open(cameraImage)
    grayScaleImage = grayScaleImage.convert("L")
    st.image(grayScaleImage)
