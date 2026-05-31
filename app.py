import streamlit as st
from run_pipeline import run_research_pipeline

st.set_page_config(page_title="AI Research Agent", layout="wide")

st.title("AI Research Agent")
st.write("Searches, scrapes, writes, and critiques a research report.")

topic = st.text_input("Enter a research topic")

if st.button("Generate Report"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Running research pipeline..."):
            result = run_research_pipeline(topic)

        st.subheader("Search Results")
        st.write(result["search_results"])

        st.subheader("Scraped Content")
        st.write(result["scraped_content"])

        st.subheader("Final Report")
        st.write(result["report"])

        st.subheader("Critic Feedback")
        st.write(result["feedback"])


        