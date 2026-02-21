import streamlit as st
import pickle
import pandas as pd
import numpy as np

# 1. Load the model
with open('noteboks/house_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏡 California House Price Predictor")

# 2. User Inputs (The ones you already have)
sqft = st.number_input("Average Rooms (was sqft)", value=5.0)
bedrooms = st.number_input("Average Bedrooms", value=1.0)
occupancy = st.number_input("Average Occupancy", value=3.0)

# 3. Predict Button
if st.button("Predict Price"):
    # 4. Create the EXACT 8 columns the model expects
    features = pd.DataFrame({
        'MedInc': [5.0],        # Placeholder Median Income
        'HouseAge': [30.0],     # Placeholder House Age
        'AveRooms': [sqft],     # Using your input
        'AveBedrms': [bedrooms], # Using your input
        'Population': [1000.0], # Placeholder
        'AveOccup': [occupancy], # Using your input
        'Latitude': [34.0],     # Placeholder
        'Longitude': [-118.0]   # Placeholder
    })

    prediction = model.predict(features)
    # California prices are usually in $100,000s
    st.success(f"Estimated Price: ${prediction[0] * 100000:,.2f}")