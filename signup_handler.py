import streamlit as st
import os

def save_email(email):
    # TODO:
    with open("emails.txt", "a") as file:
        file.write(email + "\n")

def main():
    st.title("Sign Up for Our Newsletter")
    email = st.text_input("Email:", key="email")
    if st.button("Sign Up"):
        save_email(email)
        st.success("You have successfully signed up!")

def initialize():
    st.title("")