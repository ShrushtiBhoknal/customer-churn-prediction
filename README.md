# Customer Churn Prediction

## Project Overview

This project predicts whether a customer is likely to leave (churn) or stay with a telecom company.
The goal is to help businesses identify customers who may leave so they can take action early and reduce revenue loss.

## Problem Statement
Customer churn is a major challenge for telecom companies.
If we can predict which customers are likely to churn, the company can:
- Improve customer retention  
- Offer targeted discounts  
- Improve customer satisfaction  
This project builds a machine learning model to solve that problem.

## Dataset
- Dataset: Telco Customer Churn Dataset  
- Total records: 7,043 customers  
- Features include:
  - Customer demographics  
  - Contract type  
  - Monthly charges  
  - Tenure  
  - Services used
    

## Steps Followed

1. Data Cleaning  
   - Handled missing values  
   - Converted TotalCharges to numeric  
   - Removed customerID column  

2. Feature Engineering  
   - Applied one-hot encoding to categorical variables  

3. Data Splitting  
   - 80% training data  
   - 20% testing data  

4. Model Building  
   - Logistic Regression  
   - Random Forest  

5. Model Evaluation  
   Models were compared using:
   - Accuracy  
   - Precision  
   - Recall  
   - F1 Score  

6. Model Selection  
   Logistic Regression was selected as the final model because it provided better recall and F1 score, which are important in churn prediction.

7. Deployment  
   A simple Streamlit web application was created to allow users to input customer details and predict churn.

## Model Performance

### Logistic Regression
- Accuracy: ~78%  
- Precision: ~62%  
- Recall: ~52%  
- F1 Score: ~56%  

### Random Forest
- Accuracy: ~79%  
- Precision: ~64%  
- Recall: ~48%  
- F1 Score: ~55%  

Since recall is important in churn prediction (to identify as many potential churn customers as possible), Logistic Regression was selected.

## How to Run the Project

Install required libraries:

```
pip install -r requirements.txt
```

Run the Streamlit app:

```
streamlit run app.py
```

## Project Structure

- app.py  
- churn_model.pkl  
- model_columns.pkl  
- requirements.txt  
- README.md  

## Key Learning
- Understanding business problems before modeling  
- Importance of recall in churn prediction  
- Comparing multiple models  
- Deploying ML models using Streamlit  

