import streamlit as st

st.header("Contact Me!")
with st.form(key="form_email"):
    userMail = st.text_input(
        label="Your E-Mail...",
        label_visibility="hidden",
        placeholder="Your E-Mail...",
        key="tb_userEmail",
    )
    userMessage = st.text_area(
        label="Your E-Mail...",
        label_visibility="hidden",
        placeholder="Your E-Mail...",
        key="tb_userMessage",
    )
    submit = st.form_submit_button("Submit")

st.session_state
