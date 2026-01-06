import streamlit as st

#Page setup
st.set_page_config(
page_title="Hello Streamlit",
layout="centered"
)

#Title & text
st.title("welcome to streamlit")
st.header("This is headers")
st.subheader("This is subheader")
st.text("This Function is use for simple fixed width text")
st.write("Write somethings like text,number or dataframe")
st.markdown("**Rich Text**")

#Display python code snippet
code_example="""
def add(a,b):
    return a+b
result=add(5,7)
print(result)
"""

st.code(code_example,language="python")
