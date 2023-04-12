from TTS.api import TTS
from playsound import playsound
import os


def talk(text):
    tts = TTS("tts_models/sv/cv/vits")

    tts.tts_to_file(text)

    path = os.path.abspath("output.wav")
    playsound(path)


