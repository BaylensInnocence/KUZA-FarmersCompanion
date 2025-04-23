import streamlit as st
import pandas as pd

st.header("_Welcome to *KUZA*, The Farmer's Companion app for Kenyan farmers_ 🧑‍🌾")
st.write(" *KUZA* is a predictive model meant to help farmers identify anomalies in their crops -including pests and diseases- of some of the more common crops grown locally, whether small or large scale 🔍")
# short desc.

st.subheader("_INSPIRATIONS AND GOALS OF *KUZA* 🌍:_ ")

st.write(" *KUZA* was created in a bid to push for the achievement and maintenance of SDG goal number two, Zero Hunger.")
st.write("This is achieved by using high-level machine learning techniques to create a model that can predict whether a plant is healthy or not, simply from a photo.")
st.write("In this way, *KUZA* aims to aid the farmer in identifying potential threats to their yield, the threat level, causes, treatments and preventive measures.")
st.write("In the end, the farmers yield quantity and quality is spared and that -down the supply chain- leads to higher food production and overall, a slight push in the direction of Zero Hunger. 📈")
# talk about sdg no. 2 (inspiration)


st.subheader("_HOW *KUZA* WORKS :_")

st.write("Under the hood, *KUZA* has a custom and complex pre-trained computer Vision model that separates an uploaded image into one of 42 classes, with an astonishing accuracy of *91%* . 🙆")
st.write(" *KUZA* will then diagnose the crop, list the threat level of the disease while highlighting the symptoms that the farmer should check for, thereafter suggesting treatments and preventive measures. 🧑‍⚕️")
# st.write("") #describe the apps apparent functions (prediction and cure recommendations)

st.sidebar.header("KUZA Farmer's Companion 🧑‍🌾")
st.sidebar.subheader("By Baylen Chalopa - Data Scientist🧑‍💻")
st.sidebar.subheader("Contact me here: +254706574724")
st.sidebar.subheader("Email me at: baylenchalopa@gmail.com")



