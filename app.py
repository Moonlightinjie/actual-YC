import streamlit as st
import os

st.set_page_config(page_title="CSEC Past Papers", layout="wide")
st.title("THE CSEC HUB")

# Step 1: Let user pick subject
subjects = ["Mathematics", "Chemistry", "Physics"]
selected_subject = st.selectbox("Select a Subject", subjects)

# Step 2: Find all PDFs for that subject
papers_folder = "data/papers"
subject_papers = [
    f for f in os.listdir(papers_folder)
    if f.lower().startswith(selected_subject.lower())
]

if not subject_papers:
    st.error(f"No papers found for {selected_subject} 😢")
else:
    selected_paper = st.selectbox("Select a Paper", subject_papers)

    # Full path to selected file
    pdf_path = os.path.join(papers_folder, selected_paper)

    # Step 3: Display and download
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    st.download_button(
        label=f"📥 Download {selected_paper}",
        data=pdf_data,
        file_name=selected_paper
    )

    st.components.v1.html(
        f'<embed src="{pdf_path}" width="800" height="1000" type="application/pdf">',
        height=1000,
    )


