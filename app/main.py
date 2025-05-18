import streamlit as st
from agent import handle_query
from feedback import record_feedback

from dotenv import load_dotenv
load_dotenv()

st.title("Auto Triage Support BOT")

query = st.text_input("Enter your support question:")

if st.button("Submit"):
    answer_data = handle_query(query)
    st.write("##Answer:")
    st.write(answer_data["result"])
    st.write("### Source Documents")
    for doc in answer_data["source_documents"]:
        st.text(doc.page_content[:300])

    feedback = st.radio("Was this answer helpful?", ("Yes", "No"))
    if st.button("Submit Feedback"):
        record_feedback(query, answer, feedback)
        st.success("Feedback recorded successfully!")
