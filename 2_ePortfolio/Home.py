import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("2_ePortfolio/datasource/images/photo.png")

with col2:
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
