from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition
import pyttsx3
import time

t_end = time.time() + 5

def talk(text): 
    tts = gTTS(text=text, lang='sv', slow=False)

    tts.save("tts.mp3")
    
    path = os.path.abspath("tts.mp3")
    playsound(path)
    

def speech_to_text():

    recognizer = speech_recognition.Recognizer()

    while time.time() < t_end:

        try:

            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio, language="sv-SE")
                text = text.lower()

                return (f"{text}")
            
        except speech_recognition.UnknownValueError:
            return("Could not understand audio")