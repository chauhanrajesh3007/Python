import streamlit as st
import time

st.title("Status Element Demo")
st.success("This is a success massage.")
st.warning("This is a warning massage.")
st.error("This is a error massage.")
st.info("User Information can go here")

st.write("---")

st.subheader("Progress and Spinner Example")

if st.button("Start Long Task"):
    progress=st.progress(0)
    with st.spinner("Processing...."):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)
    st.success("Task Compeleted")
