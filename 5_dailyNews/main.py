import json
import requests
import smtplib
import ssl
import datetime


def getNewsCredentials():
    """Fetches News API credentials from a JSON file.

    Returns:
    tuple: A tuple containing the email and API key for the News API.
    """
    with open("secrets/newsapi.json") as file:
        _newsCredentials = file.read()

    _newsCredentials = json.loads(_newsCredentials)
    _newsMail = _newsCredentials["email"]
    _newsKey = _newsCredentials["apikey"]

    return _newsMail, _newsKey


def getBusinessNews(_newsKey):
    """Retrieves the latest business news headlines for the US.

    Args:
        _newsKey (str): The API key for accessing the News API.

    Returns:
        dict: A dictionary containing the response JSON with news headlines.
    """
    _url = f"https://newsapi.org/v2/"\
        f"top-headlines?country=us"\
        f"&category=business&apiKey={_newsKey}"

    _newsRequest = requests.get(_url)
    _newsContent = _newsRequest.json()
    return _newsContent


def getSmtpKey():
    """Fetches SMTP email credentials from a JSON file.

    Returns:
        tuple: A tuple containing the email address and password for the SMTP server.
    """
    with open("secrets/mail.json") as file:
        _mailCredentials = file.read()

    _mailCredentials = json.loads(_mailCredentials)
    _mailMail = _mailCredentials["email"]
    _mailPassword = _mailCredentials["password"]

    return _mailMail, _mailPassword


def sendMail(_mailMail, _mailPassword, _message):
    """Sends an email using SMTP with SSL.

    Args:
        _mailMail (str): The sender's email address.
        _mailPassword (str): The password for the sender's email account.
        _message (str): The message content to be sent.

    Returns:
        str: "success" if the email is sent successfully, or an exception message if an error occurs.
    """
    _host = "smtp.gmail.com"
    _port = 465

    _username = _mailMail
    _password = _mailPassword

    _reciever = "gbppythonapps@gmail.com"
    _context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(_host, _port, context=_context) as server:
            server.login(_username, _password)
            server.sendmail(_username, _reciever, _message.encode("utf-8"))
        return "success"
    except Exception as e:
        return e


newsMail, newsKey = getNewsCredentials()
newsContent = getBusinessNews(newsKey)
mailMail, mailPassword = getSmtpKey()

newsArticles = newsContent["articles"]

body = ""
for article in newsArticles:
    body = f"""\
Subject: Daily news for {datetime.date.today().strftime("%d/%m/%Y")}
{body} {article["title"]}
{article["description"]}


    """

mailStatus = sendMail(mailMail, mailPassword, body)

match mailStatus:
    case "success":
        print("Daily news sent successfully.")

    case _:
        print(f"An error ocurred: {mailStatus}")
