import streamlit as st
import pandas

import mail_sender

topics = pandas.read_csv("./topics.csv")['topic']

with st.form("contact"):
    email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?", topics)
    text = st.text_area("Text")
    submitted = st.form_submit_button("Submit")

    if submitted:
        message = f"""\
Subject: Email from ExampleCompanyWebsite

From: {email}
Topic: {topic}
{text}"""
        is_sent = mail_sender.send_email(message)
        if is_sent:
            st.write("Email was sent")
        else:
            st.write("There were a problem with sending Your email. "
                     "Please try again later")
