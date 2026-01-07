import streamlit as st
import pandas as pd

st.title("Displaying Data in Streamlit")

data={"Students":["ABC","DEF","GHI","JKL"],"Marks":[85,92,76,88],"Passed":[True,True,True,True]}

df=pd.DataFrame(data)

st.subheader("Stramlit DataFrame")
st.dataframe(df)

st.subheader("Stramlit Table")
st.table(df)

st.subheader("Stramlit JSON")
st.json(data)
