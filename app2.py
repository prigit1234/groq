import streamlit as st
from groq import Groq
import os

# Get your API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

st.title("🤖 AI Chatbot (Groq Practice App)")

# Text input
user_input = st.text_input("Ask me anything:")

# Placeholder for response
response_box = st.empty()

# Button to send message
if st.button("Send") and user_input:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user_input}]
    )
    # Display the response
    response_box.write(response.choices[0].message.content)
