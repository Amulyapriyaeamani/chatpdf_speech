import streamlit as st
import PyPDF2
from gtts import gTTS
import os

# Streamlit UI
st.title("PDF Bot with Text-to-Speech")

# Upload a PDF file
st.sidebar.header("Upload PDF")
pdf_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    if pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_Text()
        return text

# Function to convert text to speech
def convert_text_to_speech(text):
    if text:
        tts = gTTS(text)
        tts.save("output.mp3")
        os.system("start output.mp3")  # This command plays the saved audio on Windows

# Main content
st.header("PDF Text Extraction and Text-to-Speech")

if pdf_file:
    pdf_text = extract_text_from_pdf(pdf_file)
    if pdf_text:
        st.subheader("Extracted Text:")
        st.text(pdf_text)

        # Button to convert text to speech
        if st.button("Convert to Speech"):
            convert_text_to_speech(pdf_text)
            st.success("Speech generated successfully! Click the link below to listen.")
            st.audio("output.mp3")
    else:
        st.warning("No text found in the PDF.")
else:
    st.sidebar.info("Please upload a PDF file on the sidebar.")

