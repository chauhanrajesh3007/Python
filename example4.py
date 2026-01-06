import streamlit as st

st.set_page_config(
page_title="Number Input Demo")

age=st.number_input("Enter a number:",0,100,25)
rating=st.slider("Years of experience:",0,10)

st.write("Live Output")
st.write("**Age:**",age)
st.write("**Rating:**",rating)
