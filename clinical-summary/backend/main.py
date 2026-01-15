from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data_loader import get_patient_data
from llm import generate_summary

app = FastAPI(
    title="Clinical Summary Generator API",
    description="Generates evidence-based clinical summaries from EHR CSV data",
    version="1.0.0"
)

class SummaryRequest(BaseModel):
    patient_id: int

@app.post("/generate_summary")
def generate_clinical_summary(request: SummaryRequest):
    patient_id = request.patient_id

    # Fetch patient data
    patient_data = get_patient_data(patient_id)

    # Check if any data exists
    if not any(len(v) > 0 for v in patient_data.values()):
        raise HTTPException(
            status_code=404,
            detail=f"No clinical data found for patient_id {patient_id}"
        )

    # Generate LLM summary
    summary = generate_summary(patient_data)

    return {
        "patient_id": patient_id,
        "summary": summary.get("summary", [])
    }
