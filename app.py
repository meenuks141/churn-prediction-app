import pickle
import numpy as np
import streamlit as st

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("📊 Customer Churn Prediction App")
st.write(
    "Enter the customer details below to predict if they are likely to churn."
)

# Input fields matching your churn dataset features
gender = st.selectbox("Gender", ["Male", "Female"])
subscription_type = st.selectbox(
    "Subscription Type", ["Basic", "Standard", "Premium"]
)
contract_length = st.selectbox(
    "Contract Length", ["Monthly", "Quarterly", "Annual"]
)

tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input(
    "Monthly Charges ($)", min_value=0.0, value=50.0
)
total_charges = st.number_input(
    "Total Charges ($)", min_value=0.0, value=600.0
)

# Prediction button
if st.button("Predict Churn"):
  # Note: Ensure encoding here matches how you preprocessed data in Colab (or pass standard mapped values)
  # For a quick prototype, passing numerical inputs directly:
  input_data = np.array(
      [[tenure, monthly_charges, total_charges]]
  )  # Adjust features as trained

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