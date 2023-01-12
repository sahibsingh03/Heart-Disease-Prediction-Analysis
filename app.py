
import streamlit as st
import pandas as pd
import prediction
from PIL import Image

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)



padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)



st.sidebar.title("Heart Disease Analysis & Prediction")
df=pd.read_csv("heart.csv")
name = st.text_input('Please enter your name', '')
if name=="":
    name="User"
age = st.slider('How old are you?', 20, 80, 40)


st.text("")
s = st.selectbox(
    'Please specify your gender',
    ('Male', 'Female'))
if s=="Male":
    sex=1
else:
    sex=0


st.text("")
chestpain = st.selectbox(
    'Please specify your Chest pain type',
    ("TA: Typical Angina", "ATA: Atypical Angina", "NAP: Non-Anginal Pain","ASY: Asymptomatic"))

if chestpain=="TA: Typical Angina":
    cp=0
elif chestpain=="ATA: Atypical Angina":
    cp=1
elif chestpain=="NAP: Non-Anginal Pain":
    cp=2
else:
    cp=3



st.text("")
trestbp = st.slider('Please specify your Resting Blood Pressure', 40, 240, 100)



st.text("")
chol = st.slider('Please specify your Cholestrol', 0, 620, 200)


st.text("")
fastbp = st.selectbox(
    'Please specify your Fasting Blood Sugar',
    ("More than 120 mg/dl", "Less than or equal to 120 mg/dl"))

if fastbp==">120mg/dl":
    fbp=1
else:
    fbp=0


st.text("")
restingecg=st.selectbox(
    'Please specify your Resting ECG',
    ("Normal", "Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)"," Showing probable or definite left ventricular hypertrophy by Estes' criteria"))
if restingecg=="Normal":
    restecg=0
elif restingecg=="Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)":
    restecg=1
else:
    restecg=2




st.text("")
thalach = st.slider('Please specify your Maximum Heart Rate Achieved', 60, 202, 100)


st.text("")
exangg = st.selectbox(
    'Exercise-Induced Angina ?',
    ("Yes", "No"))
if exangg=="Yes":
    exang=1
else:
    exang=0


st.text("")
oldpeak = st.slider('Oldpeak', 0.0, 5.0, 2.5)



st.text("")
slope=st.slider('The slope of the peak exercise ST segment', 0, 2, 1)


st.text("")
ca=st.slider('Number of major vessels (0-3) colored by flourosopy', 0, 4, 2)


st.text("")
thall=st.selectbox(
    'thal',
    ("Normal", "Fixed defect","Reversable defect"))
if thall=="normal":
    thal=1
elif thall=="fixed defect":
    thal=2
else:
    thal=3


if st.sidebar.button("Predict Heart Disease"):

    predictor=prediction.predict(age,sex,cp,trestbp,chol,fbp,restecg,thalach,exang,oldpeak,slope,ca,thal)
    if predictor[0] == 0:
        st.subheader('Dear '+name+"! According to our calculations, you don't seem to have any Heart disease.")
    else:
        st.subheader("Dear "+name+"! According to our calculations, you might have heart disease. Please contact a doctor.")





if st.sidebar.button("Show Analysis"):
    image1 = Image.open('21f89a45-278e-40f4-b21a-13e1660e311c.jpg')
    image2 = Image.open('81040e79-d12c-4592-aeee-61ab026d4231.jpg')
    image3 = Image.open('965830b8-f9e5-4455-8cdd-5f6d92b5750e.jpg')
    image4 = Image.open('50745832-5e3b-463a-b826-014d9dfb4f31.jpg')
    st.title("Analysing on the basis of ")
    st.image(image4, caption='Sex')
    st.header(" ")
    st.image(image1, caption='Chest pains')
    st.header(" ")
    st.image(image2, caption='Blood Sugar Level')
    st.header(" ")
    st.image(image3, caption='Exercise Angina')
