
import pandas as pd

def load_and_merge_data():
    ehr_data = pd.read_csv("data/mimic_patient_data.csv")
    genetic_data = pd.read_csv("data/genetic_variants.csv")
    wearable_data = pd.read_csv("data/wearable_data.csv")

    merged = ehr_data.merge(genetic_data, on="patient_id", how="left")
    merged = merged.merge(wearable_data, on="patient_id", how="left")
    merged.fillna(method='ffill', inplace=True)
    return merged
