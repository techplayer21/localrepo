import streamlit as st
import pickle
import pandas as pd
import numpy as np

# 1. Load your saved model
try:
    with open('house_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")

# 2. Set up the Web Page UI
st.title("🏡 House Price Predictor")
st.write("Enter house details to get an estimated price.")

# 3. Create Input Fields
sqft = st.number_input("Square Footage", min_value=500, max_value=10000, value=1500)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 5, 2)

# 4. Predict Button
if st.button("Predict Price"):
    try:
        # IMPORTANT: These column names MUST match your CSV exactly.
        # If your model crashes, try changing 'sqft_living' to 'SquareFootage' etc.
        features = pd.DataFrame({
            'sqft_living': [sqft],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms]
        })

        # 5. Make Prediction
        prediction = model.predict(features)
        
        # 6. Display the result (Properly Indented)
        st.success(f"The estimated price for this house is: ${prediction[0]:,.2f}")
        
    except ValueError as e:
        st.error(f"Feature Mismatch: {e}")
        st.write("Check if your training data used different column names.")