**Project Overview:**
This project is a Streamlit web application that translates English text to Kannada and generates speech from the translated text using state-of-the-art AI models from AI4Bharat. The app provides a simple interface for users to input English text, view the Kannada translation, and listen to the spoken output.

**Flow & Modules Used**
1. __Translation (indictrans2.py)__

Purpose: Translates English text to Kannada.

Modules Used:
transformers (AutoModelForSeq2SeqLM, AutoTokenizer): Loads the IndicTrans2 translation model and tokenizer.
IndicTransToolkit.processor.IndicProcessor: Preprocesses and postprocesses text for translation.
torch: Handles model inference on CPU.

Process: The input text is preprocessed, translated using the model, and postprocessed to produce the final Kannada output.

3. __Text-to-Speech (indic_parser_tts.py)__

Purpose: Converts Kannada text to speech.

Modules Used:
parler_tts.ParlerTTSForConditionalGeneration: Loads the Indic Parler-TTS model for speech synthesis.
transformers.AutoTokenizer: Tokenizes both the speaker description and the prompt.
soundfile: Saves the generated audio as a WAV file.
torch: Handles model inference on CPU.

Process: The translated Kannada text is synthesized into speech using a predefined speaker description, and the output is saved as a WAV file.

4. __Web Interface (app.py)__

Purpose: Provides a user-friendly interface for translation and speech generation.

Modules Used:
streamlit: Builds the interactive web app.
base64: Encodes audio for playback in the browser.
Custom modules: indictrans2 (translation), indic_parser_tts (TTS).

Process: Users input English text, click "Translate" to get Kannada output, and "Speak" to hear the audio. The app manages session state to control button availability and displays the audio using an embedded player

**How It Works**
User Input: Enter English text in the web app.
Translation: The text is sent to the IndicTrans2 model for translation to Kannada.
Speech Generation: The translated Kannada text is sent to the Indic Parler-TTS model to generate speech.
Playback: The generated audio is played back in the browser.

**Requirements:** 
Python 3.8+,
Streamlit,
Transformers,
torch,
IndicTransToolkit,
parler_tts,
soundfile

**Running the App(Install the modules before running app.py):** 
streamlit run app.py

**Additional Notes:** 
The first run may take longer due to model loading.
All processing is done on CPU by default.
The app is designed for demonstration and educational purposes.
