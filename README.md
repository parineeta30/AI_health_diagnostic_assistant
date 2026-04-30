# MediVision AI Assistant

An intelligent healthcare chatbot that analyzes medical conditions through voice input, image analysis, and AI-powered medical assessment with voice response.It performs symptom interpretation and visual pattern recognition rather than diagnosis.

## Overview

This is an educational tool that processes patient voice queries, analyzes medical images using AI, and provides doctor-like responses with voice feedback through a user-friendly web interface.

## Key Features

- **Voice-to-Text**: Transcribe patient voice using Groq's Whisper API
- **Medical Image Analysis**: AI-powered analysis of medical scans using Llama multimodal model
- **AI Doctor Response**: Intelligent medical assessment mimicking professional doctors
- **Text-to-Speech**: Voice output of doctor's analysis using Google gTTS
- **Web Interface**: Modern Gradio UI with futuristic design

## Project Structure

```
├── gradio_app.py          # Main web interface
├── brain_doctor.py        # Image analysis logic
├── voice_patient.py       # Speech-to-text
├── voice_doctor.py        # Text-to-speech
├── Pipfile                # Dependencies
└── README.md
```

## Project Setup Guide (Windows)

This guide provides step-by-step instructions to set up your project environment on Windows, including the installation of FFmpeg and PortAudio, and setting up a Python virtual environment.

### Prerequisites

- Python 3.11+
- FFmpeg (audio processing)
- PortAudio (audio input/output)
- Groq API Key (free tier available)
- ElevenLabs API Key (optional, for premium voices)

### Installing FFmpeg

**Download FFmpeg:**
- Visit the official [FFmpeg download page](https://ffmpeg.org/download.html)
- Navigate to the Windows builds section and download the latest static build

**Extract and Set Up FFmpeg:**
1. Extract the downloaded ZIP file to a folder (e.g., `C:\ffmpeg`)
2. Add the bin directory to your system's PATH:
   - Search for "Environment Variables" in the Start menu
   - Click on "Edit the system environment variables"
   - In the System Properties window, click on "Environment Variables"
   - Under "System variables," select the "Path" variable and click "Edit"
   - Click "New" and add the path to the bin directory (e.g., `C:\ffmpeg\bin`)
   - Click "OK" to apply the changes

### Installing PortAudio

- Download the PortAudio binaries from the [official website](http://www.portaudio.com/download.html)
- Follow the installation instructions provided on the website

### Setting Up a Python Virtual Environment

**Create a Virtual Environment:**
```bash
python -m venv venv
```

**Activate the Virtual Environment:**
```bash
venv\Scripts\activate
```

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

### Setting up API Keys

Create a `.env` file in the project root directory with your API keys:

```
GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here (optional)
```

## Running the Application

The application can be run in different phases:

### Phase 1: Brain of the Doctor
```bash
python brain_doctor.py
```
Runs the medical image analysis and AI assessment logic.

### Phase 2: Voice of the Patient
```bash
python voice_patient.py
```
Handles patient voice input and speech-to-text transcription.

### Phase 3: Voice of the Doctor
```bash
python voice_doctor.py
```
Generates voice output of the doctor's analysis using text-to-speech.

### Phase 4: Setup Gradio UI
```bash
python gradio_app.py
```
Launches the complete web interface with all integrated features. Access at `http://localhost:7860`

## How to Use

1. Run the Gradio application: `python gradio_app.py`
2. Record patient voice or upload an audio file
3. Upload a medical image/scan
4. Click "Analyze Patient Data"
5. View transcript, doctor's analysis, and hear the voice response

## Technology Stack

- **Frontend**: Gradio
- **APIs**: Groq (speech-to-text, image analysis), Google gTTS (text-to-speech)
- **Models**: Llama-4-scout-17b, Whisper-large-v3
- **Libraries**: LangChain, pydub, SpeechRecognition

## Module Overview

| File | Purpose |
|------|---------|
| `gradio_app.py` | Main application & UI orchestration |
| `brain_doctor.py` | Image encoding & AI analysis |
| `voice_patient.py` | Audio transcription |
| `voice_doctor.py` | Audio synthesis |

## Troubleshooting

**Audio not recording**
- Check microphone permissions and ffmpeg installation

**Image analysis failing**
- Verify Groq API key is valid
- Ensure image format is JPEG or PNG

**API errors**
- Check internet connection
- Verify API keys in `.env`
- Check Groq rate limits (free tier: ~30 req/min)

## API Limits

**Groq Free Tier**: ~30 requests per minute

## Disclaimer

This is an **educational tool only** and NOT a substitute for professional medical advice. The AI may produce inaccurate information. Always consult qualified healthcare professionals for medical concerns.

## Getting API Keys

- **Groq**: https://console.groq.com (free tier)
- **ElevenLabs**: https://elevenlabs.io (paid)(optional in project use)
- **Google gTTS**: Free, no key required

---

For issues, check the troubleshooting section or consult the Groq and Gradio documentation.
