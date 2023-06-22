import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Salary Predictor', page_icon='./data/favicon.ico')
data = pd.read_csv('./data/Salary_Data.csv')
lr = LinearRegression()
x=np.array(data["YearsExperience"]).reshape(-1,1)
lr.fit(x,np.array(data["Salary"]))


st.title("Salary Predictor")
# st.sidebar.title("Dashboard")
# nav = st.sidebar.radio("",["Home","Prediction","Contribute to Dataset"])
nav = option_menu(
    menu_title=None,
    options=["Home","Prediction","Contribute to Dataset"],
    icons=["house","cash-stack","bag-check"],
    default_index=0,
    orientation="horizontal"
)
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
        st.success(f"Your Predicted Salary is RS. {round(pred)}")
if nav=="Contribute to Dataset":
    st.header('Contribute to our dataset')
    ex = st.number_input("Enter Years of Experience",0.00,20.00,step=0.5)
    sal = st.number_input("Enter Your Salary",0.00,100000.0,step=1000.0)
    if st.button('Submit'):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add=pd.DataFrame(to_add)
        to_add.to_csv('./data/Salary_Data.csv',mode='a',header=False,index=False)
        st.success('Sucessfully submitted')