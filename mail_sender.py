import smtplib
import ssl
import streamlit as st

host = "smtp.gmail.com"
port = 587
mail_sender = st.secrets["EMAIL_SENDER"]
password = st.secrets["PASSWORD"]
mail_receiver = st.secrets["EMAIL_RECEIVER"]


def send_email(message):
    try:
        session = smtplib.SMTP(host, port)
        context = ssl.create_default_context()
        session.starttls(context=context)
        session.login(mail_sender, password)
        session.sendmail(mail_sender, mail_receiver, message)
        session.quit()
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    msg = """\
Subject: Mail from ExampleCompanyWebsite [TEST]
I just checking there is no problem with email sender"""
    send_email(msg)

