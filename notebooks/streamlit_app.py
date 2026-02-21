import streamlit as st
import pickle
import numpy as np
import pandas as pd

# 1. Load your saved model
try:
    with open('house_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file 'house_model.pkl' not found. Ensure it is pushed to GitHub.")

# 2. Set up the Web Page UI
st.title("🏡 House Price Predictor")
st.write("Enter the details of the house below to get an estimated price.")

# 3. Create Input Fields (Adjust these based on your specific model's features)
# Example: If your model was trained on Square Footage, Bedrooms, and Bathrooms
sqft = st.number_input("Square Footage", min_value=500, max_value=10000, value=1500)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 5, 2)

# 4. Predict Button
if st.button("Predict Price"):
    # Arrange inputs into the format your model expects (usually a 2D array)
# Ensure this is at the top or here

# Create a DataFrame to match the model's training format
 features = pd.DataFrame({
    'sqft_living': [sqft],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms]
})

prediction = model.predict(features)
    
    # Display the result
st.success(f"The estimated price for this house is: ${prediction[0]:,.2f}")
