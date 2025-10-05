"""
Author: Santosh Kumar

Description: This file implements a Streamlit web app for translating English text to Kannada and generating 
speech from the translation. It takes user input, translates it using the IndicTrans2 model, and then converts 
the translated text to speech using the Indic Parler-TTS model. The resulting audio is played back in the browser 
using an embedded audio player. Session state is used to manage user interactions and enable/disable buttons.

Note: When you click "Speak" button the first time, it may take a while to load the model and generate the audio.
From the next time onwards, it will be faster.
"""
import base64
import streamlit as st
import indictrans2 as translator
import indic_parser_tts as parser_tts

# Initialize a flag in session_state if it doesn't exist
if 'my_flag' not in st.session_state:
    st.session_state.my_flag = False

if 'result' not in st.session_state:
    st.session_state.result = "No Input provided"

wav_file = "indic_tts_out.wav"

def ui_app():
    st.title('Language Translator')

    eng_input = st.text_input("Text in English", "")
    if st.button("Translate"):
        st.session_state.result = translator.translator_file(eng_input)
        st.write("Translated to Kannada:")
        st.write(st.session_state.result)
        print("result: ", st.session_state.result)
        if st.session_state.result != "No Input provided":
            st.session_state.my_flag = True

    if st.button("Speak", disabled=not st.session_state.my_flag):
        print("flag is true")
        parser_tts.generate_tts(st.session_state.result)

        # Encode file to base64
        with open(wav_file, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()

        # Embed in HTML with autoplay
        md = f"""
            <audio autoplay>
                <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
        st.write("The model spoke.")

if __name__ == "__main__":
    ui_app()