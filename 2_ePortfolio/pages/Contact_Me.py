import streamlit as st
import func.emailSender as fes

st.header("Contact Me!")
with st.form(key="form_email"):
    userName = st.text_input(
        label="Your Name",
        label_visibility="collapsed",
        placeholder="Your Name...",
        key="tb_userName",
    )
    userMail = st.text_input(
        label="Your E-Mail...",
        label_visibility="collapsed",
        placeholder="Your E-Mail...",
        key="tb_userEmail",
    )
    userMessage = st.text_area(
        label="Your Message...",
        label_visibility="collapsed",
        placeholder="Your Message...",
        key="tb_userMessage",
    )
    submit = st.form_submit_button("Submit")

if submit:
    name = str(st.session_state["tb_userName"]).strip().title()
    sender = st.session_state["tb_userEmail"]
    message = st.session_state["tb_userMessage"]
    status = fes.sendEmail(name, sender, message)

    if status == "success":
        st.success("Your e-mail was sent successfully!")

    else:
        st.error(status)

st.session_state
