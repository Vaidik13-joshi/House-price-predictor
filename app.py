import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("🏠 House Price Prediction")

longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("House Age")
total_rooms = st.number_input("Total Rooms")
total_bedrooms = st.number_input("Total Bedrooms")
population = st.number_input("Population")
households = st.number_input("Households")
median_income = st.number_input("Median Income")

if st.button("Predict Price"):
    data = np.array([[longitude, latitude, housing_median_age,
                      total_rooms, total_bedrooms,
                      population, households, median_income]])

    prediction = model.predict(data)[0]

    st.success(f"Estimated Price: ₹{round(prediction, 2)}")