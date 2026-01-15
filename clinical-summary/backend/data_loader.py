import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_csv(filename):
    path = DATA_DIR / filename
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()

# Load all tables once (simulate DB tables)
diagnoses_df = load_csv("diagnoses.csv")
medications_df = load_csv("medications.csv")
vitals_df = load_csv("vitals.csv")
notes_df = load_csv("notes.csv")
wounds_df = load_csv("wounds.csv")
oasis_df = load_csv("oasis.csv")

def filter_by_patient(df, patient_id):
    if df.empty:
        return []
    return df[df["patient_id"] == patient_id].to_dict(orient="records")

def get_patient_data(patient_id: int):
    return {
        "diagnoses": filter_by_patient(diagnoses_df, patient_id),
        "medications": filter_by_patient(medications_df, patient_id),
        "vitals": filter_by_patient(vitals_df, patient_id),
        "notes": filter_by_patient(notes_df, patient_id),
        "wounds": filter_by_patient(wounds_df, patient_id),
        "oasis": filter_by_patient(oasis_df, patient_id),
    }
