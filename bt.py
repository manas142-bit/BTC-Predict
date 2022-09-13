import tensorflow as tf
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("BTC-USD.csv")
model=tf.keras.models.load_model("model.h5")

st.header("BTC Predictor")
d = st.date_input("2016-07-09")
st.dataframe(df[df["Date"] >= str(d)])

arr=np.array([df[df["Date"] >= str(d)][-7:]["Close"]])


if st.button('Predict'):
     st.write(model.predict(arr)[0][0])
else:
     st.write('Predicted value')
