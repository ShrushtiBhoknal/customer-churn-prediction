import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load feature column order
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.title("Customer Churn Prediction App")

st.write("Enter customer details to predict whether the customer is likely to churn.")

# Example Inputs (basic ones for demo)
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)

if st.button("Predict Churn"):

    # Create input dictionary
    input_dict = {col: 0 for col in model_columns}

    # Assign known values (must match actual column names)
    if "tenure" in input_dict:
        input_dict["tenure"] = tenure
    if "MonthlyCharges" in input_dict:
        input_dict["MonthlyCharges"] = monthly_charges
    if "TotalCharges" in input_dict:
        input_dict["TotalCharges"] = total_charges

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure correct column order
    input_df = input_df[model_columns]

    # Make prediction
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is likely to stay.")
