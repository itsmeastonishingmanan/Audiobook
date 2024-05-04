import os
import pdfplumber
from google.cloud import texttospeech

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def text_to_speech(text, output_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-D",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)

def convert_pdf_to_speech(pdf_path, output_file="output.wav"):
    text = extract_text_from_pdf(pdf_path)
    text_to_speech(text, output_file)

if __name__ == "__main__":
    pdf_file_path = "Command Prompt Cheatsheet.pdf"  # Replace with the path to your PDF file
    convert_pdf_to_speech(pdf_file_path)
