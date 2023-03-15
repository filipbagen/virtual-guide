from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

def talk(text): 
    tts = gTTS(text=text, lang='sv', slow=False)

    tts.save("tts.mp3")
    
    path = os.path.abspath("tts.mp3")
    playsound(path)
    
    
