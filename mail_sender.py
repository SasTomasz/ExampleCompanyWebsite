import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

host = "smtp.gmail.com"
port = 587
mail_sender = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")
mail_receiver = os.getenv("EMAIL_RECEIVER")


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

