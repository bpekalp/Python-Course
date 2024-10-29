import json
import smtplib
import ssl
import time


def sendEmail(_name, _sender, _message):
    """Sends an email with the specified message content.

    Args:
        _name (str): The name of the person sending the email.
        _sender (str): The email address of the sender.
        _message (str): The main message content to be included in the email.

    Returns:
        str: A success message if the email is sent, or an error message if an exception occurs.
    """

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with open("secrets/contactMe.json") as file:
        secrets = file.read()

    secrets = json.loads(secrets)
    email = secrets["email"]
    password = secrets["password"]

    today = time.strftime("%B %d, %Y - %H:%M:%S")
    message = f"""\
From: {_name} <{_sender}>
Reply-To: {_sender}
To: {email}
Subject: You Have a New E-mail From {_name} - {today}

Keep in mind: The sender is {_sender} but it will show up as {email}, you will be replying to the actual sender.

{_message}

    """
    try:
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(email, password)
            server.sendmail(email, email, message.encode("utf-8"))

        return "success"

    except Exception as e:
        return f"An error occured while sending the e-mail: {e}"
