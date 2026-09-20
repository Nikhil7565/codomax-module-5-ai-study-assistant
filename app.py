import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Study Assistant")
st.write("Ask a question and get an AI-powered study explanation.")

question = st.text_area(
    "Enter your question or topic:",
    placeholder="Example: Explain Machine Learning in simple words."
)

if st.button("Generate Answer"):

    if not question.strip():
        st.warning("Please enter a question first.")

    else:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            st.error("Gemini API key is not configured.")
        else:
            client = genai.Client(api_key=api_key)

            prompt = f"""
You are an AI Study Assistant.

For the following topic/question:
{question}

Give:
1. Simple explanation
2. Key points
3. Short summary
4. Three practice questions
"""

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            st.markdown("### 📚 AI Answer")
            st.write(response.text)
