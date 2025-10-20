import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import re
import io
import config

client = genai.Client(api_key=config.GEMINI_API_KEY)
def run_ai_teaching_assistant():
    st.title("???AI Teaching Assistant")
    st.write("Welcome to the AI Teaching Assistant! Ask me anything about various subjects, and I'll provide an insightful response.")

    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []
    col_clear, col_export = st.columns([1,2])

    with col_clear:
        if st.button("🧹 Clear Conversation," key="clear_ata"):
            st.session_state.history_ata = []
            
    with col_export:
        if st.session_state.history_ata:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history_ata, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"
            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label="📥 Export Conversation", data=bio,
                file_name="AI_Teaching_Assistant_Conversati.txt",mime="text/plain",)
    
    user_question = st.text_input("Enter your question here:", key="input_ata")

    if st.button("Ask", key="ask_ata"):
        if user_question.strip():
            with st.spinner("Generating response..."):
                response = genarate_response(user_question.strip(),temprature=0.3)
            st.session_state.history_ata.append({
                "question": user_question.strip(), "answer": response
            })