import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

st.title("💳 Credit Risk Predictor Using Alt Data")
st.write("Fill in the details below:")

# User Inputs
posts = st.number_input("Posts Per Day", 0)
likes = st.number_input("Likes per Post", 0)
calls = st.number_input("Call Minutes", 0)
data_used = st.number_input("Data Used (GB)", 0.0)
late = st.number_input("Late Payments", 0)
on_time = st.number_input("On-time Payments", 0)
bills = st.number_input("Average Bill Amount", 0)

# Feature Engineering
engagement = posts * likes
payment_ratio = on_time / (late + 1)
usage_index = data_used + (calls / 60)

# Create input dataframe
X = pd.DataFrame([[posts, likes, calls, data_used, late, on_time, bills,
                   engagement, payment_ratio, usage_index]],
    columns=["posts_per_day", "likes_per_post", "call_minutes", "data_used_gb",
             "late_payments", "on_time_payments", "bill_amount_avg",
             "engagement", "payment_ratio", "usage_index"]
)

# Prediction
if st.button("Predict"):
    pred = model.predict(X)
    st.success("Prediction: **{}**".format("High Risk 🔴" if pred[0] == 1 else "Low Risk 🟢"))
