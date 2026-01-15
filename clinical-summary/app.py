import streamlit as st
import requests

st.set_page_config(
    page_title="Clinical Summary Generator",
    layout="centered"
)

st.title("🩺 Clinical Summary Generator")
st.caption("Evidence-based patient summaries with source citations")

# API endpoint
API_URL = "http://127.0.0.1:8000/generate_summary"

# Input
patient_id = st.number_input(
    "Enter Patient ID",
    min_value=1,
    step=1
)

if st.button("Generate Summary"):
    if not patient_id:
        st.warning("Please enter a valid patient ID.")
    else:
        with st.spinner("Generating clinical summary..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"patient_id": patient_id},
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()
                    summary_items = data.get("summary", [])

                    if not summary_items:
                        st.info("No summary data available.")
                    else:
                        st.subheader(f"Patient ID: {patient_id}")
                        for idx, item in enumerate(summary_items, start=1):
                            st.markdown(f"**{idx}. {item['statement']}**")
                            st.caption(f"Source: {item['source']}")
                else:
                    st.error(response.json().get("detail", "Error generating summary"))

            except requests.exceptions.RequestException as e:
                st.error(f"API connection error: {e}")
