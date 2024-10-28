import streamlit as st
import pandas as pd
import func.projectDisplayer as fpd

st.set_page_config(layout="wide")

left1, right1 = st.columns(2)

with left1:
    st.image("2_ePortfolio/datasource/images/photo.png")

with right1:
    content = """
    This is Ardit Sulce. The teacher of the Python Mega Course on Udemy.com
    Excepteur consectetur enim incididunt eiusmod minim ut Lorem. Non ea eu dolore elit velit excepteur. Veniam laborum id do incididunt proident laboris sit duis velit do reprehenderit. Elit non tempor id aute exercitation voluptate non proident nulla nostrud est eu duis. Pariatur duis labore incididunt in.

    Irure esse sit qui deserunt nulla eu. Aute ullamco non Lorem consectetur anim minim commodo aliquip id proident aliqua qui do nulla. Veniam officia commodo magna proident magna sit laboris id. Ullamco velit sit ad nisi.
    """
    st.header("Lorem Ipsum")
    st.info(content)

content = """
Below, you'll find all the projects Ardit made.

Cillum nulla culpa velit nisi cupidatat consequat nisi incididunt exercitation consequat magna adipisicing culpa irure. Do est eiusmod ullamco qui pariatur exercitation. Duis consectetur occaecat dolore cillum officia esse reprehenderit ad veniam. Irure culpa enim et irure consequat.
"""
st.write(content)

projects = pd.read_csv("2_ePortfolio/datasource/data.csv", sep=";")
left2, mid2, right2 = st.columns([3, 1, 3])

with left2:
    for i, project in projects.iterrows():
        if i % 2 == 0:
            fpd.displayProject(project)

with right2:
    for i, project in projects.iterrows():
        if i % 2 != 0:
            fpd.displayProject(project)
