import os
import joblib
import pandas as pd

# Load the model using absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
model_path = os.path.join(PROJECT_ROOT, "insurance_model.pkl")

model = joblib.load(model_path)

def predict_cost(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return round(prediction[0], 2)
