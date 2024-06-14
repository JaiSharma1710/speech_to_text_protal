from transformers import pipeline
import streamlit as st

whisper = pipeline('automatic-speech-recognition',
                   model='openai/whisper-medium')

st.title("Whisper App")

# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])


if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        print(audio_file)
        transcription = whisper(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")


st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)
