"""
Author: Santosh Kumar

Description: This file defines a function to generate text-to-speech (TTS) audio from a given prompt using the 
AI4Bharat Indic Parler-TTS model. It loads the model and tokenizers, prepares a speaker description and the input 
prompt, generates the audio output, and saves the resulting speech as a WAV file.
"""
import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf

def generate_tts(prompt):
    DEVICE = "cpu"

    print("prompt is: ", prompt)

    model = ParlerTTSForConditionalGeneration.from_pretrained("ai4bharat/indic-parler-tts").to(DEVICE)
    tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-parler-tts")
    description_tokenizer = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)

    #prompt = "{prompt}"
    description = "A female speaker with a Indian accent delivers a slightly expressive and animated speech with a moderate speed and pitch. The recording is of very high quality, with the speaker's voice sounding clear and very close up."

    description_input_ids = description_tokenizer(description, return_tensors="pt").to(DEVICE)
    prompt_input_ids = tokenizer(prompt, return_tensors="pt").to(DEVICE)

    generation = model.generate(input_ids=description_input_ids.input_ids, attention_mask=description_input_ids.attention_mask, prompt_input_ids=prompt_input_ids.input_ids, prompt_attention_mask=prompt_input_ids.attention_mask)
    audio_arr = generation.cpu().numpy().squeeze()
    sf.write("indic_tts_out.wav", audio_arr, model.config.sampling_rate)