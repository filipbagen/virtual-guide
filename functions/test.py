from TTS.api import TTS
from playsound import playsound
import os


tts = TTS("tts_models/sv/cv/vits")

tts.tts_to_file("Det här är ett test med rösten. Vad gör du just nu? ")

path = os.path.abspath("output.wav")
playsound(path)