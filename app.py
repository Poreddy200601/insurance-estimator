import streamlit as st
from utils.model_utils import predict_cost

st.set_page_config(page_title="Insurance Cost Estimator", page_icon="💰")

st.title("💰 Medical Insurance Cost Estimator")

st.write("Enter the details below to estimate insurance cost:")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

if st.button("Estimate Cost"):
    input_data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }
    cost = predict_cost(input_data)
    st.success(f"💡 Estimated Insurance Cost: ₹{cost}")


