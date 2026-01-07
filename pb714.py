import streamlit as st

weight=st.number_input("Enter a weight:")
height=st.number_input("Enter a height:")

if st.button("BMI"):
    BMI=weight/((height/100)**2)
    st.write("BMI Value:",BMI)
    if BMI<18.5:
        st.warning("Underweight")
    elif 18.5<=BMI<=24.9:
        st.success("Normal")
    elif 25<=BMI<=29.9:
        st.warning("Overweight")
    elif BMI>=30:
        st.error("Obese")
