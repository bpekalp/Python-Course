import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("2_ePortfolio/datasource/images/photo.png")

with col2:
    content = """
    Laboris nisi esse anim id. Excepteur dolor duis incididunt reprehenderit tempor dolore amet in minim duis exercitation nostrud. Incididunt ad mollit quis pariatur eiusmod veniam exercitation enim ut amet sit eiusmod. Cupidatat quis deserunt sit officia consequat nulla in elit. Nisi enim et laborum ut esse adipisicing in dolor adipisicing ad consectetur in. Irure reprehenderit labore reprehenderit velit.
    """
    st.header("Lorem Ipsum")
    st.write(content)
