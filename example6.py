import streamlit as st
from datetime import date,time

st.title("Date Time and Uploader Demo")

exam_date=st.date_input("Select Exam Date:",value=date.today())

start_time=st.time_input("Exam start time:",value=time(9,0))

uploaded_file=st.file_uploader("Upload CSV file:",type=["csv"])

st.write("Live Output")
st.write("**exam_date:**",exam_date)
st.write("**start_time:**",start_time)
if uploaded_file is not None:
    st.success("File Uploaded Successfully.!!")
    st.write("File Name:",uploaded_file.name)
    st.write("File Type:",uploaded_file.type)
