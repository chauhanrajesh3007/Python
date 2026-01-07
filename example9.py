import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Mathplotlib + Streamlit Demo")

#Sample Data
x=np.arange(1,11)
y=np.random.randint(50,100,size=10)

#Line Chart
plt.figure(figsize=(6,4))
plt.plot(x,y)
plt.xlabel("Student index")
plt.ylabel("Student marks")
plt.title("Marks of 10 students")
st.pyplot(plt)
plt.clf()##-->clear the avoid overlap

st.subheader("Bar Chart")
plt.bar(x,y)
plt.xlabel("Student index")
plt.ylabel("Student marks")
plt.title("Marks of 10 students")
st.pyplot(plt)
plt.clf()

st.subheader("Scatter")
plt.figure(figsize=(6,4))
plt.scatter(x,y)
plt.xlabel("Student index")
plt.ylabel("Student marks")
plt.title("Marks of 10 students")
st.pyplot(plt)
plt.clf()

st.subheader("hystrogram")
plt.figure(figsize=(6,4))
plt.hist(x)
plt.xlabel("Student index")
plt.ylabel("Student marks")
plt.title("Marks of 10 students")
st.pyplot(plt)
plt.clf()
