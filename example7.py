import streamlit as st

st.title("Media Display Demo")

st.subheader("Image Example")
st.image("Image.jpg",use_container_width=True)

st.subheader("Audio Example")
st.audio("video.mp3")

st.subheader("Video Example")
st.video("samplevideo.mp4")
