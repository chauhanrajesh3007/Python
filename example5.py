import streamlit as st

st.title("Selection Demo")
course=st.selectbox("Select Course:",["PS","DE","Python","FSD"])
preferred_days=st.multiselect(
"Preferred days for extra lecture",
["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
delivery_mode=st.radio("Preferred Delivery Mode",["Online","Offline","Hybrid"])
subscribe=st.checkbox("Subscribe to course updates!!")

st.write("Live Output")
st.write("**Course:**",course)
st.write("**Days:**",",".join(preferred_days) if preferred_days else "None")
st.write("**Mode:**",delivery_mode)
st.write("**subscribe:**","Yes" if subscribe else "No")
