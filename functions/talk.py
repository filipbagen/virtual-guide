from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

import whisper
import sounddevice
from scipy.io.wavfile import write 

import whisper
model = whisper.load_model("tiny")

def talk(text): 
    tts = gTTS(text=text, lang='sv', slow=False)

    tts.save("tts.mp3")
    
    path = os.path.abspath("tts.mp3")
    playsound(path)
    
def listen():
    sr=44100
    seconds=3
    print('Recording\n')
    record_voice=sounddevice.rec(sr*seconds, samplerate=sr, channels=1) 
    sounddevice.wait()
    write('audiotest.mp3',sr,record_voice)

    result = model.transcribe("audio.mp3")
    print(result["text"])
    print('Finished')
