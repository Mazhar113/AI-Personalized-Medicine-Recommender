
import streamlit as st
from src.recommender import recommend_treatment

st.set_page_config(page_title="AI Personalized Medicine Recommender", layout="wide")
st.title("🧬 AI-Powered Personalized Medicine Recommender")
st.write("Provide patient details to get a personalized treatment recommendation:")

age = st.number_input("Patient Age", 0, 120)
blood_pressure = st.number_input("Blood Pressure (mmHg)")
glucose = st.number_input("Glucose Level (mg/dL)")
cholesterol = st.number_input("Cholesterol Level (mg/dL)")
heart_rate = st.number_input("Heart Rate (bpm)")

if st.button("Get Recommendation"):
    patient_data = {
        "age": age,
        "blood_pressure": blood_pressure,
        "glucose": glucose,
        "cholesterol": cholesterol,
        "heart_rate": heart_rate
    }
    result = recommend_treatment(patient_data)
    st.success(f"Recommended Plan: {result}")
