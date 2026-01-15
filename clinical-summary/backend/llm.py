import json
import os
from openai import OpenAI

# Make sure you set your API key in environment variables as i currently do not have my own free tier key as i have already used free credits for my openai key as well as for my gemini key
# setx OPENAI_API_KEY "your_key_here"   (PowerShell)
client = OpenAI()

def build_context(patient_data: dict) -> str:
    """
    Convert patient data into a readable JSON context
    that the LLM can reason over.
    """
    return json.dumps(patient_data, indent=2)

def generate_summary(patient_data: dict) -> dict:
    """
    Sends patient data to the LLM and returns a
    structured, citation-backed clinical summary.
    """

    context = build_context(patient_data)

    prompt = f"""
You are a licensed home health clinician.

TASK:
Generate a concise, evidence-based clinical summary
for the patient using ONLY the provided data.

STRICT RULES:
- Do NOT hallucinate or infer missing information
- If data is missing, explicitly say "Not documented"
- Every clinical statement MUST include a citation
- Citations must reference the source CSV and date if available

FOCUS AREAS:
1. Primary diagnoses
2. Recent vital sign trends
3. Active wounds
4. Medications and adherence
5. Functional status (OASIS)

OUTPUT FORMAT (JSON ONLY):
{{
  "summary": [
    {{
      "statement": "Patient has a diagnosis of hypertension.",
      "source": "diagnoses.csv - 2023-09-15"
    }}
  ]
}}

PATIENT DATA:
{context}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        # Fallback in case model slightly breaks format
        return {
            "summary": [
                {
                    "statement": "Failed to generate structured summary.",
                    "source": "LLM Error"
                }
            ]
        }
