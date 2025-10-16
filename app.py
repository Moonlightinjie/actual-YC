import streamlit as st

st.set_page_config(page_title="CSEC Past Papers")
st.title("📄 CSEC Past Papers Hub")

# Sidebar filters
subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "Information Technology"]
selected_subject = st.sidebar.selectbox("Select Subject", subjects)

years = [str(y) for y in range(2015, 2026)]
selected_year = st.sidebar.selectbox("Select Year", years)

papers = ["Paper 1", "Paper 2", "Paper 3"]
selected_paper = st.sidebar.selectbox("Select Paper", papers)

# Mock database of past papers (replace links with actual PDFs)
past_papers = {
    "Mathematics": {
        "2020": {
            "Paper 1": "https://example.com/math2020p1.pdf",
            "Paper 2": "https://example.com/math2020p2.pdf",
            "Paper 3": "https://example.com/math2020p3.pdf"
        }
    },
    "Physics": {
        "2020": {
            "Paper 1": "https://example.com/physics2020p1.pdf",
            "Paper 2": "https://example.com/physics2020p2.pdf",
            "Paper 3": "https://example.com/physics2020p3.pdf"
        }
    }
}

# Display the selected paper
link = past_papers.get(selected_subject, {}).get(selected_year, {}).get(selected_paper)
if link:
    st.write(f"**{selected_subject} {selected_year} {selected_paper}**")
    st.markdown(f"[📄 View/Download PDF]({link})")
else:
    st.write("No past paper available for this selection yet.")

# Optional: brief notes section
st.subheader("Notes / Hints")
st.write("You can add short notes or tips here for each subject or paper.")

