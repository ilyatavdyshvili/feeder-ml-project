import streamlit as st
import joblib
import numpy as np

model = joblib.load("model/linear_regression_model_with_ma.pkl")

st.title("Feeder Production Prediction")

f1 = st.number_input("Feeder 1")
f2 = st.number_input("Feeder 2")
f3 = st.number_input("Feeder 3")

if st.button("Predict"):
    X = np.array([[f1, f2, f3]])
    pred = model.predict(X)[0]
    st.write(f"Prediction: {pred}")
