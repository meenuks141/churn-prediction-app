import pickle
import numpy as np
import streamlit as st
model = pickle.load(open("model.pkl", "rb"))
st.title("📊 Customer Churn Prediction App")
st.write(
    "Enter the customer details below to predict if they are likely to churn."
)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
usage_frequency = st.number_input(
    "Usage Frequency", min_value=0, max_value=50, value=10
)
support_calls = st.number_input(
    "Support Calls", min_value=0, max_value=20, value=1
)
payment_delay = st.number_input(
    "Payment Delay (Days)", min_value=0, max_value=30, value=0
)
total_spend = st.number_input(
    "Total Spend ($)", min_value=0.0, value=500.0
)
last_interaction = st.number_input(
    "Last Interaction (Days ago)", min_value=0, max_value=365, value=5
)
gender = st.selectbox("Gender", ["Male", "Female"])
gender_val = 1 if gender == "Male" else 0
subscription_type = st.selectbox(
    "Subscription Type", ["Basic", "Standard", "Premium"]
)
sub_mapping = {"Basic": 0, "Standard": 1, "Premium": 2}
sub_val = sub_mapping[subscription_type]
contract_length = st.selectbox(
    "Contract Length", ["Monthly", "Quarterly", "Annual"]
)
contract_mapping = {"Monthly": 0, "Quarterly": 1, "Annual": 2}
contract_val = contract_mapping[contract_length]
if st.button("Predict Churn"):
  input_data = np.array([[
      age,
      gender_val,
      tenure,
      usage_frequency,
      support_calls,
      payment_delay,
      sub_val,
      contract_val,
      total_spend,
      last_interaction,
  ]])
  prediction = model.predict(input_data)
  prediction_proba = model.predict_proba(input_data)
  if prediction[0] == 1:
    st.error(
        f"⚠️ **High Risk:** This customer is likely to churn! (Probability:"
        f" {prediction_proba[0][1]*100:.2f}%)"
    )
  else:
    st.success(
        f"✅ **Low Risk:** This customer is likely to stay. (Probability:"
        f" {prediction_proba[0][0]*100:.2f}%)"
    )