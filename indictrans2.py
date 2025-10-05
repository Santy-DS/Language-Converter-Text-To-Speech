"""
Author: Santosh Kumar

Description: This file implements a function to translate English text to Kannada using the AI4Bharat IndicTrans2 
model. It loads the model and tokenizer, preprocesses the input text, generates the translation with the model, 
and postprocesses the output. The function prints the input and translated text, returning the translated result.
"""
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from IndicTransToolkit.processor import IndicProcessor

def translator_file(translation_text):
    DEVICE = "cpu"

    src_lang, tgt_lang = "eng_Latn", "kan_Knda"
    model_name = "ai4bharat/indictrans2-en-indic-1B"

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True).to(DEVICE)
    ip = IndicProcessor(inference=True)

    print("translation text: ", translation_text)

    # input_sentence = [
    #     "Hi How are you?",
    #     "We watched a new movie last week, which was very inspiring.",
    #     "If you had met me at that time, we would have gone out to eat.",
    #     "My friend has invited me to his birthday party, and I will give him a gift.",
    # ]

    input_sentence = [
        translation_text
    ]

    batch = ip.preprocess_batch(
        input_sentence,
        src_lang=src_lang,
        tgt_lang=tgt_lang,
    )
    inputs = tokenizer(batch,
        truncation=True,
        padding="longest",
        return_tensors="pt",
        return_attention_mask=True,).to(DEVICE)

    with torch.no_grad():
        generated_tokens = model.generate(
            **inputs,
            min_length=0,
            max_length=256,
            num_beams=1,
            #num_return_sequences=1,
        )

    # Decode the generated tokens into text
    generated_tokens = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )

    # Postprocess the translations, including entity replacement
    translations = ip.postprocess_batch(generated_tokens, lang=tgt_lang)

    for inp, translation in zip(input_sentence, translations):
        print(f"{src_lang}: {inp}")
        print(f"{tgt_lang}: {translation}")
    
    return translations[0] if translations else "No Input provided"