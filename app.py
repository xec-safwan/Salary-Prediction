import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np


data = pd.read_csv('./data/Salary_Data.csv')
lr = LinearRegression()
x=np.array(data["YearsExperience"]).reshape(-1,1)
lr.fit(x,np.array(data["Salary"]))


st.title("Salary Prediction")

nav = st.sidebar.radio("",["Home","Prediction","Contribute to Dataset"])
st.sidebar.image("./data/sal.jpg")
if nav=="Home":
    if st.checkbox('Show Table'):
        st.table(data)
    graph =st.selectbox('Which Type Of Plot?',["Non-InterActive","Interactive"])
    val = st.slider("Filter Data Based on Years",0,20)
    data = data.loc[data["YearsExperience"]>=val]
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
    st.header('Know Your Salary')
    val = st.number_input("Enter Your Experience",0.00,20.00,step=0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]
    if st.button("Predict"):
        st.success(f"Your Predicted Salary is {round(pred)}")
if nav=="Contribute to Dataset":
    st.write('Contribute')
