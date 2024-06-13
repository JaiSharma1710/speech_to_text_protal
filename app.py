import streamlit as st
from transformers import pipeline
import requests

# Streamlit app
st.title("Speech to Text")

audio_url = st.text_input("Link To Audio file")

if st.button("Transcript"):
    if not audio_url:
        st.error('no URL present')

    response = requests.get(audio_url)

    if response.status_code == 200:
        audio_data = response.content
        st.audio(audio_data)
        whisper = pipeline('automatic-speech-recognition',
                           model='openai/whisper-medium')
        transcription = whisper(audio_data)
        st.markdown(transcription["text"])
    else:
        st.error(
            f"Failed to download audio file. Status code: {response.status_code}")
