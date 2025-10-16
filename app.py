import streamlit as st
import json
import os

st.set_page_config(page_title="The CSEC Hub")
st.title("THE CSEC HUB")

subjects = ["Mathematics", "Physics", "Chemistry"] 
selected_subject = st.sidebar.selectbox("Select Subject", subjects)

years = ["2022", "2021", "2020"] 
selected_year = st.sidebar.selectbox("Select Year", years)

questions_path = f"data/questions/{selected_subject.lower()}_{selected_year}.json"
if os.path.exists(questions_path):
    with open(questions_path, "r") as f:
        data = json.load(f)
    topics = sorted(list(set(q["topic"] for q in data["questions"])))
else:
    data = {"questions": []}
    topics = []

selected_topic = st.sidebar.selectbox("Filter by Topic", ["All"] + topics)

pdf_path = f"data/papers/{selected_subject.lower()}_{selected_year}.pdf"
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
    st.download_button("Download Full Paper PDF", pdf_data, file_name=f"{selected_subject}_{selected_year}.pdf")
    
    # Embed PDF
    st.components.v1.html(f"""
        <embed src="{pdf_path}" width="700" height="1000" type="application/pdf">
    """, height=1000)
else:
    st.warning("PDF not found!")

st.header("Practice Questions")
for q in data["questions"]:
    if selected_topic != "All" and q["topic"] != selected_topic:
        continue
    
    st.subheader(f"Q{q['question_number']} ({q['topic']})")
    st.write(q["text"])
    
    user_answer = st.text_input(f"Your Answer for Q{q['question_number']}", key=f"{q['topic']}_{q['question_number']}")
    
    if user_answer:
        if user_answer.strip() == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect.")
        st.info(f"Solution: {q['solution']}")


