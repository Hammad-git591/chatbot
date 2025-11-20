from google import genai
import streamlit as st
import os

# Load API key from Streamlit Secrets
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

st.title("Talk to Agent")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_input
        )
    st.write(response.text)
