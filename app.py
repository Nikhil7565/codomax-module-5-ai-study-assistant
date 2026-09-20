import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Study Assistant")
st.write("Ask questions and get AI-powered study help.")

question = st.text_area(
    "Enter your question or topic:",
    placeholder="Example: Explain Machine Learning in simple words."
)

if st.button("Generate Answer"):
    if question.strip():
        st.info("Your AI answer will appear here.")
    else:
        st.warning("Please enter a question first.")
