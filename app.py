# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Churn Prediction", layout="centered")
st.title("Churn Prediction")

st.markdown("Upload a CSV with customer features or use the sample inputs to predict churn.")

# Example inputs (adapt to your features)
col1, col2 = st.columns(2)
with col1:
    tenure = st.number_input("tenure", min_value=0, value=12)
    monthly_charges = st.number_input("monthly_charges", min_value=0.0, value=50.0)
with col2:
    total_charges = st.number_input("total_charges", min_value=0.0, value=500.0)
    has_partner = st.selectbox("Has partner", ["No", "Yes"])

if st.button("Predict"):
    # Replace with your actual preprocessing & model loading/prediction
    try:
        model = joblib.load("model.joblib")
        # dummy features conversion — adapt to your model
        X = pd.DataFrame([{
            "tenure": tenure,
            "monthly_charges": monthly_charges,
            "total_charges": total_charges,
            "has_partner": 1 if has_partner == "Yes" else 0
        }])
        pred = model.predict(X)
        st.success(f"Prediction: {pred[0]}")
    except Exception as e:
        st.error(f"Model load/predict failed: {e}\nMake sure model.joblib exists in repo or is created at runtime.")

