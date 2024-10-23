import streamlit as st
from PIL import Image

img = None

st.header("Grayscale Converter")
st.subheader("Say Cheese!")

with st.expander("Start your webcam!"):
    cameraImage = st.camera_input("Take a photo", label_visibility="hidden")

with st.expander("Or upload an image!"):
    uploadedImage = st.file_uploader("Upload an image", label_visibility="hidden")

if cameraImage:
    img = cameraImage

elif uploadedImage:
    img = uploadedImage

st.write("Here is your converted image:")

if img:
    try:
        grayScaleImage = Image.open(img)
        grayScaleImage = grayScaleImage.convert("L")
        st.image(grayScaleImage)
    except Image.UnidentifiedImageError:
        st.error("Please upload an image file.")
