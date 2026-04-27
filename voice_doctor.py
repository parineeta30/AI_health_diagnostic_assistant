from dotenv import load_dotenv
load_dotenv()

import os
from gtts import gTTS
from elevenlabs.client import ElevenLabs
import subprocess
import platform

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_gtts(input_text, output_filepath):
    audioobj = gTTS(
        text=input_text,
        lang="en",
        slow=False
    )
    audioobj.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            os.startfile(output_filepath)
        elif os_name == "Linux":
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        raise e


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="21m00Tcm4TlvDq8ikWAM",
        model_id="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )

    # Save audio safely
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    # Play audio
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            os.startfile(output_filepath)
        elif os_name == "Linux":
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        raise e