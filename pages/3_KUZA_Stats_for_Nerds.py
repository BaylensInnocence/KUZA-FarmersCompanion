import streamlit as st
import tensorflow as tf
import pandas as pd


model = tf.keras.models.load_model("full_model.keras")

st.header("_Model Overview_")
st.write("This goes out to my slightly more cultured compatriots, a slightly more in depth view of the model I trained.")

df = pd.read_csv("Out_13.csv")
df.drop(df.columns[df.columns.str.contains(
    'unnamed', case=False)], axis=1, inplace=True)

df.set_index(df.columns[0], inplace=True)
st.dataframe(df)

st.write("KUZA's predictive model is a custom image convolution model, trained on about 42000 images of crops")
st.write("The model was trained over 7 epochs and took a total of 7 hours to train, achieving a whopping 91% validation accuracy")
st.write("During production, I chose MobileNetV2 over other Imagenet bases like Inception V3 (which has a higher accuracy) to reduce the latency, thus decrease the time the model takes to return a prediction")
st.write("In recompense, I trained the model over 20 epochs initially and settling on the model weights saved after epoch 7")
st.write("The model was not fine-tuned at all, which I will consider doing as I get to add more classes and retrain my model in the future")

st.sidebar.header("KUZA Farmer's Companion 🧑‍🌾")
st.sidebar.subheader("By Baylen Chalopa - Data Scientist🧑‍💻")
st.sidebar.subheader("Contact me here: +254706574724")
st.sidebar.subheader("Email me at: baylenchalopa@gmail.com")
