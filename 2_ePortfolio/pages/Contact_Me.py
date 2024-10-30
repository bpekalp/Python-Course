import streamlit as st
import func.emailSender as fes

st.header("Contact Me!")
with st.form(key="form_contactMe"):
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

    if not userName or not userMail or not userMessage:
        st.error("Please fill the form before sending.")

    else:
        status = fes.sendEmail(name, sender, message)

        if status == "success":
            st.success("Your e-mail was sent successfully!")

        else:
            st.error(f"An error occured: {status}")

st.session_state
