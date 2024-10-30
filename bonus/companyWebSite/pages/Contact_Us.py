import streamlit as st
import smtplib
import ssl
import json
import pandas as pd


def sendEmail(_name, _from, _topic, _message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with open("secrets/contactMe.json") as file:
        secrets = file.read()

    secrets = json.loads(secrets)
    email = secrets["email"]
    password = secrets["password"]

    message = f"""\
From: {_name} <{_from}>
Reply-To: {_from}
To: {email}
Subject: {_topic}, Sent by {_name}

Keep in mind: The sender is {_from} but it will show up as {email}, you will be replying to the actual sender.

{_message}

    """

    try:
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(email, password)
            server.sendmail(email, email, message.encode("utf-8"))

        return "success"

    except Exception as e:
        return e


topics = pd.read_csv("bonus/companyWebSite/datasource/topics.csv")

with st.form(key="form_contactUs"):
    st.text_input(label="Your Name", key="tb_name")
    st.text_input(label="Your E-Mail", key="tb_email")
    st.selectbox(
        label="Select The Topic You Want To Discuss",
        options=topics["topic"],
        key="sb_topic",
    )
    st.text_area(label="Your Message", key="tb_message")
    submit = st.form_submit_button("Submit")


if submit:
    userName = str(st.session_state["tb_name"]).strip().title()
    userMail = st.session_state["tb_email"]
    userTopic = st.session_state["sb_topic"]
    userMessage = st.session_state["tb_message"]

    if not userName or not userMail or not userTopic or not userMessage:
        st.error("Please fill the form before sending.")

    else:
        status = sendEmail(userName, userMail, userTopic, userMessage)

        if status == "success":
            st.success("Your e-mail was sent successfully!")

        else:
            st.error(f"An error occured: {status}")
