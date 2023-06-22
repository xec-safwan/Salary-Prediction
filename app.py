import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import plotly.express as px

st.title("Salary Prediction")
data = pd.read_csv('./data/Salary_Data.csv')

nav = st.sidebar.radio("",["Home","Prediction","Contribute to Dataset"])
st.sidebar.image("./data/sal.jpg")
if nav=="Home":
    if st.checkbox('Show Table'):
        st.table(data)
    graph =st.selectbox('Which Type Of Plot?',["Non-InterActive","Interactive"])

    if graph=="Non-InterActive":
        plt.figure(figsize=(10,5))
        plt.scatter(data['YearsExperience'],data['Salary'])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    if graph=="Interactive": 
        fig = px.scatter(data, x="YearsExperience", y="Salary")
        st.plotly_chart(fig)
if nav=="Prediction":
    st.write('Prediction')

if nav=="Contribute to Dataset":
    st.write('Contribute')
