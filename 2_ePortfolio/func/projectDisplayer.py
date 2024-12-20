import pathlib as pl
import streamlit as st


def displayProject(project):
    """Displays the projects with a title-image-description-url format.

    Args:
        project (dataFrame): A pandas Data Frame that contains user projects data.
    """
    title = project["title"]
    desc = project["description"]
    url = project["url"]
    source = f"[Source code]({url})"
    imgPath = "2_ePortfolio/datas/images"
    imgName = project["image"]
    img = str(pl.Path(imgPath, imgName))
    st.subheader(title)
    st.image(img)
    st.write(desc)
    st.markdown(source)
