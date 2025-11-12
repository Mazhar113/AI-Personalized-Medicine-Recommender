
import joblib
import pandas as pd

def recommend_treatment(patient_data):
    model = joblib.load("models/trained_model.pkl")
    prediction = model.predict(pd.DataFrame([patient_data]))[0]
    if prediction == "High Risk":
        return "Recommend genetic consultation and alternative drug plan."
    elif prediction == "Medium Risk":
        return "Adjust dosage and monitor vitals daily."
    else:
        return "Proceed with standard treatment and lifestyle guidance."
