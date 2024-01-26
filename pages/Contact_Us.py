import streamlit as st
import pandas

# TODO: Get topics as a list
topics = [x for x in pandas.read_csv("./topics.csv").iterrows()]
print(topics)

with st.form("contact"):
    email = st.text_input("Your Email Address")
    topic = "What topic do you want to discuss?"
    message = st.text_area("Text")
    submitted = st.form_submit_button("Submit")

    if submitted:
        is_sent = True  # TODO Send an email - create a func
        if is_sent:
            st.write("Email was sent")
        else:
            st.write("There were a problem with sending Your email. "
                     "Please try again later")