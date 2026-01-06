import streamlit as st

st.set_page_config(
page_title="Text Input Demo")

name=st.text_input("Enter Your Name:")
comments=st.text_area("Enter Your Feedback or Comment")

st.write("Live Output")
if name:
    st.write("**Name:**",name)
if comments:
    st.write("**Comments:**",comments)
