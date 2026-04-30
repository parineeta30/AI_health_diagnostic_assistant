from dotenv import load_dotenv
load_dotenv()

import os
from gtts import gTTS
import subprocess
import platform

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
