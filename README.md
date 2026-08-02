# churn-prediction-app
## **Name:** Meenu K S
## **MUID:** meenuks@mulearn

## Live Deployment
https://churn-prediction-app-znjyevj47b2n5esyzmmab5.streamlit.app/

---

## Overview
This project is part of the Epochs Data Science program (Day 9 Assignment). It features a fully deployed interactive web application built with Python and **Streamlit** that predicts whether a customer is likely to churn based on their demographic and account details. The underlying machine learning model is an optimized **Random Forest Classifier** trained on customer churn data.
---

## Challenges Faced
- **Feature Alignment:** Ensuring the exact feature order and encoding scheme (for categorical variables such as Gender, Subscription Type, and Contract Length) remained consistent between the Google Colab training notebook and the Streamlit application.
- **Deployment Optimization:** Streamlining the `requirements.txt` file to include only the essential production libraries for smooth deployment on Streamlit Community Cloud.

---

## Key Observations
- Customers with frequent support calls and payment delays generally have a higher probability of churning.
- Long-term contracts and higher customer engagement tend to reduce churn risk.
- Deploying the trained model through Streamlit enables real-time predictions with a simple and interactive user interface.

---

## Future Improvements
- Add data visualizations such as feature importance charts and prediction analytics.
- Implement batch prediction using CSV file uploads.
- Enhance input validation and user feedback.
- Deploy future versions with model monitoring and automatic retraining.
