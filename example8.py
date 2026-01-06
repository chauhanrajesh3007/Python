import streamlit as st
import pandas as pd

st.title("Button & Download Demo")

if st.button("Click to Generate sample Marks Data"):
    df=pd.DataFrame({"Enrollment No:":[1,2,3,4],"Marks:":[78,85,69,92]})
    st.write("Generated Data:")
    st.dataframe(df)
    
    csv=df.to_csv(index=False).encode("utf-8")

    st.download_button(
    label="Download as CSV",
    data=csv,
    file_name="sample_marks.csv",
    mime="text/csv")
