

import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, jsonify

#Initialize Flask App
app = Flask('superkart_app')

#load model 
model = joblib.load("backend_files/superkart_model.joblib")

# Define the route for the API
@app.get('/')
def home():
    return "Welcome to the SuperKart Sales Prediction API"

# Endpoint to predict churn for a customer
@app.post('/predict')
def predict_sales():
    data = request.get_json()

    # Convert the input data into a DataFrame
    sample = {
        'Product_Weight': data['Product_Weight'],
        'Product_Sugar_Content': data['Product_Sugar_Content'],
        'Product_Allocated_Area': data['Product_Allocated_Area'],
        'Product_MRP': data['Product_MRP'],
        'Store_Size': data['Store_Size'],
        'Store_Location_City_Type': data['Store_Location_City_Type'],
        'Store_Type': data['Store_Type'],
        'Product_ID_Type': data['Product_ID_Type'],
        'Store_Age_Years': data['Store_Age_Years'],
        'Product_Type_Category': data['Product_Type_Category'],
        "MRP_x_Area" : data["Product_MRP"] * data["Product_Allocated_Area"],
        "MRP_per_Area" : data["Product_MRP"] / data["Product_Allocated_Area"]
    }

    input_data = pd.DataFrame([sample])

    #Make prediction
    prediction = model.predict(input_data).tolist()[0]

    #Return the prediction as a JSON response
    return jsonify({"Sales": prediction})

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
