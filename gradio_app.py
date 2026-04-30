from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr

from brain_doctor import encode_image, analyze_image_with_query
from voice_patient import transcribe_with_groq
from voice_doctor import text_to_speech_with_gtts

system_prompt = """You are an AI-powered healthcare assistant for educational purposes. 
Analyze the provided image along with the user’s symptoms and identify any visible patterns or abnormalities.
Provide a clear and concise explanation of possible causes (not a medical diagnosis). 
Suggest general precautions or next steps where appropriate.
If the condition appears serious or uncertain, recommend consulting a qualified medical professional. 
Keep the response natural, human-like, and easy to understand. Limit the response to 2–3 sentences."""


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
    
# theme for futuristic foundation
theme = gr.themes.Soft(
    primary_hue="sky", 
    secondary_hue="slate", 
    neutral_hue="slate",
).set(
    body_background_fill="*neutral_950",
    body_text_color="*neutral_50",
    button_primary_background_fill="*primary_600",
)


with gr.Blocks(theme=theme) as demo:
    
    gr.Markdown("#  MediVision  ", elem_id="chatbot-title")
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Patient Voice Input")
            image_input = gr.Image(type="filepath", label="Medical Scan")
            submit_btn = gr.Button("Analyze Patient Data", variant="primary")
        
        with gr.Column():
            text_output = gr.Textbox(label="Transcript")
            doctor_response = gr.Textbox(label="Doctor's Analysis")
            audio_output = gr.Audio(label="Doctor's Voice Response")

    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[text_output, doctor_response, audio_output]
    )

if __name__ == "__main__":
    # CSS block
    futuristic_css = """
    #chatbot-title { 
        text-align: center !important; 
        font-family: 'Segoe UI', sans-serif !important; 
        color: #38bdf8 !important; 
        text-shadow: 0 0 15px #38bdf8;
    }
    .gradio-container {
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)) !important;
        background-size: cover !important;
        font-family: 'Segoe UI', sans-serif !important;
    }
    """
    demo.launch(debug=True, css=futuristic_css)
