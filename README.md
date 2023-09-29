# Loan-Prediction-Application-Deployment

## Overview
The Loan Prediction Application is a web-based tool that uses a logistic regression model to predict loan approval or rejection based on various applicant features. This project was developed using Python, Flask, HTML, and machine learning libraries. The dataset for training the model was sourced from Kaggle, and data exploratory analysis was performed to prepare and understand the data.

## Key Features
 Predicts loan approval or rejection for applicants.  
 Utilizes logistic regression machine learning model.  
 Additional models like Decision Tree Classifier and Random Forest Classifier were also explored.  
 Achieved an accuracy score of 84.72% with the logistic regression model.  
 
## Models
Three machine learning models were trained for this project: 

Logistic Regression: Achieved an accuracy of 84.72%.  
Decision Tree Classifier: Achieved an accuracy of 77.78%.  
Random Forest Classifier: Achieved an accuracy of 83.33%.  
The logistic regression model was selected for deployment due to its superior performance.  

## Usage
Enter applicant details in the web form provided.  
Click the "Predict" button to obtain a loan prediction result.  
The result will display whether the loan is approved or rejected.  

## Model Deployment
The logistic regression model is deployed using Flask. The model is serialized using Pickle and loaded for real-time predictions.  

Contributors
Ali Yaqteen (aliyaqteenbirmani512@gmail.com)
