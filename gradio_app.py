from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr

from brain_doctor import encode_image, analyze_image_with_query
from voice_patient import transcribe_with_groq
from voice_doctor import text_to_speech_with_gtts


system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):

    # Step 1: Speech to Text
    if audio_filepath:
        speech_to_text_output = transcribe_with_groq(audio_filepath)
    else:
        speech_to_text_output = "No audio provided"

    # Step 2: Image Analysis
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + " " + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    # Step 3: Text to Speech (using gTTS)
    output_audio_path = "final.mp3"

    text_to_speech_with_gtts(
        input_text=doctor_response,
        output_filepath=output_audio_path
    )

    return speech_to_text_output, doctor_response, output_audio_path


iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio()
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)