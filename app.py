import streamlit as st
import pandas as pd

st.title("Salary Prediction")

nav = st.sidebar.radio("",["Home","Prediction","Contribute to Dataset"])
st.sidebar.image("./data/sal.jpg")
if nav=="Home":
    st.write("")

if nav=="Prediction":
    st.write('Prediction')

if nav=="Contribute to Dataset":
    st.write('Contribute')
