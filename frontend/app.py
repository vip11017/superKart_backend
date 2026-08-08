
import streamlit as st
import requests
st.title("SuperKart Sales Prediction")

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, value=1.0)
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=147.03)
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Departmental Store", "Supermarket Type1", "Supermarket Type2"])
Product_Id_Type = st.selectbox("Product ID Type", ["FD", "DR", "NC"])
Store_Age_Years = st.number_input("Store Age in Years", min_value=0, value=10)
Product_Type_Category = st.selectbox("Product Type Category", ["Perishables", "Non Perishables"])

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_Type": Product_Id_Type,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category,
}
#Add the 2 calculated fields to the product_data dictionary
product_data["MRP_x_Area"] = product_data["Product_MRP"] * product_data["Product_Allocated_Area"]
product_data["MRP_per_Area"] = product_data["Product_MRP"] / product_data["Product_Allocated_Area"]

if st.button("Predict", type="primary"):
    response = requests.post("https://obscure-engine-7qpwg954rxg3p9xw-7860.app.github.dev/predict", json=product_data)
    if response.status_code == 200:
        prediction = response.json()["Sales"]
        st.success(f"Predicted Sales: ${prediction: .2f}")
    else:
        st.error("Error in prediction. Please try again.")
