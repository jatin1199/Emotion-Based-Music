import streamlit as st
from face_emotion import get_emotion


st.text_input("Singer", key="singer")
st.text_input("Language", key="language")

# You can access the value at any point with:
st.session_state.singer
st.session_state.language

if st.button("Get Emotion"):
    emotion = get_emotion()
    emotion

