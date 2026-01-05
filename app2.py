import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()  # make sure .env is in the same folder

# Get your API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# DEBUG: Check if the key is loaded
if not GROQ_API_KEY:
    st.error("⚠️ GROQ_API_KEY not found! Check your .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

st.title("🤖 AI Chatbot (Groq Practice App)")

# Text input
user_input = st.text_input("Ask me anything:")

# Placeholder for response
response_box = st.empty()

# Button to send message
if st.button("Send") and user_input:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )
        # Display the response
        response_box.write(response.choices[0].message.content)
    except Exception as e:
        response_box.write(f"Error: {e}")
