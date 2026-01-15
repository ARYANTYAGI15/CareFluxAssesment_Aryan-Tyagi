# Clinical Summary Generator
**Assessment Project — CareFlux Analytics**

## 📌 Overview

This is a **Clinical Summary Generator** application built as part of a take-home assessment for CareFlux Analytics.  
It ingests patient data from CSV files (simulating a simplified EHR) and generates concise, evidence-backed clinical summaries using an LLM.

The app provides:
- A **FastAPI backend** for summary generation
- A **Streamlit frontend** for user interaction
- Structured output with **source citations** for every clinical claim

---

## 🧱 Folder Structure

clinical-summary/
│
├── data/
│ ├── diagnoses.csv
│ ├── medications.csv
│ ├── vitals.csv
│ ├── notes.csv
│ ├── wounds.csv
│ └── oasis.csv
│
├── backend/
│ ├── main.py
│ ├── data_loader.py
│ └── llm.py
│
├── app.py
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

1. **Clone or copy the project**
   ```bash
   git clone <your-repo-url>
   cd clinical-summary


Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Set your OpenAI API key

setx OPENAI_API_KEY "your_api_key_here"

🚀 How to Run
1. Start the backend API
uvicorn backend.main:app --reload

2. Start the frontend

In a separate terminal:

streamlit run app.py

3. Interact with the UI

Open http://localhost:8501
 and enter a patient_id
Press Generate Summary to see structured clinical output with citations.

🧠 Project Highlights

Structured clinical summaries with source file and date citation

LLM prompts engineered for clinical reasoning

JSON-based backend API for integration with UIs

Simple, intuitive Streamlit frontend

🎯 Example Output

Each summary block includes:

{
  "statement": "Patient has hypertension.",
  "source": "diagnoses.csv - 2023-10-01"
}

🧪 Notes

This assessment simulates a basic EHR using CSV files. In a real product, you’d use a clinical database.

The LLM prompt is designed to restrict hallucination and provide evidence tracking.

“CareFlux Analytics” appears to be an applied health-AI company from the assessment email, although publicly listed references are under Careflux (AI) and Careflux Limited.

📞 Contact

For questions on this submission:
Aryan Tyagi — aryan.india1515@gmail.com


---

If you also want:
✅ A `.env` example file for storing API keys  
✅ A polished LinkedIn description of your project  
Just let me know!
::contentReference[oaicite:3]{index=3}