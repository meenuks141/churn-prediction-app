import pickle
import numpy as np
import streamlit as st

model = pickle.load(open("model.pkl", "rb"))

st.title("📊 Customer Churn Prediction App")
st.write(
    "Enter the customer details below to predict if they are likely to churn."
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
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input(
    "Monthly Charges ($)", min_value=0.0, value=50.0
)
total_charges = st.number_input(
    "Total Charges ($)", min_value=0.0, value=600.0
)
if st.button("Predict Churn"):
  input_data = np.array(
      [[gender_val, sub_val, contract_val, tenure, monthly_charges, total_charges]]
  )
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