import streamlit as st

st.set_page_config(
page_title="Faculty Profile",
layout="wide"
)

st.title("Faculty profile demo.")
st.markdown("This is example shows how to use **sidebar,** **expander** and **colums.**")

#Sidebar--important for filters/settings
st.sidebar.header("Profile Settings")
faculty_name=st.sidebar.text_input("Faculty Name: ","Mehul Kodiya")
department=st.sidebar.selectbox("Department",["CE","IT","CSE","MA&CP"])
experience=st.sidebar.slider("Years of experience:",0,40,10)
st.sidebar.markdown("---")
st.write("you can put filters,toggles, etc.in the sidebar")

#Columns 
col1,col2=st.columns([1,2])#1:2 ratio

with col1:
    st.subheader("Basic Info")
    st.write("**Name:**",faculty_name)
    st.write("**Department:**",department)
    st.write("Experience:",experience)

with col2:
    st.subheader("About")
    st.markdown("""
    Use this area to show detail information about
    the faculty member. such as research interests,
    publications and course Handled""")
    
#Expander
with st.expander("Show Course Handle"):
    st.write("Data Structures")
    st.write("Python")
    st.write("FSD")
    st.write("PS")
    st.write("DE")
    
with st.expander("Show Publication"):
    st.write("Research Paper-A")
    st.write("Research Paper-B")
    st.write("Research Paper-C")
